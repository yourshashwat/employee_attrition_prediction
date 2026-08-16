import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Employee Attrition Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load dataset
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )


df = load_data()

# -----------------------------
# Header
# -----------------------------

st.title("👥 Employee Attrition Analytics")
st.write(
    "An interactive dashboard for analyzing employee attrition and predicting employee retention risk."
)

st.divider()

# -----------------------------
# Dataset statistics
# -----------------------------

total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
attrition_rate = employees_left / total_employees * 100
average_age = df["Age"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Employees",
        total_employees
    )

with col2:
    st.metric(
        "Employees Left",
        employees_left
    )

with col3:
    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.1f}%"
    )

with col4:
    st.metric(
        "Average Age",
        f"{average_age:.1f}"
    )

st.divider()

# -----------------------------
# Charts
# -----------------------------

st.subheader("📊 Attrition Overview")

col1, col2 = st.columns(2)

with col1:

    st.bar_chart(
        df["Attrition"].value_counts(),
        x_label="Attrition Status",
        y_label="NUmber of Employees"
        )

with col2:


    st.bar_chart(
        df[df["Attrition"]=="Yes"]["Department"].value_counts(),
        x_label="Department",
        y_label="Number of Employees"
    )

st.divider()
   #---------------------------------
   # MORE ANALYSIS
   # --------------------------------

st.subheader("Workforce Analysis")

col1, col2= st.columns(2)

with col1:
    st.markdown("#### Attrition by Overtime")
    overtime_chart= pd.crosstab(df["OverTime"], df["Attrition"])

    st.bar_chart(
        overtime_chart,
        use_container_width=True,
        x_label="Overtime Status",
        y_label= "Number of Employees"
    )

with col2:
    st.markdown("#### Attrition by Job Satisfaction")

    satisfaction_chart= pd.crosstab(df["JobSatisfaction"], df["Attrition"])

    st.bar_chart(
        satisfaction_chart,
        use_container_width=True,
        x_label="Job Satisfaction Label",
        y_label="Number of Employees"
    )
 

# -----------------------------
# Prediction section
# -----------------------------

st.divider()

st.subheader("🔮 Employee Attrition Prediction")

st.info(
    "Prediction model is currently under development. "
    "The interface below is a prototype and will be connected "
    "to Logistic Regression and Decision Tree models."
)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=200000,
        value=50000
    )

    years_at_company = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=40,
        value=5
    )

    overtime = st.selectbox(
        "Overtime",
        ["Yes", "No"]
    )

with col2:

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1, 2, 3, 4],
        index=2
    )

    work_life_balance = st.selectbox(
        "Work-Life Balance",
        [1, 2, 3, 4],
        index=2
    )

    job_role = st.selectbox(
        "Job Role",
        sorted(df["JobRole"].unique())
    )

    department = st.selectbox(
        "Department",
        sorted(df["Department"].unique())
    )

st.write("")

if st.button(
    "🔍 Check Attrition Risk",
    use_container_width=True
):

    st.warning(
        "⚠️ Demo Mode: The machine learning model "
        "has not been connected yet."
    )

    st.write(
        "These inputs will later be passed to our trained "
        "Logistic Regression and Decision Tree models."
    )

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "Employee Attrition Prediction System • "
    "Machine Learning Project"
)