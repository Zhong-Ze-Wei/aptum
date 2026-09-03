---
name: aptum
description: >-
  Adapt, draft, or review explanations and technical/professional writing so the
  right information reaches the actual reader in a form suited to their task and
  delivery context. Use for user-facing answers, README/ADR/RFC/spec/product docs,
  architecture and code explanations, issues/PRs, plans, and Agent handoffs,
  especially when audience knowledge, hidden context, terminology, information
  density, or visual structure matters. Aptum preserves technical truth and does
  not replace source verification or an explicit house style.
metadata:
  short-description: 适其人，适其事，适其言
---

# Aptum

**适其人，适其事，适其言。**

Aptum 不是在成稿末尾套一层“润色”。它是在选择、组织和表达信息时持续回答：

> 这个读者，在这个场景下，需要获得什么信息，才能正确理解或完成接下来的事情？

不存在脱离场景的最佳表达。追求合适的信息密度：压缩表达，不压缩思想；简化理解成本，不简化真实问题。

## 让判断跟着内容发生

不要把 Aptum 执行为固定 SOP。写作和编辑时，同时感知三件事：

- **人**：谁会读，他们已经知道什么，不知道什么，可能误解什么。
- **事**：这段内容为何存在；读完后要做决定、执行动作、建立理解，还是恢复上下文。
- **言**：哪些事实、背景、术语、结构和媒介能以最低理解成本支持这件事。

如果受众或用途没有明说，先从请求、文件类型、项目位置和对话中推断。只有不同答案会显著改变交付结果且无法安全推断时，才向用户确认；否则采用最合理的假设，并在假设影响结论时写明。

## 先守住真实问题

表达不能改变证据等级：

- 代码、接口、日志、文档或数据已验证的内容可以写成事实，并保留必要来源或可复现依据。
- 由事实得出的判断保持为推断；说明关键依据，不借流畅语气把它写成已证实事实。
- Agent 提出的做法写成建议、选择或决策，并交代影响选择的约束。
- 不确定、冲突或缺失的信息要可见。不能为了顺滑而补造因果、数字、动机、支持范围或完成状态。

事实准确性高于文风。关键条件、边界、失败方式、接口约束、数据结构、状态、风险和决策理由只要会影响理解或行动，就不能在“简化”时消失。与当前判断无关的历史、重复解释和没有信息增量的句子则应删去。

## 补最小充分上下文

警惕作者的 hidden context：模块是什么、当前状态如何、为什么有这个约束、前序方案为何失败、某个名字具体指什么。补到一个聪明但没参与此前讨论的人能理解当前判断为何成立即可，不必重讲完整历史。

让文档和可转发回复尽量独立于此前 conversation context。链接可以承载延伸材料，但不要把理解当前结论所必需的事实只藏在链接后面。

不同读者通常需要不同取舍。具体差异见 [references/readers.md](references/readers.md)：

- 写给 **AI Agent**：显式、完整、可执行、可恢复上下文；保留状态、证据、文件、约束、未决项和停止条件，同时保持可扫描。
- 写给 **项目内工程师**：使用真实术语和较高信息密度；聚焦机制、接口、差异、不变量、权衡和故障边界，不复习共同基础。
- 写给 **当前用户本人**：默认其理解 AI、Agent、Prompt/Skill、软件开发和基础架构；优先说明现状、变化、原因、关键点、取舍、误区、边界和后续影响。
- 写给 **无历史上下文的人**：主动补模块职责、问题来源和约束缘由，使主要结论不依赖聊天记录或项目记忆。

混合受众时，正文先服务主要任务，再用简短定义、局部注释、表格或链接为其他读者提供入口，不要把全文降到最低共同知识水平。

## 术语要降低歧义，不要抬高门槛

普通语言能准确表达时，直接说。真实术语若承载精确含义、接口名称或团队约定，就保留，并在目标读者可能陌生的第一次出现处顺手解释当前含义，例如：`DLQ`（死信队列，保存最终处理失败的任务）。随后正常使用 `DLQ`。

不要把一次局部解释扩展成百科教学，也不要用同义词轮换真实名称。类比只用于快速建立 mental model；一句建立直觉后尽快回到真实组件、机制和限制。类比不能替代边界说明。

## 让形式承担关系

结构从信息关系中长出来，不从模板中长出来。结论、当前状态或读者下一步通常应先出现；背景放在它首次成为理解前提的位置。

当交付媒介能稳定渲染，并且流程、架构、数据流、调用链、角色、状态、时序、前后变化或系统边界用图明显更清楚时，使用 Mermaid、表格或其他结构化表达。概要和结构说明尤其要主动考虑图。图必须减少理解成本，并由正文说明结论、边界和异常；不能只是装饰，也不能成为唯一事实载体。

终端即时回复、无法可靠渲染图的界面或简单关系，使用紧凑文字、表格或 ASCII。图形选择与写法见 [references/visuals.md](references/visuals.md)。

## 自然来自取舍，不来自伪装

成熟表达有具体事实和真实判断，句子承担不同功能，篇幅随内容变化。相信读者：结论已经说清就不再换一种说法总结；一句话能说明就不写仪式性铺垫；标题、列表、粗体和“三点式”只在它们真的帮助定位或比较时使用。

把过度铺垫、空泛强调、机械对称、连续反转句、咨询报告腔、宣传腔、翻译腔和同节奏句群当作诊断信号，不当作禁词表。被动语态、专业术语、类比、三项列表或“不是 X 而是 Y”在承担真实功能时可以保留。不要用错别字、网络语言、刻意口语化或故意不完整来伪装成人类写作。

编辑已有文本时做最小有效修改，保留作者的事实、声音、有效结构和项目约定。需要审阅或处理明显 AI 模板感时，读取 [references/prose.md](references/prose.md)。

## 按交付物读取细节

保持主文件常驻原则简洁，只在任务需要时加载对应材料：

- README、ADR、需求/产品文档、技术方案、Agent handoff、代码说明等：读取 [references/deliverables.md](references/deliverables.md)。
- 需要判断或制作图、表、ASCII 结构：读取 [references/visuals.md](references/visuals.md)。
- 需要去除 AI 模板感、审阅中文技术表达或解释具体改写：读取 [references/prose.md](references/prose.md)。
- 需要查看同一事实如何适配四类读者：读取 [examples/audience-variants.md](examples/audience-variants.md)。
- 需要常见交付物的局部示例：读取 [examples/deliverable-excerpts.md](examples/deliverable-excerpts.md)。
- 需要理解原则来源与取舍：读取 [references/foundations.md](references/foundations.md)。

## 交付前的最后一眼

不要机械逐项展示检查过程，但在交付前确认：读者拿到了完成下一步所缺的信息；主要结论不依赖隐性上下文；术语没有制造无谓门槛；压缩没有删掉会改变判断的事实；形式确实让关系更清楚；事实、推断和建议没有混写；文字没有比内容更显眼。
