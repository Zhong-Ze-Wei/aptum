---
name: aptum
description: >-
  Adapt information when a reader's knowledge, missing context, task, or
  delivery setting changes what needs explaining or preserving. Use for
  explanations obscured by jargon or assumed knowledge, teaching, cross-role
  communication, summaries, and human or Agent handoffs with material context
  gaps. Adjust information and explanation depth without a fixed writing
  template; preserve facts, uncertainty, and action boundaries. Leave already
  suitable answers unchanged. Does not replace domain reasoning or verification.
metadata:
  version: "0.1.1"
  short-description: 适其人，适其事，适其言
---

# Aptum

**适其人，适其事，适其言。**

Aptum 帮助 Agent 判断：**这个读者，在这个场景下，需要获得什么信息，才能正确理解或完成接下来的事情？** 根据读者已有的知识与当前任务，选择背景、解释深度和表达形式，让理解更轻松，同时保留真实问题的条件、复杂性和风险。

压缩表达，不压缩思想；简化理解成本，不简化真实问题。领域推理与事实核查仍由原任务完成，表达判断自然参与解释和交付，不要求先生成一版再执行固定改写流程。

## 何时介入

只在存在真实的信息适配问题时介入。以下任一因素会实质改变应该选择什么信息：

- 接收方与当前作者掌握的上下文明显不同；
- 解释依赖未经确认的知识，或术语、隐含背景、关系不清已经妨碍理解；
- 信息要从一个团队或角色传给另一个角色；
- 接收方拿到内容后需要做决定或执行动作；
- 当前上下文要交给下一位工程师或下一次 Agent 会话；
- 简化、总结、改写可能丢失重要事实、风险、状态或边界；
- 用户明确要求针对某类读者适配。

理解一个概念或建立因果认识，本身就可以是任务目的。普通问答已经清楚、没有实质知识缺口时保持原样；不因文档类型或使用了术语就强行介入。

## 理解与下一步

不要把职业、使用过的术语、作者自己知道的背景，直接当成读者已经掌握的知识。一个领域的熟练不能外推到另一个领域。根据当前问题和反馈判断，长期记录只提供可修正的背景。

缺口妨碍理解时，补足最小的对象、作用或因果关系：谁在做什么，为什么如此，对当前问题有什么影响。能用普通语言准确说清就直接说；必要的真实术语保留，陌生术语在当前语境里顺手解释，不用另一个陌生术语解释它，也不从头讲通识课程。类比只用来搭桥，随后回到真实系统。

身份只是弱线索。判断接收方要理解、决定或执行什么，据此取舍信息；不需要支持一个立即动作，才能保留有助于理解的解释。读者判断、教学和代笔的区别见 [references/readers.md](references/readers.md)。

## 本人的读者档案

未指定读者时默认当前用户本人。本次上下文首次使用 Aptum 且主要读者是本人时，按 [references/personalization.md](references/personalization.md) 读取存在的 `~/.config/aptum/reader-profile.md`；当前上下文已有有效内容就复用。替本人代笔时仅选适用的写作场景规则，解释深度仍以实际读者为准。

文件不存在、不可访问或本次明确不用档案时正常回答，不要求初始化。当前要求与反馈优先；识别到知识缺口可以当场调整，但不得自动把临时受众或推断写成长期偏好。建立、修改或删除档案前读取个性化参考；私人内容不随 Skill 发布。

## 关键信息的显著度

找出最可能改变接收方下一步决策、行动或风险判断的信息，让它不容易被漏掉。这是目标，不是格式规定。不同交付物有不同实现：周报里可能是"需要决策 / 阻塞项"，release note 里可能是"升级须知 / breaking change"，技术债清单可能通过优先级排序体现，汇报第一屏给风险和需要拍板的事，handoff 第一句就是下一步。形式由模型根据内容自行决定。

## 证据等级（硬约束）

表达可以改变，证据等级不能改变。稳定区分：

- 输入中明确提供或已经验证的事实；
- 由事实做出的推断；
- 模型提出的建议；
- 仍未知、待确认或冲突的信息。

强模型可以利用通用知识帮助解释、分析和提出建议，但不能为了让交付物显得完整，把"通常如此""合理猜测"或"惯例"写成当前项目已经确认的事实。对操作性细节尤其严格：API schema 与响应字段、文件路径、启动命令、配置字段、环境版本、owner、日期、系统状态、权限、数值、测试结果、实际部署方式——输入没给，就不能静默补成事实。

允许："可以采用……""例如……""字段名待接口确认"。
不允许：因为看起来合理，直接写进正式文档。

## 交接不变量

当内容交给下一位工程师、未来的自己、下一次 AI 会话或其他执行者时，压缩不得丢失：目标、当前状态、已完成、已验证、未完成、已知问题、关键决定及原因、有意的行为差异、风险、权限、禁止修改的范围、停止条件、下一步。

不设固定模板。核心目标只有一条：接手者不需要重新猜，也不会因为缺状态而重复工作、把有意的差异修回去，或越过权限边界。

## 最小干预

Aptum 不要求每次使用都产生可见变化。原答案已经适合当前读者和任务时，保持它。不强行扩写、不强行换标题结构、不强行加术语解释、不强行加表格、不强行画 Mermaid、不强行 humanize，也不为了显示"适配过"而修改本来已经很好的表达。

## 按需读取

除上述适用的本地档案外，其余材料按需，不全量加载：

- 需要知识边界判断、教学或代笔适配：[references/readers.md](references/readers.md)
- 需要交付物的高风险遗漏提醒（ADR 复审条件、release note 迁移动作、handoff 停止条件、API 文档不得补造 schema 等）：[references/deliverables.md](references/deliverables.md)
- 用户明确要求润色或自然化、输出已出现明显模板化重复、表达风格本身已阻碍理解时（默认不加载）：[references/prose.md](references/prose.md)
- 用户明确需要视觉化，或图表能显著降低当前读者理解关系、流程、状态或比较的成本时：[references/visuals.md](references/visuals.md)
- 需要建立、读取或修改长期读者模型时：[references/personalization.md](references/personalization.md)
- 同一事实面向不同下游读者的信息选择对照：[examples/audience-variants.md](examples/audience-variants.md)

[references/foundations.md](references/foundations.md) 是维护者文档（原则来源与取舍），正常运行不读取。

## 版本自检（每日至多一次）

本 Skill 安装目录是 git 克隆时：首次介入任务的间隙，若 `~/.config/aptum/.update-check` 不存在或已超过 24 小时，运行 `git -C <安装目录> fetch -q` 并比较 `HEAD` 与 `origin/HEAD`；落后则用一行提示用户可运行 `git -C <安装目录> pull` 更新，然后把当前时间写回该文件。不自动拉取、不中断当前任务；fetch 失败或非 git 安装（复制、平台快照）一律静默跳过。
