# orders 表数据字典 v2

> 更新：2026-08-20。本版覆盖迁移后的新结构。

| 字段 | 类型 | 说明 |
|---|---|---|
| order_id | bigint | 订单号（雪花 ID） |
| user_id | bigint | 用户 ID |
| amount | bigint | 订单金额，**单位：分** |
| status | varchar | 订单状态：pending / paid / refunded / refund_pending |
| created_at | datetime | 下单时间（UTC+8） |

## 备注

- status 枚举以线上实际为准，历史上还有过几个中间态，没全部列进来。
- 本字典只覆盖核心 5 字段，其余字段（优惠券、渠道等）待补。
