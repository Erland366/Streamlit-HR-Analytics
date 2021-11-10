import streamlit as st
import src.assets as asset
from src.plot import *
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache

def hranalytics(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 

    st.title("HR Analytics")
    st.header("Context About Data")
    st.markdown("""
A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment.

This dataset designed to understand the factors that lead a person to leave current job for HR researches too. By model(s) that uses the current credentials,demographics,experience data you will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.

Link to Dataset → [Kaggle](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists)
    """)
    data = load_data('../aug_train.csv')
    with st.spinner("Wait for page to load"):
        st.header("Take a look at top 10 data")
        st.dataframe(data.head(10))
        buffer = io.StringIO()
        st.header("Some information about the data")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                with st.expander("See data info"):
                    data_info = pd.concat([pd.DataFrame(data.dtypes), data.count()], axis=1).set_axis(
                        ['dtypes', 'count'], axis="columns")
                    st.dataframe(data_info.astype('str'),
                                    width=1000, height=250)
            with col2:
                with st.expander("See data describe"):
                    st.dataframe(data.describe(), height=250)
    st.header("Data after Preprocessing")
    data_after_preprocessing = load_data("../aug_train_ready.csv", header=None, names=[f"col {x}" for x in range(19)])
    st.dataframe(data_after_preprocessing.head(10))
    base_img_path = "./res/img"
    with st.expander("Pipeline Preprocessing"):
        st.image(Image.open(os.path.join(base_img_path, "diagram pipeline.jpg")))
    
   
    save([start_index], "placeholder1", ["App2", "App3"]) 


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    with st.form(key="Selecting File"):
        selected_filename = st.selectbox('Select a file', filenames)
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        return os.path.join(folder_path, selected_filename)


@st.cache
def load_data(url, header='infer', **kwargs):
    return pd.read_csv(url, **kwargs)
