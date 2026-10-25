---
name: pdf-quality-check
description: "Inspect PDF page sizes, embedded fonts, searchable text, links, annotations and export quality."
---

# PDF Toolkit — PDF 原生质量检查

**唯一职责**：检查 PDF 本身是否是可用的成品，而不是重复排版 DOCX 或制作 PPT。负责页面尺寸/数量、可提取文字、扫描页线索、字体、图片、超链接、批注和嵌入文件的清点，尤其是 WPS/PowerPoint 导出的文字层质量。

1. 使用 `python3 scripts/pdf_review.py INPUT.pdf [--require-text]` 生成逐页 JSON 审计。 `--require-text` 用于原本应可检索的简历、论文、报告，遇到无文字页返回非零退出码。
2. 针对需要视觉保真的 PDF，在真实目标输出 PDF 上逐页核对字形、字体替换、裁切、分页、图片分辨率和排版。文本层 PASS 不表示像素视觉 PASS。
3. 含扫描/轮廓文字的 PDF 标注为需 OCR/人工判断，不得把 0 个可提取字符当作原文为空。PDF 重新转 DOCX 属于 Word 专项（Word/word-layout-repair），需要复杂布局时转交 Word。
4. 任何导出都记录生成软件与实际导出路径；用户使用 WPS/PowerPoint 自带 PDF 输出是支持的默认方案，无需强制开发 GUI 导出自动化。
5. 文件与文字层审计、PDF 每页渲染、用户目标应用确认是三个不同证据等级。只宣称实际通过的等级。不得改写 PDF 原件。

这是 PDF 页结构、文字层、字体与导出检查的**唯一解析实现**，不是 Word/PPT 生成或多格式转换引擎。Word 的 `document_audit.py pdf/compare` 已直接调用本 Skill 的 `scripts/pdf_review.py:audit()`；跨格式文本相似度属于 Word 的比较逻辑，但不再另写 PDF 解析。
