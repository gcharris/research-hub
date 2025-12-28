# **Technical Disclosure Report: The Open-Ludic Stack**

## **System and Method for Topologically Governed Generative Design via Hybrid Agent-Tool Orchestration**

### **1\. Introduction and Architectural Thesis**

The domain of Computer-Aided Design (CAD) and Building Information Modeling (BIM) stands at a critical juncture, precipitating a shift from static, explicit modeling to dynamic, generative synthesis. However, a significant dichotomy persists in the current state of the art: systems are either geometrically rigorous but semantically hollow (e.g., standard parametric modeling), or semantically rich but geometrically undisciplined (e.g., diffusion-based image generation). This report presents the "Open-Ludic Stack," a novel architectural framework designed to bridge this gap through the convergence of topological spatial analysis, stochastic constraint solving, and autonomous agent orchestration.

The primary objective of this disclosure is to establish a rigorous technical foundation for a Provisional Patent Application. The core innovation—the system for topologically governed generative design—introduces a governance layer based on "living structure" metrics, specifically the $ht$-index derived from Head/Tail Breaks classification, to constrain and guide stochastic generation algorithms such as Wave Function Collapse (WFC). Furthermore, the system necessitates a generalized communication protocol, herein defined as the Hybrid Agent-Tool Interface (HATI), which abstracts tool execution beyond current vendor-specific implementations like the Model Context Protocol (MCP) or Rhino.Compute, enabling a truly interoperable "Tool Universe."

This report provides an exhaustive analysis of the theoretical underpinnings, system architecture, and operational methodologies of the Open-Ludic Stack. It synthesizes advanced research in geographic information science, quantum-inspired algorithms, neuro-symbolic AI, and graph theory to demonstrate the non-obviousness and utility of the proposed invention. By integrating the recursive scaling laws of geographic space with the semantic reasoning of Large Language Models (LLMs), the Open-Ludic Stack offers a verifiable mechanism for generating designs that are not only functionally compliant but structurally resilient and organically coherent.

### **2\. The Theoretical Imperative: Topological Governance in Generative Design**

The fundamental deficiency in contemporary generative design lies in its reliance on Gaussian statistics and Euclidean geometry as primary descriptors of form. This approach fails to capture the inherent complexity of "living structures," which are characterized by heavy-tailed distributions and recursive hierarchies. To solve this, the Open-Ludic Stack adopts a governance model rooted in the topological analysis of scaling structures.

#### **2.1 The Failure of Gaussian Governance in Spatial Design**

Standard design optimization often seeks to minimize variance around a mean, assuming a normal distribution of features (e.g., average room size, average street length). However, empirical research into urban morphology and complex networks demonstrates that natural and successful artificial systems follow power-law distributions, where "far more small things than large ones" is the dominant rule.1

In geographic space, intrinsic scaling structures reveal that natural streets, hotspot clusters, and urban substructures follow these heavy-tailed distributions.1 The exponents for node- and Point-of-Interest (POI)-based clusters typically fall within the range of 2.0–2.2, indicating a specific fractal dimensionality that Gaussian models cannot represent.1 When generative algorithms are trained or constrained by Gaussian parameters, they produce "dead" structures—grids that lack the hierarchical vitality of organic cities or the functional coherence of evolved biological systems.

#### **2.2 Head/Tail Breaks as a Generative Constraint**

To rectify this, the Open-Ludic Stack utilizes the **Head/Tail Breaks** classification scheme as a primary governance mechanism. Unlike traditional classification methods (e.g., Jenks natural breaks) that seek to minimize within-class variance, Head/Tail Breaks explicitly reveals the underlying scaling hierarchy of a dataset.3

The mechanism operates recursively:

1. **Partitioning:** The dataset (e.g., a collection of generated spatial units) is divided into a "head" (values above the mean) and a "tail" (values below the mean).  
2. **Recursion:** The process is repeated for the head, continuing until the distribution of the remaining head is no longer heavy-tailed (i.e., the head/tail ratio is no longer significant).2  
3. **Indexing:** The number of recursions performed plus one constitutes the **$ht$-index**.5

In the proposed system, the $ht$-index serves as a **Topological Fitness Function**. During the generative process, the system evaluates the emerging geometry not merely on geometric collisions or boundary compliance, but on its $ht$-index. A valid design must exhibit an $ht$-index above a pre-determined threshold (typically $\\ge 3$ or $\\ge 7$ for high-complexity urban systems), ensuring that the generated structure possesses the requisite hierarchy of "far more smalls than larges".2 This effectively encodes the "universal rule" of geographic scaling directly into the generative logic, forcing the stochastic solver to converge on solutions that mirror the living geometry of the physical world.2

#### **2.3 The Shift from Fractal Geometry to Living Geometry**

While Mandelbrot’s fractal geometry provided the initial mathematical language for roughness and self-similarity, the Open-Ludic Stack aligns more closely with Christopher Alexander’s organic conception of the physical world, which posits that space is not a vacuum but a "living structure" defined by the recurrence of centers.7

The system distinguishes itself from prior art by operationalizing this philosophical shift. Where previous systems might use fractal dimension as a post-hoc analytical metric 5, the Open-Ludic Stack uses the $ht$-index and the underlying scaling pattern as *a priori* design constraints. This ensures that the generated output—whether a microscopic material lattice or a macroscopic urban plan—adheres to the structural laws that govern successful organic systems.2 This "Living Geometry" approach is more profound than simple self-similarity; it encompasses the inter-level relationships between the "head" (vital, large centers) and the "tail" (numerous, small centers), enforcing a structural coherence that simple iterative splitting cannot achieve.7

### **3\. The Generative Engine: Neuro-Symbolic Wave Function Collapse**

The second pillar of the Open-Ludic Stack is the generative engine itself. To satisfy the topological constraints imposed by the governance layer while adhering to the semantic intent of the user, the system employs a neuro-symbolic architecture. This architecture couples the rigorous constraint satisfaction of the **Wave Function Collapse (WFC)** algorithm with the semantic reasoning capabilities of Large Language Models (LLMs) operating via **Graph of Thought (GoT)** protocols.

#### **3.1 Wave Function Collapse: Entropy Reduction as Design Synthesis**

Wave Function Collapse (WFC) is a constraint-based algorithm inspired by quantum mechanics. In the context of the Open-Ludic Stack, the design domain (e.g., a 3D building grid) is initialized in a state of **superposition**, where every discrete unit (voxel) simultaneously contains all possible states (e.g., wall, floor, void, window).11

The generative process proceeds via **entropy reduction**:

1. **Observation:** The algorithm identifies the unit with the lowest non-zero entropy (the fewest possible remaining states) and "collapses" it to a single state based on weighted probabilities derived from the topological governance layer.  
2. **Propagation:** The consequences of this collapse are propagated to neighboring units based on adjacency rules (e.g., "a window cannot face a solid wall"), reducing their entropy.  
3. **Iteration:** This cycle repeats until the entire domain is resolved or a contradiction is reached.13

The novelty in this implementation lies in the modification of the collapse function. Standard WFC relies on local adjacency rules and random weights. The Open-Ludic Stack introduces **"Incursive Noetic" weighting**, a theoretical construct inspired by quantum patents that allows the system to manipulate state evolution from a position of "causal separation".15 Practically, this means the probability weights for the collapse are dynamically adjusted in real-time by the $ht$-index of the *current partial solution*. If a potential collapse would reduce the global $ht$-index below the threshold, its probability is suppressed, effectively steering the "wave function" toward topologically valid configurations.11

#### **3.2 Graph of Thought (GoT): Semantic Reasoning Integration**

While WFC handles the geometric syntax, it lacks semantic understanding. To bridge this, the system incorporates a **Graph of Thought (GoT)** module. Unlike linear "Chain of Thought" prompting, GoT allows LLMs to model reasoning as a non-linear network of "thoughts" (nodes) and dependencies (edges).16

This is critical for architectural design, which is inherently non-linear and iterative. The GoT module decomposes high-level user queries (e.g., "Design a hospital layout minimizing cross-contamination") into a **Function-Behavior-Structure (FBS)** graph.16 This graph maps:

* **Function:** The purpose of a space (e.g., "Patient Isolation").  
* **Behavior:** The performance characteristics (e.g., "Negative Pressure," "Restricted Access").  
* **Structure:** The physical elements required (e.g., "Airlock," "Solid Wall").

The GoT module translates these semantic requirements into *topological constraints* that are fed into the WFC solver. For example, the requirement for "efficiency" might be translated via GoT into a constraint minimizing the average path length between specific node types in the hypergraph.19 Furthermore, GoT enables the system to perform "backtracking" and "branch merging," allowing the LLM to explore multiple design hypothesis simultaneously before committing to a constraint set for the WFC engine.21

#### **3.3 The KAGS Framework: Knowledge Augmented Generalizer Specializer**

To further enhance the semantic capabilities of the engine, the Open-Ludic Stack integrates the **Knowledge Augmented Generalizer Specializer (KAGS)** framework.16 KAGS addresses the "cold start" problem in generative design by automating problem formulation.

* **Generalizer:** The system scans the "Tool Universe" and external knowledge bases (including patent repositories) to identify analogous design problems (e.g., using subsea layout optimization as an analogy for urban utility routing).16  
* **Specializer:** It then refines these general analogies into specific constraints applicable to the current project.

By employing KAGS within the GoT architecture, the system can automatically identify variables and parameters that the user may have omitted. For instance, if the user requests a "sustainable facade," the KAGS framework might infer the need for "variable shading coefficients" based on analogous patent data, injecting these as specific entropy weights into the WFC solver.16

### **4\. Data Structures: Hypergraphs and Semilattices**

To support the complex, multi-dimensional relationships inherent in topologically governed design, the Open-Ludic Stack eschews simple graph structures in favor of **Hypergraphs** and **Semilattices**.

#### **4.1 Hypergraphs for BIM Data Representation**

Traditional Building Information Modeling (BIM) often relies on relational databases or simple trees, which struggle to represent multi-party relationships (e.g., a wall that belongs to a room, a structural frame, and a fire zone simultaneously). The Open-Ludic Stack utilizes a **Hypergraph** data structure, where a single "hyperedge" can connect any number of nodes.24

This is essential for the *ht*\-index calculation, as the "head" of a distribution often consists of hyper-connected nodes (hubs) that serve multiple functional roles. The system employs **dynamic hypergraph structure learning** to update these relationships in real-time as the WFC algorithm collapses states.24 Furthermore, the system supports **Neutrosophic Multidirected Graphs**, capturing not just the existence of a relationship but its *indeterminacy* or *fuzziness*—a critical feature during the early conceptual phases where relationships are "soft" constraints.26

#### **4.2 The Semilattice of Design Problems**

Drawing again from Christopher Alexander, the system models the design problem not as a tree (which implies strictly hierarchical, non-overlapping subsets) but as a **Semilattice**.27 In a semilattice, two overlapping sets of requirements can belong to a larger parent set without forcing a rigid hierarchy.

This structure allows the Open-Ludic Stack to manage conflicting constraints (e.g., "maximize solar gain" vs. "minimize glare") without premature pruning. The WFC solver operates on this semilattice, finding solutions that satisfy the intersection of multiple overlapping constraint sets. The **$ht$-index** acts as the metric for the "coherence" of this semilattice, ensuring that the overlap of functions creates a coherent whole rather than a fragmented assembly of parts.27

### **5\. The Communication Protocol: Hybrid Agent-Tool Interface (HATI)**

The operational backbone of the Open-Ludic Stack is the **Hybrid Agent-Tool Interface (HATI)**. While recent developments like the Model Context Protocol (MCP) attempt to standardize LLM-tool interaction, they remain largely stateless and server-client bound. HATI generalizes this into a state-aware, protocol-agnostic orchestration layer.

#### **5.1 Protocol Specification and Architecture**

HATI is defined as a meta-protocol that governs the negotiation between **Agents** (logic carriers) and **Tools** (function carriers). It rests on three core specifications:

1. **State Injection (Topological Context Vector):** Unlike standard RPC calls, every request within HATI must include a "Topological Context Vector." This vector encapsulates the current $ht$-index, entropy distribution, and graph topology of the design state. This allows tools to be "state-aware." For example, a structural analysis tool receiving a vector indicating "high entropy/early conceptual phase" might automatically select a low-fidelity, rapid approximation method, whereas a "low entropy/final documentation" vector would trigger a high-fidelity FEM simulation.29  
2. **Capability Broadcasting & Bidding:** Tools in the Open-Ludic ecosystem do not wait to be called; they actively broadcast their capabilities via **Function-Behavior-Structure (FBS) descriptors**. When the Generative Engine identifies a need (e.g., "Verify Load Path"), relevant tools "bid" for execution rights based on their suitability for the current topological context. A **Tool Selection Agent** evaluates these bids, optimizing for the trade-off between computational cost and information gain.31  
3. **Output Refinement Augmentation (ORA):** To prevent "dead ends" in the generative process, HATI mandates that tools return **Output Refinement Augmentation**. If a tool identifies a failure (e.g., structural collapse), it does not merely return an error; it returns a *gradient* or *heuristic* suggesting how the input geometry should be modified to resolve the failure. This feedback is fed directly back into the GoT reasoning graph, closing the neuro-symbolic loop.33

#### **5.2 Beyond Vendor Lock-in: The "Tool Universe"**

HATI abstracts the underlying software layer. A "Wall Creation" request is standardized at the protocol level. Whether that request is executed by a Revit plugin, a Rhino/Grasshopper script, or a Blender geometry node is determined dynamically at runtime by the **Tool Optimizer** agent.31

This is achieved through **Dynamic Capability Discovery**. The interface queries the "Tool Universe" (a registry of available local and cloud services) and constructs a dynamic execution graph. This allows for **Heterogeneous Workflow Construction**, where a single design process might weave together a structural check from Robot (Autodesk), a daylight simulation from Radiance (Open Source), and a cost estimation from a custom Excel macro, all orchestrated transparently by the HATI protocol.31

#### **5.3 Multi-Agent Orchestration and Security**

The protocol supports hierarchical multi-agent systems. A "Supervisor Agent" maintains the global Graph of Thought, while specialized "Worker Agents" (e.g., Compliance Checker, Material Selector) execute specific sub-graphs.36 HATI includes strict **Privacy-Aware Prompt Design** and access control layers to ensure that sensitive design data (e.g., proprietary patent claims found during KAGS search) is not leaked to public LLMs during the orchestration process.21

### **6\. Prior Art Analysis and Differentiation**

To demonstrate patentability, it is crucial to differentiate the Open-Ludic Stack from existing solutions.

| Feature | Autodesk / Standard Generative Design | Pure Wave Function Collapse (Game Dev) | Standard LLM Agents (AutoGPT / MCP) | The Open-Ludic Stack (Proposed Invention) |
| :---- | :---- | :---- | :---- | :---- |
| **Governance** | Explicit Parameters (User Sliders) | Local Adjacency Rules | Semantic Prompts | **Topological ($ht$-index) \+ Universal Scaling Laws** |
| **Logic** | Evolutionary Optimization / Parametric | Stochastic Entropy Reduction | Probabilistic Token Prediction | **Neuro-Symbolic (GoT \+ WFC \+ KAGS)** |
| **Data Structure** | B-Rep / Mesh | Grid / Voxel / Tile | Vector Embeddings / Text | **Hypergraph / Semilattice / Neutrosophic Graph** |
| **Protocol** | Proprietary API / Plugins | Hardcoded Functions | Stateless REST / MCP | **HATI (State-Aware, ORA-enabled, Negotiation)** |
| **Objective** | Performance Metrics (Weight, Cost) | Visual Pattern Consistency | Task Completion | **"Living Structure" / Fractal Coherence** |

**Specific Patent Analysis:**

* **Autodesk (Generative Design):** Patents typically focus on parametric optimization and "design exploration" via evolutionary algorithms.38 They lack the explicit *topological governance* using heavy-tailed distributions.  
* **WFC (Maxim Gumin/Others):** While WFC is known 12, its application is largely confined to texture synthesis and game level layout. The integration of **Graph of Thought** reasoning and **$ht$-index governance** to drive WFC is a novel, non-obvious improvement.  
* **Agent Systems (Cognizant/IBM):** Recent patents focus on "Orchestration" of business processes.35 They do not address the specific requirements of *spatial* and *geometric* state management (Hypergraphs) or the feedback loop of topological fitness required for architectural validity.  
* **Quantum/Noetic Models:** Patents referencing "Wave Function Collapse" in quantum computing 11 establish the physical theory. The Open-Ludic Stack claims the *algorithmic adaptation* of these principles for design governance, specifically the "Incursive" control of entropy, which is a distinct application area.

### **7\. Feasibility and Implementation Strategy**

#### **7.1 Computational Feasibility of the $ht$\-index**

Calculating the $ht$-index is computationally efficient ($O(N \\log N)$), making it suitable for real-time iteration. For massive datasets (e.g., city-scale digital twins), the system applies the **Head/Tail Breaks** recursively to discard the "tail" (trivial data) and focus computational resources on the "head" (structural hubs), acting as a natural compression algorithm that preserves topological structure.2

#### **7.2 Integration of KAGS and GoT**

The implementation relies on a "Reasoning Kernel" that hosts the KAGS framework. This kernel utilizes a vector database (e.g., Qdrant/Weaviate) to store patent embeddings and design analogies.21 The Graph of Thought is managed via a graph database (e.g., Neo4j) where nodes represent "Reasoning States." This allows the system to persist the "thought process" alongside the geometry, enabling "Explainable AI" where a user can query *why* a specific wall was placed (e.g., "Placed to satisfy Fire Code X, derived from Patent Y, via Analogous Reasoning Z").16

### **8\. Draft Patent Specification**

The following section constitutes the formal draft of the "Abstract" and "Claims Summary" for the United States Patent and Trademark Office (USPTO) Provisional Patent Application.

#### **8.1 Abstract**

**Title:** SYSTEM AND METHOD FOR TOPOLOGICALLY GOVERNED GENERATIVE DESIGN VIA HYBRID AGENT-TOOL ORCHESTRATION (THE OPEN-LUDIC STACK)

Abstract:  
A system and method for generating complex, multi-scalar geometric structures through a topologically governed, neuro-symbolic architecture. The system comprises a Topological Governance Module configured to enforce heavy-tailed distribution scaling laws, specifically the head/tail breaks index ($ht$-index), upon geometric datasets to ensure fractal coherence; a Neuro-Symbolic Generative Engine that couples Large Language Model (LLM) reasoning using Graph of Thought (GoT) logic with a stochastic Wave Function Collapse (WFC) solver to iteratively reduce design entropy; and a Hybrid Agent-Tool Interface (HATI) that generalizes tool execution across heterogeneous software environments. The method involves initializing a design space in a state of superposition, decomposing user intent into a Function-Behavior-Structure (FBS) graph via a Knowledge Augmented Generalizer Specializer (KAGS) framework, and iteratively collapsing the wave function of the design space subject to constraints derived from both the semantic graph and the topological governance metrics. The HATI protocol enables dynamic, state-aware negotiation between autonomous agents and external digital tools, facilitating the generation of "living structures" that exhibit recursive fractal hierarchies. This architecture addresses the limitations of purely data-driven generative models by enforcing rigorous topological validity while maintaining semantic interpretability and tool interoperability through a state-aware, output-refinement-augmented protocol.

#### **8.2 Claims Summary**

The following claims are drafted to secure the core innovations of the Open-Ludic Stack, focusing on the system architecture, the governance method, and the communication protocol.

Independent System Claim:  
Claim 1\. A system for topologically governed generative design, comprising:

* **A Topological Governance Module** configured to ingest geometric or geographic data and compute a fractal scaling metric, specifically a head/tail breaks index ($ht$-index), wherein said module compares the computed metric against a pre-determined "living structure" threshold (e.g., $ht$-index $\\ge 3$) to generate a topological validity signal;  
* **A Generative Engine** communicatively coupled to the Governance Module, comprising:  
  * A semantic reasoning processor utilizing a **Graph of Thought (GoT)** architecture to decompose natural language input into a structured **Function-Behavior-Structure (FBS)** graph of constraints; and  
  * A stochastic constraint solver utilizing a **Wave Function Collapse (WFC)** algorithm to iteratively reduce the entropy of a multi-dimensional design domain based on said constraints and the topological validity signal;  
* **A Hybrid Agent-Tool Interface (HATI)** configured to orchestrate communication between the Generative Engine and a plurality of external execution tools, wherein the interface utilizes a schema-agnostic, state-aware protocol to dynamically select and execute tools based on the current entropy state and topological context of the Generative Engine.

Independent Method Claim:  
Claim 10\. A computer-implemented method for generating valid geometric configurations, the method comprising:

* **Initializing** a design domain wherein a plurality of discrete units exist in a superposition of all possible states;  
* **Deriving** a set of semantic constraints from an input query using a non-linear reasoning graph and a **Knowledge Augmented Generalizer Specializer (KAGS)** framework;  
* **Propagating** said constraints through the design domain to reduce the entropy of the discrete units;  
* **Collapsing** the state of the discrete units iteratively using an **incursive noetic weighting** function derived from real-time topological analysis;  
* **Analyzing** the resolved partial or complete configuration to determine a hierarchical scaling index based on the recurrence of heavy-tailed distributions (head/tail breaks); and  
* **Regenerating** or optimizing portions of the configuration if the hierarchical scaling index fails to meet a defined liveliness threshold, utilizing **Output Refinement Augmentation (ORA)** feedback from external tools.

**Dependent Claims (Selected):**

* **Claim 2 (Data Structure):** The system of Claim 1, wherein the geometric data is represented as a **Hypergraph** or a **Semilattice**, allowing for the representation of multi-dimensional, overlapping relationships and **neutrosophic** (indeterminate) connections typically found in early-stage Building Information Modeling (BIM).24  
* **Claim 3 (KAGS Framework):** The system of Claim 1, wherein the semantic reasoning processor utilizes the **Knowledge Augmented Generalizer Specializer (KAGS)** framework to automate problem formulation by retrieving and mapping analogous design solutions from external patent or knowledge databases.16  
* **Claim 4 (HATI Protocol):** The system of Claim 1, wherein the Hybrid Agent-Tool Interface employs a **state-aware negotiation protocol** that includes a "Tool Optimizer" agent configured to refine tool specifications, broadcast capabilities via FBS descriptors, and select execution variants based on a computational cost versus information gain ratio.31  
* **Claim 5 (Trajectory Alignment):** The system of Claim 1, wherein the Generative Engine incorporates a **Trajectory Alignment** mechanism to regulate the shape change velocities of the implicit surface representation during the entropy reduction process, ensuring the emerging geometry aligns with physical fabrication constraints.41  
* **Claim 6 (Output Refinement):** The method of Claim 10, wherein the step of regenerating utilizes **Output Refinement Augmentation (ORA)**, wherein external tools return gradient-based or heuristic feedback to the semantic reasoning processor to guide subsequent entropy reduction steps.33

### **9\. Conclusion**

The "Open-Ludic Stack" defines a comprehensive architecture for the next generation of generative design. By rejecting the "black box" approach of pure deep learning and the "manual knob-turning" of parametric design, it establishes a third path: **Topologically Governed Neuro-Symbolic Synthesis**.

The integration of Bin Jiang’s $ht$-index provides the necessary "Objective Function for Life," ensuring that the systems we build resonate with the scaling laws of the natural world. The WFC algorithm, augmented by Graph of Thought reasoning and the KAGS framework, provides a robust engine for navigating the immense combinatorial space of design. Finally, the HATI protocol ensures that this intelligence is not siloed, but can orchestrate the full diversity of the digital tool ecosystem.

This report serves as the technical baseline for the Provisional Patent Application. The claims drafted herein are designed to be robust, defensible, and broad enough to cover future iterations of this rapidly evolving technology.

### ---

**Citation Index**

* 1: "Head/Tail Breaks" patent generative design (MDPI, 2025).  
* 3: Classifying Street Spaces... (ResearchGate).  
* 2: Scaling of Geographic Space... (ResearchGate).  
* 42: Head/Tail Breaks-Based Approach... (SIAM).  
* 4: Streetscape measurement... (MDPI).  
* 5: ht-index patent spatial analysis (UCL).  
* 7: New Paradigm in Mapping (Jiang, 2023).  
* 43: Mapping structural evolution... (ResearchGate).  
* 6: Crime distribution... (MDPI).  
* 1: POI data... (MDPI).  
* 16: Graph-of-Thought patent architecture (ResearchGate).  
* 21: Graph-of-Thought RAG pipelines (MDPI).  
* 11: Wave Function Collapse patent (Google Patents).  
* 15: Dirac-Noetic Interferometer... (Google Patents).  
* 44: Agentic RAG framework... (MDPI).  
* 24: Hypergraph patent BIM data structure (MDPI).  
* 25: Digital twin models... (MDPI).  
* 45: Patent big data analysis... (ResearchGate).  
* 46: Point cloud resampling... (Google Patents).  
* 9: Fractal dimension quantization... (MDPI).  
* 2: Smooth curves can be fractal... (ResearchGate).  
* 7: Head/tail breaks recursive process (Jiang).  
* 8: A Map Is a Living Structure... (CartoGIS).  
* 2: ht-index as supplementary tool... (ResearchGate).  
* 40: ht-index for pixel values... (MDPI).  
* 10: Scale-free design... (MDPI).  
* 38: Generative Design for Architectural Space Planning... (MDPI).  
* 16: Deep learning-based approach for patent... (ResearchGate).  
* 21: Graph-of-Thought extends this idea... (MDPI).  
* 19: Subsea layout design... (MDPI).  
* 16: Knowledge Augmented Generalizer Specializer (KAGS)... (ResearchGate).  
* 47: Automatic extraction of FBS... (ResearchGate).  
* 12: Automatic generation of building instructions... (Google Patents).  
* 26: Soft graphs and neutrosophic graphs... (MDPI).  
* 48: Neuro-Symbolic AI for Compliance... (World Scientific).  
* 49: Engineering Health... (Innovation Endeavors).  
* 31: LLM in-context search & tool execution (Arxiv).  
* 34: Generating live DE documents... (Google Patents).  
* 29: LLM-based application hosts... (MDPI).  
* 31: Tool Optimizer... (Arxiv).  
* 50: Agent orchestration patent (Medium/Google).  
* 36: Using Amazon Bedrock for AI orchestration... (Caylent).  
* 37: AI agent orchestration... (IBM).  
* 35: Cognizant Neuro AI platform... (Cognizant).  
* 51: Towards Efficient Neuro-Symbolic AI... (MDPI).  
* 20: KAGS framework implemented... (ResearchGate).  
* 22: KAGS citations... (Google Scholar).  
* 47: Automated Extraction and Creation of FBS... (ResearchGate).  
* 32: Tool selection agent patent... (Justia).  
* 52: LLM-based system patent... (Justia).  
* 39: Agent OS... (PwC).  
* 18: Revisiting Gero's FBS... (ResearchGate).  
* 23: Time-line representation... (ResearchGate).  
* 41: Constraint satisfaction in generative design (Google Patents).  
* 24: Sensor placement in BIM... (MDPI).  
* 33: ChatBattery multi-agent model... (OAE Publishing).  
* 33: Ethical challenges... (OAE Publishing).  
* 17: Graph of Thought in RAG (MDPI).  
* 30: Graphs for Agent Memory... (Arxiv).  
* 21: Graph-of-Thought extends this idea... (MDPI).  
* 53: Multi-modal LLM with GoT... (ACL Anthology).  
* 15: Incursive Noetic Model... (Google Patents).  
* 13: WFC in architectural layout (MDPI).  
* 14: Entropy reduction patent... (Google Patents).  
* 54: Iterative entropy reduction... (Google Patents).  
* 55: Patent claim revision... (ACL Anthology).  
* 41: Purely data-driven approaches... (Google Patents).  
* 27: Semilattice in design computing (MIT).  
* 28: Semilattice of infinite breadth... (Lancaster University).

#### **Works cited**

1. Exploring the Association Between Street Scaling Structure and POI Distributions: Evidence from Shenzhen, China \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2073-445X/15/1/22](https://www.mdpi.com/2073-445X/15/1/22)  
2. Scaling of Geographic Space as a Universal Rule for Map Generalization \- ResearchGate, accessed December 26, 2025, [https://www.researchgate.net/publication/48203983\_Scaling\_of\_Geographic\_Space\_as\_a\_Universal\_Rule\_for\_Map\_Generalization](https://www.researchgate.net/publication/48203983_Scaling_of_Geographic_Space_as_a_Universal_Rule_for_Map_Generalization)  
3. Classifying Street Spaces with Street View Images for a Spatial Indicator of Urban Functions, accessed December 26, 2025, [https://www.researchgate.net/publication/337299958\_Classifying\_Street\_Spaces\_with\_Street\_View\_Images\_for\_a\_Spatial\_Indicator\_of\_Urban\_Functions](https://www.researchgate.net/publication/337299958_Classifying_Street_Spaces_with_Street_View_Images_for_a_Spatial_Indicator_of_Urban_Functions)  
4. Classifying Street Spaces with Street View Images for a Spatial Indicator of Urban Functions, accessed December 26, 2025, [https://www.mdpi.com/2071-1050/11/22/6424](https://www.mdpi.com/2071-1050/11/22/6424)  
5. Understanding Uneven Urban Expansion with Natural Cities using Open Data \- UCL Discovery, accessed December 26, 2025, [https://discovery.ucl.ac.uk/10047107/1/ys-LUP.pdf](https://discovery.ucl.ac.uk/10047107/1/ys-LUP.pdf)  
6. Measuring the Influence of Multiscale Geographic Space on the Heterogeneity of Crime Distribution \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2220-9964/12/10/437](https://www.mdpi.com/2220-9964/12/10/437)  
7. Translating EO data into economic value for governments, accessed December 26, 2025, [https://nationalmapping.icaci.org/wp-content/uploads/2023/05/NewParadigm.pdf](https://nationalmapping.icaci.org/wp-content/uploads/2023/05/NewParadigm.pdf)  
8. A Map Is a Living Structure with the Recurring Notion of Far More Smalls than Larges, accessed December 26, 2025, [https://cartogis.org/docs/autocarto/2020/docs/presentations/1c%20A%20Map%20Is%20a%20Living%20Structure%20with%20the%20Recurring%20Notion%20of%20Far%20More%20Smalls%20than%20Larges.pdf](https://cartogis.org/docs/autocarto/2020/docs/presentations/1c%20A%20Map%20Is%20a%20Living%20Structure%20with%20the%20Recurring%20Notion%20of%20Far%20More%20Smalls%20than%20Larges.pdf)  
9. Fractal Description of Rock Fracture Networks Based on the Space Syntax Metric \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2504-3110/6/7/353](https://www.mdpi.com/2504-3110/6/7/353)  
10. The 2-D Cluster Variation Method: Topography Illustrations and Their Enthalpy Parameter Correlations \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/1099-4300/23/3/319](https://www.mdpi.com/1099-4300/23/3/319)  
11. US20230152066A1 \- Efficient transmission of matter and energy via quantum phase modulation \- Google Patents, accessed December 26, 2025, [https://patents.google.com/patent/US20230152066A1/en](https://patents.google.com/patent/US20230152066A1/en)  
12. EP2135222B1 \- Automatic generation of building instructions for building element models \- Google Patents, accessed December 26, 2025, [https://patents.google.com/patent/EP2135222B1/un](https://patents.google.com/patent/EP2135222B1/un)  
13. Underground Parking Layout Generation Based on the WaveFunctionCollapse Algorithm, accessed December 27, 2025, [https://www.mdpi.com/2075-5309/13/11/2898](https://www.mdpi.com/2075-5309/13/11/2898)  
14. US4852173A \- Design and construction of a binary-tree system for language modelling \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/US4852173A/en](https://patents.google.com/patent/US4852173A/en)  
15. US20120075682A1 \- Spacetime energy resonator: a transistor of complex dirac polarized vacuum topology \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/US20120075682A1/en](https://patents.google.com/patent/US20120075682A1/en)  
16. Integrating and navigating engineering design decision-related knowledge using decision knowledge graph | Request PDF \- ResearchGate, accessed December 26, 2025, [https://www.researchgate.net/publication/353548595\_Integrating\_and\_navigating\_engineering\_design\_decision-related\_knowledge\_using\_decision\_knowledge\_graph](https://www.researchgate.net/publication/353548595_Integrating_and_navigating_engineering_design_decision-related_knowledge_using_decision_knowledge_graph)  
17. CRP-RAG: A Retrieval-Augmented Generation Framework for Supporting Complex Logical Reasoning and Knowledge Planning \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/2079-9292/14/1/47](https://www.mdpi.com/2079-9292/14/1/47)  
18. Revisiting Gero's Function-Behaviour-Structure (FBS) Framework to Establish Fundamental Principles, Novel Insights, and Propositions | Request PDF \- ResearchGate, accessed December 27, 2025, [https://www.researchgate.net/publication/396744773\_Revisiting\_Gero's\_Function-Behaviour-Structure\_FBS\_Framework\_to\_Establish\_Fundamental\_Principles\_Novel\_Insights\_and\_Propositions](https://www.researchgate.net/publication/396744773_Revisiting_Gero's_Function-Behaviour-Structure_FBS_Framework_to_Establish_Fundamental_Principles_Novel_Insights_and_Propositions)  
19. Research on Subsea Cluster Layout Optimization Method Considering Three-Dimensional Terrain Constraints \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2077-1312/13/12/2385](https://www.mdpi.com/2077-1312/13/12/2385)  
20. Knowledge augmented generalizer specializer: A framework for early stage design exploration | Request PDF \- ResearchGate, accessed December 27, 2025, [https://www.researchgate.net/publication/388658547\_Knowledge\_augmented\_generalizer\_specializer\_A\_framework\_for\_early\_stage\_design\_exploration](https://www.researchgate.net/publication/388658547_Knowledge_augmented_generalizer_specializer_A_framework_for_early_stage_design_exploration)  
21. A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/2504-2289/9/12/320](https://www.mdpi.com/2504-2289/9/12/320)  
22. ‪Soban Babu Beemaraj‬ \- ‪Google Scholar‬, accessed December 27, 2025, [https://scholar.google.com/citations?user=ERaU6JEAAAAJ\&hl=en](https://scholar.google.com/citations?user=ERaU6JEAAAAJ&hl=en)  
23. Time line representation of user inputs and application functions. \- ResearchGate, accessed December 27, 2025, [https://www.researchgate.net/figure/Time-line-representation-of-user-inputs-and-application-functions\_fig4\_296704156](https://www.researchgate.net/figure/Time-line-representation-of-user-inputs-and-application-functions_fig4_296704156)  
24. A Sensor Placement Approach Using Multi-Objective Hypergraph Particle Swarm Optimization to Improve Effectiveness of Structural Health Monitoring Systems \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/1424-8220/24/5/1423](https://www.mdpi.com/1424-8220/24/5/1423)  
25. Modularization Design for Smart Industrial Service Ecosystem: A Framework Based on the Smart Industrial Service Identification Blueprint and Hypergraph Clustering \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/2071-1050/15/11/8858](https://www.mdpi.com/2071-1050/15/11/8858)  
26. Extensions of Multidirected Graphs: Fuzzy, Neutrosophic, Plithogenic, Rough, Soft, Hypergraph, and Superhypergraph Variants \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2813-9542/2/3/11](https://www.mdpi.com/2813-9542/2/3/11)  
27. Graphing Theory: New Mathematics, Design, and the Participatory Turn by Theodora Vardouli Diploma in Architectural Engineering N \- DSpace@MIT, accessed December 27, 2025, [https://dspace.mit.edu/bitstream/handle/1721.1/113917/1023433294-MIT.pdf?sequence=1\&isAllowed=y](https://dspace.mit.edu/bitstream/handle/1721.1/113917/1023433294-MIT.pdf?sequence=1&isAllowed=y)  
28. Items where Year is 2025 \- Lancaster EPrints, accessed December 27, 2025, [https://eprints.lancs.ac.uk/view/year/2025.html](https://eprints.lancs.ac.uk/view/year/2025.html)  
29. Human–AI Teaming in Structural Analysis: A Model Context Protocol Approach for Explainable and Accurate Generative AI \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/2075-5309/15/17/3190](https://www.mdpi.com/2075-5309/15/17/3190)  
30. Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportunities \- arXiv, accessed December 27, 2025, [https://arxiv.org/html/2506.18019v1](https://arxiv.org/html/2506.18019v1)  
31. Democratizing AI scientists using ToolUniverse \- arXiv, accessed December 27, 2025, [https://arxiv.org/html/2509.23426v1](https://arxiv.org/html/2509.23426v1)  
32. Shivendra Singh Malik Inventions, Patents and Patent Applications, accessed December 27, 2025, [https://patents.justia.com/inventor/shivendra-singh-malik](https://patents.justia.com/inventor/shivendra-singh-malik)  
33. From large language models to AI agents in energy materials research: enabling discovery, design, and automation \- OAE Publishing Inc., accessed December 27, 2025, [https://www.oaepublish.com/articles/aiagent.2025.03](https://www.oaepublish.com/articles/aiagent.2025.03)  
34. WO2025137657A1 \- Alternative digital tool selection and optimization in digital model platforms \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/WO2025137657A1/en](https://patents.google.com/patent/WO2025137657A1/en)  
35. Cognizant Announces Multi-Agent Orchestration for its Neuro® AI Platform, accessed December 27, 2025, [https://investors.cognizant.com/news-and-events/news/news-details/2024/Cognizant-Announces-Multi-Agent-Orchestration-for-its-Neuro-AI-Platform/default.aspx](https://investors.cognizant.com/news-and-events/news/news-details/2024/Cognizant-Announces-Multi-Agent-Orchestration-for-its-Neuro-AI-Platform/default.aspx)  
36. Using Amazon Bedrock for AI Orchestration \- Caylent, accessed December 27, 2025, [https://caylent.com/blog/using-amazon-bedrock-for-ai-orchestration](https://caylent.com/blog/using-amazon-bedrock-for-ai-orchestration)  
37. Oversee a prior art search AI agent with human-in-the-loop by using LangGraph and watsonx.ai \- IBM, accessed December 27, 2025, [https://www.ibm.com/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai](https://www.ibm.com/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai)  
38. Generative Design in Building Information Modelling (BIM): Approaches and Requirements, accessed December 26, 2025, [https://www.mdpi.com/1424-8220/21/16/5439](https://www.mdpi.com/1424-8220/21/16/5439)  
39. Agent OS Recent Enhancements \- PwC, accessed December 27, 2025, [https://www.pwc.com/us/en/services/ai/agent-os/agent-os-recent-enhancements.html](https://www.pwc.com/us/en/services/ai/agent-os/agent-os-recent-enhancements.html)  
40. Intra-Urban Scaling Properties Examined by Automatically Extracted City Hotspots from Street Data and Nighttime Light Imagery \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2072-4292/13/7/1322](https://www.mdpi.com/2072-4292/13/7/1322)  
41. US20250292092A1 \- Generative optimization models for machine learning \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/US20250292092A1/en](https://patents.google.com/patent/US20250292092A1/en)  
42. Power-Law Distributions in Empirical Data | SIAM Review, accessed December 26, 2025, [https://epubs.siam.org/doi/10.1137/070710111](https://epubs.siam.org/doi/10.1137/070710111)  
43. (PDF) Mapping the structural evolution of intercity patent transfer constrained by space: a case study of China \- ResearchGate, accessed December 26, 2025, [https://www.researchgate.net/publication/382099571\_Mapping\_the\_structural\_evolution\_of\_intercity\_patent\_transfer\_constrained\_by\_space\_a\_case\_study\_of\_China](https://www.researchgate.net/publication/382099571_Mapping_the_structural_evolution_of_intercity_patent_transfer_constrained_by_space_a_case_study_of_China)  
44. Hybrid Multi-Agent GraphRAG for E-Government: Towards a Trustworthy AI Assistant \- MDPI, accessed December 26, 2025, [https://www.mdpi.com/2076-3417/15/11/6315](https://www.mdpi.com/2076-3417/15/11/6315)  
45. The structure and knowledge flow of building information modeling based on patent citation network analysis | Request PDF \- ResearchGate, accessed December 26, 2025, [https://www.researchgate.net/publication/345671726\_The\_structure\_and\_knowledge\_flow\_of\_building\_information\_modeling\_based\_on\_patent\_citation\_network\_analysis](https://www.researchgate.net/publication/345671726_The_structure_and_knowledge_flow_of_building_information_modeling_based_on_patent_citation_network_analysis)  
46. US7397473B2 \- Geometry based search method for 3D CAx/PDM repositories \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/US7397473B2/en](https://patents.google.com/patent/US7397473B2/en)  
47. Automatic extraction of function–behaviour–state information from patents | Request PDF, accessed December 27, 2025, [https://www.researchgate.net/publication/259161027\_Automatic\_extraction\_of\_function-behaviour-state\_information\_from\_patents](https://www.researchgate.net/publication/259161027_Automatic_extraction_of_function-behaviour-state_information_from_patents)  
48. Artificial Intelligence Applications for Industry 4.0: A Literature-Based Study, accessed December 27, 2025, [https://www.worldscientific.com/doi/full/10.1142/S2424862221300040](https://www.worldscientific.com/doi/full/10.1142/S2424862221300040)  
49. Engineering Health \- Innovation Endeavors, accessed December 27, 2025, [https://www.innovationendeavors.com/thesis/engineering-health](https://www.innovationendeavors.com/thesis/engineering-health)  
50. Build Powerful, Stateful AI Agents in Java with Agent Development Kit (ADK) \- Medium, accessed December 27, 2025, [https://medium.com/google-cloud/build-powerful-stateful-ai-agents-in-java-with-agent-development-kit-adk-0f7e2cd3d094](https://medium.com/google-cloud/build-powerful-stateful-ai-agents-in-java-with-agent-development-kit-adk-0f7e2cd3d094)  
51. Challenging Scientific Categorizations Through Dispute Learning \- MDPI, accessed December 27, 2025, [https://www.mdpi.com/2076-3417/15/4/2241](https://www.mdpi.com/2076-3417/15/4/2241)  
52. Saratendu Sethi Inventions, Patents and Patent Applications, accessed December 27, 2025, [https://patents.justia.com/inventor/saratendu-sethi](https://patents.justia.com/inventor/saratendu-sethi)  
53. Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) \- ACL Anthology, accessed December 27, 2025, [https://aclanthology.org/volumes/2025.naacl-long/](https://aclanthology.org/volumes/2025.naacl-long/)  
54. US11520971B2 \- System and method for artificial intelligence story generation allowing content introduction \- Google Patents, accessed December 27, 2025, [https://patents.google.com/patent/US11520971B2/en](https://patents.google.com/patent/US11520971B2/en)  
55. CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning \- ACL Anthology, accessed December 27, 2025, [https://aclanthology.org/2025.findings-emnlp.700.pdf](https://aclanthology.org/2025.findings-emnlp.700.pdf)