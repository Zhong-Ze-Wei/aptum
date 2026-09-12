# Aptum 版本与演变

本页根据仓库提交和对应文件重建历史，整理日期为 2026-09-12。它说明内容如何变化，不把提交次数当成发布次数，也不补造当时未记录的决策理由。当前生效规则仍以 `SKILL.md` 为准。

## 能确认的版本节点

| 版本 | 快照 | 日期 | 定位依据 |
| --- | --- | --- | --- |
| 0.0.3 | [7e25640](https://github.com/Zhong-Ze-Wei/aptum/commit/7e25640) | 2026-09-03 | README 明确写有 `Version: 0.0.3`；新增长期读者模型协议 |
| 0.1.0 | [180555d](https://github.com/Zhong-Ze-Wei/aptum/commit/180555d) | 2026-09-09 | README 与 SKILL.md 同时标明 0.1.0，已包含此前的核心收缩和版本自检 |
| 0.1.1 | [9c2c4bd](https://github.com/Zhong-Ze-Wei/aptum/commit/9c2c4bd) | 2026-09-12 | 当时已创建发布标签 `v0.1.1` |

`v0.0.3`、`v0.1.0` 是本次依据上述快照补建的历史标签，不代表当时就存在相同标签，也不证明其他分发平台当时发布的是同一产物。0.1.0 的 README 在更早的 [86a4e8d](https://github.com/Zhong-Ze-Wei/aptum/commit/86a4e8d) 已改成对外版本号；这里选择随后两个文件版本一致的提交作为可复现快照。

检查过的 Git 历史没有找到明确标注 0.0.1、0.0.2 的 README 或 SKILL.md。因此保留早期提交名称，不人为给它们分配版本号；这不排除仓库之外曾有其他分发版本。

## 大致经历了哪些变化

| 阶段 | 主要差异 | 查看原始变更 |
| --- | --- | --- |
| 首次入库，未标版本 | 已具备读者、任务与表达判断，包含术语、最小上下文、图表、自然表达及评估材料 | [dadebd4](https://github.com/Zhong-Ze-Wei/aptum/commit/dadebd4) |
| README 简化 | 简化四个场景的展示和安装说明，未改 SKILL.md | [dadebd4 → 4eed28f](https://github.com/Zhong-Ze-Wei/aptum/compare/dadebd4...4eed28f) |
| 术语与对照增强 | 主文件明确先说明结果与因果、按需使用内部代号；README 改成更有区别的读者对照 | [4eed28f → 401ee31](https://github.com/Zhong-Ze-Wei/aptum/compare/4eed28f...401ee31) |
| 项目案例调整 | README 改成三个项目场景，含外部记忆系统示例；这次仅改 README，不代表新增该系统模块 | [401ee31 → 42facaf](https://github.com/Zhong-Ze-Wei/aptum/compare/401ee31...42facaf) |
| 场景泛化 | 加入教学与短期场景边界；不再把作者自己的 AI / 开发知识默认赋给所有用户；强调原答案合适时不改 | [42facaf → d244d9f](https://github.com/Zhong-Ze-Wei/aptum/compare/42facaf...d244d9f) |
| 0.0.3：长期读者模型 | 加入本地档案位置与确认协议；当前任务优先，缺档案不强制初始化，推断不能静默长期化 | [d244d9f → 7e25640](https://github.com/Zhong-Ze-Wei/aptum/compare/d244d9f...7e25640) |
| 0.1.0：收缩核心 | 改为交付前四项审计；写作、视觉和文档细节移到按需参考；增加证据硬门槛与三组评估协议、ADR 和每日版本检查 | [0.0.3 → 0.1.0](https://github.com/Zhong-Ze-Wei/aptum/compare/v0.0.3...v0.1.0) |
| 0.1.0 后的展示更新 | 增加网页与测试档案，README 增加网页入口；此区间没有修改 SKILL.md | [180555d → acc383d](https://github.com/Zhong-Ze-Wei/aptum/compare/180555d...acc383d) |
| 0.1.1：恢复理解目标 | 不再只做交付后审计；补足知识缺口，明确档案读取与场景区分、更新、删除；加入 11 个记忆行为用例 | [本次发布改动](https://github.com/Zhong-Ze-Wei/aptum/compare/acc383d...v0.1.1) |

### 历史里的 0.4.0 是什么

[1a5bcd4 的 README](https://github.com/Zhong-Ze-Wei/aptum/blob/1a5bcd4/README.md) 确实写过 `0.4.0`。随后 [86a4e8d](https://github.com/Zhong-Ze-Wei/aptum/commit/86a4e8d) 将它改成 `0.1.0`，提交说明为首次面向公众的 README。两个节点之间 SKILL.md 没有变化。

据此将 `0.4.0` 记作这段重构历史中的过渡标记，不创建正式 `v0.4.0` 标签，也不伪造从 0.1.1 升级到 0.4.0 的发布顺序。为何当时选用这个过渡数字，现有记录不足以确定。

## 比较版本时怎么读 diff

要看完整仓库变化，用 [0.0.3 → 0.1.0](https://github.com/Zhong-Ze-Wei/aptum/compare/v0.0.3...v0.1.0) 或 [0.1.0 → 0.1.1](https://github.com/Zhong-Ze-Wei/aptum/compare/v0.1.0...v0.1.1)。后者包含中间加入的网页和测试档案；它们体积大，不等于 Skill 行为变化也同样大。

只看方法变化，可以在仓库执行：

```bash
git diff v0.0.3 v0.1.0 -- SKILL.md references/
git diff v0.1.0 v0.1.1 -- SKILL.md references/
```

从内容上看，Aptum 经历了“表达判断范围较广 → 收缩到交付审计 → 恢复理解目标并限定记忆范围”的调整。这个概括描述设计变化，不意味着每一步都已被证明比前一版更好。

重要理由见 [ADR-0001](adr/0001-core-contraction-for-strong-models.md) 和 [ADR-0002](adr/0002-understanding-and-scoped-reader-memory.md)。旧文档的测试表述保留为当时记录；0.1.1 新增的是用例规格，不能当作已完成的独立盲测。
