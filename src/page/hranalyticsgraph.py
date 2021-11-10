import streamlit as st
import src.assets as asset
from src.plot import *
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache

def hranalyticsgraph(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 

    with st.spinner("Wait for the page to load"):
        st.header("Take a look at the graph")
        base_img_path = './res/img/'
        with st.expander("Percentage of Each Class"):
            with st.spinner("Wait for image to load"):
                with st.container():
                    _, col, _ = st.columns(3)
                    with col:
                        image = Image.open(os.path.join(
                            base_img_path, 'p_d_t.png'))
                        st.image(image)
        with st.expander("Data Gender"):
            base_img_path = './res/img/'
            with st.spinner("Wait for image to load"):
                with st.container():
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.subheader("Count plot")
                    with col2:
                        st.subheader(f"Percentage of each Gender")
                    with col3:
                        st.subheader(
                            f"Percentage of each Gender by target")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        image = Image.open(os.path.join(
                            base_img_path, 'cp_g.png'))
                        st.image(image)
                    with col2:
                        image = Image.open(os.path.join(
                            base_img_path, 'p_g.png'))
                        st.image(image)
                    with col3:
                        image = Image.open(os.path.join(
                            base_img_path, 'p_g_b_t.png'))
                        st.image(image)
        with st.expander("Data City Development Index"):
            base_img_path = './res/img/'
            with st.spinner("Wait for image to load"):
                with st.container():
                    _, col, _ = st.columns(3)
                    with col:
                        st.subheader("KDE City Development Index")
                        image = Image.open(os.path.join(
                            base_img_path, 'kde_c_d_i.png'))
                        st.image(image)
                    

    save([start_index], "placeholder1", ["App2", "App3"]) 