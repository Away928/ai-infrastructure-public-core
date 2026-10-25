---
name: career-opportunity-evaluation
description: Analyze job or RA requirements, candidate-role fit, opportunity prioritization and offer trade-offs using verified career evidence; not job scraping or application writing.
---

# Career Opportunity Evaluation｜岗位与机会评估

**唯一职责：评价职业机会及匹配度，形成申请或选择建议。** 覆盖申请前的职位和 RA 机会评价，以及录用后 Offer 的条件比较；不负责获取原始招聘信息或写申请材料。

## 执行
1. 从 ~/Work-Space/Career/Positions/ 读取目标岗位与 JD；没有资料时通过 01-Information-Acquisition 发现原始来源，通过 02-Research 核实机构、教授、团队与研究方向，记录时效和来源。
2. 从 career-fact-verification 获取已核实的经历与技能，拆解岗位硬性条件、可加分条件、职责、研究契合点，并标注无法确定的信息。
3. 输出证据驱动的匹配矩阵：要求、对应经历、证据、差距、优先级、可采取的行动。评分仅在用户需要且有明确规则时使用，不捏造胜率。
4. 多岗位机会可按用户既有职业目标、工作内容、地域、培养价值和约束进行比较。收到 Offer 时分析书面条款、薪酬与发展权衡、需确认的问题及谈判策略。
5. 将目标岗位和需要强调的证据传递给 career-content-writing；实际投递/Offer 状态由 career-application-tracking 记录。

## 边界
- 信息发现和外部研究：01 / 02 板块；**本 Skill 只做职业匹配和决策分析**。
- 写简历、邮件、谈判话术：career-content-writing；事实真实性：career-fact-verification。
- 不代替用户接受或拒绝 Offer，也不推测缺失的薪酬或招聘状态。

## 专业方法（按需读取）
- 对 JD、教授 RA、职业转向或多个职位进行适配分析时，阅读 [role-fit](references/role-fit.md)。
- 对 Offer、薪酬构成、谈判空间及接受/拒绝决策，阅读 [offer-decision](references/offer-decision.md)。谈判邮件交 career-content-writing。
- 固定匹配百分比或招聘文案中的单一措辞不能代替证据与实际机会分析。
