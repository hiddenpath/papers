# figures/

本目录存放论文矢量图形文件。

## 格式要求

- 优先使用 PDF 格式（矢量图）
- 如需位图，使用 PNG 格式，分辨率不低于 300 DPI

## 命名规范

- `fig-<number>-<description>.pdf` - 正文章节图形
- `fig-a<number>-<description>.pdf` - 附录图形

## 当前图形来源

论文中的 TikZ 图形直接嵌入在 `.tex` 文件中：
- `sections/01_introduction.tex`: 分层架构图 (fig:layered-architecture-overview)
- `sections/04_theoretical_foundation.tex`: 能力图 (fig:capability-graph)

如需导出为独立 PDF 文件，可使用 `pdflatex` 配合 `standalone` 文档类。

## arXiv 提交检查清单

- [ ] 确认所有 `\includegraphics` 引用的图形文件存在
- [ ] 图形文件使用 PDF 或 PNG 格式
- [ ] 文件名使用小写字母和连字符，避免空格
