# The AI Native Software Stack: Toward a Capability-Driven Ecosystem

**Authors:** Wang Luqiang  
**Affiliation:** ai-lib  
**Date:** March 2026  
**Preprint Version:** 1.1  

---

## Abstract

The rapid expansion of AI capabilities has created a fragmented integration landscape. Applications must interact with multiple AI providers, tools, services, and devices, each exposing different APIs and capability definitions. This fragmentation leads to tight coupling, limited portability, and ecosystem fragmentation.

This paper introduces the AI Native Software Stack, a layered architecture designed for agent-driven environments. The stack comprises five distinct layers: Interface Layer, AI Native Applications, AI Action Layer, Capability Ecosystem, and Infrastructure. Each layer has clearly defined responsibilities and interfaces, enabling modularity and interoperability.

We present the theoretical foundation of this architecture, including four core principles: the Capability Abstraction Principle, the Cognition–Action Separation Principle, the Capability Routing Principle, and the Capability Graph Execution model. We demonstrate how this stack enables the transition from API Economy to Capability Economy, where capabilities become the fundamental units of software composition.

The AI Native Stack represents a paradigm shift in software architecture, from code orchestrating APIs to agents orchestrating capabilities. This shift enables portable AI applications, decoupled providers, and the emergence of capability marketplaces.

**Keywords:** AI Native Architecture, Capability Economy, Software Stack, AI Infrastructure, Capability Abstraction

---

## 1. Introduction

### 1.1 The Fragmentation Problem

The AI ecosystem has experienced explosive growth, with models from providers such as OpenAI, Anthropic, Google, and DeepSeek demonstrating increasingly powerful capabilities. However, this growth has created a significant integration challenge:

**Provider Proliferation:** Multiple AI providers offer overlapping but incompatible APIs. Applications must implement provider-specific integrations, leading to:

- Maintenance burden as APIs evolve
- Lock-in to specific providers
- Limited flexibility in capability selection

**Tool Fragmentation:** AI tools, plugins, and frameworks each define their own interfaces. Developers must learn multiple tool ecosystems, and applications become tightly coupled to specific frameworks.

**Application Coupling:** Current AI applications typically embed provider-specific logic directly into application code. This coupling makes it difficult to:

- Switch providers when better options emerge
- Implement multi-provider strategies
- Port applications across different execution environments

### 1.2 The Missing Architecture

Despite the proliferation of AI frameworks and tools, the ecosystem lacks a unified architectural framework. Current approaches address pieces of the problem:

- **API Abstractions:** SDKs that wrap multiple providers, but remain tied to specific programming languages
- **Agent Frameworks:** Orchestration systems for AI agents, but mixing orchestration with execution
- **Tool Standards:** Formats for defining tools, but without runtime standardization

What is missing is a **complete software stack** that:

1. Defines clear layer boundaries
2. Establishes standardized interfaces between layers
3. Enables portable applications
4. Supports capability ecosystems

This paper introduces such a stack: the AI Native Software Stack.

### 1.3 Contributions

This paper makes the following contributions:

1. **Architectural Framework:** We define a five-layer architecture that separates concerns between interfaces, applications, cognition, action, capabilities, and infrastructure.

2. **Theoretical Principles:** We establish four core principles that define the stack's behavior: Capability Abstraction, Cognition–Action Separation, Capability Routing, and Capability Graph Execution.

3. **Economic Model:** We introduce the Capability Economy as the successor to the API Economy, where capabilities become the fundamental units of software composition.

4. **Ecosystem Architecture:** We describe the components necessary for capability ecosystems, including registries, marketplaces, and discovery mechanisms.

---

## 2. From API Economy to Capability Economy

### 2.1 The API Economy (Current State)

For the past two decades, software ecosystems have been organized around the **API Economy**. Companies provide capabilities through APIs, and applications consume these APIs directly.

**Structure:**
```
Application → API → Provider
```

**Examples:**
- Stripe: Payment processing API
- Twilio: Communication API
- Google Maps: Geolocation API
- AWS: Cloud service APIs

**Characteristics:**
- APIs are the atomic units of software composition
- Applications maintain direct provider relationships
- Integration is application-specific

### 2.2 The AI Disruption

AI fundamentally changes this model. AI agents do not call APIs directly—they invoke **capabilities**. This shift has profound implications:

**Agent Behavior:** Agents reason about tasks and decide which capabilities to invoke. However, agents should not be burdened with:

- Which provider implements a capability
- How to invoke provider-specific APIs
- Which execution environment to use

**Capability Abstraction:** Agents express capability requirements, not provider choices. The system determines:

- Which provider to use
- How to invoke the provider's API
- Where to execute the capability

### 2.3 The Capability Economy (Proposed Model)

We propose a new economic model: the **Capability Economy**.

**Structure:**
```
Agent → Capability → Provider
```

**Key Differences:**

| Aspect | API Economy | Capability Economy |
|--------|-------------|-------------------|
| Atomic Unit | API | Capability |
| Application Focus | Provider integration | Capability composition |
| Provider Relationship | Direct | Abstracted |
| Portability | Limited | High |
| Market Structure | API marketplaces | Capability marketplaces |

**Implications:**

1. **Provider Substitution:** Capabilities can be provided by multiple vendors, enabling substitution
2. **Standardized Interfaces:** Capabilities are defined by protocols, not provider-specific formats
3. **Capability Markets:** Capabilities can be discovered, compared, and selected dynamically
4. **Application Portability:** Applications depend on capabilities, not providers

✅ **Incentive Compatibility and Provider Adoption**

A critical question for the Capability Economy is: *Why would providers (like OpenAI, Anthropic) adopt standardized capability protocols when API lock-in benefits their business model?*

**The Lock-in Incentive:** Provider-specific APIs create switching costs that retain customers. Standardized capabilities reduce these barriers, potentially commoditizing provider offerings.

**Market-Driven Adoption Forces:**

Despite lock-in incentives, several forces drive providers toward capability standardization:

| Force | Mechanism | Example |
|-------|-----------|---------|
| **Developer demand** | Developers prefer portable applications | LangChain's [9] multi-provider support |
| **Enterprise requirements** | Procurement mandates flexibility | "No vendor lock-in" clauses |
| **Ecosystem effects** | Standards increase total market size | USB, HTTP, SQL history |
| **Competitive pressure** | Laggards adopt standards to compete | OpenAI's API evolution |

**Technical Adoption Mechanisms:**

1. **Decentralized Capability Registry:**
   
   ```yaml
   # Distributed registry architecture
   capability_registry:
     topology: federated
     
     nodes:
       - type: community_registry
         url: https://registry.capability.dev
         governance: open_source
         
       - type: enterprise_registry
         url: https://internal.company/registry
         sync: community_registry
         
     provider_registration:
       mechanism: self_publish
       verification: automated_schema_check
       reputation: community_ratings
   ```

2. **Open Protocol Standards:**
   
   The `ai-protocol` specification is an open standard that:
   - Defines capability schemas independent of any provider
   - Enables any provider to publish capability manifests
   - Supports both centralized and federated registries
   
   Providers adopting `ai-protocol` gain:
   - Access to applications built on standard capabilities
   - Reduced integration friction for developers
   - Participation in growing capability ecosystem

3. **Application-Level Standards Pressure:**
   
   When applications specify capability requirements rather than providers:
   
   ```yaml
   # Application requirements (provider-agnostic)
   app_requirements:
     capabilities:
       - text_generation
       - text_embedding
       - search_web
     
   # NOT: providers: [openai]
   ```
   
   The market shifts from competing on API lock-in to competing on capability quality, latency, and cost.

**Adoption Pathway:**

```
Early Adopters → Capability Standards → Application Portability 
    → Developer Demand → Provider Adoption (or market exit)
```

**Historical Precedent:**

Similar transitions occurred in:
- **Cloud APIs**: AWS proprietary → Kubernetes [2]/Terraform standards
- **Databases**: Oracle lock-in → PostgreSQL, MySQL standards
- **Communication**: Proprietary protocols → SIP, WebRTC standards

In each case, standards emerged through developer demand and competitive pressure, not purely through provider willingness. The Capability Economy follows this pattern: market forces will drive standardization regardless of individual provider preferences.

### 2.4 What is a Capability?

✅ **Precise Definition**

A capability is a semantically defined executable ability that transforms specified inputs into intended outcomes through a well-defined execution process.

**Formal Definition:**
```
Capability C = (Name, Input Schema, Output Schema, Execution Semantics)
```

**Components:**

1. **Name:** Semantic identifier (e.g., `generate_text`, `search_web`, `send_email`)
2. **Input Schema:** Structured specification of valid inputs
3. **Output Schema:** Structured specification of outputs
4. **Execution Semantics:** How the capability is performed

**Essential Distinction:**

| Concept | Essence | Role |
|---------|---------|------|
| Function | Computation | Algorithmic operation |
| API | Remote interface | Access mechanism |
| Tool | Agent-callable function | Invocation interface |
| **Capability** | **Executable ability** | **Real-world action** |

**Key Insight:**
> *Capabilities represent abilities (what can be done), while APIs represent access mechanisms (how to invoke).*

This distinction is fundamental to understanding the Capability Economy. Capabilities abstract what actions are possible, while APIs specify how to perform them.

---

## 3. The AI Native Software Stack

### 3.1 Five-Layer Architecture

The AI Native Stack comprises five distinct layers:

```
┌─────────────────────────────────────┐
│        Interface Layer               │
│   Web UI │ Mobile │ Voice │ CLI      │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│    AI Native Applications           │
│    Agents │ Workflows │ Services    │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│      AI Cognition Layer             │
│    LLMs │ Reasoning │ Planning      │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│       AI Action Layer               │
│                                     │
│  ┌───────────────────────────────┐ │
│  │   Contact Layer (Routing)     │ │
│  │   • Capability Routing        │ │
│  │   • Provider Selection        │ │
│  │   • Policy Evaluation         │ │
│  └───────────┬───────────────────┘ │
│              │                      │
│              ▼                      │
│  ┌───────────────────────────────┐ │
│  │   Execution Runtime           │ │
│  │   • API Invocation            │ │
│  │   • Tool Execution            │ │
│  │   • Error Handling            │ │
│  └───────────────────────────────┘ │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Capability Ecosystem           │
│   Models │ APIs │ Tools │ Devices   │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│        Infrastructure               │
│   Cloud │ Edge │ Networks │ GPUs    │
└─────────────────────────────────────┘
```

### 3.2 Layer Responsibilities

#### 3.2.1 Interface Layer

**Purpose:** User interaction mechanisms.

**Components:**
- Web interfaces
- Mobile applications
- Voice assistants
- Command-line tools
- Chat interfaces

**Responsibilities:**
- Present AI capabilities to users
- Collect user input and intent
- Display results and feedback
- Handle user sessions

**Examples:**
- ChatGPT web interface
- Perplexity search UI
- Cursor IDE integration
- Custom application interfaces

#### 3.2.2 AI Native Applications

**Purpose:** Application logic and agent coordination.

**Components:**
- AI agents
- Workflows
- Autonomous systems
- AI assistants
- Vertical AI services

**Responsibilities:**
- Define application goals
- Orchestrate agent behavior
- Manage application state
- Coordinate multiple agents
- Integrate with data sources

**Key Concept:** AI Native Applications differ fundamentally from traditional applications:

| Aspect | Traditional Applications | AI Native Applications |
|--------|-------------------------|----------------------|
| Logic Source | Developer-written code | Agent reasoning + code |
| Capability Integration | Direct API calls | Capability composition |
| Flexibility | Static workflows | Dynamic capability graphs |
| Provider Relationship | Direct coupling | Capability abstraction |

**Application Packaging:**

AI Native Applications are packaged as application schemas:

```yaml
app_schema:
  name: research_assistant
  version: "1.0"
  
  agents:
    - name: researcher
      type: autonomous
      capabilities: [search_web, analyze_document, summarize]
  
  data_sources:
    - type: knowledge_base
      path: /data/papers
  
  ui:
    type: chat
    components: [input, output, status]
  
  capability_requirements:
    - search_web
    - analyze_document
    - summarize_text
```

#### 3.2.3 AI Cognition Layer

**Purpose:** Intelligent reasoning and planning.

**Components:**
- Large Language Models (LLMs)
- Foundation models
- Reasoning engines
- Planning systems
- Memory systems

**Responsibilities:**
- Understand user intent
- Plan sequences of actions
- Make decisions
- Maintain context and memory
- Generate capability requests

**Output:** Capability intents (what capabilities to invoke, with what parameters).

**Examples:**
- GPT-4, Claude, Gemini (LLMs)
- Chain-of-thought reasoning
- Multi-step planning
- Context management

✅ **Clarifying Layer Boundary: Cognition and Routing**

A critical architectural question arises: *Does the Cognition Layer participate in routing decisions, or does routing belong entirely to the Action Layer?*

**The Principle:** The Cognition Layer outputs **capability intents** (what to do), while the Action Layer determines **how to execute** (which provider, which parameters). This separation maintains the Cognition–Action boundary.

**Complex Routing Scenarios:** Some routing decisions may require cognitive judgment—for example, selecting a model with better emotional understanding based on conversation tone. In such cases:

```yaml
# Routing Policy with Cognitive Delegation
routing_rule:
  capability: text_generation
  context: {tone: empathetic}
  
  # Action Layer delegates to micro-cognition
  micro_cognition:
    model: classifier-small
    task: "detect_emotional_context"
    output: routing_hint
    
  # Final routing uses cognitive output
  provider_selection:
    strategy: use_routing_hint
    fallback: default_provider
```

**Micro-Cognition Pattern:** The Action Layer can invoke lightweight cognitive models to assist routing decisions without violating the separation principle:

| Decision Type | Handled By | Mechanism |
|---------------|------------|-----------|
| Standard routing | Action Layer | Policy evaluation |
| Context-aware routing | Action Layer + Micro-Cognition | Delegated classification |
| Strategic planning | Cognition Layer | Agent reasoning |
| Intent generation | Cognition Layer | LLM inference |

This architecture ensures that complex routing decisions remain within the Action Layer's domain while leveraging cognitive capabilities as needed.

#### 3.2.4 AI Action Layer

**Purpose:** Mediate between cognition and execution.

**Components:**

**Contact Layer (Routing/Policy):**
- Capability routing
- Provider selection
- Policy evaluation
- Environment selection
- Cost optimization

**Execution Runtime:**
- API invocation
- Tool execution
- Protocol translation
- Error handling
- Result normalization

**Responsibilities:**
- Route capability requests to appropriate providers
- Execute capability invocations
- Handle failures and retries
- Normalize results
- Enforce policies

✅ **Clarifying Terminology**

A common source of confusion is the relationship between Contact Layer and Execution Layer. Based on architectural clarity:

**Original Intuition:** Many practitioners conceive of a single "execution/contact layer" that handles both routing and execution. This intuition is correct—there is one macro layer: the **AI Action Layer**.

**Architectural Decomposition:** For software engineering purposes, the Action Layer decomposes into:

1. **Contact Layer:** Routing and policy decisions (control plane)
2. **Execution Runtime:** Capability invocation mechanics (data plane)

**Unified View:**
```
AI Action Layer (Macro Layer)
├── Contact Layer (Routing - Control Plane)
└── Execution Runtime (Execution - Data Plane)
```

Both perspectives are valid—different abstraction levels for different purposes.

**Defining Statement:**
> *The Action Layer is the action interface between AI cognition and the real-world capability ecosystem.*

#### 3.2.5 Capability Ecosystem

**Purpose:** Supply side of AI capabilities.

**Components:**

**Capability Providers:**
- AI model providers (OpenAI, Anthropic, Google, DeepSeek)
- SaaS API providers (Stripe, Twilio, Salesforce)
- Database providers (PostgreSQL, MongoDB, Redis)
- Automation tools (Zapier, Make, n8n)
- Device/IoT providers (MQTT, Home Assistant)

**Capability Registry:**
- Capability catalog
- Provider discovery
- Capability indexing
- Type checking

**Capability Marketplace:**
- Capability catalog
- Pricing and billing
- Reviews and ratings
- Quality assurance

**Capability Protocol (ai-protocol):**
- Provider manifests
- Capability definitions
- Validation rules
- Version management

**Responsibilities:**
- Provide capabilities
- Register capabilities with protocol
- Maintain capability metadata
- Expose capability endpoints

#### 3.2.6 Infrastructure Layer

**Purpose:** Computational and network resources.

**Components:**
- Cloud platforms (AWS, GCP, Azure)
- Edge devices
- Local machines
- GPUs and accelerators
- Storage systems
- Networks

**Responsibilities:**
- Provide compute resources
- Enable network connectivity
- Store data and models
- Support edge deployment

---

## 4. Four Core Principles

### 4.1 Principle 1: Capability Abstraction Principle

**Statement:**
> *An AI agent should depend on capabilities rather than concrete providers or APIs.*

**Formal Definition:**

A capability C is defined as:
```
C = (Name, Input Schema, Output Schema, Execution Semantics)
```

A provider P implements capability C:
```
P implements C
```

Agents invoke capabilities:
```
Invoke(C, Input) → Output
```

Rather than invoking provider APIs directly:
```
Invoke(P.API, Input) → Output
```

**Significance:**

This principle achieves **agent-provider decoupling**. Agents express what they need (capabilities) without specifying how to obtain it (which provider).

**Benefits:**

1. **Provider Substitution:** Providers can be substituted without modifying agents
2. **Multi-Provider Capabilities:** A capability can be implemented by multiple providers
3. **Standardized Discovery:** Capabilities can be discovered through standardized registries
4. **Ecosystem Growth:** New providers can enter by implementing standard capabilities

**Example:**

An agent needs to translate text. Instead of:
```python
# Direct API call (coupled)
result = openai.translate(text, target_lang="es")
```

The agent invokes a capability:
```python
# Capability abstraction (decoupled)
result = invoke_capability("translate_text", {
    "text": text,
    "target_lang": "es"
})
```

The capability layer determines which provider to use based on context (cost, latency, quality).

### 4.2 Principle 2: Cognition–Action Separation Principle

**Statement:**
> *AI cognition and capability execution should be separated by an action layer.*

**Architecture:**

```
Cognition Layer (Think)
      ↓
Action Layer (Route & Execute)
      ↓
Capability Providers (Act)
```

**Rationale:**

Without this separation, agents must directly call APIs, tools, and services, leading to:
- Tight coupling to specific providers
- Limited portability across environments
- Ecosystem fragmentation

The Action Layer mediates between:
- **What to do** (decided by cognition)
- **How to do it** (handled by action layer)

**Responsibilities:**

**Cognition Layer:**
- Understand user goals
- Plan action sequences
- Make decisions
- Generate capability intents

**Action Layer:**
- Route capability requests
- Select providers
- Execute invocations
- Handle failures
- Normalize results

**Analogy:**

This separation parallels other system designs:

| System | Think | Act |
|--------|-------|-----|
| Operating System | Process scheduler | I/O subsystem |
| Network | Control plane | Data plane |
| AI Native | Cognition layer | Action layer |

### 4.3 Principle 3: Capability Routing Principle

**Statement:**
> *Capability execution should be dynamically routed based on context.*

**Routing Function:**
```
Route(Capability, Context) → Provider
```

**Context Parameters:**

1. **Latency:** Response time requirements
2. **Cost:** Budget constraints
3. **Policy:** Organizational or regulatory policies
4. **Availability:** Provider uptime and reliability
5. **Security:** Data handling and privacy requirements
6. **Quality:** Output quality requirements

**Routing Example:**

For capability `translate_text`, available providers:
- Provider A: $0.001/request, 500ms latency, 95% accuracy
- Provider B: $0.002/request, 200ms latency, 98% accuracy

Routing decisions:

```
Context: {priority: "speed"}
Route(translate_text, Context) → Provider B

Context: {priority: "cost"}
Route(translate_text, Context) → Provider A

Context: {priority: "quality"}
Route(translate_text, Context) → Provider B
```

**Implementation:**

Routing can be implemented through:

1. **Static Policies:** Organization-defined routing rules
2. **Dynamic Optimization:** Runtime optimization based on metrics
3. **Machine Learning:** Learned routing models
4. **User Preferences:** User-specified provider preferences

**Analogy:**

This mechanism is similar to:
- DNS routing (routing domain requests to servers)
- Service mesh routing (routing service requests to instances)
- CDN routing (routing content requests to edge nodes)

However, the objects being routed are **capabilities**, not network requests.

### 4.4 Principle 4: Capability Graph Execution

**Statement:**
> *Complex AI tasks can be modeled as execution over a capability graph.*

**Formal Definition:**

A Capability Graph G is:
```
G = (Nodes, Edges)
```

Where:
- Nodes = Capabilities to execute
- Edges = Dependencies between capabilities

**Example Task:**

"Research and write a blog post about AI architecture trends"

**Capability Graph:**

```
search_web("AI architecture 2024")
        ↓
analyze_documents(search_results)
        ↓
synthesize_findings(analysis)
        ↓
generate_outline(synthesis)
        ↓
write_draft(outline)
        ↓
edit_and_polish(draft)
```

**Execution Process:**

1. **Agent Reasoning:** Agent analyzes task and constructs capability graph
2. **Routing:** Action layer determines which provider for each capability
3. **Execution:** Runtime invokes each capability in dependency order
4. **Data Flow:** Results flow through graph, each capability receiving inputs from predecessors
5. **Result:** Final output returned to agent

**Graph Properties:**

**Directed Acyclic Graph (DAG):** Most capability graphs are DAGs, ensuring execution completes.

**Parallel Execution:** Independent capabilities can execute in parallel:

```
search_web ──┐
             ├──→ analyze_and_synthesize
search_db  ──┘
```

**Conditional Execution:** Some graphs include conditional branches:

```
search_capability
      ↓
[quality_check]
   ↓        ↓
[great]    [poor]
   ↓          ↓
use_direct  retry_different
```

**Dynamic Construction:** Agents can construct capability graphs dynamically based on:

- Task complexity
- Available capabilities
- Intermediate results
- User feedback

✅ **Distributed Graph Execution: Failure Handling and Transactions**

In distributed environments, capability graph execution introduces significant complexity. The Action Layer must handle partial failures and maintain consistency.

**Partial Node Failure Handling:**

When a node in the capability graph fails, the system must decide: retry, compensate, or propagate failure.

```yaml
# Failure Handling Strategies
graph_execution:
  failure_policy:
    # Node-level retry with exponential backoff
    node_retry:
      max_attempts: 3
      backoff_ms: [100, 500, 2000]
      
    # Fallback to alternative provider
    fallback:
      enabled: true
      strategy: next_provider
      
    # Compensation for completed nodes
    compensation:
      enabled: true
      trigger: downstream_failure
```

**Saga Pattern for Long Transactions:**

For multi-step capability graphs, the Action Layer implements the Saga pattern to handle long-running transactions:

```yaml
# Saga Pattern Implementation
saga_execution:
  name: research_workflow
  
  steps:
    - name: search_web
      capability: search
      compensate: clear_cache
      
    - name: analyze_documents
      capability: analyze
      compensate: delete_analysis
      
    - name: generate_report
      capability: generate
      compensate: delete_report
      
  execution_mode: sequential
  
  failure_handling:
    on_step_failure: compensate_previous
    compensation_order: reverse
```

**Execution State Machine:**

Each capability node maintains execution state:

| State | Description | Next States |
|-------|-------------|-------------|
| `pending` | Waiting to execute | `running` |
| `running` | Currently executing | `completed`, `failed`, `timeout` |
| `completed` | Successfully finished | `compensating` (if downstream fails) |
| `failed` | Execution failed | `retrying`, `compensated` |
| `compensating` | Running compensation | `compensated` |
| `compensated` | Compensation complete | Terminal |

**Data Dependency Management:**

Between graph nodes, data flows through typed channels:

```
search_web(search_results) → analyze(analyzed_data) → generate(report)
```

The Action Layer manages:
- **Data transformation**: Converting outputs to match downstream input schemas
- **State checkpointing**: Saving intermediate results for recovery
- **Parallel coordination**: Synchronizing data from parallel branches

✅ **Data Mapping Layer (Optional)**

In complex capability graphs, upstream outputs may not perfectly match downstream input schemas. The Action Layer can optionally support lightweight data mapping:

```yaml
# Data Mapping Configuration
data_mapping:
  enabled: true
  transformations:
    # Field renaming
    - type: rename
      source: search_results.items
      target: documents
    
    # Field extraction
    - type: extract
      source: analysis.key_points
      target: summary.points
    
    # Type coercion
    - type: coerce
      source: metadata.count
      target: pagination.total
      from_type: string
      to_type: integer
    
    # Nested object flattening
    - type: flatten
      source: response.data
      prefix: result_
```

**Mapping Layer Scope:**

| Transformation Type | Allowed | Rationale |
|---------------------|---------|-----------|
| Field rename/alias | ✅ | Non-destructive, semantic equivalence |
| Type coercion | ✅ | Common necessity (string→int, etc.) |
| Field extraction | ✅ | Reducing data to relevant subset |
| Object flattening | ✅ | Adapting structure |
| Computed fields | ⚠️ Limited | Should remain simple (no LLM calls) |
| Business logic | ❌ | Belongs in application layer |

**Design Principle:** The data mapping layer should remain **declarative and deterministic**. Complex transformations requiring semantic understanding (e.g., summarization, entity extraction) should be implemented as separate capabilities in the graph, not as mapping rules.

**Recovery Mechanisms:**

```python
# Pseudo-code for graph recovery
class CapabilityGraphExecutor:
    def execute_with_recovery(self, graph, checkpoint_path):
        # Load checkpoint if exists
        state = self.load_checkpoint(checkpoint_path)
        
        for node in graph.get_pending_nodes(state):
            try:
                result = self.execute_node(node)
                self.save_checkpoint(checkpoint_path, node, result)
            except NodeFailure as e:
                if self.should_retry(node):
                    continue  # Retry with backoff
                elif self.should_compensate(e):
                    self.run_compensation(graph, node)
                    raise SagaAborted(node, e)
                else:
                    raise
```

This architecture ensures that capability graphs execute reliably in distributed environments, with clear failure semantics and recovery mechanisms.

---

## 5. Capability Ecosystem Architecture

### 5.1 Ecosystem Components

The Capability Ecosystem comprises four essential components:

#### 5.1.1 Capability Providers

**Definition:** Entities that implement and expose capabilities.

**Types:**

1. **AI Model Providers:**
   - Large language models (OpenAI, Anthropic, Google)
   - Image generation (DALL-E, Midjourney, Stable Diffusion)
   - Speech models (Whisper, TTS systems)
   - Embedding models (text-embedding-ada, Cohere)

2. **SaaS API Providers:**
   - Payment (Stripe, PayPal)
   - Communication (Twilio, SendGrid)
   - CRM (Salesforce, HubSpot)
   - Storage (S3, Cloud Storage)

3. **Database Providers:**
   - SQL databases (PostgreSQL, MySQL)
   - NoSQL databases (MongoDB, Redis)
   - Vector databases (Pinecone, Weaviate)
   - Graph databases (Neo4j, Amazon Neptune)

4. **Automation Providers:**
   - Workflow automation (Zapier, Make)
   - Integration platforms (n8n, Huginn)
   - RPA systems (UiPath, Automation Anywhere)

5. **Device/IoT Providers:**
   - Home automation (Home Assistant, SmartThings)
   - Industrial IoT (AWS IoT, Azure IoT)
   - Robotics platforms (ROS, industrial controllers)
   - Sensors and actuators

**Provider Responsibilities:**
- Implement capabilities according to protocol
- Register capabilities with ecosystem
- Maintain capability availability
- Provide capability metadata

#### 5.1.2 Capability Protocol

**Definition:** Standardized format for describing capabilities.

**Components:**

**Provider Manifest:**

```yaml
provider:
  name: example_provider
  version: "1.0.0"
  description: Example AI capability provider
  website: https://example.com
  
  capabilities:
    - name: generate_text
      version: "1.0"
      description: Generate text based on prompt
      
      input_schema:
        type: object
        properties:
          prompt:
            type: string
          max_tokens:
            type: integer
            default: 1000
        required: [prompt]
      
      output_schema:
        type: object
        properties:
          text:
            type: string
          tokens_used:
            type: integer
      
      execution:
        endpoint: /v1/generate
        method: POST
        timeout_ms: 30000
      
      pricing:
        model: per_token
        rate: 0.00002
      
      metadata:
        category: AI
        tags: [text, generation, llm]
```

**Capability Type Definitions:**

Standard types for common capabilities:

- `text_generation` - Generate text from prompts
- `text_embedding` - Create text embeddings
- `image_generation` - Generate images from descriptions
- `image_analysis` - Analyze image content
- `speech_recognition` - Transcribe audio
- `speech_synthesis` - Generate speech
- `translation` - Translate between languages
- `search` - Search for information
- `data_query` - Query data sources

#### 5.1.3 Capability Registry

**Definition:** Central index of available capabilities.

**Functions:**

1. **Capability Indexing:**

```
Capability Index:
chat/
├── openai (gpt-4, gpt-3.5-turbo)
├── anthropic (claude-3-opus, claude-3-sonnet)
└── google (gemini-pro)

embedding/
├── openai (text-embedding-ada-002)
├── cohere (embed-multilingual)
└── google (text-embedding-gecko)

translation/
├── google (translation-api)
├── deepl (api-v2)
└── amazon (translate)
```

2. **Provider Discovery:**

```
Query: capabilities providing "text_generation"
Result:
  - openai/gpt-4
  - anthropic/claude-3-opus
  - google/gemini-pro
  - deepseek/deepseek-chat
```

3. **Type Checking:**

Validate capability invocations against schemas:

```
Invocation: generate_text(prompt=123)
Error: Type mismatch - expected string, got integer
```

4. **Version Management:**

Track capability versions and compatibility:

```
generate_text:
  v1.1: Basic generation
  v1.1: Added max_tokens parameter
  v2.0: Streaming support (breaking change)
```

#### 5.1.4 Capability Marketplace

**Definition:** Platform for capability discovery and monetization.

**Functions:**

1. **Capability Catalog:**

Browse available capabilities by:
- Category
- Provider
- Use case
- Popularity

2. **Pricing & Billing:**

- Per-call pricing
- Subscription models
- Usage-based billing
- Credit systems

3. **Quality Assurance:**

- Provider verification
- Capability reviews
- Performance benchmarks
- Uptime monitoring

4. **Discovery:**

- Search capabilities
- Compare providers
- View examples
- Read documentation

### 5.2 Ecosystem Interactions

**Provider Registration Flow:**

```
1. Provider implements capabilities
2. Provider creates manifest (ai-protocol)
3. Provider registers with registry
4. Registry validates manifest
5. Capabilities indexed and discoverable
6. Marketplace lists capabilities
```

**Capability Invocation Flow:**

```
1. Agent requests capability
2. Contact layer queries registry
3. Registry returns available providers
4. Contact layer selects provider (routing)
5. Execution runtime invokes provider
6. Result normalized and returned
```

**Ecosystem Growth:**

```
New Provider → Register → Available → Applications Use → Ecosystem Expands
```

---

## 6. Software Development Paradigm Shift

### 6.1 Traditional Software Development

**Code-Centric Model:**

Traditional software development is **code-centric**:

```
Developer writes code
      ↓
Code calls APIs
      ↓
APIs perform actions
```

**Characteristics:**
- Logic is explicitly programmed
- API calls are hardcoded
- Provider relationships are direct
- Changes require code modification

### 6.2 AI Native Software Development

**Capability-Centric Model:**

AI Native development is **capability-centric**:

```
Agent reasons about task
      ↓
Agent invokes capabilities
      ↓
Capabilities perform actions
```

**Characteristics:**
- Logic is partially generated by AI
- Capability invocations are abstract
- Provider relationships are mediated
- Changes can be runtime decisions

### 6.3 Paradigm Comparison

| Aspect | Traditional Software | AI Native Software |
|--------|---------------------|-------------------|
| Logic Source | Developer code | Agent reasoning + code |
| Integration Unit | API | Capability |
| Provider Relationship | Direct | Abstracted |
| Flexibility | Static | Dynamic |
| Portability | Limited | High |
| Adaptation | Code change | Capability selection |

### 6.4 Implications for Developers

**Role Shift:**

From:
- Writing API integration code
- Managing provider credentials
- Implementing retry logic
- Hardcoding provider selection

To:
- Defining capability requirements
- Designing agent workflows
- Configuring routing policies
- Composing capability graphs

**Skill Evolution:**

New skills required:
- Capability modeling
- Agent behavior design
- Policy configuration
- Ecosystem navigation

### 6.5 Software Composition

**Traditional Composition:**

```python
# Direct API composition
def research_topic(topic):
    # Hardcoded provider
    search_results = google_search(topic)
    
    # Direct API call
    analysis = openai_analyze(search_results)
    
    # Explicit provider
    summary = anthropic_summarize(analysis)
    
    return summary
```

**AI Native Composition:**

```python
# Capability composition
def research_topic(topic):
    # Capability graph
    workflow = CapabilityGraph([
        ("search_web", {"query": topic}),
        ("analyze_documents", {}),
        ("summarize_text", {})
    ])
    
    # Agent-driven execution
    result = agent.execute(workflow)
    
    return result
```

**Benefits:**
- Provider selection is abstracted
- Workflow can be dynamically optimized
- Capabilities can be substituted
- Execution can be distributed

---

## 7. Architectural Benefits

### 7.1 Decoupling

**Agent-Provider Decoupling:**

Agents express capability requirements without knowing providers:

```
Agent Request: "search_web"
              ↓
Action Layer: Selects provider based on context
              ↓
Provider A or Provider B
```

**Benefits:**
- Providers can be substituted
- Multi-provider strategies are possible
- Failover is automatic
- Ecosystem competition improves quality

### 7.2 Portability

**Application Portability:**

Applications defined by capability requirements, not provider dependencies:

```
Application Requirements:
  - generate_text
  - search_web
  - send_email
```

Can run on any runtime that provides these capabilities.

**Benefits:**
- Applications are cloud-agnostic
- Edge deployment is straightforward
- Vendor lock-in is reduced
- Migration costs are lower

### 7.3 Capability Discovery

**Dynamic Discovery:**

New capabilities are discovered at runtime:

```
Application Startup:
  - Query registry for required capabilities
  - Select providers based on policies
  - Configure routing rules
  - Begin execution
```

**Benefits:**
- New providers enter ecosystem without application changes
- Capabilities are discovered at runtime
- Ecosystem growth is organic
- Competition is encouraged

### 7.4 Ecosystem Growth

**Network Effects:**

```
More Providers → More Capabilities → More Applications → More Users → More Providers
```

**Benefits:**
- Ecosystem grows organically
- Competition improves quality
- Innovation is accelerated
- Standardization is incentivized

---

## 8. Future Directions

### 8.1 Capability Internet

**Vision:** Global network of discoverable capabilities.

**Analogy:**
- Web: Network of documents
- Cloud: Network of compute
- Capability Internet: Network of actions

**Architecture:**

```
Global Capability Registry
         ↓
    Regional Registries
         ↓
    Local Registries
         ↓
    Capability Providers
```

**Implications:**
- AI agents can invoke global capabilities
- Capability discovery is worldwide
- Local and global capabilities interoperate
- New economic models emerge

### 8.2 Capability Discovery Protocol

**Standardized Protocol for:**

1. **Registration:** How providers register capabilities
2. **Discovery:** How applications find capabilities
3. **Negotiation:** How terms are agreed
4. **Invocation:** How capabilities are called

**Requirements:**
- Decentralized
- Secure
- Efficient
- Interoperable

### 8.3 AI Application Packaging Standard

**Standardized Format:**

```yaml
ai_app_package:
  metadata:
    name: my_ai_app
    version: "1.0"
    author: Developer
  
  requirements:
    capabilities:
      - text_generation
      - search_web
    
    runtime:
      min_memory: 512MB
      recommended_gpu: true
  
  agents:
    - main_agent.yaml
  
  configuration:
    routing_policies:
      - cost_optimization.yaml
    
    providers:
      preferred: [openai, anthropic]
      fallback: [google]
  
  deployment:
    - cloud.yaml
    - edge.yaml
```

**Benefits:**
- Applications are portable
- Deployment is standardized
- Configuration is externalized
- Distribution is simplified

### 8.4 Edge-First Architecture

**Edge Deployment:**

AI Native Stack naturally supports edge deployment:

```
Edge Runtime:
├── Local Contact Layer
├── Local Execution Runtime
├── Local Capabilities
│   ├── On-device models
│   ├── Local automation
│   └── Home IoT
└── Cloud Fallback
```

**Benefits:**
- Low latency
- Privacy preservation
- Offline operation
- Reduced cloud costs

✅ **Lightweight Edge Runtime Mode**

Edge devices often have constrained resources (limited memory, no GPU, intermittent connectivity). The architecture supports a **"Forward-First, State-Up"** lightweight runtime mode:

```yaml
# Lightweight Edge Configuration
edge_runtime:
  mode: forward_first
  
  # Minimal local capabilities
  local_capabilities:
    - name: local_inference
      model: small_llm_quantized
      max_memory_mb: 512
    
    - name: local_control
      devices: [home_automation, sensors]
  
  # State management moved up
  state_handling:
    mode: stateless_local
    session_store: cloud_orchestrator
    checkpoint_interval: disabled  # No local persistence
    
  # Simplified routing
  routing:
    local_first: true
    fallback: cloud_contact_layer
    connection_mode: intermittent_ok
```

**Lightweight Mode Characteristics:**

| Feature | Full Runtime | Lightweight Edge |
|---------|--------------|------------------|
| Local Saga state machine | ✅ | ❌ (delegated to cloud) |
| Full policy evaluation | ✅ | ❌ (static or delegated) |
| Complex graph execution | ✅ | ⚠️ (simple sequences only) |
| Connection pooling | ✅ | ⚠️ (minimal) |
| Local capability cache | ✅ | ⚠️ (on-demand) |
| Failover handling | Full | Simplified (report and retry) |

**Use Cases:**
- IoT gateways with 512MB-1GB RAM
- Mobile devices with offline requirements
- Industrial controllers with real-time constraints
- Home automation hubs without persistent storage

### 8.5 End-to-End Testing in Capability-Abstracted Environments

**The Testing Challenge:**

Dynamic provider selection breaks traditional deterministic integration testing. An application may invoke different providers across test runs, making assertions on provider-specific behavior unreliable.

**Mock Provider Mechanism:**

The AI Protocol supports a standardized Mock Provider system for deterministic testing:

```yaml
# test_config.yaml
test_mode:
  enabled: true
  
  mock_providers:
    - capability: generate_text
      provider_id: mock_llm
      responses:
        - input_pattern: ".*summarize.*"
          output:
            text: "MOCK_SUMMARY"
            tokens_used: 100
          latency_ms: 50
        
        - input_pattern: ".*translate.*"
          output:
            text: "MOCK_TRANSLATION"
            tokens_used: 50
          latency_ms: 30
    
    - capability: search_web
      provider_id: mock_search
      responses:
        - input_pattern: ".*"
          output:
            results:
              - url: "https://mock.example.com"
                title: "Mock Search Result"
                snippet: "Mock content for testing"
            total_results: 1
          latency_ms: 10
  
  routing_policy:
    mode: deterministic
    provider_mapping:
      generate_text: mock_llm
      search_web: mock_search
```

**Test Implementation Example:**

```python
# Test with Mock Providers
def test_research_workflow():
    # Configure test environment
    runtime = TestRuntime(config="test_config.yaml")
    
    # Execute workflow (all calls go to mocks)
    result = runtime.execute("""
    research_topic("AI architecture")
    """)
    
    # Deterministic assertions
    assert result.status == "success"
    assert "MOCK_SUMMARY" in result.output
    assert runtime.call_count("mock_llm") == 1
    assert runtime.call_count("mock_search") >= 1
```

**Testing Levels:**

| Level | Provider | Purpose |
|-------|----------|---------|
| Unit | Mock | Algorithm correctness |
| Integration | Mock | Component interaction |
| Contract | Mock + Schema | Protocol compliance |
| E2E (dev) | Mock | Full workflow |
| E2E (staging) | Real | Provider compatibility |
| E2E (prod) | Real | Production behavior |

This layered approach enables deterministic testing while preserving the ability to validate against real providers when needed.

---

## 9. Related Work

### 9.1 Cloud Native Architecture

**Similarities:**
- Layered architecture
- Standardized interfaces
- Ecosystem focus

**Differences:**
- Cloud Native: Infrastructure automation
- AI Native: Agent-driven capability orchestration

### 9.2 Service Mesh

**Similarities:**
- Routing layer
- Policy enforcement
- Observability

**Differences:**
- Service Mesh: Network services
- AI Native: AI capabilities

### 9.3 Microservices

**Similarities:**
- Modular architecture
- Service composition
- Independent deployment

**Differences:**
- Microservices: Service-to-service communication
- AI Native: Agent-to-capability interaction

### 9.4 Current AI Frameworks

**LangChain [9]:**
- Provides agent orchestration
- Embeds execution in framework
- Limited standardization

**Model Context Protocol (MCP):**
- Defines capability-like tools
- Lacks action layer architecture
- Provider-specific integration
- **Limitations:**
  - Tool definitions are provider-coupled
  - No standardized routing abstraction
  - Missing capability graph execution model
  - Limited multi-provider composition

**OpenAI Plugins:**
- Capability exposure model
- Provider-centric
- No capability abstraction

---

## 10. Conclusion

The emergence of AI agents requires a new architectural framework for building software systems. This paper introduced the AI Native Software Stack, a five-layer architecture designed for agent-driven environments.

The stack separates concerns across five layers:

1. **Interface Layer:** User interaction
2. **AI Native Applications:** Agent orchestration
3. **AI Cognition Layer:** Reasoning and planning
4. **AI Action Layer:** Capability routing and execution
5. **Capability Ecosystem:** Capability provision

Four core principles define the stack's behavior:

1. **Capability Abstraction:** Agents depend on capabilities, not providers
2. **Cognition–Action Separation:** Intelligence and execution are separate
3. **Capability Routing:** Execution is dynamically routed based on context
4. **Capability Graph Execution:** Complex tasks decompose into capability graphs

This architecture enables the transition from API Economy to Capability Economy, where capabilities become the fundamental units of software composition. By introducing standardized protocols and runtime systems, the AI ecosystem can evolve toward a more modular and scalable architecture.

**Capability vs API: The Core Distinction**

As emphasized throughout this paper, the fundamental shift from API Economy to Capability Economy rests on a crucial distinction:

| Aspect | API Economy | Capability Economy |
|--------|-------------|-------------------|
| **Atomic Unit** | API endpoint | Capability definition |
| **Abstraction Level** | How to invoke | What can be done |
| **Provider Coupling** | Direct dependency | Abstracted through protocol |
| **Discovery** | Provider documentation | Standardized registry |
| **Substitution** | Code refactoring required | Policy change sufficient |
| **Market Structure** | API lock-in dynamics | Capability competition |

The Capability Economy does not eliminate APIs—it elevates them. APIs remain the implementation mechanism, but capabilities become the interface contract. This shift enables the portability, substitution, and ecosystem growth that the API Economy fundamentally cannot support.

As the ecosystem evolves, the AI Native Stack may serve as a foundational model for the next generation of intelligent software infrastructure.

---

## Appendix A: Capability Ecosystem Map

### A.1 Complete Ecosystem Structure

```
┌─────────────────────────────────────────────┐
│              Developers                      │
└──────────────────┬──────────────────────────┘
                   │ build
                   ▼
┌─────────────────────────────────────────────┐
│         AI Native Applications               │
│                                             │
│  • Agents                                   │
│  • Workflows                                │
│  • Services                                 │
│                                             │
│  Defined by: App Schema                     │
└──────────────────┬──────────────────────────┘
                   │ execute
                   ▼
┌─────────────────────────────────────────────┐
│           Action Layer                       │
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │      Contact Layer (Routing)            ││
│  │                                         ││
│  │  • Capability Routing                  ││
│  │  • Provider Selection                  ││
│  │  • Policy Evaluation                   ││
│  │  • Environment Selection               ││
│  └──────────────┬──────────────────────────┘│
│                 │                            │
│                 ▼                            │
│  ┌─────────────────────────────────────────┐│
│  │      Execution Runtime                   ││
│  │                                         ││
│  │  • API Invocation                      ││
│  │  • Tool Execution                      ││
│  │  • Error Handling                      ││
│  │  • Result Normalization                ││
│  └──────────────────────────────────────────┘│
└──────────────────┬──────────────────────────┘
                   │ invoke
                   ▼
┌─────────────────────────────────────────────┐
│         Capability Ecosystem                │
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │      Capability Providers               ││
│  │                                         ││
│  │  • AI Models                           ││
│  │  • SaaS APIs                           ││
│  │  • Databases                           ││
│  │  • Automation                          ││
│  │  • Devices                             ││
│  └─────────────────────────────────────────┘│
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │      Capability Protocol                ││
│  │                                         ││
│  │  • Provider Manifests                   ││
│  │  • Capability Definitions              ││
│  │  • Validation Rules                    ││
│  └─────────────────────────────────────────┘│
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │      Capability Registry                ││
│  │                                         ││
│  │  • Capability Index                    ││
│  │  • Provider Discovery                  ││
│  │  • Type Checking                       ││
│  └─────────────────────────────────────────┘│
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │      Capability Marketplace             ││
│  │                                         ││
│  │  • Capability Catalog                  ││
│  │  • Pricing & Billing                   ││
│  │  • Reviews                             ││
│  └─────────────────────────────────────────┘│
└──────────────────┬──────────────────────────┘
                   │ run on
                   ▼
┌─────────────────────────────────────────────┐
│           Infrastructure                     │
│                                             │
│  • Cloud Platforms                          │
│  • Edge Devices                             │
│  • Networks                                 │
│  • GPUs                                     │
└─────────────────────────────────────────────┘
```

---

## Appendix B: Capability Definition Examples

### B.1 Text Generation Capability

```yaml
name: generate_text
version: "1.0"
provider: openai
model: gpt-4

description: |
  Generate text based on a prompt using large language model.

input_schema:
  type: object
  properties:
    prompt:
      type: string
      description: The input prompt for generation
    max_tokens:
      type: integer
      default: 1000
      description: Maximum tokens to generate
    temperature:
      type: number
      default: 0.7
      minimum: 0
      maximum: 2
      description: Sampling temperature
  required: [prompt]

output_schema:
  type: object
  properties:
    text:
      type: string
      description: Generated text
    tokens_used:
      type: integer
      description: Number of tokens consumed
    finish_reason:
      type: string
      enum: [complete, length_limit, content_filter]

execution:
  endpoint: /v1/chat/completions
  method: POST
  timeout_ms: 30000
  retry:
    max_attempts: 3
    backoff_ms: 1000

pricing:
  model: per_token
  input_rate: 0.00003
  output_rate: 0.00006

metadata:
  category: AI
  tags: [text, generation, llm, language]
  capabilities: [streaming, function_calling]
```

### B.2 Web Search Capability

```yaml
name: search_web
version: "1.0"
provider: search_service

description: |
  Search the web for information.

input_schema:
  type: object
  properties:
    query:
      type: string
      description: Search query
    num_results:
      type: integer
      default: 10
      maximum: 100
      description: Number of results to return
    date_range:
      type: object
      properties:
        start:
          type: string
          format: date
        end:
          type: string
          format: date
  required: [query]

output_schema:
  type: object
  properties:
    results:
      type: array
      items:
        type: object
        properties:
          url:
            type: string
          title:
            type: string
          snippet:
            type: string
          relevance_score:
            type: number
    total_results:
      type: integer

execution:
  endpoint: /v1/search
  method: GET
  timeout_ms: 10000

pricing:
  model: per_request
  rate: 0.001

metadata:
  category: API
  tags: [search, web, information]
```

---

## Appendix C: Routing Policy Examples

### C.1 Cost Optimization Policy

```yaml
policy: cost_optimization
version: "1.0"

description: |
  Minimize cost while maintaining acceptable quality.

rules:
  - capability: "*"
    strategy: lowest_cost
    constraints:
      min_quality: 0.8
      max_latency_ms: 5000

  - capability: text_generation
    strategy: cost_quality_balance
    parameters:
      cost_weight: 0.7
      quality_weight: 0.3

  - capability: translation
    providers:
      preferred: [deepl, google]
      fallback: [amazon]
```

### C.2 Latency Optimization Policy

```yaml
policy: latency_optimization
version: "1.0"

description: |
  Minimize latency for real-time applications.

rules:
  - capability: "*"
    strategy: lowest_latency
    constraints:
      max_latency_ms: 500
      
  - capability: text_generation
    strategy: edge_first
    parameters:
      edge_threshold_ms: 1000
      cloud_fallback: true

  - capability: search_web
    providers:
      edge: [local_index]
      cloud: [google, bing]
    routing:
      - condition: "latency_requirement < 100ms"
        target: local_index
      - condition: "default"
        target: google
```

---

## Appendix D: Application Schema Example

### D.1 Research Assistant Application

```yaml
app_schema:
  metadata:
    name: research_assistant
    version: "1.0.0"
    description: AI-powered research assistant
    author: Research Team
  
  agents:
    - name: main_agent
      type: autonomous
      model: gpt-4
      capabilities:
        required:
          - search_web
          - analyze_document
          - summarize_text
          - generate_report
        optional:
          - translate_text
          - extract_entities
      
      behavior:
        max_iterations: 10
        timeout_ms: 60000
        retry_on_failure: true
      
      memory:
        type: conversation
        max_tokens: 8000
  
  data_sources:
    - name: papers
      type: knowledge_base
      path: /data/papers
      format: pdf
      
    - name: notes
      type: database
      connection: postgresql://localhost/research
  
  workflows:
    - name: research_topic
      trigger: user_request
      steps:
        - search_web
        - analyze_document
        - synthesize_findings
        - generate_report
  
  ui:
    type: chat_interface
    components:
      - input_box
      - output_display
      - status_indicator
      - capability_status
  
  configuration:
    routing_policy: balanced
    providers:
      preferred:
        text_generation: [openai, anthropic]
        search: [google, bing]
      fallback:
        text_generation: [google]
  
deployment:
  environments:
  - name: production
    runtime: cloud
    scaling: auto
    min_instances: 2

  - name: edge
    runtime: local
    capabilities:
      local: [text_generation_small]
      cloud_fallback: true
```

✅ **Portability Demonstration: Provider Switching Without Code Changes**

The following example demonstrates how the Research Assistant application can switch providers by modifying only the routing policy, without any application code changes:

**Scenario:** Organization initially deploys with OpenAI, then decides to switch to local DeepSeek for cost optimization.

**Original Configuration (OpenAI):**
```yaml
# config/routing_policy.yaml (original)
routing_policy:
  name: production_default
  version: "1.0"
  
  rules:
    - capability: text_generation
      providers:
        preferred: [openai]
        fallback: [anthropic]
      parameters:
        model: gpt-4
        
    - capability: search_web
      providers:
        preferred: [google]
```

**Modified Configuration (DeepSeek Local):**
```yaml
# config/routing_policy.yaml (modified)
routing_policy:
  name: production_default
  version: "1.1"  # Only version bump needed
  
  rules:
    - capability: text_generation
      providers:
        preferred: [deepseek_local]  # Changed provider
        fallback: [openai]           # Previous provider as fallback
      parameters:
        model: deepseek-chat
        endpoint: http://localhost:8080
        
    - capability: search_web
      providers:
        preferred: [google]          # Unchanged
```

**Application Code (No Changes Required):**
```python
# research_assistant.py - UNMODIFIED
from ai_runtime import CapabilityClient

def research_topic(topic):
    client = CapabilityClient()
    
    # Capability invocation - no provider references
    search_results = client.invoke("search_web", {"query": topic})
    analysis = client.invoke("analyze_document", {"content": search_results})
    summary = client.invoke("summarize_text", {"content": analysis})
    
    return summary
```

**Deployment Verification:**
```bash
# Switch providers with single command
kubectl apply -f config/routing_policy.yaml

# Verify routing change
ai-runtime status --capability text_generation
# Output: active_provider: deepseek_local (was: openai)

# No application restart required - routing is dynamic
```

**Key Observations:**

| Aspect | Traditional Approach | Capability-Based Approach |
|--------|---------------------|--------------------------|
| Provider switch requires | Code changes + redeployment | Config change only |
| Testing needed | Full regression test | Routing policy validation |
| Downtime | Application restart | Zero (hot-swap) |
| Rollback | Code rollback | Config revert |
| Developer involvement | Required | Not required |

This example illustrates the core benefit of capability abstraction: applications remain stable while infrastructure evolves. Operations teams can optimize provider selection without coordinating with development teams.

---

## References

[1] Newman, S. (2021). Building Microservices: Designing Fine-Grained Systems (2nd ed.). O'Reilly Media.

[2] Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). Borg, Omega, and Kubernetes. Communications of the ACM, 59(5), 50-57.

[3] Richardson, C. (2018). Microservices Patterns. Manning Publications.

[4] Fowler, M., & Lewis, J. (2014). Microservices: A Definition of This New Architectural Term. martinfowler.com.

[5] Cloud Native Computing Foundation. (2024). Cloud Native Definition v1.1. https://github.com/cncf/toc/blob/main/DEFINITION.md (Approved by TOC/GB: 2024-02-26)

[6] Service Mesh Interface. (2024). Service Mesh Interface Specification. https://smi-spec.io

[7] OpenAPI Initiative. (2024). OpenAPI Specification. https://spec.openapis.org/oas/latest.html

[8] GraphQL Foundation. (2024). GraphQL Specification. https://spec.graphql.org

[9] LangChain. (2024). LangChain Documentation. https://python.langchain.com/docs

[10] OpenAI. (2023). GPT-4 API Documentation. https://platform.openai.com/docs

[11] Anthropic. (2024). Claude API Reference. https://docs.anthropic.com

---

## Document Information

**Document Type:** Preprint
**Version:** 1.2
**Last Updated:** March 20, 2026
**Classification:** System Architecture Paper
**Review Status:** Revised Submission

---

**Acknowledgments**

The authors thank the reviewers whose feedback significantly strengthened this paper. Their comments led to: (1) clarification of the Cognition–Action boundary in routing decisions and the introduction of the micro-cognition pattern; (2) expansion of the capability graph execution model to address distributed failure handling and the Saga pattern; (3) deeper analysis of incentive compatibility and the market forces driving capability standardization; (4) requesting inline citations for improved academic rigor; and (5) suggesting updates to reference versions. We also thank the reviewers for suggesting the portability demonstration and the MCP limitations comparison, which clarified the Action Layer's unique contributions.

**Open Source Resources:** Reference implementations are available at https://github.com/ailib-official, including ai-lib-rust, ai-lib-python, ai-lib-ts, ai-lib-go, ai-protocol, and ai-lib-benchmark. The AI Protocol specification is maintained at https://github.com/ailib-official/ai-protocol.
