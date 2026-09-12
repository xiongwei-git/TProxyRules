# TProxyRules

按代理软件组织的个人规则仓库。当前提供 Loon 规则；其他软件按需适配后放入各自目录。

### Loon

在 Loon 配置的 `[Remote Rule]` 中添加以下订阅。策略名称需与自己的策略组一致；个人规则在前，YouTube、Telegram、GlobalAI 等专用策略在通用代理规则之前。

```ini
[Remote Rule]
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/personal/personalDirect.list, policy=DIRECT, tag=Personal Direct, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/personal/personalProxy.list, policy=Available, tag=Personal Proxy, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/YouTube.list, policy=YouTube, tag=YouTube, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/Telegram.list, policy=Telegram, tag=Telegram, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/GlobalAI.list, policy=GlobalAI, tag=GlobalAI, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/Google.list, policy=Available, tag=Google, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/Global.list, policy=Available, tag=Global, enabled=true
https://raw.githubusercontent.com/xiongwei-git/TProxyRules/main/Loon/ProxyGFWlist.list, policy=Available, tag=ProxyGFWlist, enabled=true
```

私有域名、个人 IP 和内网规则继续保存在本地 `[Rule]`，兜底 `FINAL` 保留原有策略。规则文件不写策略，由订阅的 `policy=` 指定。IP-CIDR 可以放入个人列表，但公开仓库不得包含私密网络信息。

通用列表与分类列表允许重叠，无需从 ProxyGFWlist 手工剔除；通过规则顺序决定策略。域名、IP 等不同类型另受 Loon 匹配算法影响。GlobalAI 包含 PROCESS-NAME，使用前需确认客户端支持；本次仅迁移内容，未进行客户端运行验证。

1. [personal/personalDirect.list](Loon/personal/personalDirect.list)

   个人自定义直连规则。迁移自旧仓库同名文件。

2. [personal/personalProxy.list](Loon/personal/personalProxy.list)

   个人自定义代理规则。迁移自旧仓库同名文件。

3. [Global.list](Loon/Global.list)

   参考 [blackmatrix7/ios_rule_script 的 Loon/Proxy/Proxy.list](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy.list)。

4. [Google.list](Loon/Google.list)

   参考 [Loon0x00/LoonLiteRules 的 Google.list](https://raw.githubusercontent.com/Loon0x00/LoonLiteRules/main/proxy/Google.list)。

5. [YouTube.list](Loon/YouTube.list)

   参考 [Loon0x00/LoonLiteRules 的 YouTube.list](https://raw.githubusercontent.com/Loon0x00/LoonLiteRules/main/proxy/YouTube.list)。

6. [Telegram.list](Loon/Telegram.list)

   参考 [Loon0x00/LoonLiteRules 的 Telegram.list](https://raw.githubusercontent.com/Loon0x00/LoonLiteRules/main/proxy/Telegram.list)。

7. [GlobalAI.list](Loon/GlobalAI.list)

   参考 [VPSDance/ai-proxy-rules 的 rules/loon/global.list](https://raw.githubusercontent.com/VPSDance/ai-proxy-rules/main/rules/loon/global.list)。原订阅使用 [jsDelivr 地址](https://cdn.jsdelivr.net/gh/VPSDance/ai-proxy-rules@main/rules/loon/global.list)。

8. [ProxyGFWlist.list](Loon/ProxyGFWlist.list)

   自动同步 [ACL4SSR 的 Clash/ProxyGFWlist.list](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list)，不依赖旧仓库。

### Passwall2

计划支持，当前尚未生成 Passwall2 规则或提供可用订阅。后续根据实际版本、核心与分流配置适配并验证，不能直接把 Loon 格式当作 Passwall2 规则使用。

计划目录及来源：

1. `Passwall2/personal/personalDirect.list`、`Passwall2/personal/personalProxy.list`

   个人自定义规则，参考对应的 `Loon/personal/` 清单，转换后独立发布。

2. `Passwall2/Global.list`

   参考 `Loon/Global.list`。

3. `Passwall2/Google.list`

   参考 `Loon/Google.list`。

### 维护与迁移记录

2026-09-11 从 [xiongwei-git/ProxyRules](https://github.com/xiongwei-git/ProxyRules/tree/10249fa831607c3988f44eeabc59eea8c6cee667) 提交 `10249fa831607c3988f44eeabc59eea8c6cee667` 迁移，8 份规则保留源文件内容和名称。仅 ProxyGFWlist 从 `Clash/` 移入 `Loon/`。不恢复已删除的 Bybit 清单。

2026-09-13 起，GitHub Actions 每天北京时间 06:23 检查上述 6 份公共规则（调度可能延迟），有变化才提交。可在 Actions → Update public rules → Run workflow 手动运行。来源映射在 `scripts/update_rules.py`，`personal/` 不参与更新。

每个来源独立校验：下载失败、空文件、未知规则类型、格式异常，或规则数减少超过 20% / 增长超过 100% 时保留原文件；其他通过校验的列表正常提交，任务最后标记失败，在运行摘要中列明异常。失败通知取决于你的 GitHub Actions 通知设置。无变更不提交，可通过 Git 历史回滚错误更新。部分上游注释统计可能与正文不一致，以实际规则为准。旧仓库的生成脚本不在本仓库运行。

保留源文件中的作者及来源声明，并保留旧仓库的 [LICENCE](LICENCE)。第三方规则的使用和再分发同时遵循各原项目许可及声明。
