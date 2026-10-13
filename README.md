# Aptum

**适其人，适其事，适其言。**

最新发布版：`0.1.1`；本地开发改动见 [Unreleased](CHANGELOG.md#unreleased)。

Aptum 帮助 AI 根据读者已有的知识，把事情讲清楚：该补的背景补上，该解释的术语解释清楚，关键条件和风险不省略。它是面向 Claude Code / Codex 的表达判断 Skill。

## 为什么需要它

AI 的回答可以很流畅，却依然难懂：默认你知道项目背景，用一串陌生术语解释另一串术语，或者写了很多，却没有说明事情为什么会这样。有时每句话都懂，放在一起却抓不住重点、不知道先做什么，中断后也找不到进度。

Aptum 根据谁在读、这次要理解或完成什么，选择必要的背景、解释深度和表达方式。需要时把操作拆清楚、恢复当前进度、突出决策所需的信息；完整交接仍保留状态和权限边界。

> **这个读者，在这个场景下，需要获得什么信息，才能正确理解或完成接下来的事情？**

## 用了以后有什么不同

| 你遇到的情况 | 合适的表达可以是什么样 |
| --- | --- |
| 听不懂为什么 202 不代表邮件已送达 | “202 只说明任务已接收；实际邮件稍后才由 Worker（处理任务的程序）发送。” |
| 事项很多，不知道先处理哪个 | “先补采购审批：它是下单的前提，且明天截止。报价已齐；参会名单周五才需要。” |
| 讨论中断，忘了迁移做到哪里 | “转换和测试已完成，但没写入生产。当前等产品确认异常数据处理方式，确认前不能继续。” |
| 信息很多，但需要完整比较 | 六种园区分摊方式与各自限制放在同一张表里；保留“自动划分准确率尚未验证”的事实。 |

以上是构造场景的表达示例，不是实测提升结论；对应材料与核对见[场景验证](examples/attention-scenarios.md)。

没有固定的 Aptum 文风。解释、教学、项目汇报、需求文档、README 和代码交接，可能需要不同的信息密度。原答案已经合适时保持不动。

它选择性借鉴了 [i-have-adhd](references/attention.md) 中让信息更容易跟住、行动更容易开始的方法。根据当前需要选用，不要求诊断、固定列表数量或每轮复述进度；也不把一次“跟不上”记成长期标签。

**压缩表达，不压缩思想；简化理解成本，不简化真实问题。**

## 安装

把这句话复制给支持 Skills 的 Claude Code 或 Codex：

```text
请替我安装这个 Skill：https://github.com/Zhong-Ze-Wei/aptum
```

或手动安装，选择对应工具的一条命令：

```bash
# Claude Code
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.claude/skills/aptum

# Codex
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.codex/skills/aptum
```

已有安装不要重复克隆；在安装目录执行 `git pull --ff-only` 更新。安装或更新后重新开始会话。

## 使用

Agent 可在出现知识或上下文缺口、信息难以跟随或不知道如何开始时选择 Aptum；也可以直接点名：

```text
用 Aptum 解释这个方案。不要默认我熟悉这里的基础设施机制，保留必要的术语和风险。
```

```text
用 Aptum 把当前工作写成新 Agent 能接手的说明，保留未验证事项和禁止部署的边界。
```

### 可选：去 AI 味

明确要求“去 AI 味”时，Aptum 会使用内置的完整 [humanizer-zh](references/humanizer-zh.md)，处理空话、重复和模板化表达，同时保留事实、作者语气和技术边界。默认只处理本次内容，不需要另装 Skill。

```text
用 Aptum 给下面这段去 AI 味，保留事实、语气和技术边界，只给我最终稿：
```

模块来源与使用边界见[调用约定](references/humanizing.md)。它不保证通过 AI 检测器。

## 可选：让它记住怎样向你解释

首次使用无需配置，不默认生成画像。需要跨会话记住时，可以说：

```text
用 Aptum 记住：以后向我解释机制时，先说明它实际在做什么，再引入必要术语。
```

档案保存在本机 `~/.config/aptum/reader-profile.md`，当前要求优先，场景写法单独限定范围。可随时要求查看、修改、删除或本次不用；一次追问不会自动变成长期“不懂”的标签。它不后台扫描聊天，也不自动跨设备同步。详见[读者档案规则](references/personalization.md)。

## 示例与验证

[同一事实面向不同读者](examples/audience-variants.md) · [场景验证](examples/attention-scenarios.md) · [行为评估](evals/rubric.md) · [跟随与行动用例](evals/attention.yaml) · [去 AI 味验证](evals/humanizer-zh/README.md)

[在线对照页](https://zhong-ze-wei.github.io/aptum/)保留的是 0.1.0 阶段的测试展示，不代表 0.1.1 的效果。当前不指定最低模型型号，也不保证每次使用都有提升；判断依据应是读者能否理解、关键事实是否保留，而非哪版更像某种文风。

维护者可查看[版本变化](CHANGELOG.md)、[历史差异](docs/version-history.md)与[设计决策](docs/adr/)。
