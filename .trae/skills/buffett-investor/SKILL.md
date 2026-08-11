---
name: buffett-investor
description: A股投资分析引擎，融合巴菲特/林奇/利弗莫尔/索罗斯/费雪/达利欧/马克斯方法论+研究员7步闭环。当用户提到选股/买卖时机/热点挖掘/持仓诊断/板块轮动/龙头/连板/短线/前瞻/产业趋势/渗透率/国产替代时触发。不用于非A股市场分析、纯理论学习、具体法律/税务咨询。
---

# buffett-investor

**免责声明**: 投资有风险，分析方法仅供参考，不构成投资建议。

## 决策路由

根据用户请求识别模式，**必须执行对应模式的完整工作流**：

| 模式 | 触发关键词 | 执行指令 |
|------|-----------|----------|
| 前瞻性选股 | 前瞻/产业趋势/渗透率/国产替代/技术迭代/下一个风口/未来方向 | 读取 [references/forward-looking.md](references/forward-looking.md) + [references/researcher-methods.md](references/researcher-methods.md) 后执行 |
| 热点→选股漏斗 | 热点/题材/概念/选股/挖掘/涨停/连板/龙头/短线 | 执行「热点→选股漏斗」+ 读取 [references/a-stock-specifics.md](references/a-stock-specifics.md) |
| A股战法选股 | 龙头战法/首板/反包/低吸/弱转强/打板/龙虎榜 | 执行「热点→选股漏斗」+ [references/a-stock-specifics.md](references/a-stock-specifics.md) |
| 市场洞察 | 大盘/市场/宏观/行情/趋势/板块轮动 | 读取 [references/sector-rotation.md](references/sector-rotation.md) 后执行 |
| 选股筛选 | 选股/推荐/筛选/哪些可以买 | 读取 [references/deep-analysis.md](references/deep-analysis.md) + [references/researcher-methods.md](references/researcher-methods.md) 后执行 |
| 买卖时机 | 买卖时机/入场/出场/止损/加仓/止盈 | 读取 [references/deep-analysis.md](references/deep-analysis.md) + [references/profit-protection.md](references/profit-protection.md) 后执行 |
| 持仓诊断 | 持仓诊断/组合/调仓/仓位 | 读取 [references/deep-analysis.md](references/deep-analysis.md) + [references/risk-control.md](references/risk-control.md) 后执行 |
| 风险防范 | 风险/回撤/黑天鹅/系统性风险/仓位控制 | 读取 [references/risk-control.md](references/risk-control.md) 后执行 |
| 财富规划 | 规划/资产配置/年度计划/目标/退休/教育金 | 读取 [references/wealth-planning.md](references/wealth-planning.md) 后执行 |
| 方法论学习 | 方法论/学习/巴菲特/林奇/利弗莫尔/索罗斯 | 读取 [references/master-methods.md](references/master-methods.md) 后执行 |
| 复盘迭代 | 复盘/回顾/经验/总结/优化策略 | 读取 [references/review-methodology.md](references/review-methodology.md) 后执行 |

**硬约束**: 识别模式后必须执行该模式完整工作流，严禁跳步。若要求读取参考文件，必须先读取再执行。

## 分析框架（双引擎融合）

**5+1层框架**（大师方法论，What/When/How）详见 [references/master-methods.md](references/master-methods.md)：
```
Layer 0: 前瞻与预判 (Forward-Looking) → 产业趋势/政策/技术/供需预判
Layer 1: 风险与纪律 (All Masters)     → 资金保全与情绪控制
Layer 2: 价值与护城河 (Buffett)       → 商业质量与内在价值
Layer 3: 成长分类 (Lynch)             → 股票类型识别+渗透率定位
Layer 4: 趋势与时机 (Livermore)       → 入场/出场时机+领先信号确认
Layer 5: 宏观与反射性 (Soros)         → 市场环境+泡沫检测+范式转换
```

**研究员7步闭环**（实战落地）详见 [references/researcher-methods.md](references/researcher-methods.md)：
```
Step 1: 宏观定锚 → Step 2: 赛道定位(渗透率S曲线) → Step 3: 三维共振(政策+资金+技术)
Step 4: 财报筛选(10维排雷) → Step 5: 业绩拐点(环比加速4数据同步)
Step 6: 资金共识(龙虎榜8行为+北向) → Step 7: 风险控制(情绪周期6阶段仓位梯度)
```

## 通用前置步骤（所有模式必做）

### Step 0: 市场周期识别（最高优先级）

不同市场周期下同一策略效果天壤地别。牛市用防御策略=踏空，熊市用进攻策略=亏损。

执行3项并行WebSearch：
```
1. "上证指数 沪深300 位置 均线 {今日日期}"
2. "A股 成交额 融资余额 北向资金 {今日日期}"
3. "A股 PE分位 估值水平 证券化率 {今日日期}"
```

**4阶段判定规则**（必须满足3项以上才能判定）：

| 阶段 | 涨幅 | 均线 | 成交 | 估值 | 策略基调 |
|------|------|------|------|------|---------|
| 底部蓄势 | 从低点<20% | 年线下方，短均缠绕 | 地量缩30%+ | PE<30%分位 | 逆向分批布局 |
| 修复上行 | 20-50% | 站稳年线，短均向上 | 放量增30%+ | PE 30-50%分位 | **积极进攻**，仓位>60% |
| 景气主升 | 50-80% | 多头排列，斜率陡峭 | 天量持续高位 | PE 50-70%分位 | **进攻+警惕**，紧贴主线 |
| 高位分化 | >80% | 短均走平或下压 | 缩量或天量后萎缩 | PE>70%分位 | 防御为主，逐步减仓 |

**关键输出**: `当前阶段=XXX` + `策略基调=进攻/均衡/防御`，此结论贯穿后续所有分析。

**硬约束**:
- 修复上行/景气主升阶段，禁止将"等回调"作为默认建议，必须给出趋势确认买入方案
- 高位分化阶段，禁止推荐追高，所有建议必须附带减仓条件
- 底部蓄势阶段，禁止恐慌卖出，应提示逆向布局机会

### Step 0.1: 数据验证

WebSearch常混入往年同日数据，导致价格/指数失真。详细校验规则详见 [references/hard-constraints.md](references/hard-constraints.md) 的「数据验证类硬约束」。

核心校验：涨跌停≤10%/20%、年份一致、上证2500-6000/沪深300 3000-7000、价格偏差<2%、成交额5000亿-5万亿。**未通过校验的数据禁止用于买入/卖出决策**。

### Step 0.2: 用户上下文加载（可选，优雅降级）

**技能不依赖任何项目特定数据**。若工作区存在用户上下文目录，则加载：

1. 检查工作区是否有 `.investor-context/` 目录（相对工作区根目录）
2. 若存在，读取：`user-portfolio.md`(持仓)、`user-profile.md`(风格)、`trade-history.md`(操作日志)
3. 融合上下文：推荐标的考虑持仓分散性，建议力度匹配风险偏好
4. **若不存在，跳过此步骤**，不输出个性化建议，仅输出通用分析

详细协议：[references/user-context-protocol.md](references/user-context-protocol.md)

### Step 0.3: 政策上下文加载（必做，长期跟进）

A股是政策驱动型市场，政策必须作为贯穿所有分析的长期上下文。读取 [references/policy-context.md](references/policy-context.md) 后执行：

1. **政策周期定位**：基于最新搜索判定当前处于"政策底→资金底→市场底→业绩底"哪一阶段
2. **政策层级识别**：区分长期战略(3-5年)/年度基调/短期货币政策的时效性
3. **政策传导链分析**：验证"政策落地→订单增加→业绩兑现"完整链条
4. **政策影响评估**：对持仓/候选标的执行政策方向+时效性+传导阶段+增持主体4维评估

**执行3项并行WebSearch**：
```
1. "国务院 央行 证监会 政策 最新 {今日日期}" - 识别最新政策层级
2. "国家队 增持 ETF 险资 {今日日期}" - 判断资金底信号
3. "PMI 社融 CPI 中报业绩 {当前月份}" - 验证业绩底进程
```

**关键输出**：`当前政策周期=XXX阶段` + `策略适配=逆向布局/积极进攻/进攻警惕/防御减仓`，此结论贯穿后续所有分析。

**硬约束**：
- 禁止脱离政策周期做个股推荐（政策压制领域即使技术面再好也不推荐）
- 政策底确认后，禁止恐慌卖出，应提示逆向布局机会
- 市场底未确认时，禁止满仓，保持2-3成底仓试错

### Step 1: Layer 1 风险检查

- 能力圈: 能否用3句话解释该业务？
- 情绪: 是否出于恐惧/贪婪/希望？若是则警告
- 资金规则: 不用杠杆、不向下摊平、单股≤20%、单板块≤30%、现金≥10%、预设止损7-8%（连板股-5%）
- 回撤检查: 当前账户回撤是否触及15%警戒线？详见 [references/risk-control.md](references/risk-control.md)
- 周期适配: 当前策略基调是否与Step 0判定的市场周期一致？不一致则警告

## 核心工作流：热点→选股漏斗

读取 [references/hotspot-funnel.md](references/hotspot-funnel.md) 后执行4阶段工作流：
- Phase 1: 热点信息采集（4批次≥12次搜索 + 每热点5项纵深搜索）
- Phase 2: 热点质量评估（4维12分制，≥10分主线/6-9分次级/<6分回避）
- Phase 3: 标的筛选（龙头分类 → 5层框架 → 研究员7步+20项红旗检查 → 割裂度）
- Phase 4: 按报告模板输出

## 通用后置步骤（所有模式必做）

### Step 5: 输出质量验证

| 检查项 | 通过标准 | 未通过处理 |
|--------|----------|-----------|
| 数据完整性 | 必需数据点≥80%已获取 | 标注"数据不足"，不臆测 |
| 逻辑自洽性 | 5+1层框架+7步闭环判断无矛盾 | 重新审视矛盾层级 |
| 止损完整性 | 每个评级都附带了止损位 | 补充止损位 |
| 止盈策略 | 每个BUY评级附带止盈规则 | 补充（参考 [references/profit-protection.md](references/profit-protection.md)）|
| 风险提示 | 至少列出3项风险 | 补充风险项 |
| 回撤控制 | 检查是否触及回撤警戒线 | 触及则强制减仓（参考 [references/risk-control.md](references/risk-control.md)）|
| 数据来源 | 关键数据标注了来源 | 补充来源 |
| 前瞻验证 | 前瞻判断标注了待验证假设 | 补充假设 |

### Step 6: 硬约束检查

对照 [references/hard-constraints.md](references/hard-constraints.md) 检查所有硬约束（选股筛选类/仓位管理类/市场周期适配类/数据验证类/前瞻性判断类）。违反任一硬约束→重新评估。

### Step 7: 复盘与经验沉淀（写入工作区，不写入技能）

按 [references/review-methodology.md](references/review-methodology.md) 执行复盘流程：
1. 事实还原→归因分析→踏空成本对等评估→模式提炼→经验沉淀
2. 复盘文档写入工作区 `.investor-reviews/` 目录（若存在），文件名 `review-YYYYMMDD-HHmm.md`
3. 高置信度经验（≥2次验证）提炼为通用规则→考虑写入 [references/hard-constraints.md](references/hard-constraints.md)
4. **踏空成本对等规则**: 记录"追涨亏钱"类经验时，必须同时评估"如果等回调而踏空，成本是多少"

## 执行红线

**流程红线**（违反=输出无效）:
1. 跳步执行 — 未完成工作流全部阶段就输出报告
2. 搜索不足 — 热点漏斗Phase 1少于12次搜索
3. 跳过A股特色数据 — 未搜索连板梯队/龙虎榜
4. 跳过红旗检查 — 未执行20项红旗检查
5. 利好出尽追入 — 消息3天+且股价已大涨
6. 忽视量价配合 — 价涨无量=派发陷阱

**决策红线**（违反=重新评估）:
- 禁止使用模拟/mock数据，所有数据必须来自实时搜索
- 禁止对亏损股推荐加仓（不向下摊平）
- 禁止推荐ST股、退市风险股、庄股、妖股
- 禁止给出"一定涨"等绝对性判断
- 禁止参与纯概念炒作（题材收入占比<1%）
- 禁止推荐5板以上连板股
- 禁止在空头环境（Layer 5≤0分）下推荐任何A股战法
- 所有评级必须附带止损位
- 所有BUY评级必须附带止盈策略（参考 [references/profit-protection.md](references/profit-protection.md)）
- 若数据不足，必须标注"数据不足"而非臆测
- 前瞻性判断必须标注置信度和验证期限
- 禁止用滞后指标（产品价格/利润/融资余额）做前瞻决策
- A股战法必须与5+1层框架+研究员7步闭环结合使用

**风控红线**（违反=强制执行）:
- 账户回撤>15%时必须强制减仓至30%以下（参考 [references/risk-control.md](references/risk-control.md)）
- 单板块仓位>30%时必须提示超标风险
- 修复上行/景气主升阶段，BUY评级必须给出趋势确认买入方案，不能只说"等回调"
- 持仓中高股息防御股占比>60%且市场处于修复上行/景气主升时，必须提示"持仓风格与市场周期错配"风险
- WebSearch数据必须通过Step 0.1数据验证，未通过校验的数据禁止用于决策
- 经验沉淀必须双向记录：记录"追涨亏钱"时也必须评估"踏空成本"
- **技能不依赖任何项目特定数据，工作区数据可选（优雅降级）**

详细硬约束（选股/仓位/周期/数据/前瞻/政策传导）→ [references/hard-constraints.md](references/hard-constraints.md)

## References

- [hotspot-funnel.md](references/hotspot-funnel.md) — 热点→选股漏斗4阶段工作流（信息采集→质量评估→标的筛选→输出报告）
- [master-methods.md](references/master-methods.md) — 5+1层框架（巴菲特/林奇/利弗莫尔/索罗斯/费雪/达利欧/马克斯方法论）
- [researcher-methods.md](references/researcher-methods.md) — 研究员7步闭环方法论（宏观定锚→赛道定位→三维共振→财报筛选→业绩拐点→资金共识→风控）
- [a-stock-specifics.md](references/a-stock-specifics.md) — A股市场特有知识与选股战法
- [deep-analysis.md](references/deep-analysis.md) — 深度分析与20项红旗检查
- [forward-looking.md](references/forward-looking.md) — 前瞻性选股工作流
- [sector-rotation.md](references/sector-rotation.md) — 板块轮动与市场洞察
- [risk-control.md](references/risk-control.md) — 风险控制与回撤管理
- [profit-protection.md](references/profit-protection.md) — 止盈策略与利润保护
- [wealth-planning.md](references/wealth-planning.md) — 财富规划与资产配置
- [report-templates.md](references/report-templates.md) — 报告模板
- [hard-constraints.md](references/hard-constraints.md) — 通用高置信度硬约束（选股/仓位/周期/数据/前瞻/政策传导）
- [policy-context.md](references/policy-context.md) — 政策上下文长期跟踪（传导链/层级时效/政策日历/影响评估）
- [review-methodology.md](references/review-methodology.md) — 通用复盘方法论（5步流程+模式提炼+双向记录）
- [user-context-protocol.md](references/user-context-protocol.md) — 用户上下文加载协议（可选，优雅降级）
- [workflow-checklists.md](references/workflow-checklists.md) — 工作流检查清单
