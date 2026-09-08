# Aptum

**适其人，适其事，适其言。**

Version: `0.4.0`

AI 往往已经会写：语法通顺、结构清楚、术语也基本用对。但在复杂的工作上下文里，它仍可能犯四类错：

- 漏掉接收方真正需要的信息——测试同学要的是"怎么重置状态避免每轮等 15 分钟"，得到的却是一段 Redis 入门；
- 把最关键的事埋住——唯一的阻塞项混在十条完成项里，breaking change 排在功能列表末尾；
- 为了显得完整，补出没有确认的细节——素材里没有的接口字段、命令、日期，写得像已验证过一样；
- 交接时丢状态——下一个接手的人或下一次 Agent 会话缺少"哪些已验证、哪些不能动、何时该停"，只好重新猜。

Aptum 解决这些问题。它是一次交付前的静默审计：先相信模型原生把任务做完，再检查接收方的下一步是否被支持、决策关键是否容易被漏掉、证据等级是否被写错、交接内容能否安全续接。

## 它不解决什么

- 不是文档模板库——不教 README 或 ADR 长什么样，模型已经会；
- 不是 Humanizer——不追求"像人写的"，不用口语化或错别字伪装；
- 不是固定写作 SOP——不要求每次回答发生变化；原答案已经合适时，Aptum 的正确动作是不动它。

## 推荐模型

**推荐 GLM 5.3 或同等级及以上。** Aptum 刻意保持很薄的规则层，把"怎么写好"交还给模型本身，只保留模型自己不稳定做到的几件事：读者对齐、上下文传递、决策显著度、证据纪律、边界保护。它不为兼容弱模型增加规则。

## 安装

把这句话交给支持 Skills 的 Claude Code 或 Codex：

```text
请替我安装这个 Skill：
https://github.com/Zhong-Ze-Wei/aptum
```

或手动安装：

```bash
# Claude Code
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.claude/skills/aptum

# Codex
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.codex/skills/aptum
```

安装后重新开始会话，让 Agent 重新发现 Skills。

## 什么时候它会生效

存在真实的"上下文转换成本"时：跨角色或跨团队传递信息、交给下一位工程师或下一次 Agent 会话、简化可能丢事实或边界、用户点名要为某类读者适配。普通问答没有信息适配问题时，它不介入。

同一组事实面对不同接收方时信息选择如何变化，见 [examples/audience-variants.md](examples/audience-variants.md)。

Aptum 不替代事实核查、领域判断、项目约定或现有 Style Guide。

## 可选的长期读者模型

Aptum 无需配置即可使用。需要长期个性化时，它可以读取一份由用户确认的本地读者模型（只记录知识边界、表达偏好等会改变信息选择的内容，见 [references/personalization.md](references/personalization.md)）。长期模型不覆盖当前任务，也不会从一次对话静默生成：

```text
使用 Aptum，根据我们的交流生成一份长期读者模型草稿，先让我确认，不要直接保存。
```
