# Paper 2 LaTeX 转换计划

## 一、arXiv文档包要求

### 必需文件
- `main.tex` - 主文件
- `sections/*.tex` - 各章节分离文件
- `references.bib` - BibTeX参考文献
- `figures/*.pdf` - 图片文件（如有）

### arXiv标准
- 使用标准article类
- 避免自定义包依赖
- 图片嵌入而非外部链接
- UTF-8编码

---

## 二、转换原则

### 核心原则
1. **绝对不修改原文内容** - 只转换格式
2. **绝对不遗漏任何段落** - 逐段对照检查
3. **保持原文结构** - 章节编号不变
4. **每步回头检查** - 转换一段检查一段

### 格式映射规则

| Markdown | LaTeX |
|----------|-------|
| `# 标题` | `\title{}` |
| `## 1. Section` | `\section{Section}` |
| `### 1.1 Subsection` | `\subsection{Subsection}` |
| `**粗体**` | `\textbf{粗体}` |
| `*斜体*` | `\textit{斜体}` |
| `> 引用` | `\begin{quote}...\end{quote}` |
| `- 列表项` | `\begin{itemize}...\end{itemize}` |
| `1. 编号项` | `\begin{enumerate}...\end{enumerate}` |
| ```代码块``` | `\begin{verbatim}...\end{verbatim}` |
| `[链接](url)` | `\url{url}` |
| `|表格|` | `\begin{tabular}...\end{tabular}` |

---

## 三、分段转换计划

### Phase 1: 主文件结构
- [ ] 创建 `main.tex` 主框架
- [ ] 设置文档类和包
- [ ] 设置标题、作者、日期
- [ ] 添加 `\input{sections/*}` 引用

### Phase 2: 章节文件转换

#### Section 0: 标题信息
- [ ] Title: The AI Contact Layer
- [ ] Authors: Wang Luqiang
- [ ] Affiliation: ai-lib
- [ ] Date: March 2026
- [ ] Version: 1.5

#### Section 1: Abstract
- [ ] 摘要内容转换
- [ ] Keywords转换

#### Section 2: Introduction (Section 1)
- [ ] 1.1 The Limitation of Intelligence Alone
- [ ] 1.2 The Missing Conceptual Layer
- [ ] 1.3 Relationship to the Execution Layer Paper
- [ ] 1.4 Contributions

#### Section 3: Intelligence vs. Action (Section 2)
- [ ] 2.1 Two Fundamental Aspects
- [ ] 2.2 Why Separation Matters
- [ ] 2.3 Historical Context

#### Section 4: The Contact Layer Concept (Section 3)
- [ ] 3.1 Definition
- [ ] 3.2 Core Functions (含2.1, 5.1子节)
- [ ] 3.3 Capabilities as the Language of Interaction

#### Section 5: Architectural Realization (Section 4)
- [ ] 4.1 From Concept to Architecture
- [ ] 4.2 Clarifying Terminology Boundaries
- [ ] 4.3 Precise Definition

#### Section 6: Digital and Physical Interaction (Section 5)
- [ ] 5.1 Dual Domain Support
- [ ] 5.2 The Significance of Physical Interaction
- [ ] 5.3 Edge Computing Implications

#### Section 7: Action Interface Definition (Section 6)
- [ ] 6.1 Formal Definition
- [ ] 6.2 Precision Statement
- [ ] 6.3 Architectural Significance

#### Section 8: Comparison (Section 7)
- [ ] 7.1 Current Approaches
- [ ] 7.2 Distinctive Approach
- [ ] 7.3 Integration Path
- [ ] 7.4 Comparison with Multi-Agent Frameworks (表格)

#### Section 9: Evolution (Section 8)
- [ ] 8.1 Historical Progression
- [ ] 8.2 Future Trajectory

#### Section 10: Personal AI (Section 9)
- [ ] 9.1 Concept
- [ ] 9.2 Architecture (ASCII图 → 保持)
- [ ] 9.3 Deployment Scenarios
- [ ] 9.4 Personal AI Use Case: Smart Home + Email (序列图)

#### Section 11: AI Native Stack (Section 10)
- [ ] 10.1 Position in the Stack (ASCII图)
- [ ] 10.2 Conceptual Unity

#### Section 12: Philosophical Implications (Section 11)
- [ ] 11.1 Thought and Action in AI
- [ ] 11.2 The Mediator Role
- [ ] 11.3 Implications for AI Safety
- [ ] 11.4 Safety Mechanisms at the Contact Layer

#### Section 13: Conclusion (Section 12)
- [ ] 结论全文

#### Appendices
- [ ] Appendix A: Capability Interaction Patterns
- [ ] Appendix B: Capability Definition Schema
- [ ] Appendix C: Contact Layer Interface Specification

#### Back Matter
- [ ] References (转换为BibTeX)
- [ ] Document Information
- [ ] Acknowledgments
- [ ] Open Source Resources

### Phase 3: 特殊元素处理

#### 表格转换
- [ ] Section 1.3 对比表格
- [ ] Section 7.4 多Agent框架对比表

#### 代码块转换
- [ ] YAML配置 → verbatim或listings
- [ ] TypeScript接口 → verbatim或listings
- [ ] 数学公式 → equation/align环境

#### ASCII图处理
- [ ] 保持原样（verbatim）或
- [ ] 注释说明"原ASCII图"

---

## 四、检查清单

### 每段转换后检查
- [ ] 内容完整无遗漏
- [ ] 格式正确
- [ ] 特殊字符转义

### 每节完成后检查
- [ ] 章节编号正确
- [ ] 所有子节完整
- [ ] 交叉引用有效

### 全文完成后检查
- [ ] 从头到尾通读
- [ ] 对照原文逐段核对
- [ ] 编译无错误
- [ ] PDF输出完整

---

## 五、执行顺序

1. ⏳ 创建目录结构
2. ⏳ 创建main.tex框架
3. ⏳ 逐节转换并检查
4. ⏳ 创建references.bib
5. ⏳ 编译测试
6. ⏳ 全文检查
7. ⏳ 生成最终PDF
8. ⏳ 发送到邮箱
