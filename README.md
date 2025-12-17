# Bank Customer Churn Prediction

## Project Overview

Customer churn is a critical problem for the banking industry: retaining existing customers is significantly cheaper than acquiring new ones. This project aims to build an end-to-end **machine learning pipeline** to predict customer churn and to identify the key factors that influence a customer's decision to leave the bank.

The project is designed as a **portfolio-quality ML case study**, covering all major stages of a real-world data science workflow: data exploration, preprocessing, model training, evaluation, interpretation, and presentation of results.

---

## Business Objective

The main business goals of this project are:

* Predict the probability of customer churn.
* Identify high-risk customer segments.
* Understand the main drivers of churn.
* Provide actionable insights that can be used for customer retention strategies.

---

## Dataset Description

The project uses a **Bank Customer Churn** dataset containing anonymized information about bank clients.

**Each row represents a customer.**

Typical features include:

* Demographics: age, gender, geography
* Financial indicators: credit score, account balance, estimated salary
* Product usage: number of products, credit card ownership
* Engagement: account tenure, activity status

**Target variable:**

* `Exited` — binary indicator of whether the customer left the bank.

> The dataset is publicly available (e.g. Kaggle). Due to size and licensing considerations, raw data is not stored in this repository.

---

## Problem Formulation

* **Task type:** Binary classification
* **Target:** Customer churn (`Exited`)
* **Primary metric:** ROC-AUC
* **Additional metrics:** Recall, Precision, F1-score

Special attention is given to **recall for churned customers**, since failing to identify a potential churner is usually more costly than a false positive.

---

## Project Structure

```
bank-churn-prediction/
├── README.md
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline.ipynb
│   ├── 04_models.ipynb
│   ├── 05_tuning.ipynb
│   └── 06_interpretation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   └── metrics.py
└── requirements.txt
```

---

## Workflow and Methodology

### 1. Exploratory Data Analysis (EDA)

* Dataset overview and data quality checks
* Class balance analysis
* Feature distributions
* Comparison of churned vs non-churned customers
* Initial business insights

### 2. Data Preprocessing

* Train/test split
* Encoding of categorical features
* Feature scaling (where required)
* Preparation of modeling-ready datasets

### 3. Baseline Model

* Logistic Regression as a benchmark
* Cross-validation
* Baseline metric evaluation

### 4. Model Training

* Random Forest
* Gradient Boosting models
* CatBoost (main model)
* Model comparison using consistent metrics

### 5. Hyperparameter Tuning

* Grid / randomized search
* Class imbalance handling
* Threshold optimization

### 6. Model Interpretation & Analysis

* Feature importance analysis
* Error analysis
* Identification of high-risk customer segments
* Business-oriented interpretation of results

---

## Tools and Technologies

* **Python**
* **pandas, numpy** — data processing
* **matplotlib, seaborn** — visualization
* **scikit-learn** — modeling and evaluation
* **CatBoost** — gradient boosting for categorical data
* **Optuna** — hyperparameter optimization
* **Google Colab** — experimentation environment

---

## Results

The final model demonstrates strong predictive performance and provides interpretable insights into customer churn drivers. Detailed results, metrics, and visualizations are available in the notebooks.

> The focus of this project is not only model performance, but also **interpretability and business relevance**.

---

## Reproducibility

To reproduce the experiments:

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the dataset and place it locally (see EDA notebook for details).
4. Run notebooks in sequential order.

---

## Future Improvements

Possible extensions of this project include:

* Advanced feature engineering
* Model explainability with SHAP
* Customer segmentation combined with churn prediction
* Deployment as an interactive dashboard (e.g. Streamlit)

---

## Author

This project was created as part of a machine learning course and serves as a demonstration of practical ML skills, from data analysis to model interpretation.

---

## License

This project is intended for educational and portfolio purposes.
