# Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikitlearn&logoColor=white)
![Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-EDA%20ready-2EA44F)

ML project: **predict customer churn** and identify the **main churn drivers** using an end-to-end workflow (EDA → preprocessing → modeling → evaluation → interpretation).

---

## Table of contents
- [Why this project](#why-this-project)
- [Problem formulation](#problem-formulation)
- [Dataset](#dataset)
- [Quickstart](#quickstart)
- [Project structure](#project-structure)
- [Notebooks](#notebooks)
- [Tech stack](#tech-stack)
- [Roadmap](#roadmap)
- [License](#license)

---

## Why this project
Customer churn is a critical problem for the banking industry: retaining existing customers is significantly cheaper than acquiring new ones. The goals here are:
- predict churn probability
- identify high-risk segments
- understand key churn drivers
- translate model insights into retention actions

---

## Problem formulation
- **Task type**: binary classification
- **Target**: customer churn (in the dataset used in `01_eda.ipynb` it is `churn`)
- **Primary metric**: ROC-AUC
- **Secondary metrics**: Recall, Precision, F1

Special attention is paid to **recall for churners**, because missing a potential churner is often more costly than a false positive.

---

## Dataset
This project uses Kaggle’s **Bank Customer Churn Dataset**:
- Source: `https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset`

Typical features include:
- demographics: age, gender, country
- financial indicators: credit score, balance, estimated salary
- product usage: number of products, credit card
- engagement: tenure, active member flag

Target column naming differs across similar churn datasets:
- this repo’s EDA notebook uses `TARGET_COL = "churn"`
- in other common versions the same target may be named `Exited`

Raw data is not stored in this repository. The EDA notebook supports:
- **programmatic download** via KaggleHub (Colab-friendly)
- **local CSV** via `LOCAL_DATA_PATH` (recommended for stable offline runs)

---

## Quickstart

### Option A — Google Colab
Open and run:
- `notebooks/01_eda.ipynb`

The notebook can download the dataset using KaggleHub. If your environment requires Kaggle auth, configure it in Colab as usual.

### Option B — Local run
1) Create venv and install deps:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2) Download the CSV locally (from Kaggle) and set in the notebook:
- `LOCAL_DATA_PATH = Path(".../your.csv")`

3) Run notebooks in order (starting from `01_eda.ipynb`).

---

## Project structure
Current repo layout:

```
bank-churn-prediction/
├── README.md
├── notebooks/
│   └── 01_eda.ipynb
├── src/
└── requirements.txt
```

---

## Notebooks
- **`01_eda.ipynb`**: data source & acquisition, schema/type inspection, target distribution, data-quality checks, key univariate and churn-vs-feature comparisons

Planned:
- `02_preprocessing.ipynb`
- `03_baseline.ipynb`
- `04_models.ipynb`
- `05_tuning.ipynb`
- `06_interpretation.ipynb`

---

## Tech stack
- **Python**, **Jupyter**
- **pandas / numpy** — data processing
- **matplotlib / seaborn** — visualization
- **scikit-learn** — modeling and evaluation
- (planned) **CatBoost** — main model
- (planned) **Optuna** — hyperparameter optimization

---

## Roadmap
Next steps after EDA:
- preprocessing pipeline (train/test split, encoding, scaling where needed)
- baseline model + robust evaluation
- model comparison (tree ensembles / boosting)
- threshold tuning with churner recall focus
- interpretation (feature importance / error analysis / segments)

---

## License
Educational use.
