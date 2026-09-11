# 重构 TODO

> 供应商对接层重构（parser 模块）

- [x] 梳理旧 parser 的全部入口
- [x] 新建 ParserV2 骨架 + 单测框架
- [x] 迁移 CSV 解析（含 quoted 字段）
- [x] 迁移定宽格式解析
- [ ] 迁移 EDI 格式解析（三家里最复杂的一家）
- [ ] 性能对比
- [x] 竞态问题修复
- [ ] 清理旧 parser 死代码

## 备注

- 目标和验收标准见 refactor-plan.md。
- 快收尾了，剩的不多。
