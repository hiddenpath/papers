# Paper 2 v1.4 修订计划

## 修订清单（按章节顺序）

### 1. Abstract（摘要）
- [ ] 无需修改（已在v1.3中添加系列说明）

### 2. Section 1.3 Relationship to the Execution Layer Paper
- [ ] 检查：确保与Paper 1的对比清晰
- [ ] 修正：References [1]版本号 v1.8 → v1.5

### 3. Section 3.1 Definition
- [ ] 已有形式化定义CL = (C, Policy, Context)
- [ ] 添加标注：明确这是概念形式化

### 4. Section 3.2 Core Functions
- [ ] 检查：Error Handling和Context Management是否越界
- [ ] 修改：明确说明"Contact Layer协调这些功能，execution由Execution Runtime执行"

### 5. Section 4.2 Clarifying Terminology Boundaries
- [ ] 检查：术语定义是否清晰
- [ ] 强化：明确Contact Layer（narrow）vs Action Layer（broad）

### 6. Section 6.1 Formal Definition
- [ ] 添加标注："此为概念形式化，展示决策逻辑框架"
- [ ] 添加："详细算法实现见ai-lib参考实现"

### 7. Section 6.2 Precision Statement
- [ ] **关键修改**：将"The execution layer is the action interface..."
- [ ] 改为："The Contact Layer is the policy/routing component of the action interface between AI cognition and the capability ecosystem."

### 8. Section 8.1 Historical Progression（时间线）
- [ ] 修改："Phase 3: Environment Interaction (2025-)" → "Phase 3: Environment Interaction"
- [ ] 移除具体时间预测

### 9. Section 11 Philosophical Implications
- [ ] 11.1-11.3：保留（概念洞见）
- [ ] 11.4 Action Interception and Safety Constraints：
  - [ ] 压缩为概念性描述
  - [ ] 移除详细YAML配置，改为简短说明
- [ ] 11.5 Trust Domain and Batch Authorization：
  - [ ] 压缩，保留概念，移除详细YAML
- [ ] 11.6 Physical Action Pre-Flight Simulation：
  - [ ] 压缩，保留概念，移除详细配置

### 10. Section 2.3 Historical Context（次要修订）
- [ ] 添加AI-specific历史：ReAct/tool-use → agentic AI演进

### 11. References
- [ ] [1] 版本号修正：v1.8 → v1.5

### 12. Document Information
- [ ] 版本号：v1.3 → v1.4
- [ ] 日期：更新为今天

---

## 修订执行顺序

1. ✅ 先读取当前版本
2. ⏳ 按顺序执行修订
3. ⏳ 完成后通读全文
4. ⏳ 检查术语一致性
5. ⏳ 生成v1.4版本
6. ⏳ 发送审阅
