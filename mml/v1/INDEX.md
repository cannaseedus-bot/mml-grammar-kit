# MML Suite — v1

Content dictionary epoch: `urn:kuhul:*:v1`

All files in this directory are MathML `<semantics>` contracts. Each carries a
`<csymbol cd="urn:kuhul:<name>:v1">` annotation and a plain-text invariant list.
The machine contract authority for each is the corresponding `.contracts.json`
sibling in `data/grammar/`.

## Foundation contracts

| File | Contract identity |
|---|---|
| `vectors.mml` | **lives at `data/grammar/vectors.mml`** — `urn:kuhul:fold-graph:v1` FoldPair / continuous-field / tensor-bundle contract (`KHANARY_VECTORS_XML_TEST`). Not duplicated in this suite: the registry `vectors.xml` names that path as the source, and two copies would drift. |
| `metric_graph.mml` | `urn:kuhul:metric-graph:v1` — metric/geodesic graph |
| `map-filter-fold.mml` | `urn:kuhul:map-filter-fold:v1` — HOF pipeline operators |

## Operator contracts

| File | Contract identity |
|---|---|
| `SraiOperators.mml` | `urn:kuhul:srai-operators:v1` — SRAI dispatch surface (SCORE/RANK/COLLAPSE/VERIFY/TRAIN/COMPARE/RECALL/PROJECT/QUESTION) |
| `PatternKernelCalls.mml` | `urn:kuhul:pattern-kernel-calls:v1` — pattern kernel call surface |

## Daemon pattern contracts

| File | Contract identity |
|---|---|
| `DaemonPatterns.mml` | `urn:kuhul:daemon-patterns:v1` — shared daemon discussion/dialogue cycle |
| `CheeseCritic.mml` | `urn:kuhul:cheese-critic:v1` — evidence critic and challenge evaluation |
| `MicronautPatterns.mml` | `urn:kuhul:micronaut-patterns:v1` — cross-micronaut pattern recognition |
| `DaemonBehaviorModes.mml` | `urn:kuhul:daemon-behavior-modes:v1` — separates AIML priors, graph affinities, temporary context, and authorized learned deltas |

## Phase-driver contracts (one per K'UHUL phase)

| File | Phase |
|---|---|
| `phase-driver-pop.mml` | Pop |
| `phase-driver-wo.mml` | Wo |
| `phase-driver-yax.mml` | Yax |
| `phase-driver-sek.mml` | Sek |
| `phase-driver-chen.mml` | Ch'en |
| `phase-driver-xul.mml` | Xul |

## Individual daemon contracts

| File | Daemon |
|---|---|
| `daemon-eliza.mml` | ELIZA |
| `daemon-alice.mml` | ALICE |
| `daemon-think.mml` | Think |
| `daemon-reason.mml` | Reason |
| `daemon-expand.mml` | Expand |
| `daemon-coder.mml` | Coder |
| `daemon-ts_coder.mml` | TS Coder |
| `daemon-ast.mml` | AST |
| `daemon-tool.mml` | Tool |
| `daemon-memory.mml` | Memory |
| `daemon-librarian.mml` | Librarian |
| `daemon-sheogorath.mml` | Sheogorath (T=0.97, Xul) |
| `daemon-jyggalag.mml` | Jyggalag (T=0.00, Ch'en) |
| `daemon-factory.mml` | Factory |
| `daemon-evolution.mml` | Evolution |
| `daemon-atomic.mml` | Atomic |

## Micronaut CODEGEN contracts

| File | Domain |
|---|---|
| `micronaut-CODEGEN-KUHUL.mml` | K'UHUL phase/fold/XCFE op |
| `micronaut-CODEGEN-CPP.mml` | C++ source |
| `micronaut-CODEGEN-PY.mml` | Python tooling |
| `micronaut-CODEGEN-JS.mml` | JavaScript/TypeScript |
| `micronaut-CODEGEN-CSHARP.mml` | C# |
| `micronaut-CODEGEN-HTML.mml` | HTML templates |
| `micronaut-CODEGEN-CSS.mml` | CSS |
| `micronaut-CODEGEN-JSON.mml` | JSON manifests/contracts |
| `micronaut-CODEGEN-KHL.mml` | KHL host-lang |
| `micronaut-CODEGEN-KLSL.mml` | KLSL compiler/shader |

## GML topology and field resolution contracts

| File | Contract identity |
|---|---|
| `GMLTopology.mml` | `urn:kuhul:gml-topology:v1` — runtime GML file registry and authority distinctions, including `daemon_behavior_modes.gml` as optional behavioral affinities rather than FoldGraph B topology. |
| `WildcardFieldResolution.mml` | `urn:kuhul:wildcard-field-resolution:v1` — capture → field lookup → vector projection → VectorLane scoring → bound result pipeline. Defines `WildcardFieldPipeline` (5 stages), `FieldKeyLookup` (capture key family → GML file → read-only parameter vector: entropy→entropy_gradient_field, curvature→tensor_field, wave→quantum_field_boundaries, gradient→euclidean_gradient_field), `VectorLaneScoringLaw` (mode=score, mutation_authorized=false), `BoundResultWithProvenance` (score + param_vector + source_gml + semantic_authority=false), and `ScoringNotTruth` (scores are evidence; cannot authorize a route; XCFE/Ch'en/Xul remain authority chain). |

## XAIML dispatch contracts

| File | Contract identity |
|---|---|
| `XaimlMicronautDispatch.mml` | `urn:kuhul:xaiml-micronaut:v1` — XAIML → Micronaut admission and dispatch. Defines `DispatchProposal`, `ValidateProposal` (5-term Admit formula refined from `CaptureGate` in `vectors.mml`), `ProposalOnly` (dispatchAuthorized=0), `LaneSetBinding` (Wo-only), `CandidatePromotion` (σ: observed → validated), and `BindingGap` (COMPARE right-binding gap). Machine contract: `data/grammar/aiml-pattern-bank.contracts.json`. |

## Versioning policy

A new `v2/` sibling directory is created when the content dictionary epoch
advances (i.e., any `csymbol cd="urn:kuhul:*:v2"` is introduced). Files in
`v1/` are frozen at that point. Cross-version references are explicit:
a v2 document may import a v1 contract but must name the epoch.

Run `py -3 tools/check_srai_operators.py` and `py -3 tools/grammar/mini_transpilers.py fold-geometry-check`
after any edit to verify suite invariants.
