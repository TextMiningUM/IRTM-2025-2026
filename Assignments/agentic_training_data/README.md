# Tutorial 13 — From Text to Agentic Training Data

This package contains everything you need to run **Tutorial 13** end-to-end on
your own machine. The notebook walks you through converting raw domain text
into the six artifact families an agentic LLM actually needs (RAG chunks,
reranker triplets, knowledge graphs, SFT trajectories, RLHF preference pairs,
tool trajectories), then evaluates the same pipeline on three corpora of
increasing distance from pretraining:

| Corpus | What it tests |
|---|---|
| **Cyber** (MITRE ATT&CK / CWE / CAPEC / OWASP) | The "easy" extreme: cybersecurity is well-represented in pretraining. |
| **Faraday** (19th-century scientific writing) | A domain less represented in pretraining. |
| **Cadzand** (1998 Dutch tourist booklet) | The "hard" extreme: a corpus the model has provably never seen. |

Total runtime, end-to-end with caching: **~1.5 h** code + ~3 h reading.
See the *How long will this notebook take?* table at the top of the notebook
for a per-section breakdown.

---

## Quick start

```bash
# 1. Clone (or download) this folder
cd Assignments/agentic_training_data

# 2. Create a Python 3.10 virtual environment
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate      # macOS / Linux

# 3. Install dependencies
pip install -r requirements_notebook13.txt

# 4. Set your OpenAI API key (the notebook will also prompt interactively)
$env:OPENAI_API_KEY = "sk-..."     # Windows PowerShell
# export OPENAI_API_KEY=sk-...     # macOS / Linux

# 5. Launch
jupyter lab
```

Then open `13_IRTM_From_Text_to_Agentic_Training_Data_2025_2026.ipynb` and
run cells top-to-bottom.

---

## What's in this folder

```
13_IRTM_From_Text_to_Agentic_Training_Data_2025_2026.ipynb   ← the tutorial
requirements_notebook13.txt                                  ← pinned deps
training_data/                                               ← Cyber + Faraday artifacts
  cyber_rag_chunks.json,  cyber_concept_graph.json, ...
  faraday_rag_chunks.json, faraday_concept_graph.json, ...
  tool_trajectories_examples.json                            ← §3.3 medical + SAP examples
Cadzand/                                                     ← §11 stress-test corpus
  cadzand_booklet.txt, cadzand_eval_questions.json,
  cadzand_rag_chunks.jsonl, cadzand_knowledge_graph.json,
  EN_cadzand_*  (English translations of the same)
```

---

## Pre-trained Tier-2 adapters (for §9.7 and §10.7)

Sections **§9.7** and **§10.7** show *real* fine-tuning results, not just
prompt-only conditioning: a fine-tuned embedder, fine-tuned reranker, a
LoRA-SFT adapter on Qwen-1.5B, and a DPO adapter on top of that — for both
the Cyber and Faraday corpora.

You have **two ways** to get these adapters:

### Option A — Download them (recommended, ~1 GB, one-time)

The notebook does this automatically the first time §9.7 runs. It calls
`huggingface_hub.snapshot_download("TextMiningUM/irtm-tutorial-13-adapters")`,
caches the result under `~/.cache/huggingface/`, and re-uses it on subsequent
runs.

To pre-download them manually (e.g. before going offline):

```bash
huggingface-cli download TextMiningUM/irtm-tutorial-13-adapters
```

### Option B — Train them yourself

If you skip §9.7 / §10.7, the rest of the notebook still runs fine — every
Tier-1 (prompt-only) condition works without any pre-trained weights. The
notebook will print a clear "skipping Tier-2" message rather than crash.

To train your own adapters from scratch you can adapt the scripts under
`_training/` in the source repository (instructor copy). Expect ~3 min on a
single consumer GPU per adapter, ~15 min on CPU.

---

## Required environment

| Item | Value |
|---|---|
| Python | 3.10 (3.11 also works) |
| OS | Windows 11 / macOS 14 / Ubuntu 22.04 tested |
| RAM | 8 GB minimum, 16 GB recommended for §9.7 / §10.7 on CPU |
| Disk | ~3 GB for cached HF models + adapter download |
| Required env vars | `OPENAI_API_KEY` |
| Optional | `HF_HUB_OFFLINE=1` after first run, `HF_TUTORIAL13_REPO` to override the model repo |

---

## Exercises

The notebook ends with **four exercises** (5 + 5 + 5 + 10 = 25 points). Each
has a markdown answer cell containing `YOUR ANSWER HERE`. Replace that line
with your written answer (and any code, tables, or screenshots you want to
include) before submitting.

> **Submission.** Submit the completed notebook (with all cells executed and
> outputs preserved) via the course's standard submission channel.

---

## Troubleshooting

* **`OPENAI_API_KEY` rejected as non-ASCII**  → you pasted a smart-quote.
  Re-type the key by hand and ensure your terminal uses UTF-8.
* **`snapshot_download` hangs**  → check `HF_HUB_OFFLINE` is unset and you
  have outbound HTTPS to `huggingface.co`. Behind a corporate proxy, set
  `HTTPS_PROXY` first.
* **§9.7b OOMs on CPU**  → set `BATCH_SIZE = 1` in the cell, or skip §9.7
  entirely and stay with Tier-1.
* **Cadzand RAG returns empty** → make sure the `Cadzand/` sub-folder is in
  the same directory as the notebook (relative paths matter).

---

## Acknowledgements & licensing

* The Cadzand booklet is © 1998 VVV Cadzand-Bad and used here under fair-use
  for educational purposes.
* The Faraday corpus is in the public domain.
* The cyber corpus is derived from MITRE ATT&CK, CWE, CAPEC and OWASP, all
  under permissive licences (see `training_data/book_source.json`).
* Notebook © 2026 Maastricht University — Information Retrieval & Text Mining.
