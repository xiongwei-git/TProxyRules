"""Generate Passwall2 domain/IP input lists without modifying Loon sources."""
import ipaddress
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def convert(text):
    domains, ips, skipped = [], [], []
    for number, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        parts = [p.strip() for p in line.split(",")]
        kind, value = parts[:2]
        if kind in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}:
            prefix = {"DOMAIN": "full:", "DOMAIN-SUFFIX": "domain:", "DOMAIN-KEYWORD": ""}[kind]
            domains.append(prefix + value)
        elif kind in {"IP-CIDR", "IP-CIDR6"}:
            ips.append(str(ipaddress.ip_network(value, strict=False)))
        else:
            skipped.append({"line": number, "rule": line, "reason": "No equivalent in domain_list/ip_list"})
    return list(dict.fromkeys(domains)), list(dict.fromkeys(ips)), skipped


def main():
    output = ROOT / "Passwall2"
    report = {}
    for source in sorted((ROOT / "Loon").rglob("*.list")):
        relative = source.relative_to(ROOT / "Loon")
        domains, ips, skipped = convert(source.read_text(encoding="utf-8-sig"))
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        header = "# Generated from Loon/" + relative.as_posix() + "; do not edit here.\n"
        target.write_text(header + "".join(d + "\n" for d in domains), encoding="utf-8")
        target.with_suffix(".ip.list").write_text(header + "".join(ip + "\n" for ip in ips), encoding="utf-8")
        report[relative.as_posix()] = {"domains": len(domains), "ips": len(ips), "skipped": skipped}
    (output / "conversion-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Converted", len(report), "lists; skipped", sum(len(r["skipped"]) for r in report.values()), "unsupported rules")


if __name__ == "__main__":
    main()
