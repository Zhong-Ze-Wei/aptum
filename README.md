# Aptum

**适其人，适其事，适其言。**

Aptum 是一个面向 Claude Code、Codex 等 Agent 的表达判断 Skill。

它不只是润色或“去 AI 味”，而是帮助 Agent 判断：面对当前读者和任务，哪些信息必须保留，哪些背景需要补充，术语解释到什么程度，以及什么结构最容易理解。

> 这个读者，在这个场景下，需要获得什么信息，才能正确理解或完成接下来的事情？

## 它解决什么问题

- 给 Agent 的 handoff 缺少状态和边界，接手后只能重新调查。
- 给工程师的说明重复基础知识，却没有接口、故障和迁移约束。
- 给用户的回复堆满术语，没有解释变化、原因和实际影响。
- 为了简短而删掉关键事实，或者为了完整而堆入无关背景。

Aptum 追求合适的信息密度：压缩表达，不压缩思想；简化理解成本，不简化真实问题。

## 四个真实场景

### 1. 同一段代码，面对不同读者

事实：`claimIdempotencyKey()` 使用 Redis `SET NX EX`，幂等键保留 24 小时。若先 `GET` 再 `SET`，并发 Worker 可能重复发送邮件。

| 写给当前用户 | 写给项目工程师 |
|---|---|
| `SET NX EX` 把“检查 request ID”和“写入 request ID”合成一次原子操作。若先 `GET` 再 `SET`，两个 Worker 可能同时认为任务未处理，于是各发一封邮件。<br><br>24 小时 TTL（过期时间）是产品的重复提交窗口；缩短它会改变外部行为。 | `claimIdempotencyKey()` 使用 `SET key value NX EX 86400`，避免 `GET`/`SET` 之间的 TOCTOU race。TTL 是 request ID 的业务去重窗口，不是 cache tuning 参数。 |

同一份事实，前者补充术语、因果和用户影响，后者保留工程师需要的精确术语和信息密度。

### 2. Agent handoff

| 模糊 handoff | 使用 Aptum |
|---|---|
| 数据库迁移基本完成了，测试大部分通过。接下来补一下剩余部分，然后发布。 | **目标**：把 `users.email` 改为 `NOT NULL`，当前没有发布授权。<br><br>**已完成**：回填脚本处理了 92% 的空值记录；24 个 repository 测试通过。<br><br>**阻塞**：仍有 18,420 条记录无法推导邮箱，现在执行 `SET NOT NULL` 会失败。<br><br>**下一步**：运行 dry-run 脚本生成租户清单，等待产品决定处理规则；确认前不要部署。 |

右侧让新 Agent 不依赖此前 conversation，也能知道状态、证据、风险、下一步和停止条件。

### 3. ADR 中的事实、推断和决定

| 混在一起 | 使用 Aptum |
|---|---|
| 我们将邮件发送改成队列，因为新架构会解决接口延迟问题，并显著提高系统可靠性。 | **事实**：同步调用供应商时，API 的 p95 延迟为 2.4 秒。<br><br>**决定**：API 入队后返回 `202`，由 Worker 异步发送。<br><br>**推断**：这应能降低 API worker 占用，但尚未进行生产压测。<br><br>**后果**：`202` 只表示任务已接受，不再表示邮件已送达。 |

右侧没有把预期收益写成已经验证的结果，也保留了接口语义变化。

### 4. 架构关系是否需要视觉化

| 连续文字 | 使用 Aptum |
|---|---|
| Webhook API 验证签名后写入 inbox，再返回 `202`。Consumer 读取事件并调用 Billing。失败后会重试，最终进入 DLQ。 | **主路径**：`Sender → API → Inbox → Consumer → Billing`<br><br>**去重**：Inbox 对 event ID 有唯一约束；Consumer 调用 Billing 时继续传递 event ID 作为幂等键。<br><br>**失败**：重试耗尽后进入 DLQ，不会自动恢复。<br><br>**接口语义**：`202` 只确认事件已持久化。 |

Aptum 不机械要求画图。这里关系不多，紧凑结构比完整架构图更合适；当组件、状态或分支继续增加时，再使用 Mermaid。

## 适用场景

README、CLAUDE.md、AGENTS.md、ADR、RFC、需求文档、技术方案、Issue、PR、Agent handoff、代码解释和复杂技术问题分析。

## 安装

Claude Code：

```bash
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.claude/skills/aptum
```

Codex：

```bash
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.codex/skills/aptum
```

同时使用两个客户端时，可以只保留一份仓库，再创建软链接：

```bash
git clone https://github.com/Zhong-Ze-Wei/aptum.git ~/.codex/skills/aptum
ln -s ~/.codex/skills/aptum ~/.claude/skills/aptum
```

安装后重新打开客户端或开始新会话，让 Agent 重新发现 Skills。

## 使用

直接告诉 Agent 读者和任务：

```text
使用 Aptum，把这次缓存改动解释给懂后端开发、但不熟悉 Redis 一致性模型的用户。
```

```text
使用 Aptum，把当前进度写成一个新 Agent 可以直接继续的 handoff。
```

Aptum 不替代事实核查、项目术语或已有 Style Guide。它负责让正确的信息，以适合当前的人、当前的事、当前场景的方式抵达。
