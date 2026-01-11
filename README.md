# Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikitlearn&logoColor=white)
![Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Model%20Complete-2EA44F)

ML project: **predict customer churn** and identify the **main churn drivers** using an end-to-end workflow (EDA → preprocessing → modeling → evaluation → interpretation).

---

## 🚀 Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bank-churn-prediction-fwfq5zklvke4gxst2fxeuw.streamlit.app/)

**Try the app here:** [Bank Churn Predictor](https://bank-churn-prediction-fwfq5zklvke4gxst2fxeuw.streamlit.app/)

### How to use:
1.  **Input Features**: Use the sidebar to enter customer details (Age, Balance, Number of Products, etc.).
2.  **Predict**: Click the **"Analyze Risk"** button.
3.  **Result**: The app will show the churn probability and a risk level (Low/High).

---

## Table of contents
- [Live Demo](#live-demo)
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
- **Target**: customer churn (target variable is `churn`)
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
- this notebook uses 
- in other common versions the same target may be named `Exited`

Raw data is not stored in this repository. The notebook supports:
- **programmatic download** via KaggleHub (Colab-friendly)
- **local CSV** via `LOCAL_DATA_PATH` (recommended for stable offline runs)

---

## Quickstart

### Option A — Google Colab
Open the public notebook directly: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/158Tygq9jqqtW11sFoQ8QDkJaQD2Abhb6)

The notebook can download the dataset using KaggleHub. If your environment requires Kaggle authentication, configure it in Colab as usual.

### Option B — Local run
1) Create venv and install deps:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2) Open and run `notebooks/run_pipeline.ipynb` in Jupyter:
   - The notebook will download data via KaggleHub automatically
   - Or set `LOCAL_DATA_PATH = Path(".../your.csv")` to use local data

3) Optional: Run the Streamlit app:

```bash
streamlit run app.py
```

---

## Project structure
Current repo layout:

```
bank-churn-prediction/
├── README.md
├── notebooks/
│   └── run_pipeline.ipynb     # ⭐ Complete ML pipeline
├── artifacts/
│   ├── preprocessor.joblib    # Trained preprocessor
│   └── final_model.joblib     # Trained CatBoost model
├── app.py                      # Streamlit web app
└── requirements.txt
```

---

## Notebooks

**`run_pipeline.ipynb`** ⭐ — Complete end-to-end ML pipeline:
- Data source & acquisition (KaggleHub integration)
- Exploratory data analysis
- Data preprocessing & feature engineering
- Baseline Logistic Regression model
- CatBoost gradient boosting model
- Hyperparameter optimization with Optuna
- Model evaluation & business insights
- Artifact saving

---

## Tech stack
- **Python**, **Jupyter**
- **pandas / numpy** — data processing
- **matplotlib / seaborn** — visualization
- **scikit-learn** — modeling and evaluation
- **CatBoost** — gradient boosting model
- **Optuna** — hyperparameter optimization
- **Streamlit** — web application

---

## Roadmap

**Completed:**
- ✅ Baseline Logistic Regression model
- ✅ CatBoost gradient boosting model
- ✅ Hyperparameter optimization with Optuna
- ✅ Model evaluation (ROC-AUC ~0.87)
- ✅ Feature importance analysis
- ✅ Streamlit web application

**Future improvements:**
- Threshold tuning with churner recall focus
- Additional model comparison (XGBoost, LightGBM)
- Deep error analysis and customer segmentation
- A/B testing framework for retention campaigns

---

## License
Educational use.
