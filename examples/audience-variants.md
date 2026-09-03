# 同一份事实，四种表达

这个例子验证 Aptum 改变的是信息选择和上下文，而不只是语气。

## 共同事实

通知 API 原先在请求内同步调用邮件供应商。供应商延迟会占住 API worker，并使 p95 达到 2.4 秒。新实现让 API 写入 `notification-jobs` 队列后返回 `202 Accepted`，由 `EmailWorker` 异步发送。首次发送失败后，Worker 最多重试三次，间隔为 10、30、90 秒；第四次调用仍失败的任务进入 `email-dlq`。以 request ID 生成的幂等键保存在 Redis 24 小时，避免客户端重试导致重复发送。API 响应不再表示邮件已经送达，只表示任务已被接受。上线前还缺 DLQ 重放工具和队列积压告警。以上行为由代码和 18 个集成测试验证；生产容量尚未验证。

## 给 AI Agent 的 handoff

> 目标：完成异步邮件发送迁移，但不要发布。
>
> 已完成：`POST /notifications/email` 现在写入 `notification-jobs` 后返回 `202`；`EmailWorker` 调用邮件供应商。首次失败后按 10、30、90 秒最多重试三次，重试耗尽后写入 `email-dlq`。Redis 幂等键 TTL 为 24 小时。相关代码在 `api/notifications.ts`、`workers/email.ts` 和 `infra/queues.ts`。18 个集成测试通过。
>
> 行为边界：`202` 只表示队列已接受任务，不表示邮件已送达。不要恢复同步等待，也不要改变 24 小时幂等窗口；客户端依赖当前 request ID 去重。
>
> 未完成：实现可按 job ID 重放 DLQ 的工具；添加 `notification-jobs` age 和 depth 告警；做生产容量验证。完成定义是这三项有测试或监控证据。没有发布授权。

这里显式保留了文件、状态、不变量、下一步和授权边界；没有解释队列基础知识。

## 给当前用户本人

> 邮件发送已经从“API 等供应商返回”改成“API 先接收任务，后台再发送”。因此接口延迟不再直接受邮件供应商拖累；原先 2.4 秒的 p95（95% 请求不超过的延迟值）问题在架构上被移出了请求链路。
>
> 返回的 `202 Accepted` 现在只表示任务已入队，不表示邮件已经送达。这是最容易误解的变化。首次发送失败后，后台会按 10、30、90 秒间隔最多重试三次；四次调用均失败后，任务进入 DLQ（死信队列，保存无法继续自动处理的任务）。Redis 中 24 小时有效的幂等键会阻止客户端重试造成重复邮件。
>
> 代码和 18 个集成测试已经验证这些行为，但还不能据此判断生产容量。上线前仍需补 DLQ 重放工具和积压告警，否则失败任务能被保存，却不能方便恢复，队列变慢时也可能太晚发现。

这里优先解释现状、变化、真正关键的语义差异、术语和上线影响。

## 给项目内工程师

> `POST /notifications/email` 已从同步 provider call 改为 enqueue-and-ack：写入 `notification-jobs` 后返回 `202`，发送由 `EmailWorker` 完成。重试 backoff 固定为 10/30/90 秒，耗尽后转入 `email-dlq`。Redis idempotency key 的 TTL 保持 24 小时，request ID 仍是去重边界。
>
> 这项改动把 provider latency 和 API worker occupancy 解耦，但也改变了成功语义：`202` 只确认接收，不确认 delivery。18 个集成测试通过；生产 queue depth、consumer throughput 和 provider 限流下的容量仍未验证。合入前还需要 DLQ replay 和 queue age/depth alerts。

这里保留团队术语和高密度机制说明，不解释普遍的异步队列概念。

## 给没有历史上下文的人

> 通知服务负责接收产品发出的邮件请求，并调用外部邮件供应商。过去，这个调用发生在 API 请求内：供应商变慢时，API worker 会一直等待，接口 p95 因此升到 2.4 秒。
>
> 新方案把接收和发送拆开：API 将任务写入 `notification-jobs` 队列并返回 `202 Accepted`，`EmailWorker` 再从队列取出任务发送。下图只表示主要路径：
>
> ```mermaid
> flowchart LR
>     Client --> API
>     API -->|enqueue; return 202| Queue[(notification-jobs)]
>     Queue --> Worker[EmailWorker]
>     Worker --> Provider[Email provider]
>     Worker -->|after initial attempt + 3 retries fail| DLQ[(email-dlq)]
> ```
>
> `202` 表示系统接受了发送任务，并不保证邮件已经送达。Worker 在失败后按 10、30、90 秒间隔重试，最终失败的任务进入 `email-dlq`。Redis 保存 24 小时的幂等键，用于识别客户端重试并避免重复邮件。
>
> 代码和 18 个集成测试已经验证功能行为，但尚未验证生产流量下的处理能力。上线前还需要重放失败任务的工具和队列积压告警。

这里补了模块职责、旧问题、变化原因和系统关系，使结论不依赖此前讨论。

## 比较

| 读者 | 增加的信息 | 主动省略的信息 |
|---|---|---|
| AI Agent | 文件、完成状态、不变量、授权、完成定义 | 通用概念教学 |
| 当前用户 | 前后变化、关键语义、术语、取舍、上线影响 | 文件级执行细节 |
| 项目内工程师 | 机制、接口语义、容量边界、工程待办 | 项目和队列基础背景 |
| 无历史上下文者 | 模块职责、历史问题、因果、结构图 | 完整项目沿革和代码路径 |
