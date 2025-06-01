import streamlit as st

st.title("Title: Bio data")
st.write("This is a sample web app.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last name")
gender = st.selectbox("Gender", ["Male", "Female", "Gay"])
age = st.number_input("Your Age", 0, 100, 30, 1)
dob = st.date_input("Your Birthday")
marital_status = st.radio("Marital status", ["Single","Married", "Divorced"])
years_of_experience = st.slider("Years of experience", 0, 40)


