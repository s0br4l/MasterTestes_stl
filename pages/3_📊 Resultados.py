import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(page_title="Resultados", page_icon='images/resultados.ico', layout="centered", initial_sidebar_state="auto", menu_items=None)

container1 = st.container()
container1.image(Image.open('images/large_master_image_resultados.png'))

avaliacoes = pd.read_excel('tables/db_avaliacoes.xlsx', index_col=0)
listanomes_geral = avaliacoes['nome'].unique().astype(str)

avaliacoes['imc'] = (avaliacoes['peso']) / ((avaliacoes['estatura']/100) * (avaliacoes['estatura']/100))
avaliacoes['RCE'] = avaliacoes['p_cintura'] / avaliacoes['estatura']
avaliacoes['RCQ'] = avaliacoes['p_cintura'] / avaliacoes['p_quadril']
avaliacoes['handgrip_f'] = avaliacoes[["handgripD1", "handgripE1", "handgripD2", "handgripE2"]].max(axis=1)
avaliacoes['irvir_f'] = avaliacoes[["irvir1", "irvir2"]].min(axis=1)
avaliacoes['senlev_f'] = avaliacoes[["senlev1", "senlev2"]].max(axis=1)
avaliacoes['marcha_f'] = avaliacoes[["marcha1", "marcha2"]].min(axis=1)


container2 = st.container()
container2.dataframe(avaliacoes, use_container_width=True)
container2.dataframe(avaliacoes.describe(), use_container_width=True)
