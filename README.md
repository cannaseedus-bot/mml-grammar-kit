# K'UHUL MML Grammar Kit

MathML/MML vector grammar assets for the KHANARY / K'UHUL semantic runtime stack.

This kit preserves the original KHANARY.CPP paths so references inside the XML and docs stay valid. The primary MML artifact is `data/grammar/vectors.mml`; it depends on the Fold content dictionary in `data/grammar/fold.cd.xml`. `data/grammar/fold_graph.xml` links the vector layer to the fold graph and shader companions.

## Files

| File | Description |
|------|-------------|
| `data/grammar/vectors.mml` | MathML vector/operator projection for fold/vector semantics. |
| `data/grammar/fold.cd.xml` | OpenMath-style Fold content dictionary referenced by `vectors.mml`. |
| `data/grammar/fold_graph.xml` | XML fold graph bridge that references `fold.cd.xml`, `vectors.mml`, and shader companions. |
| `data/shaders/attention.hlsl` | Attention shader companion referenced by the fold graph. |
| `data/shaders/fold_compute.hlsl` | Fold-compute shader companion referenced by the fold graph. |
| `docs/MATHML+KUHUL.html` | MathML + K'UHUL explanatory document. |
| `docs/KUHUL_PHASE_ALGEBRA.md` | Phase algebra reference. |
| `docs/SEMANTIC_FOLDS.md` | Semantic fold/topology reference. |
| `tools/check_mml_kit.py` | Dependency-free XML/reference smoke check for this kit. |

## Validate

```powershell
python tools/check_mml_kit.py
```

Expected result:

```text
PASS | mml-kit: 3 XML files parsed, 4 reference(s) resolved
```

## Part of

[KHANARY.CPP](https://github.com/cannaseedus-bot) — K'UHUL semantic runtime stack.
