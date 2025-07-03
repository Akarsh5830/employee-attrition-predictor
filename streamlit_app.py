import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("attrition_model.pkl")

st.title("💼 Employee Attrition Predictor")

st.markdown("Enter the employee's details below:")

# Define input form for all 30 features
def user_input_features():
    Age = st.slider("Age", 18, 60, 30)
    BusinessTravel = st.selectbox("Business Travel", [0, 1, 2])  # Encoded values
    DailyRate = st.slider("Daily Rate", 100, 1500, 1000)
    Department = st.selectbox("Department", [0, 1, 2])
    DistanceFromHome = st.slider("Distance From Home", 1, 30, 5)
    Education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    EducationField = st.selectbox("Education Field", [0, 1, 2, 3, 4, 5])
    EnvironmentSatisfaction = st.slider("Environment Satisfaction", 1, 4, 3)
    Gender = st.selectbox("Gender", [0, 1])  # Female:0, Male:1
    HourlyRate = st.slider("Hourly Rate", 30, 100, 70)
    JobInvolvement = st.slider("Job Involvement", 1, 4, 3)
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobRole = st.selectbox("Job Role", list(range(9)))  # 0-8
    JobSatisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    MaritalStatus = st.selectbox("Marital Status", [0, 1, 2])  # Single, Married, Divorced
    MonthlyIncome = st.slider("Monthly Income", 1000, 20000, 5000)
    MonthlyRate = st.slider("Monthly Rate", 1000, 30000, 18000)
    NumCompaniesWorked = st.slider("Number of Companies Worked", 0, 10, 1)
    OverTime = st.selectbox("OverTime", [0, 1])  # No:0, Yes:1
    PercentSalaryHike = st.slider("Percent Salary Hike", 10, 25, 13)
    PerformanceRating = st.selectbox("Performance Rating", [1, 2, 3, 4])
    RelationshipSatisfaction = st.slider("Relationship Satisfaction", 1, 4, 3)
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    TotalWorkingYears = st.slider("Total Working Years", 0, 40, 10)
    TrainingTimesLastYear = st.slider("Training Times Last Year", 0, 6, 3)
    WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    YearsAtCompany = st.slider("Years at Company", 0, 40, 5)
    YearsInCurrentRole = st.slider("Years in Current Role", 0, 20, 4)
    YearsSinceLastPromotion = st.slider("Years Since Last Promotion", 0, 15, 2)
    YearsWithCurrManager = st.slider("Years With Current Manager", 0, 20, 3)

    data = {
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'DailyRate': DailyRate,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': EducationField,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'Gender': Gender,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime': OverTime,
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager,
    }

    return pd.DataFrame([data])

input_df = user_input_features()

# Predict on button click
if st.button("🔍 Predict Attrition"):
    prediction = model.predict(input_df)
    st.write("### ✅ Prediction:")
    if prediction[0] == 1:
        st.error("⚠️ The employee is **likely to leave** the company.")
    else:
        st.success("🎉 The employee is **likely to stay** with the company.")

