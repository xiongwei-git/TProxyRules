"""Sync only the explicitly listed public rules; personal rules are never targets."""
import ipaddress
import os
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Google": "Loon0x00/LoonLiteRules/main/proxy/Google.list",
    "YouTube": "Loon0x00/LoonLiteRules/main/proxy/YouTube.list",
    "Telegram": "Loon0x00/LoonLiteRules/main/proxy/Telegram.list",
    "GlobalAI": "VPSDance/ai-proxy-rules/main/rules/loon/global.list",
    "Global": "blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy.list",
    "ProxyGFWlist": "ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list",
}


def validate(data):
    text = data.decode("utf-8-sig")
    count = 0
    allowed = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD",
               "USER-AGENT", "URL-REGEX", "PROCESS-NAME", "IP-CIDR", "IP-CIDR6", "IP-ASN"}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        parts = [p.strip() for p in line.split(",")]
        kind = parts[0]
        if kind not in allowed or len(parts) < 2 or not parts[1]:
            raise ValueError("unknown or malformed rule")
        if kind in {"IP-CIDR", "IP-CIDR6"}:
            net = ipaddress.ip_network(parts[1], strict=False)
            if net.version != (4 if kind == "IP-CIDR" else 6):
                raise ValueError("IP version mismatch")
            if len(parts) > 3 or (len(parts) == 3 and parts[2] != "no-resolve"):
                raise ValueError("unexpected IP rule option")
        elif kind == "IP-ASN":
            if not parts[1].isdigit() or len(parts) > 3 or (len(parts) == 3 and parts[2] != "no-resolve"):
                raise ValueError("invalid ASN rule")
        elif len(parts) != 2:
            raise ValueError("unexpected rule field")
        if kind.startswith("DOMAIN") and any(c.isspace() for c in parts[1]):
            raise ValueError("invalid domain")
        count += 1
    if count == 0:
        raise ValueError("empty rules")
    return count


def check_change(old, new):
    old_count, new_count = validate(old), validate(new)
    if new_count < old_count * 0.8 or new_count > old_count * 2:
        raise ValueError("rule count changed by more than -20% or +100%; review required")
    return new_count


def main():
    failed = False
    reports = []
    for name, source in SOURCES.items():
        target = ROOT / "Loon" / (name + ".list")
        try:
            with urllib.request.urlopen(
                "https://raw.githubusercontent.com/" + source, timeout=45
            ) as response:
                data = response.read(5_000_001)
            if len(data) > 5_000_000:
                raise ValueError("file exceeds 5 MB")
            old = target.read_bytes()
            count = check_change(old, data)
            if old != data:
                temporary = target.with_suffix(".list.tmp")
                temporary.write_bytes(data)
                temporary.replace(target)
                reports.append(f"{name}: updated ({count} rules)")
            else:
                reports.append(f"{name}: unchanged ({count} rules)")
        except Exception as exc:
            failed = True
            reports.append(f"{name}: FAILED ({type(exc).__name__}: {exc}); original retained")
    report = "\n".join(reports)
    print(report)
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as summary:
            summary.write(report + "\n")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
