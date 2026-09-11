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

   迁移自 [xiongwei-git/ProxyRules 的 Clash/ProxyGFWlist.list](https://raw.githubusercontent.com/xiongwei-git/ProxyRules/master/Clash/ProxyGFWlist.list)。旧仓库有生成工作流；本仓库目前保存快照，未迁移自动生成任务。

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

未来更新时，根据上面的参考地址获取最新文件，与当前文件对比后审查增删及规则类型，再更新并提交。个人清单独立维护，不被上游覆盖。本次未重新同步第三方上游；迁移日期不代表上游规则更新日期。部分上游注释统计可能与正文不一致，以实际规则为准。

保留源文件中的作者及来源声明，并保留旧仓库的 [LICENCE](LICENCE)。第三方规则的使用和再分发同时遵循各原项目许可及声明。
