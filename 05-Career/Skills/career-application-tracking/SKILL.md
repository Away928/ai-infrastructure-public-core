---
name: career-application-tracking
description: Manage actual application records, submission evidence, stages, deadlines and follow-up actions without duplicating the user's Career workspace or assuming actions succeeded.
---

# Career Application Tracking｜申请进度管理

**唯一职责：维护求职申请的事实状态与后续行动。** 使用 ~/Work-Space/Career/Applications/ 作为申请文件与记录的权威位置；岗位详情在 Positions/，简历母版在 Resume/。

## 执行
1. 在已有项目结构中读取目标公司/教授、岗位、申请版本、链接、截止日、投递日期、当前状态、下一动作和相关回执。
2. 区分计划投递、已提交、待回复、测评/面试、收到 Offer、结束等状态；仅凭用户确认或可验证外部证据更新，不把起草完成当作成功投递。
3. 核对截止日期、跟进间隔和状态变化，产出优先级明确的待办；需要外发内容时调用 career-content-writing。
4. 对需要回复、预约、提交或联系第三方的动作，先确认操作权限与收件人/目标，不未经授权发信、提交、撤回或接受 Offer。
5. 记录面试与测评节点，但准备内容由 career-assessment-preparation 承担；收到 Offer 的价值分析由 career-opportunity-evaluation 承担。

## 边界
- 本 Skill 管**事实进度、记录、提醒和后续动作**，不负责评估职位质量或改写简历。
- 不新建招聘数据库、独立追踪服务或自动投递系统；未验证平台连接时只提供人工/现有连接器支持。
- 不宣称已有端到端同步、实时状态获取或自动投递能力。

## 专业方法（按需读取）
- 提交证明、申请字段、阶段变化、期限和跟进动作按 [submission-records](references/submission-records.md) 执行。
- 如涉及外部网站或邮件操作，保留实际回执；未获授权时仅准备内容和待办，不执行提交或发信。
