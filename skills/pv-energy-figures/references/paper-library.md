# 精选论文图谱与来源索引

分析日期：2026-10-18。来源为用户提供的20份本地PDF，共301页；提取文本并渲染主要图页后逐篇查看。下面只记录已观察图型与可迁移设计，不复述论文完整研究内容，也不是对每一个子面板的重现验证。图号按文内标注，页码均为从1开始的PDF文件页码，不是期刊印刷页码；`F`=Figure。图注与图版分离的稿件分别列出。

原始文件位于本次工作目录，但本skill不依赖固定绝对路径。需要原图细节时，在用户提供的目录按以下精确文件名查找；找不到时不要声称已重新查看。原图未复制进安装包。

需要按程序检索文件名、DOI或图页锚点时，可读取 [source-index.json](source-index.json)。

## 快速按主题定位

- 技术/可部署光伏潜力：P20、P04、P02；建筑多尺度：P01。
- 未来气候、供需错配、反弹与替代：P06、P07、P08、P10、P13。
- 家庭负担、公平与政策：P03、P09、P14、P17、P18、P19。
- 风光储可靠性与电网：P11、P12、P15、P16、P17。
- 多效益协同与部署优先级：P10、P20、P04。

## P01 | A building-scale modeling framework for urban net-zero transitions in Nanjing

- 原始文件：`A building-scale modeling framework for urban net-zero transitions in Nanjing.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-025-64016-7)；PDF共11页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p6。
- 图型与组合：多尺度建筑地图；行业→建筑类型→终端用途的流图；供给→需求排放流；街区×情景的堆叠面积矩阵。
- 配色/绘制观察：粉/黄/蓝/棕等低饱和分类色和浅边界；同类技术在多面板延续。
- 迁移建议与边界：把空间定位、来源分解和未来路径分成不同证据任务；流图必须有真实核算关系。

## P02 | Building façade photovoltaics enhance global climate resilience

- 原始文件：`Building façade photovoltaics enhance global climate resilience.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41558-026-02606-z)；PDF共23页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p7；Extended Data F3 p17。
- 图型与组合：全球栅格地图配经纬边际统计、时间插图与区域统计；经济地图配分布；区域分布脊线图。
- 配色/绘制观察：紫色突出立面发电，绿色联系节电收益；其他指标切换蓝/紫/绿等色系，许多面板有独立色条。
- 迁移建议与边界：适合全球潜力地图+边际统计；不同指标切换颜色可强化语义，但多色连续带和过密插图需谨慎。

## P03 | Burden of the global energy price crisis on households

- 原始文件：`Burden of the global energy price crisis on households.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-023-01209-8)；PDF共13页。
- 已查看重点：F1–2 p3；F3 p4；F4 p5；F5 p6；F6 p7。
- 图型与组合：价格冲击时序；直接/间接成本的横向堆叠条；地图叠加规模点；按国家收入组×支出项的散点矩阵；收入分位小多图。
- 配色/绘制观察：燃料及支出项用蓝、橙、深红；同支出项在矩阵中保持颜色。
- 迁移建议与边界：特别适合成本冲击的累退性；成本涨幅与负担百分点变化需分别编码。

## P04 | Carbon mitigation potential afforded by rooftop photovoltaic in China

- 原始文件：`Carbon mitigation potential afforded by rooftop photovoltaic in China.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-023-38079-3)；PDF共12页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p6；F5 p7；F6 p9。
- 图型与组合：城市资源地图与遥感局部；相关/预测验证散点及误差直方；聚类地图配组内箱线；潜力地图配小提琴；排序条与散点。
- 配色/绘制观察：装机、发电、减碳分别使用暖色、蓝绿、紫色；聚类用少数固定类别色。
- 迁移建议与边界：直接借鉴“地图讲位置，分布讲组内差距”；原有显著性表和复杂分区不必机械保留。

## P05 | City-level analysis of subsidy-free solar photovoltaic electricity price, profits and grid parity in China

- 原始文件：`City-level analysis of subsidy-free solar photovoltaic electricity price, profits and grid parity in China.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-019-0441-z)；PDF共9页。
- 已查看重点：F1 p2；F2 p3；F3 p4；F4 p5。
- 图型与组合：历史LCOE曲线与辐照上下界；平价与盈利地图；按平价指标排序的城市比较。
- 配色/绘制观察：平价地图以蓝色为主，成本灰度，收益暖色；重点位置叠加符号。
- 迁移建议与边界：先分清用户侧/电厂侧指标；不同财务单位用独立面板。排序图的双轴可改为上下对齐面板。

## P06 | Climate change impacts on planned supply–demand match in global wind and solar energy systems

- 原始文件：`Climate change impacts on planned supply–demand match in global wind and solar energy systems.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-023-01304-w)；PDF共11页。
- 已查看重点：F1 p2；F2 p3；F3 p4；F4 p5；F5 p6。
- 图型与组合：供需错配概念曲线；风/光×来源分解的变化地图矩阵，旁有纬向曲线；地区热图。
- 配色/绘制观察：蓝红发散表达负正变化，点描辅助表达统计/模型一致性信息。
- 迁移建议与边界：适合分解供给、需求、均值和变率来源；每种点描的真实含义需从图注确认。

## P07 | Climate change will impact the value and optimal adoption of residential rooftop solar

- 原始文件：`Climate change will impact the value and optimal adoption of residential rooftop solar.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41558-024-01978-4)；PDF共11页。
- 已查看重点：F1 p2；F2 p3；F3 p4；F4 p5；F5 p6。
- 图型与组合：冷/温/热城市分面；年份/情景箱线与条形；家庭散点对照负荷变化、单位价值、总价值和最优容量。
- 配色/绘制观察：基线及未来时期采用蓝/暖色；城市身份由点色与图例保持。
- 迁移建议与边界：分层展示地理气候与家庭异质性；变量过多时减少同时编码的维度。

## P08 | Emissions reductions of rooftop solar are overstated by approaches that inadequately capture substitution effects

- 原始文件：`Emissions reductions of rooftop solar are overstated by approaches that inadequately capture substitution effects.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41558-025-02459-y)；PDF共7页。
- 已查看重点：F1–2 p2；Extended Data F1 p5；Extended Data F2 p6；Extended Data F3 p7。
- 图型与组合：逐时屋顶光伏出力与装机参照；情景排放强度曲线；区域技术环图；年×小时排放热图及出力剖面；日内比较小多图。
- 配色/绘制观察：主图浅蓝出力与多色情景；扩展热图采用深背景，区域技术保持类别色。
- 迁移建议与边界：时间匹配可解释替代效应差异；深色热图不是论文印刷默认，年平均不能替代逐时关联。

## P09 | Examining energy inequality under the rapid residential energy transition in China through household surveys

- 原始文件：`Examining energy inequality under the rapid residential energy transition in China through household surveys.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-023-01193-z)；PDF共16页。
- 已查看重点：F1 p2；F2 p3；F3 p4；F4 p5；F5 p6；F6 p8。
- 图型与组合：多期燃料转型alluvial；城乡收入群体极坐标/环形摘要；Lorenz曲线；年份箱线；负担气泡；模型预测与部分依赖曲线。
- 配色/绘制观察：燃料类别采用柔和黄、绿、蓝、红并跨时间延续；城乡与年份使用固定编码。
- 迁移建议与边界：家庭追踪支持转型流；模型解释曲线不能视为因果机制。

## P10 | future rooftop photovoltaics will weaken carbon mitigation but offer promising water and land benefits

- 原始文件：`future rooftop photovoltaics will weaken carbon mitigation but offer promising water and land benefits.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-026-70923-0)；PDF共31页。
- 已查看重点：图注 p24–26；F1 p27；F2 p28；F3 p29；F4 p30；F5 p31。
- 图型与组合：数据与生命周期方法框架；屋顶面积/自给潜力地图；碳水土地经济多指标地图；带区间情景趋势及变化地图；跨效益城市排名流动。
- 配色/绘制观察：各效益地图独立色标，情景曲线使用低饱和多色与同色区间；排名重点彩色、其余灰色。
- 迁移建议与边界：对本用户多效益研究高度相关；文末图版和图注分离，不能用正文页码代替图页。文件为Article in Press，版本可能与最终刊载不同。

## P11 | Geophysical constraints on the reliability of solar and wind power worldwide

- 原始文件：`Geophysical constraints on the reliability of solar-tongdan.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-021-26355-z)；PDF共12页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p6；F5 p7。
- 图型与组合：6国×季节/日内资源负荷剖面及分位带；风光比例×国家的可靠性热图；面积/可靠性散点；缺供幅度与时数曲线；区域互联地图。
- 配色/绘制观察：光伏偏黄橙、风偏蓝/紫、负荷红线；可靠性热图黄紫高对比。
- 迁移建议与边界：对照跨年分位与单一负荷年，不能将两者区间混为一谈；缺供持续曲线与原始时序互补。

## P12 | Globally interconnected solar-wind system addresses future electricity demands

- 原始文件：`Globally interconnected solar-wind system addresses future electricity demands.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-025-59879-9)；PDF共16页。
- 已查看重点：F1 p3；F2 p4；F3 p7；F4 p8。
- 图型与组合：全球资源地图配经纬边际；时区/地区昼夜热图；部署地图、跨区网络及技术/系统环图；互联流向弦图；分配曲线；韧性情景测试。
- 配色/绘制观察：地区多色在网络和弦图延续；资源量暖色，时间/阶段另有类别色。
- 迁移建议与边界：适合地理网络与区域结构的互补表达；多地区全彩容易难辨，应保留重点通道和统一图例。

## P13 | Implications of the solar rebound effect for the European energy transition

- 原始文件：`Implications of the solar rebound effect for the European energy transition.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-026-02031-8)；PDF共23页。
- 已查看重点：F1 p2；F2 p3；F3 p4；F4 p5；F5 p6；F6 p7；F7 p8。
- 图型与组合：已有反弹估计点区间；反弹情景与时间曲线；技术容量/发电储能堆叠条；欧洲输电网络；成本曲线；电价变化地图。
- 配色/绘制观察：技术类别在多情景堆叠条保持固定高区分色，区域/情景地图采用不同量值编码。
- 迁移建议与边界：反弹的幅度和发生时段应分开比较；技术类别很多时避免所有面板重复巨大图例。

## P14 | Modeling the potential effects of rooftop solar on household energy burden in the United States

- 原始文件：`Modeling the potential effects of rooftop solar on household energy burden in the United States.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-024-48967-x)；PDF共10页。
- 已查看重点：F1 p3；F2–4 p4；F5 p5；F6–7 p6；F8 p7。
- 图型与组合：收入/供暖燃料/地区/融资分组均值与误差；节省分布直方；有无光伏箱线并标负担阈值；时间趋势；数据匹配估算框架。
- 配色/绘制观察：浅蓝强调平均效应，灰阶箱线区分条件，时间趋势按收入组着色。
- 迁移建议与边界：最值得保留的是分布、阈值与财务条件；总体平均可能掩盖负节省或融资负担。

## P15 | Opportunities for decentralised solar power to improve reliability, reduce emissions and avoid stranded assets

- 原始文件：`Opportunities for decentralised solar power to improve reliability, reduce emissions and avoid stranded assets.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-025-62948-8)；PDF共14页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p6；F5 p7。
- 图型与组合：微电网示意与系统结构；可靠性要求×电网可用小时的容量/成本/排放热图；边际变化曲线；错配/搁浅域矩阵；资产利用时序。
- 配色/绘制观察：容量蓝/绿、排放另色带；绿紫表达正负或不同资产利用后果。
- 迁移建议与边界：可行边界和不适用区域是图的一部分；需要分清电网可用小时与服务可用小时。

## P16 | Power supply disruptions deter electric vehicle adoption in cities in China

- 原始文件：`Power supply disruptions deter electric vehicle adoption in cities in China.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-024-50447-1)；PDF共14页。
- 已查看重点：F1 p3；F2 p6；F3 p7。
- 图型与组合：停电频次/时长地图与车辆销量规模点；采用率及减排S形概念框架；车型、地区、GDP异质性系数区间。
- 配色/绘制观察：停电暴露暖色，车型蓝/绿；估计结果主要用灰黑点线。
- 迁移建议与边界：概念采用曲线与经验系数严格分开；地图符号大小为规模时用面积映射。

## P17 | Solar and battery can reduce energy costs and provide affordable outage backup for US households

- 原始文件：`Solar and battery can reduce energy costs and provide affordable outage backup for US households.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-025-01821-w)；PDF共20页。
- 已查看重点：F1 p3；F2–3 p4；F4 p5；F5 p6；F6 p7；F7 p8；F8 p9。
- 图型与组合：经济可行与备用可行份额的条/环摘要；县级双变量地图；节省与备用时长覆盖曲线；州分面联合摘要；回归森林图；电价制度对比。
- 配色/绘制观察：经济/备用及光伏/电池组合采用稳定蓝、绿、紫、暖色；双变量地图有二维图例。
- 迁移建议与边界：对光储公平与可靠性很有价值；整页多层嵌套过密时拆为主文核心和补充组图。

## P18 | The comfort rebound from heat pumps and impact on household cooling behaviour and energy security

- 原始文件：`The comfort rebound from heat pumps and impact on household cooling behaviour and energy security.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41560-025-01845-2)；PDF共19页。
- 已查看重点：F1 p3；F2 p4；F3–4 p5；F5–6 p7。
- 图型与组合：收入组×季节/年份的支出与舒适度箱线；主效应/工具变量与收入、族群异质性区间。
- 配色/绘制观察：采用与否用淡暖/蓝绿等成对色；两种舒适度结局在系数图中保持固定点色。
- 迁移建议与边界：把费用、实际舒适度和异质性区分开；箱线描述不能替代因果估计。

## P19 | Unclean but affordable solid fuels effectively sustained household energy equity

- 原始文件：`Unclean but affordable solid fuels effectively sustained household energy equity.pdf`
- 来源：[DOI](https://doi.org/10.1038/s41467-024-54166-5)；PDF共13页。
- 已查看重点：F1 p2；F2 p3；F3–4 p4；F5 p5；F6 p7。
- 图型与组合：按收入排序的集中曲线及城乡位置；城乡小提琴；农村强度地图叠加城市规模；能源/用途嵌套组成；集中指数贡献分解；转型情景热图。
- 配色/绘制观察：城乡粉红/青色配对；能源类别跨组成和贡献分解保持颜色。
- 迁移建议与边界：区分总能耗、有效能耗、支出和负担；贡献分解与转型情景可揭示平均数隐藏的公平代价。

## P20 | Unveiling deployable rooftop solar potential across Chinese cities

- 原始文件：`Unveiling deployable rooftop solar.pdf`
- 来源：[DOI](https://doi.org/10.1038/s44284-025-00270-6)；PDF共16页。
- 已查看重点：F1 p3；F2 p4；F3 p5；F4 p6；F5 p7。
- 图型与组合：容量因子与技术/可部署潜力地图；城市层级箱线；建筑类型组成与区域散点；可部署/技术比地图；变宽经济/减碳收益排序曲线；部署路径地图。
- 配色/绘制观察：不同建筑类型及地区采用固定类别色；各指标使用紫、绿、蓝、灰、暖色单色地图。
- 迁移建议与边界：本用户屋顶光伏部署研究的优先锚点；曲线横轴是真实累计容量，不能等宽城市条替代。

## 形式参考与原创边界

用户指定的 [Yuan1z0825/nature-skills / nature-figure](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-figure) 于2026-10-18查看。参考其把简短入口、按需设计资料与绘图检查分层的组织方式；本skill的领域图谱、图型选择、组合与色库依据上述用户论文独立编写，不包含该仓库的代码或共享运行依赖。

可回查的结构参考：[SKILL.md](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-figure/SKILL.md)、[多面板证据组织](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-figure/references/multipanel-evidence-architecture.md)、[图型参考](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-figure/references/chart-types.md)、[设计参考](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-figure/references/design-theory.md)。这些是方法参考，不是目标期刊的正式规范。
