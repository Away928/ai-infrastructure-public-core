---
name: engineering-five-step
description: >
  Five-step engineering thinking for development, infrastructure architecture,
  refactoring and workflow simplification. Use when questioning requirements,
  deleting or consolidating redundant Skills/Plugins/MCP/Tools, optimizing
  processes, accelerating iteration, or deciding whether to automate.
  适用于开发前的需求质疑、系统精简、删除冗余、重构、流程优化、加快迭代与自动化决策。
---

# Engineering Five-Step｜五步工程法

**目标：以最少的必要组件和流程，可靠达成用户目标。** 这是决策思维，不是新增 Router、评测框架或审批系统。适用于架构设计、开发计划、重大重构及 AI Infrastructure 精简；小修小补不强制输出五步报告。

按顺序执行；发现前提不成立，就返回前一步，不要为了“完成五步”而增加工作。

1. **质疑每条需求（Question requirements）**：先确认用户真正需要的结果、限制和成功标准。问：谁需要？不做会怎样？现有能力是否足够？区分必须、偏好和未经验证的假设。质疑的是**需求假设**，不是否定用户目标。
2. **删除零件或流程（Delete）**：先寻找整块可取消的功能、工具、Skill、Plugin、MCP、路由层、重复文档和人为步骤。对每项提出“删除后具体损失什么能力、如何验证、能否回滚”；**未获得授权，不删除用户文件、不停用生产路径或改客户端配置**。不要把合并视为天然比删除更好。“删了再加回部分内容”是启发式，不是机械地必须删掉 10%。
3. **简化与优化（Simplify / optimize）**：只优化经过删减仍必须存在的部分。优先复用 Agent 原生能力和已有单一实现，缩短依赖链与调用链；不为了“统一”而重复封装。
4. **加快迭代（Accelerate cycle time）**：在最小可行路径正确后，缩短反馈循环；先做低风险、小范围、能验证的修改，及时实测，减少冗长报告与反复审批。不要靠跳过必要安全或质量检查来提速。
5. **最后自动化（Automate last）**：只自动化已确认必要、稳定且重复出现的工作；检查节省的时间是否大于维护、权限、监控和故障成本。一次性任务通常不值得构建常驻 Agent 或复杂工作流。

## 最小决策与执行规则

- 默认**先调查、提出删减建议，再实施必要部分**；未核实依赖时不能声称“无损删除”。高风险、不可逆、涉及账户/生产配置的操作先请求用户批准。
- 新增任何 Skill/Plugin/MCP/Tool/Router/Registry/测试设施前，先说明为什么原生工具或现有组件不能更简单地满足目标。**没有证明价值就不新增**。
- 保留既有项目规则与用户限制；能直接完成的低风险任务不需要多余问卷、计划文件、流程图或专门实验平台。
- 对复杂优化，汇报只需：**目标与被质疑的假设 → 拟删除/保留及能力损失 → 必要的简化 → 最小验证 → 是否值得加速或自动化**。不需把每一项都形式化成新产物。
- 若发现自己正在“优化不该存在的组件”或“自动化尚未简化的流程”，立即返回步骤 1 或 2。
