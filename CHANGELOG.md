# Changelog

记录每个版本对使用者有意义的变化。精确文件差异见各节链接，重要取舍见 ADR。历史条目根据 Git 补记，版本定位依据和未编号迭代见[版本历史](docs/version-history.md)。

## Unreleased

- 统一版本日志，整理早期迭代与版本差异，补记 0.1.1 的决策理由及仓库维护约定。
- 为有明确文件依据的 0.0.3、0.1.0 快照补建历史标签；不移动既有 `v0.1.1`。
- 新增明确启用的去 AI 味模式：随包保留 humanizer-zh 2026-09-23 修订全文、31 类检查点、示例和 MIT 许可证；普通 Aptum 任务不加载，也不依赖另装 Skill。
- 限定当前交付、审阅与写回权限、事实和技术内容保护；一次调用不转成长久偏好。README 增加可复制用法，来源提交与文件校验值单独记录。
- 引入上游 18 个短文本用例和只读文件结构检查，另补 Aptum 的触发、范围切换和理解目标用例。验证范围见[评估说明](evals/humanizer-zh/README.md)，设计理由见 [ADR-0003](docs/adr/0003-opt-in-humanizer-zh.md)。
- 上述改动尚未发布；最近发布版仍为 0.1.1。不以源码完整性或结构检查通过声称模型效果提升。

## 0.1.1 — 2026-09-12

- 恢复理解本身作为交付目标：主动判断陌生术语与隐含知识，补足对象、作用和因果，不限定为成稿后的审计。
- 完善本地读者档案：明确读取时机，区分通用理解习惯与代笔场景；当前反馈优先，长期更新与删除有范围，不自动建立广泛画像。
- README 聚焦理解困难，保留可复制安装句；不再指定最低模型型号，网页旧测试明确属于历史展示。
- 新增 11 个记忆行为用例，评估中分离 Skill 方法与读者档案的影响，不把风格变化直接视为提升。

验证：Skill 格式、版本、UI 元数据、YAML、31 个唯一用例的结构、本地链接、差异空白与隐私隔离检查通过。新增行为用例尚未执行独立模型盲测。个人档案仅在本机迁移、保留备份，未开启自动积累，未进入发布提交；网页发布设置未改变。

[发布提交](https://github.com/Zhong-Ze-Wei/aptum/commit/9c2c4bd) · [此次发布差异](https://github.com/Zhong-Ze-Wei/aptum/compare/acc383d...v0.1.1) · [与 0.1.0 快照的全部差异](https://github.com/Zhong-Ze-Wei/aptum/compare/v0.1.0...v0.1.1) · [ADR-0002](docs/adr/0002-understanding-and-scoped-reader-memory.md)

<details>
<summary>0.1.1 文件变更清单</summary>

| 文件 | 变更 | 目的 |
| --- | --- | --- |
| SKILL.md | 修改 | 加入理解目标与档案入口；版本 0.1.1 存入兼容的 metadata 字段 |
| references/readers.md | 修改 | 区分当前知识证据、教学目的、作者声音与实际读者 |
| references/personalization.md | 修改 | 规定按需读取、范围、来源、确认、更新与删除；限定并发及宿主能力 |
| README.md | 修改 | 产品说明聚焦理解困难，提供可复制安装句，旧网页测试明确标记为历史结果 |
| agents/openai.yaml | 修改 | 发现文案与解释目标一致，保留默认自动选择能力 |
| .gitignore | 修改 | 防止个人档案及本地场景文件误入仓库 |
| evals/cases.yaml、evals/rubric.md | 修改 | 分离方法和记忆的影响，增加理解成本与记录范围评估 |
| evals/reader-memory.yaml | 新增 | 11 个隔离行为用例，覆盖首次使用、场景切换、知识更新、临时偏好、停用、删除与写入冲突 |
| references/foundations.md | 修改 | 记录轻量记忆的来源与取舍，保持为维护者参考 |
| docs/adr/0001-core-contraction-for-strong-models.md | 修改 | 保留历史决策，补充 0.1.1 的修订范围 |

原日志使用了修改提交前的临时哈希 `a3bb1e69` 命名，最终发布提交为 `9c2c4bd`。内容已并入本页，不再按提交哈希生成独立日志；[原文仍保留在 v0.1.1](https://github.com/Zhong-Ze-Wei/aptum/blob/v0.1.1/changelogs/a3bb1e69.md)。

</details>

## 0.1.0 — 2026-09-09

- 核心收缩为交付前四项审计：接收方下一步、决策显著度、证据等级、交接不变量；强调原答案合适时不改。
- 文档写法、术语、自然表达和视觉判断移到按需参考，减少核心约束。个人档案示例改为不预设任何默认知识。
- 评估改为 No Skill / Core / Full 三组比较，增加编造操作性细节直接失败的门槛及决策显著度维度。
- 增加每日最多一次的 Git 版本检查，只通知、不自动更新。README 与 SKILL.md 在 `180555d` 一致标明 0.1.0。

当时的理由与测试表述见 [ADR-0001](docs/adr/0001-core-contraction-for-strong-models.md)，本次未重新运行历史评测。其仅限交付后审计及模型档位约定后来被 0.1.1 部分替代。

[0.0.3 → 0.1.0](https://github.com/Zhong-Ze-Wei/aptum/compare/v0.0.3...v0.1.0)

0.1.0 之后、0.1.1 之前另有网页与测试档案更新，此区间 SKILL.md 未变：[展示更新差异](https://github.com/Zhong-Ze-Wei/aptum/compare/180555d...acc383d)。不将这些提交单独命名为新版本。

## 0.0.3 — 2026-09-03

- 新增长期读者模型协议及本地文件约定：记录知识边界、表达偏好与纠偏要求，当前任务和会话证据优先。
- 明确确认后保存、更新冲突条目、可查看或删除，缺少档案时正常回答，不强制初始化。
- README 标明 0.0.3，提供可选档案说明。

[此次新增协议的差异](https://github.com/Zhong-Ze-Wei/aptum/compare/d244d9f...7e25640) · [从首次入库累计到 0.0.3](https://github.com/Zhong-Ze-Wei/aptum/compare/dadebd4...v0.0.3)

## 更早的未编号迭代

首次入库已包含表达方法、references、examples 和 evals；随后加强术语与内部代号解释、调整 README 场景、加入教学与短期场景边界。没有足够依据将这些提交分别命名为 0.0.1 或 0.0.2，逐次变化见[历史差异表](docs/version-history.md)。
