# 唯一事实母版与定制版本：从 resume-version-manager、旧 cv init/add/generate 提炼

1. **唯一事实源**：~/Work-Space/Career/Resume/experiences/ 和原项目 evidence_index；先核验，才允许更改正式经历记录。
2. **导入（旧 init 的有效部分）**：可以从用户提供的 PDF/Markdown/经历描述提取“候选事实”，逐项核对公司、日期、角色、本人行动、成绩、来源；在既有目录中合并，绝不默认创建 ~/.cv、jobs/、.history/ 等第二套事实仓。
3. **增量更新（旧 add 的有效部分）**：读取已有事实与当前审阅稿 → 形成差异 → 核查来源与披露权限 → 经授权后修改对应既有文件，不自动从模糊文字提炼数字。
4. **岗位版本（旧 generate 的内容部分）**：读原始 JD → 向 opportunity-evaluation 获取分析 → 拟定经历选取和重点 → 生成 Markdown 候选 → 提供对比与修改原因 → 按完整指定版本审批。
5. 追溯记录应包含：原事实材料定位、目标岗位、稿件路径、版本或 SHA-256、审核/批准状态、日期。使用已有 PROJECT_STATUS.md / docs / archive，不新建简历版本管理器。
6. **文本定稿之后才排版**：所有 Word/DOCX/PDF 排版与格式质量验收均交给 06-Documents。因一页限制需要实质删改时，返回本 Skill 修订并重新确认。
7. 用户要求试排可以在标为 PREVIEW / NOT FOR SUBMISSION 的前提下进行；排版试稿不等于批准正式内容。

该流程是方法而非可自动执行的 /cv CLI；历史命令原文归档于 _System/Archive/05-Career/_Archive；LaTeX 专用活动 Skill 已撤销。
