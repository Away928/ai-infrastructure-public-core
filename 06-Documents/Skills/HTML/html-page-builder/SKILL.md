---
name: html-page-builder
description: "Create or edit accessible responsive HTML/CSS/JS pages, then check assets and browser behavior."
---

# HTML Author — 网页原生制作与验收

**唯一职责**：制作与修改真正可编辑的 HTML/CSS/JavaScript 源码并验证网页端可用性，不拿截图伪装为 HTML，不将 HTML 无条件转成 PDF 或 PPT。

1. 根据用户要求确定静态单页、多文件网站还是带交互的页面；优先少量语义化 HTML/CSS 和必要的 JS，不新建框架、依赖或构建流程，除非已有项目或需求决定。
2. 支持中文与英文、手机/桌面响应式布局、键盘可访问性、图片 alt、表单 label、清晰标题层级、色彩对比和外部资源可用性。
3. 创建/修改后运行 `python3 scripts/html_audit.py FILE.html` 作为最小静态门，检查 DOCTYPE、语言、charset、viewport、标题、关联的本地资源和基础无障碍线索。它不能证明 CSS 或 JS 在浏览器运行正确。
4. 需要视觉或交互验收时通过真实浏览器检查不同视口、布局溢出、链接、表单和交互操作；修复后在最后版本重复检查。后台 Computer Use 规则仍然有效。
5. 如果用户要求网站上线、远程资源或账户变更，另按明确授权操作；默认输出本地可运行源文件及必要资产，保留原件。
6. HTML→PDF/Word/PPT 仅按用户明确要求的输出格式交给相关专业能力；不要把转换成功当作目标应用验收通过。
