# Passwall2 分流规则

由本仓库 `Loon/` 的同名清单生成，来源沿用根目录 README 中的上游说明。适用于 Passwall2 分流规则的 domain_list / ip_list 文本输入，不是节点订阅或可直接导入的完整配置。

## 使用

1. 在 Passwall2 的分流规则页面为所需分类创建规则。
2. 将 `Google.list` 等文件内容粘贴到“域名”框，将对应 `Google.ip.list` 内容粘贴到“IP”框。只有注释的 IP 文件表示没有 IP 条目，可留空。
3. 在正在使用的分流节点中，把各分类关联到对应代理节点或直连出口，并启用这个分流节点。仅添加规则文件不会自动生效。
4. 个人直连、个人代理优先，YouTube / Telegram / GlobalAI 等专用分类在 Google / Global / ProxyGFWlist 通用分类之前；兜底出口按自己的需求设置。

文件下载前缀：`https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Passwall2/`。例如 `Google.list` 与 `Google.ip.list`。普通 Raw 文本 URL 不能直接填入域名框当成订阅；本方案需要粘贴文件内容。仓库自动更新不等于路由器自动更新，路由器同步尚未配置。

## 文件和来源

| 域名文件 | IP 文件 | 参考来源 |
| --- | --- | --- |
| personal/personalDirect.list | personal/personalDirect.ip.list | Loon/personal/personalDirect.list，个人直连 |
| personal/personalProxy.list | personal/personalProxy.ip.list | Loon/personal/personalProxy.list，个人代理 |
| Global.list | Global.ip.list | Loon/Global.list |
| Google.list | Google.ip.list | Loon/Google.list |
| YouTube.list | YouTube.ip.list | Loon/YouTube.list |
| Telegram.list | Telegram.ip.list | Loon/Telegram.list |
| GlobalAI.list | GlobalAI.ip.list | Loon/GlobalAI.list |
| ProxyGFWlist.list | ProxyGFWlist.ip.list | Loon/ProxyGFWlist.list |

## 转换边界

- DOMAIN → full:；DOMAIN-SUFFIX → domain:；DOMAIN-KEYWORD → 无前缀关键词。
- IP-CIDR / IP-CIDR6 → IP 框中的 CIDR。去掉 Loon 的 no-resolve 参数；DNS 解析与 IP 匹配行为由路由器核心配置决定，不保证与 Loon 完全等价。
- PROCESS-NAME、USER-AGENT、URL-REGEX、IP-ASN 未转换，逐条列在 conversion-report.json 中。路由器通常无法获知客户端进程名，ASN 也不能直接作为 CIDR 粘贴。
- 每个分类内去除完全相同的输出项，保留首次出现顺序；不进行跨分类去重。
- 尚未在你的 OpenWrt 设备上实测。依据 [Passwall2 官方分流规则源码](https://github.com/Openwrt-Passwall/openwrt-passwall2/blob/main/luci-app-passwall2/luasrc/model/cbi/passwall2/client/shunt_rules.lua) 的文本格式转换。

## 维护

运行 `python3 scripts/convert_passwall2.py` 重新生成。每日公共规则更新后自动生成；推送 Loon 规则变更也会触发。个人规则只从本仓库的 Loon/personal 派生，不从外部上游覆盖。请修改 Loon 源清单，不要直接编辑生成文件。
