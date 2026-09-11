# orders 迁移日志（0814）

- 08-14 22:00 开始，08-15 03:40 结束，旧库 → 新库。
- 结构变更：amount 由元改为**分**（整数存储）；order_id 换雪花 ID；status 增加 refund_pending 中间态。
- 遗留问题：约 3% 的 2026 年以前老订单 amount 为 NULL（旧库本来就缺），未迁成功，等专项补数。做全时段统计时注意。
- 迁移后字典见 data-dictionary-v2。旧字典（v1）已过时。
