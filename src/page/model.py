from multipage import save, MultiPage, start_app, clear_cache
import streamlit as st
from joblib import load
import pandas as pd
import os

def model(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1
    pickle_dir = "C:/Users/user/Documents/SEMESTER 5/Pengantar Sains Data/Project Python/res/pickle"
    list_city = load(os.path.join(pickle_dir, "list_city.pkl"))
    key_pair = load(os.path.join(pickle_dir, "key_pair.pkl"))
    clf = load(os.path.join(pickle_dir, "model.pkl"))
    pipeline = load(os.path.join(pickle_dir, "pipeline.pkl"))
    st.title("Predict your data")
    city = st.selectbox("City", list_city)
    city_development_index = key_pair[city]
    gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
    relevent_experience = st.selectbox("Relevent Experienve",  ['Has relevent experience', 'No relevent experience'])
    enrolled_university = st.selectbox("Enrolled University", ['no_enrollment', 'Part time course', 'Full time course'])
    education_level = st.selectbox("Education Level", ['Primary School', 'High School', 'Graduate', 'Masters',  'Phd'])
    major_discipline = st.selectbox("Major Discipline", ['STEM', 'Business Degree','Arts', 'Humanities', 'No Major',
       'Other'])
    experience = st.selectbox("Experience", ['<1'] + [str(x) for x in range(1, 21)] + [">20"])
    company_size = st.selectbox("Company Size", ['<10', '10/49','50-99', '100-500', '500-999','1000-4999','5000-9999', '10000+'])
    last_new_job = st.selectbox("Last New Job", ['never', '1', '2', '3', '4', '>4'])
    company_type = st.selectbox("Company Type", ['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other',
       'Public Sector', 'NGO'])
    training_hours = st.slider("Training Hours", 1, 336)
    _list_column = ['city', 'city_development_index', 'gender',
       'relevent_experience', 'enrolled_university', 'education_level',
       'major_discipline', 'experience', 'company_size', 'company_type',
       'last_new_job', 'training_hours']
    if st.button("Go Predict!"):
        data_raw = [city, city_development_index, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours]
        data = pd.DataFrame([data_raw], columns=_list_column)
        with st.spinner("Wait for model to predict"):
            x = pipeline.transform(data)
            y = clf.predict(x)[0]  # just get single value
            prob = clf.predict_proba(x)[0].tolist()  # send to list for return
            print(y)
            if prob:
                final_dict = {0 : "Employee is not going to leave", 1 : "Employee is going to Leave"}
                st.text(f"Your prediction is {final_dict[y]} with probability of {max(prob)}")
    
    save([start_index], "placeholder1", ["App2", "App3"])
