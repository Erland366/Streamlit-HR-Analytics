import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
from src.page.hranalytics import hranalytics
from src.page.hranalyticsgraph import hranalyticsgraph
from src.page.model import model
from PIL import Image
import os

def main():
    st.set_page_config(page_title="HR Analytics", page_icon="📊", layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
        )
    start_app() #Clears the cache when the app is started

    app = MultiPage()
    app.start_button = "Let's go!"
    app.navbar_name = "Navigation"
    app.next_page_button = "Next Page"
    app.previous_page_button = "Previous Page"
    app.set_initial_page(startpage)
    app.add_app("About Me", startpage)
    app.add_app("HR Analytics", hranalytics)
    app.add_app("HR Analytics Graph", hranalyticsgraph)
    app.add_app("Predict", model)
    app.run()
    
def startpage(prev_vars=0):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 

    _, col, _ = st.columns(3)
    base_img_path = "./res/img"
    with col:
        st.image(Image.open(os.path.join(base_img_path, "template/Foto Profil Nyamar.jpeg")))
    st.markdown("""
    This is Me, I am Erland Hilman Fuadi, I am in my third year of Informatics Engineering at Faculty of Computer Science in Brawijaya University. I am really passionate in Deep Learning, especially in Computer Vision.
    
    """)
    
    st.write("Connect me to Linkedin")
    col1, col2,_, _, _, _, _ = st.columns(7)
    with col1:
        st.image(Image.open(os.path.join(base_img_path, "template/linkedin_logo.png")), width=50)
    with col2:
        st.markdown("[Linkedin](https://www.linkedin.com/in/erland-hilman-306a50192/)")
    
    st.write("Check out my dashboard on Kaggle Data Survey 2021")
    col1, col2,_, _, _,_, _ = st.columns(7)
    with col1:
        st.image(Image.open(os.path.join(base_img_path, "template/tableau-logo.png")), width=50)
    with col2:
        st.markdown("[Tableau](https://public.tableau.com/app/profile/erland.hilman.fuadi/viz/KaggleDataScienceDataset3/FinalDashboard?publish=yes)")

    save([start_index], "placeholder1", ["App2", "App3"]) 

if __name__ == "__main__":
    main()
