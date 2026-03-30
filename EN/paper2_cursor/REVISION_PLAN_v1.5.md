# Paper 2 v1.5 修订计划（Minor Revisions）

## 剩余问题清单

### 优先修订（必须完成）

#### 1. Section 3.2 Core Functions - Error Handling & Context Management
- **问题**：职责描述与Execution Runtime略有重叠
- **修订**：强调"Contact Layer **decides** policy，Execution Runtime **performs** mechanics"
- **具体修改**：
  - Error Handling → "Failure Policy Evaluation"
  - Context Management：强调协调规则，引用Paper 1

#### 2. GitHub链接一致性
- **问题**：ailib-official vs hiddenpath实际仓库
- **修订**：添加迁移说明脚注

### 可选修订（建议完成）

#### 3. Section 8.1 时间线中性化
- **问题**：隐含近期时间预测
- **修订**：表述为"current and emerging phase"

#### 4. Section 3.2.1 Policy Evaluation Performance
- **问题**：作为概念论文略显工程化
- **修订**：缩短或添加"performance considerations"标注

#### 5. Section 11.4 Safety Mechanisms
- **问题**：Pre-Flight Simulation前瞻性强
- **修订**：添加"in scenarios involving irreversible actions"

#### 6. Keywords优化
- **当前**：AI Contact Layer, Intelligence-Action Interface, AI Native Architecture, Capability Mediation, Action Architecture
- **建议添加**：Control Plane, Capability Routing

---

## 执行顺序

1. ⏳ 修改Section 3.2（Error Handling → Failure Policy Evaluation）
2. ⏳ 添加GitHub迁移说明
3. ⏳ Section 8.1时间线中性化
4. ⏳ Keywords添加Control Plane, Capability Routing
5. ⏳ 版本号更新为v1.5
6. ⏳ 通读检查
7. ⏳ 发送审阅
