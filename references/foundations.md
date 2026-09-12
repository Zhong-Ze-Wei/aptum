# 研究基础与取舍

**维护者文档，正常运行不读取。** 本文件记录 Aptum 借鉴了什么，以及刻意没有继承什么。SKILL.md 仅提供维护入口，不要求任务运行时加载。

## 0.1.1：理解与小型记忆

0.1.1 将理解本身保留为交付目的，不只检查是否支持下游动作。读者档案采用少量、有范围、可修正的当前条目；没有档案也必须正常工作。私人内容与公共 Skill 分离，场景声音不决定跨场景解释深度。

2026-09-12 核对的参考：

- [Hermes Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)：借鉴用户文件与一般记忆分离、小容量和替换删除，不引入全量自动积累。
- [OpenClaw User model](https://docs.openclaw.ai/concepts/user-model)：借鉴可执行偏好和原处更新；活动档案仅保留当前规则，避免携带矛盾历史。
- [Claude Code memory](https://code.claude.com/docs/en/memory)：借鉴精简主档和按需主题文件；宿主加载能力不能当成普通 Skill 自带能力。
- [PrefEval](https://arxiv.org/abs/2502.09597) 与 [HorizonBench](https://arxiv.org/abs/2604.17283)：分别验证识别、记忆、应用和偏好更新，而非以“存过”代表“用对”。不将其他任务或旧模型成绩迁移为 Aptum 的效果结论。

## 采用的原则

- Google Technical Writing 的 audience 模型把文档内容理解为“读者完成任务所需知识”与“已有知识”的差额。Aptum 将角色、技术熟悉度、项目距离和接触时间都视为读者模型的一部分。
- Google Developer Documentation Style Guide 强调定义受众可能陌生的术语、保持术语一致、把条件放在指令之前，并让文档服务用户目标。Aptum 采用这些原则，但不把主动语态或短句绝对化。
- Diátaxis 区分 tutorial、how-to、reference 和 explanation，说明文档形式由读者任务决定。Aptum 把它作为交付物判断工具，不强迫一个现实文档只能使用单一模式。
- `blader/humanizer`、`humanizer-zh`、`stop-slop` 和 plain-writing 类 Skill 对填充语、机械反转、虚假强调、同节奏句群、宣传腔和无效总结的观察很有用。Aptum 将这些模式视为“没有做出内容取舍”的症状。
- Vercel eve 的 technical-writing Skill 把源代码、测试和当前行为放在文风之前，并要求 Agent 与开发者都能检索和行动。Aptum 继承“技术主张先验证”和“machine completeness 不要求 human unreadability”的方向。
- 2025 年的 *Measuring AI "Slop" in Text* 发现，二元 slop 判断有主观性，相关性、连贯性和结构等维度会随领域变化。Aptum 因此不以禁词数量或固定总分代表质量。

## 没有采用的做法

- 不禁止所有副词、被动语态、破折号、类比、三项列表或某一词表。这些形式有时承担精确的技术功能。
- 不要求每次输出展示 audience 分析、评分表或修改步骤。方法应影响结果，不应成为额外仪式。
- 不把“像人”定义为口语、错别字、随意结构或强制个人观点。参考文档、事故说明和接口契约可以保持克制。
- 不把“plain”理解为删除术语和复杂性。术语只要真实、必要并被适度解释，就比含糊替代词更清楚。
- 不无差别要求图。视觉表达必须与媒介和关系匹配。

## 主要来源

访问日期：2026-09-02。

- Google Technical Writing, Audience: <https://developers.google.com/tech-writing/one/audience>
- Google Technical Writing, Words: <https://developers.google.com/tech-writing/one/words>
- Google Technical Writing, Documents: <https://developers.google.com/tech-writing/one/documents>
- Google Developer Documentation Style Guide, Voice and tone: <https://developers.google.com/style/tone>
- Diátaxis: <https://diataxis.fr/>
- Mermaid documentation: <https://mermaid.js.org/intro/>
- Humanizer: <https://github.com/blader/humanizer>
- Stop Slop: <https://github.com/hardikpandya/stop-slop>
- Plain Writing Skill: <https://github.com/docwriter-org/plain-writing-skill>
- Vercel eve technical-writing Skill: <https://github.com/vercel/eve/tree/main/.agents/skills/technical-writing>
- Shaib et al., *Measuring AI "Slop" in Text*: <https://arxiv.org/abs/2509.19163>
