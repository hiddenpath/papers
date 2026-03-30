#!/usr/bin/env python3
"""
安全修改论文 md 文件 - 处理标准 markdown 格式
"""

# 读取原文件
with open('Paper1_AI_Execution_Layer_v1.2.md', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file length: {len(content)} chars")

# === P1: Limitations 修改 ===
old_limitations = '''## 11. Limitations and Evaluation Agenda

This work focuses on architectural formalization and runtime boundaries. It does not provide a full-scale benchmark study of latency overhead, translation cost distribution, or end-to-end economic efficiency under production traffic.

A complete systems evaluation should include:

1. **Translation Overhead:** protocol-to-provider transformation latency and variance.
2. **Runtime Scalability:** throughput and tail latency under mixed synchronous/streaming workloads.
3. **Failure Behavior:** bounded retry impact and error propagation under provider instability.
4. **Policy-Execution Separation Cost:** control-plane/data-plane interaction overhead under dynamic routing.

These measurements are left to subsequent experimental work and cross-runtime benchmark suites.'''

new_limitations = '''## 11. Limitations and Evaluation Agenda

This work focuses on architectural formalization and runtime boundaries. Beyond the evaluation agenda, we acknowledge several design tradeoffs and known limitations.

### 11.1 Design Tradeoffs

**Minimal vs. Full-Featured.** The AI Execution Layer deliberately constrains its responsibility to deterministic invocation. This minimalism enables portability and clear boundaries but sacrifices convenience features found in integrated frameworks:

- *No built-in policy logic.* Routing decisions, fallback chains, and cost optimization must be implemented by the Policy Orchestration Layer, not the runtime itself.
- *No conversation management.* Chat history, context windowing, and memory are outside the execution boundary.
- *No built-in observability stack.* Metrics, tracing, and logging hooks are provided, but the observability infrastructure is deployment-specific.

**Protocol vs. Implementation.** The design prioritizes protocol stability over implementation convenience. Capability manifests must be declared explicitly; there is no "auto-discovery by introspection" mechanism. This tradeoff reduces runtime magic but increases provider onboarding effort.

### 11.2 Known Boundaries

The architecture is not suitable for all scenarios:

- *Single-provider lock-in.* Applications using provider-specific features beyond standardized capabilities lose portability benefits.
- *Ultra-low-latency requirements.* The protocol translation layer adds overhead unsuitable for sub-millisecond response scenarios (e.g., high-frequency trading).
- *Offline-only environments.* While edge runtimes are supported, capability discovery and provider registration assume network connectivity during initialization.

### 11.3 Dependency Assumptions

The architecture relies on several assumptions:

- *Protocol standardization.* The benefits diminish if providers do not adopt common capability schemas.
- *Provider cooperation.* Capability manifests must accurately describe provider behavior; misaligned manifests cause runtime failures.
- *Orchestration maturity.* Organizations without policy orchestration expertise may not fully realize the separation benefits.

### 11.4 Evaluation Agenda

A complete systems evaluation should include:

1. **Translation Overhead:** protocol-to-provider transformation latency and variance.
2. **Runtime Scalability:** throughput and tail latency under mixed synchronous/streaming workloads.
3. **Failure Behavior:** bounded retry impact and error propagation under provider instability.
4. **Policy-Execution Separation Cost:** control-plane/data-plane interaction overhead under dynamic routing.

These measurements are left to subsequent experimental work and cross-runtime benchmark suites.'''

if old_limitations in content:
    content = content.replace(old_limitations, new_limitations)
    print("P1 Limitations: OK")
else:
    print("P1 Limitations: NOT FOUND")
    # 尝试查找相似内容
    if "## 11. Limitations" in content:
        print("  -> Found '## 11. Limitations' in content")

# === P2: Related Work 修改 ===
old_related = '''## 8. Related Work

### 8.1 AI Orchestration Frameworks

Frameworks such as LangChain provide practical orchestration abstractions, but often couple orchestration policy and execution mechanics in one framework runtime. This coupling improves developer convenience but weakens boundary clarity and runtime portability.

### 8.2 Workflow Engines

Workflow engines such as Airflow and Temporal provide robust DAG execution and fault handling. However, their abstraction unit is typically task/workflow-level orchestration, not capability-level semantic invocation with provider-agnostic protocol contracts.

### 8.3 Service Mesh and RPC Systems

Service meshes and RPC infrastructures provide routing, retries, and observability at network request granularity. By contrast, the AI Execution Layer operates at capability semantics and explicitly separates policy routing from deterministic invocation.

### 8.4 Serverless and Function Runtimes

FaaS platforms provide scalable execution environments but do not standardize capability abstraction, capability manifests, or cross-provider semantic equivalence.

### 8.5 Position of This Work

This paper contributes a minimal execution boundary for AI-native systems:

- protocol-first capability invocation
- strict cognition-policy-execution separation
- runtime-level portability across providers and languages
- explicit non-responsibilities that prevent policy leakage into execution

### 8.6 Multi-Language Implementation'''

new_related = '''## 8. Related Work

### 8.1 AI Orchestration Frameworks

Frameworks such as LangChain provide practical orchestration abstractions, but often couple orchestration policy and execution mechanics in one framework runtime. This coupling improves developer convenience but weakens boundary clarity and runtime portability.

**Specific Coupling Issues.** In LangChain, prompt templates, model selection, and output parsing are frequently intertwined within chain definitions:

- *Model-specific prompts.* Templates often embed provider-specific parameters (e.g., OpenAI function calling syntax), making provider substitution non-trivial.
- *Implicit routing.* LangGraph conditional edges embed routing logic within the graph definition, conflating policy decisions with execution flow.
- *Tight tool integration.* Tool definitions often reference specific model capabilities (e.g., vision, function calling), reducing portability across models without those features.

The AI Execution Layer explicitly separates these concerns: prompts are managed by the cognition layer, routing by the policy layer, and invocation by the execution layer.

### 8.2 Model Context Protocol (MCP)

Anthropic's Model Context Protocol provides a standardized interface for AI models to interact with external tools and resources. MCP and the AI Execution Layer address complementary concerns:

- *MCP scope.* MCP focuses on the model-tool interface, defining how models discover and invoke tools through a JSON-RPC protocol.
- *Execution Layer scope.* This work focuses on the runtime-provider interface, defining how execution layers translate capability requests into provider-specific API calls.
- *Complementary positioning.* An AI Execution Layer can implement MCP as one of its capability protocols, translating MCP tool invocations into provider-specific implementations.

MCP standardizes the "model asks, tool responds" interaction pattern; the AI Execution Layer standardizes the "runtime asks, provider responds" invocation pattern.

### 8.3 OpenAI Assistants and Agents SDK

OpenAI's Assistants API and Agents SDK provide managed orchestration for multi-turn conversations with tool use. Key architectural differences:

- *State management.* Assistants API maintains server-side conversation state, including message history and tool outputs. The AI Execution Layer explicitly excludes state management from its boundary.
- *Provider lock-in.* Assistants API is specific to OpenAI models. The Execution Layer's protocol-first design enables cross-provider portability.
- *Abstraction level.* Assistants API combines cognition (thread management), policy (tool selection), and execution (API calls). The three-layer separation enables independent evolution of each layer.

### 8.4 Workflow Engines

Workflow engines such as Airflow and Temporal provide robust DAG execution and fault handling. However, their abstraction unit is typically task/workflow-level orchestration, not capability-level semantic invocation with provider-agnostic protocol contracts.

**Temporal Comparison.** Temporal's workflow orchestration handles long-running processes with durable execution. However:

- Temporal workflows are defined at the application logic level, not the capability invocation level.
- Activity implementations are typically single-language, while the AI Execution Layer requires cross-language consistency.
- Temporal does not address provider-agnostic capability translation.

### 8.5 Service Mesh and RPC Systems

Service meshes and RPC infrastructures provide routing, retries, and observability at network request granularity. By contrast, the AI Execution Layer operates at capability semantics and explicitly separates policy routing from deterministic invocation.

**Semantic vs. Network Abstraction.**

- *Service mesh.* Routes HTTP/gRPC requests based on service identity and network-level policies. Unaware of capability semantics.
- *AI Execution Layer.* Routes capability requests based on semantic declarations (e.g., "text-to-image generation"). Translates between protocol-standard requests and provider-specific APIs.

### 8.6 Serverless and Function Runtimes

FaaS platforms provide scalable execution environments but do not standardize capability abstraction, capability manifests, or cross-provider semantic equivalence.

### 8.7 Position of This Work

This paper contributes a minimal execution boundary for AI-native systems:

- protocol-first capability invocation
- strict cognition-policy-execution separation
- runtime-level portability across providers and languages
- explicit non-responsibilities that prevent policy leakage into execution

### 8.8 Multi-Language Implementation'''

if old_related in content:
    content = content.replace(old_related, new_related)
    print("P2 Related Work: OK")
else:
    print("P2 Related Work: NOT FOUND")

# === P3: Benefits 修改 ===
old_benefits = '''## 7. Architectural Benefits

### 7.1 Decoupling

Applications become independent of specific providers. Agents express capability requirements without needing to know which provider will fulfill them. This decoupling enables:

- Provider substitution without application changes
- Multi-vendor strategies
- Graceful degradation when providers are unavailable

### 7.2 Portability

AI applications can run across different runtime environments. As long as runtimes implement the AI Protocol, applications can be deployed without modification. This portability is similar to how container images can run on any container runtime [4][6].

### 7.3 Capability Discovery

New providers can register capabilities without modifying applications. The capability registry serves as a dynamic discovery mechanism, enabling:

- New capability providers to enter the ecosystem
- Applications to discover new capabilities at runtime
- Ecosystem growth without centralized coordination

### 7.4 Ecosystem Growth

Standard protocols enable third-party extensions and tools. The minimal runtime design creates clear extension points:

- Custom capability providers
- Alternative orchestration strategies
- Specialized runtime implementations
- Monitoring and observability tools'''

new_benefits = '''## 7. Architectural Benefits

### 7.1 Decoupling

Applications become independent of specific providers. Agents express capability requirements without needing to know which provider will fulfill them. This decoupling enables:

- Provider substitution without application changes
- Multi-vendor strategies
- Graceful degradation when providers are unavailable

**Case Study: Provider Failover.** Consider an image generation service using DALL-E. When OpenAI experiences an outage, the Policy Orchestration Layer can route requests to Stable Diffusion (via a different provider) without any application code changes. The Execution Layer translates the same "text-to-image" capability request to the alternative provider's API format. This failover occurs at the capability level, not the network level.

### 7.2 Portability

AI applications can run across different runtime environments. As long as runtimes implement the AI Protocol, applications can be deployed without modification. This portability is similar to how container images can run on any container runtime [4][6].

**Cross-Language Validation.** The ai-lib project validates this portability across four programming languages:

- *ai-lib-rust:* Systems programming with zero-cost abstractions, suitable for high-performance services.
- *ai-lib-python:* Data science and ML workflows, integrated with NumPy and PyTorch ecosystems.
- *ai-lib-ts:* Node.js applications and browser-based AI via WASM compilation.
- *ai-lib-go:* Cloud-native services with native Kubernetes integration.

All four runtimes share identical capability request/response semantics and pass a common compliance test suite.

### 7.3 Capability Discovery

New providers can register capabilities without modifying applications. The capability registry serves as a dynamic discovery mechanism, enabling:

- New capability providers to enter the ecosystem
- Applications to discover new capabilities at runtime
- Ecosystem growth without centralized coordination

**Ecosystem Scale.** The ai-protocol ecosystem currently supports 30+ AI providers with standardized, configuration-driven interfaces. New providers contribute capability manifests conforming to the v2 schema; runtimes automatically discover and validate these manifests without code changes.

### 7.4 Ecosystem Growth

Standard protocols enable third-party extensions and tools. The minimal runtime design creates clear extension points:

- Custom capability providers
- Alternative orchestration strategies
- Specialized runtime implementations
- Monitoring and observability tools

### 7.5 Operational Benefits

Beyond architectural benefits, the design yields practical operational advantages:

**Debugging Clarity.** When a capability invocation fails, the boundary clearly indicates where to investigate:

- Protocol-level errors: manifest validation, schema mismatches.
- Translation-level errors: provider-specific format issues.
- Provider-level errors: rate limits, authentication, service outages.

**Testing Isolation.** The three-layer separation enables independent testing:

- Cognition layer tests focus on prompt engineering and agent logic.
- Policy layer tests focus on routing decisions and fallback chains.
- Execution layer tests focus on protocol compliance and provider translation.

This isolation reduces test complexity and enables targeted regression testing.'''

if old_benefits in content:
    content = content.replace(old_benefits, new_benefits)
    print("P3 Benefits: OK")
else:
    print("P3 Benefits: NOT FOUND")

# === P4: Future Directions 修改 ===
old_future = '''## 10. Future Directions

### 10.1 Capability Discovery Protocol

Future work could define a standardized capability discovery protocol, enabling:

- Dynamic capability registration
- Capability health monitoring
- Automatic capability indexing

### 10.2 Application Packaging Standard

A standardized application packaging format would enable:

- Portable AI application distribution
- Standard deployment models
- Capability requirement declaration

### 10.3 Capability Marketplace

As capabilities become standardized, marketplaces may emerge for:

- Premium capability offerings
- Capability quality ratings
- Usage-based pricing

### 10.4 Edge Runtime Support

The execution layer architecture naturally supports edge computing scenarios. Runtimes can operate locally on:

- Personal devices
- Home servers
- Embedded systems

Edge runtimes may connect to:

- Local models
- Local automation systems
- Cloud capabilities

This architecture enables personal AI infrastructure, where users operate local runtimes orchestrating personal capabilities.

### 10.5 Asynchronous Notification Support (Future Work)

While the current design relies on polling for long-running tasks, future runtime versions may support callback-based notifications. In this model:

- Providers register webhook endpoints in their manifests
- The runtime translates provider-specific callbacks into protocol-standard events
- The Contact Layer subscribes to capability completion events rather than polling

This would reduce connection overhead for high-concurrency scenarios and enable true event-driven capability orchestration.'''

new_future = '''## 10. Future Directions

### 10.1 Near-Term Priorities (6 Months)

**Capability Discovery Protocol.** Future work could define a standardized capability discovery protocol enabling dynamic capability registration, capability health monitoring, and automatic capability indexing.

**Status.** The ai-lib project has initiated work on this protocol, with draft specifications for:

- Provider heartbeat and health reporting
- Capability deprecation notices
- Version negotiation for capability schemas

**Benchmark Suite.** A cross-runtime benchmark suite is planned to evaluate:

- Translation overhead across Rust, Python, TypeScript, and Go runtimes
- Throughput under concurrent synchronous and streaming workloads
- Memory footprint and startup latency comparisons

### 10.2 Medium-Term Priorities (12-18 Months)

**Application Packaging Standard.** A standardized application packaging format would enable:

- Portable AI application distribution
- Standard deployment models
- Capability requirement declaration

**Design Considerations.**

- Manifest-based capability requirements (similar to package.json or Cargo.toml)
- Container-native packaging for cloud deployment
- Version-pinned capability declarations for reproducibility

**Edge Runtime Support.** The execution layer architecture naturally supports edge computing scenarios. Runtimes can operate locally on:

- Personal devices (smartphones, tablets)
- Home servers (NAS devices, personal cloud)
- Embedded systems (IoT gateways, automotive systems)

This architecture enables personal AI infrastructure, where users operate local runtimes orchestrating personal capabilities.

### 10.3 Long-Term Vision (18+ Months)

**Capability Marketplace.** As capabilities become standardized, marketplaces may emerge for:

- Premium capability offerings
- Capability quality ratings and reviews
- Usage-based pricing and metering

**Asynchronous Notification Support.** While the current design relies on polling for long-running tasks, future runtime versions may support callback-based notifications. In this model:

- Providers register webhook endpoints in their manifests
- The runtime translates provider-specific callbacks into protocol-standard events
- The Contact Layer subscribes to capability completion events rather than polling

This would reduce connection overhead for high-concurrency scenarios and enable true event-driven capability orchestration.

### 10.4 Research Agenda

Beyond engineering priorities, several research questions remain open:

1. **Formal Verification.** Can capability contracts be formally verified for provider compliance?
2. **Economic Modeling.** How do pricing models influence routing strategies at the policy layer?
3. **Security Boundaries.** What is the minimal trusted computing base for capability execution?

These questions extend the architectural formalization into formal methods, computational economics, and security domains.'''

if old_future in content:
    content = content.replace(old_future, new_future)
    print("P4 Future Directions: OK")
else:
    print("P4 Future Directions: NOT FOUND")

# 更新版本号
content = content.replace('**Preprint Version:** 1.2', '**Preprint Version:** 1.3')

# 写入新文件
with open('Paper1_AI_Execution_Layer_v1.3.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nNew file length: {len(content)} chars")
print("Done! Output: Paper1_AI_Execution_Layer_v1.3.md")
