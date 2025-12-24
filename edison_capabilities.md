# Edison Scientific Platform Capabilities

Your subscription gives you access to a suite of AI agents designed for different stages of scientific research. Here is what each one can do:

## 1. Literature Search (`JobNames.LITERATURE`)
**Best for:** Answering complex scientific questions based on published papers.
- **Engine:** PaperQA3
- **What it does:** Searches scientific literature, reads full-text papers, and synthesizes an answer with inline citations.
- **Example Queries:**
  - *"What are the known mechanisms of action for Metformin in longevity?"*
  - *"Which enzymes are involved in the degradation of PET plastic?"*

## 2. Precedent Search (`JobNames.PRECEDENT`)
**Best for:** Determining novelty or checking if an experiment has been done.
- **Engine:** HasAnyone
- **What it does:** Scans literature to see if a specific hypothesis or method has already been tested.
- **Example Queries:**
  - *"Has anyone tested therapeutic exerkines in humans or NHPs?"*
  - *"Have exosomes been used to deliver CRISPR-Cas9 to the brain?"*

## 3. Chemistry & Molecules (`JobNames.MOLECULES`)
**Best for:** Chemical synthesis planning, property prediction, and safety assessments.
- **Engine:** Phoenix (next-gen ChemCrow)
- **What it does:** interfacing with cheminformatics tools to plan synthesis routes or predict molecular properties.
- **Best Practices:** Use SMILES strings or CAS numbers for precision.
- **Example Queries:**
  - *"Design a synthesis route for ethyl acetate using reaction SMILES: CCO.CC(=O)O>>CC(=O)OC"*
  - *"What are the ADMET properties for aspirin (SMILES: CC(=O)OC1=CC=CC=C1C(=O)O)?"*
  - *"Perform a safety assessment for [Molecule Name]."*

## 4. Data Analysis (`JobNames.ANALYSIS`)
**Best for:** Analyzing your own biological or scientific datasets.
- **Engine:** Kosmos
- **What it does:** Takes your raw data (CSVs, RNA-seq, etc.) and performs statistical analysis, visualization, and hypothesis testing.
- **Requirements:** Requires uploading files to Edison Data Storage first.
- **Example Objectives:**
  - *"Compare ECM pathway expression levels in the melanoma tissue samples."*
  - *"Build a regression model to test if air pollution correlates with asthma rates in this dataset."*

---

## Quick Example Script for Molecules
Since you don't need external files for this, you can try it right away:

```python
from edison_client import EdisonClient, JobNames
import os

client = EdisonClient(api_key=os.getenv("EDISON_API_KEY"))

# Ask for physical properties of caffeine
query = "What is the water solubility and logP of Caffeine (SMILES: CN1C=NC2=C1C(=O)N(C(=O)N2C)C)?"

task_data = {
    "name": JobNames.MOLECULES,
    "query": query
}

response = client.run_tasks_until_done(task_data)
print(response.answer)
```
