
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("attrition_model.pkl")

st.title("💼 Employee Attrition Predictor")
st.markdown("Enter the employee's details below:")

def user_input_features():
    # Label mappings
    gender_map = {"Female": 0, "Male": 1}
    marital_map = {"Divorced": 0, "Married": 1, "Single": 2}
    education_map = {
        "Below College": 1,
        "College": 2,
        "Bachelor": 3,
        "Master": 4,
        "Doctor": 5
    }
    business_travel_map = {
        "Non-Travel": 0,
        "Travel_Frequently": 1,
        "Travel_Rarely": 2
    }
    department_map = {
        "Human Resources": 0,
        "Research & Development": 1,
        "Sales": 2
    }
    education_field_map = {
        "Human Resources": 0,
        "Life Sciences": 1,
        "Marketing": 2,
        "Medical": 3,
        "Other": 4,
        "Technical Degree": 5
    }
    job_role_map = {
        "Healthcare Representative": 0,
        "Human Resources": 1,
        "Laboratory Technician": 2,
        "Manager": 3,
        "Manufacturing Director": 4,
        "Research Director": 5,
        "Research Scientist": 6,
        "Sales Executive": 7,
        "Sales Representative": 8
    }
    overtime_map = {"No": 0, "Yes": 1}

    # Inputs with mappings
    Age = st.slider("Age", 18, 60, 30)
    BusinessTravel = business_travel_map[st.selectbox("Business Travel", list(business_travel_map.keys()))]
    DailyRate = st.slider("Daily Rate", 100, 1500, 1000)
    Department = department_map[st.selectbox("Department", list(department_map.keys()))]
    DistanceFromHome = st.slider("Distance From Home", 1, 30, 5)
    Education = education_map[st.selectbox("Education", list(education_map.keys()))]
    EducationField = education_field_map[st.selectbox("Education Field", list(education_field_map.keys()))]
    EnvironmentSatisfaction = st.slider("Environment Satisfaction", 1, 4, 3)
    Gender = gender_map[st.selectbox("Gender", list(gender_map.keys()))]
    HourlyRate = st.slider("Hourly Rate", 30, 100, 70)
    JobInvolvement = st.slider("Job Involvement", 1, 4, 3)
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobRole = job_role_map[st.selectbox("Job Role", list(job_role_map.keys()))]
    JobSatisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    MaritalStatus = marital_map[st.selectbox("Marital Status", list(marital_map.keys()))]
    MonthlyIncome = st.slider("Monthly Income", 1000, 20000, 5000)
    MonthlyRate = st.slider("Monthly Rate", 1000, 30000, 18000)
    NumCompaniesWorked = st.slider("Number of Companies Worked", 0, 10, 1)
    OverTime = overtime_map[st.selectbox("OverTime", list(overtime_map.keys()))]
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

# Prediction
if st.button("🔍 Predict Attrition"):
    prediction = model.predict(input_df)
    st.write("### ✅ Prediction:")
    if prediction[0] == 1:
        st.error("⚠️ The employee is **likely to leave** the company.")
    else:
        st.success("🎉 The employee is **likely to stay** with the company.")
