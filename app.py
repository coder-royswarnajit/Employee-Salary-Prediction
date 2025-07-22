import streamlit as st
import joblib
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar with info
st.sidebar.title("About")
st.sidebar.info(
    """
    **Employee Salary Prediction App**\n
    Enter your years at the company and job rating to predict your salary.\n
    - Model: Linear Regression\n    - Features: Years at Company, Job Rating\n    - Output: Predicted Salary (per year)
    """
)

st.title("Salary Prediction")
st.divider()

# Model loading with error handling
def load_model(path):
    try:
        model = joblib.load(path)
        return model, None
    except Exception as e:
        return None, str(e)

model, model_error = load_model("linearmodel.pkl")

# Input section in columns
col1, col2 = st.columns(2)
with col1:
    years = st.number_input(
        "Enter Years at Company",
        value=1,
        step=1,
        min_value=0,
        help="Number of years you have worked at the company."
    )
with col2:
    jobrate = st.number_input(
        "Enter the Job Rating",
        value=3.5,
        step=0.5,
        min_value=0.0,
        max_value=5.0,
        help="Your job performance rating (0.0 to 5.0)."
    )

X = [years, jobrate]

st.divider()

if model_error:
    st.error(f"Model could not be loaded: {model_error}")
else:
    predict = st.button("Predict Salary")
    if predict and model is not None:
        try:
            st.balloons()
            X1 = np.array(X).reshape(1, -1)
            prediction = model.predict(X1)[0]
            st.success(f"The predicted salary is ₹{prediction:,.2f} per year")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# Model info section
with st.expander("Model Information"):
    st.write("""
    - **Model Type:** Linear Regression
    - **Features Used:**
        - Years at Company
        - Job Rating
    - **Output:** Predicted annual salary (in INR)
    """)

with st.expander("Data Visualization: Years vs Annual Salary"):
    try:
        # Download and load the data
        import kagglehub
        data_path = kagglehub.dataset_download("abdallahwagih/company-employees")
        data_path = os.path.join(data_path, "employees.xlsx")
        data = pd.read_excel(data_path)
        data.dropna(inplace=True)
        data.drop_duplicates(inplace=True)
        # Plot
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(data["Years"], data["Annual Salary"], alpha=0.6)
        ax.set_xlabel("Years at Company")
        ax.set_ylabel("Annual Salary")
        ax.set_title("Years at Company vs Annual Salary")
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Could not display graph: {e}")
