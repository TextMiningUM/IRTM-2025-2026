# IRTM 2025-2026 — Student Repository

**Information Retrieval & Text Mining** — Maastricht University  
Department of Advanced Computer Sciences, Faculty of Science and Engineering

## Structure

```
Tutorials/          ← Reference tutorials (read-only, for self-study)
Assignments/        ← Graded assignments (work here)
  tokenization/
  document_representation/
  search_engines/
  measuring_quality/
  structured_representations_1/
  structured_representations_2/
  detecting_patterns_1/
  detecting_patterns_2/
  conversational_search_basics/
  conversational_search_facts/
  agents/
SubmittedWork/      ← Copy your finished notebooks here to submit
  tokenization/
  document_representation/
  search_engines/
  measuring_quality/
  structured_representations_1/
  structured_representations_2/
  detecting_patterns_1/
  detecting_patterns_2/
  conversational_search_basics/
  conversational_search_facts/
  agents/
```

## Getting Started

### On JupyterHub (`irtm-course-um.nl`)

1. Open a terminal in JupyterLab
2. Clone this repository:
   ```bash
   git clone https://github.com/TextMiningUM/IRTM-2025-2026.git
   ```
3. Navigate to the `Assignments/` folder and open the relevant notebook
4. Complete the exercises and submit as instructed

### Fetching New Assignments

When new assignments are released, pull the latest changes:
```bash
cd IRTM-2025-2026
git pull
```

## Tutorials

The `Tutorials/` folder contains reference notebooks covering all course topics.
These are for self-study and are not graded.

## Assignments

Assignment notebooks are in `Assignments/<topic>/`. Each notebook contains:
- Instructional content explaining the concepts
- **Exercise cells** where you write your code (marked with `# YOUR CODE HERE`)
- **Test cells** that validate your solution (do not modify these)

## Submission

When you have finished an assignment, copy your completed notebook to the
matching folder inside `SubmittedWork/`. For example, for the Tokenization
assignment:

```bash
cp Assignments/tokenization/01_IRTM_Tokenization_2025_2026.ipynb \
   SubmittedWork/tokenization/
```

**Important:**
- Keep the original filename — do not rename the notebook.
- Make sure the notebook runs from top to bottom without errors before submitting.
- You can overwrite a previous submission by copying again (latest version counts).
- Deadline: see Canvas for due dates per assignment.
