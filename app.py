import streamlit as st
import pandas as pd
import joblib
import numpy as np
from catboost import CatBoostClassifier

# Set page configuration
st.set_page_config(page_title="Bank Churn Predictor", page_icon="🏦")

# 1. Load the saved artifacts
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load('artifacts/final_model.joblib')
        preprocessor = joblib.load('artifacts/preprocessor.joblib')
        return model, preprocessor
    except Exception as e:
        return None, None

model, preprocessor = load_artifacts()

if model is None or preprocessor is None:
    st.error("❌ Failed to load model artifacts.")
    st.info("""
    **Possible reasons:**
    1. The `artifacts/` folder is missing in your repository.
    2. The `.joblib` files are saved with a different version of `scikit-learn`.
    
    **Current local fix attempt:** We have pinned `scikit-learn==1.5.2` in `requirements.txt`. 
    Please push the changes and wait for the app to rebuild.
    """)
    st.stop()

# 2. UI Header
st.title("🏦 Bank Customer Churn Predictor")
st.markdown("""
This app predicts the probability of a customer leaving the bank using a **CatBoost** model 
optimized with **Optuna**.
""")

# 3. User Inputs in Sidebar
st.sidebar.header("Customer Information")

def user_input_features():
    age = st.sidebar.slider("Age", 18, 100, 35)
    balance = st.sidebar.number_input("Balance ($)", 0.0, 250000.0, 50000.0)
    products = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
    is_active = st.sidebar.selectbox("Is Active Member?", [0, 1], help="1 = Yes, 0 = No")
    country = st.sidebar.selectbox("Country", ["France", "Germany", "Spain"])
    gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
    tenure = st.sidebar.slider("Tenure (Years with bank)", 0, 10, 5)
    credit_score = st.sidebar.number_input("Credit Score", 300, 850, 650)
    has_cr_card = st.sidebar.selectbox("Has Credit Card?", [0, 1])
    salary = st.sidebar.number_input("Estimated Salary ($)", 0.0, 200000.0, 100000.0)

    data = {
        'credit_score': credit_score,
        'country': country,
        'gender': gender,
        'age': age,
        'tenure': tenure,
        'balance': balance,
        'products_number': products,
        'credit_card': has_cr_card,
        'active_member': is_active,
        'estimated_salary': salary
    }
    return pd.DataFrame([data])

input_df = user_input_features()

# 4. Display input and prediction
st.subheader("Customer Profile Summary")
st.write(input_df)

if st.button("Analyze Risk"):
    # Apply the same preprocessing as in training
    X_processed = preprocessor.transform(input_df)
    
    # Get probability from the model
    probability = model.predict_proba(X_processed)[0][1]
    
    # Visual result
    st.subheader("Prediction Result")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Churn Probability", f"{probability:.1%}")
    
    with col2:
        if probability > 0.5:
            st.error("⚠️ HIGH RISK: Likely to Churn")
        else:
            st.success("✅ LOW RISK: Likely to Stay")
            
    # Progress bar for visual impact
    st.progress(probability)