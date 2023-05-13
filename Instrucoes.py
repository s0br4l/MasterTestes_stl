
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Programa Master Vida", page_icon='images/logomaster_icon.ico', layout="centered",
                   initial_sidebar_state="auto", menu_items=None)

container1 = st.container()
container1.image(Image.open('images/large_master_image.png'))

container2 = st.container()
container2.text_area('info', "🗒️ Avaliacões Master Vida  \n\n"
                             "instrucoes gerais \n\n"
                             "", label_visibility='hidden')
