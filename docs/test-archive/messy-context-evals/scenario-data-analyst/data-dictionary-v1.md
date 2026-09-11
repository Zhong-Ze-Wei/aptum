# orders 表数据字典

> 更新：2026-05-11

| 字段 | 类型 | 说明 |
|---|---|---|
| order_id | bigint | 订单号 |
| user_id | bigint | 用户 ID |
| amount | bigint | 订单金额，单位：元 |
| status | varchar | 订单状态：pending / paid / refunded |
| created_at | datetime | 下单时间 |

## 使用建议

- 金额直接 SUM 即可。
- 业务报表一般用 paid 口径。
