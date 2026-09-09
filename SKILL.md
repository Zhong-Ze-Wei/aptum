---
name: aptum
description: >-
  Use when audience, downstream action, context transfer, or evidence
  boundaries materially change what information should be selected or stated:
  cross-role or cross-team communication, handoffs to the next engineer or
  Agent session, summaries where simplization could drop facts, risks, states,
  or boundaries, and explicit reader-adaptation requests. Works as a silent
  pre-delivery audit on top of the model's native answer, not as a writing
  SOP; ordinary answers with no real reader/context gap do not trigger it.
  Aptum preserves truth and does not replace domain reasoning or source
  verification.
metadata:
  short-description: 适其人，适其事，适其言
---

# Aptum

**适其人，适其事，适其言。**

Aptum 不参与"答案怎么想出来"。它是交付前的一次静默审计：默认相信模型的原生能力先正常完成任务，然后只检查几类真实风险——接收方拿没拿到改变其下一步的信息、决策关键有没有被埋、证据等级有没有被表达改变、交接状态会不会丢。没有发现实质问题，就不改写。

## 何时介入

只在存在真实的信息适配问题时介入。以下任一因素会实质改变应该选择什么信息：

- 接收方与当前作者掌握的上下文明显不同；
- 信息要从一个团队或角色传给另一个角色；
- 接收方拿到内容后需要做决定或执行动作；
- 当前上下文要交给下一位工程师或下一次 Agent 会话；
- 简化、总结、改写可能丢失重要事实、风险、状态或边界；
- 用户明确要求针对某类读者适配。

普通问答（例如简单解释一个技术概念）没有明显 reader/context gap 时，让模型正常回答，不启动额外方法论。

## 工作方式：先解题，后审计

默认信任模型自身能力完成任务。Aptum 不是生成答案的流程，不规定判断读者、判断任务、判断术语、选择结构、humanize、画图或 review 的步骤，没有 SOP。模型先正常解决问题，交付前只审计四件事：

1. 接收方的下一步是否被支持；
2. 最可能改变决策的信息是否容易被漏掉；
3. 证据等级是否被表达改变；
4. 交接内容是否可安全续接（如适用）。

## 审计一：接收方的下一步

身份（管理者、工程师、测试、运营）只是弱先验。真正要判断的是：**这个接收者拿到信息后，要理解什么、判断什么、决定什么、执行什么？** 然后只补充会改变其行动的信息。

- 测试同学需要的往往不只是"Redis 是什么"，而是怎么重置状态避免每轮干等 15 分钟；
- 管理者需要的是哪个问题正在阻塞、需要他拍什么板；
- 下一会话的 Agent 需要的是当前状态、已知差异、禁止事项和什么时候应该停下；
- 分析师需要的是"金额单位是分"会怎样影响 SQL 和报表，而不是字段定义本身。

读者判断的优先顺序与弱先验用法见 [references/readers.md](references/readers.md)。

## 审计二：决策显著度

找出最可能改变接收方下一步决策、行动或风险判断的信息，让它不容易被漏掉。这是目标，不是格式规定。不同交付物有不同实现：周报里可能是"需要决策 / 阻塞项"，release note 里可能是"升级须知 / breaking change"，技术债清单可能通过优先级排序体现，汇报第一屏给风险和需要拍板的事，handoff 第一句就是下一步。形式由模型根据内容自行决定。

## 审计三：证据等级（硬约束）

表达可以改变，证据等级不能改变。稳定区分：

- 输入中明确提供或已经验证的事实；
- 由事实做出的推断；
- 模型提出的建议；
- 仍未知、待确认或冲突的信息。

强模型可以利用通用知识帮助解释、分析和提出建议，但不能为了让交付物显得完整，把"通常如此""合理猜测"或"惯例"写成当前项目已经确认的事实。对操作性细节尤其严格：API schema 与响应字段、文件路径、启动命令、配置字段、环境版本、owner、日期、系统状态、权限、数值、测试结果、实际部署方式——输入没给，就不能静默补成事实。

允许："可以采用……""例如……""字段名待接口确认"。
不允许：因为看起来合理，直接写进正式文档。

## 审计四：交接不变量

当内容交给下一位工程师、未来的自己、下一次 AI 会话或其他执行者时，压缩不得丢失：目标、当前状态、已完成、已验证、未完成、已知问题、关键决定及原因、有意的行为差异、风险、权限、禁止修改的范围、停止条件、下一步。

不设固定模板。核心目标只有一条：接手者不需要重新猜，也不会因为缺状态而重复工作、把有意的差异修回去，或越过权限边界。

## 最小干预

Aptum 不要求每次使用都产生可见变化。原答案已经适合当前读者和任务时，保持它。不强行扩写、不强行换标题结构、不强行加术语解释、不强行加表格、不强行画 Mermaid、不强行 humanize，也不为了显示"适配过"而修改本来已经很好的表达。

## 按需读取

默认只加载本文件，其余材料按需：

- 需要读者判断的优先顺序或身份弱先验：[references/readers.md](references/readers.md)
- 需要交付物的高风险遗漏提醒（ADR 复审条件、release note 迁移动作、handoff 停止条件、API 文档不得补造 schema 等）：[references/deliverables.md](references/deliverables.md)
- 用户明确要求润色或自然化、输出已出现明显模板化重复、表达风格本身已阻碍理解时（默认不加载）：[references/prose.md](references/prose.md)
- 用户明确需要视觉化，或图表能显著降低当前读者理解关系、流程、状态或比较的成本时：[references/visuals.md](references/visuals.md)
- 需要建立、读取或修改长期读者模型时：[references/personalization.md](references/personalization.md)
- 同一事实面向不同下游读者的信息选择对照：[examples/audience-variants.md](examples/audience-variants.md)

[references/foundations.md](references/foundations.md) 是维护者文档（原则来源与取舍），正常运行不读取。

## 版本自检（每日至多一次）

本 Skill 安装目录是 git 克隆时：首次介入任务的间隙，若 `~/.config/aptum/.update-check` 不存在或已超过 24 小时，运行 `git -C <安装目录> fetch -q` 并比较 `HEAD` 与 `origin/HEAD`；落后则用一行提示用户可运行 `git -C <安装目录> pull` 更新，然后把当前时间写回该文件。不自动拉取、不中断当前任务；fetch 失败或非 git 安装（复制、平台快照）一律静默跳过。
