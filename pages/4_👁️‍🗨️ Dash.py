import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Dash", page_icon='images/logomaster_icon.ico', layout="wide",
                   initial_sidebar_state="collapsed", menu_items=None)

avaliacoes = pd.read_excel('tables/db_avaliacoes.xlsx', index_col=0)
listanomes_geral = avaliacoes['nome'].unique().astype(str)

select_nome = st.sidebar.selectbox('Selecionar Nome', listanomes_geral)
nome_data = avaliacoes.loc[avaliacoes['nome'] == select_nome]

nome_value = nome_data['nome'].values[0]
data_value = nome_data['data_medida'].values[0]
idade_value = nome_data['idade'].values[0]
sexo_value = nome_data['sexo'].values[0]
peso_value = nome_data['peso'].values[0]
estatura_value = nome_data['estatura'].values[0]
imc_value = (nome_data['peso']) / ((nome_data['estatura'] / 100) * (nome_data['estatura'] / 100))
rce_value = nome_data['p_cintura'] / nome_data['estatura']
rcq_value = nome_data['p_cintura'] / nome_data['p_quadril']
fpm_value = nome_data[['handgripD1', 'handgripE1', 'handgripD2', 'handgripE2']].max(axis=1).values[0]
sl_value = nome_data[['senlev1', 'senlev2']].max(axis=1).values[0]
iv_value = nome_data[['irvir1', 'irvir2']].min(axis=1).values[0]
mu_value = nome_data[['marcha1', 'marcha2']].min(axis=1).values[0]
mm_value = nome_data['dexa_mm'].values[0]
mg_value = nome_data['dexa_mg'].values[0]
mo_value = nome_data['dexa_pg'].values[0]
tscore_value = nome_data['dexa_bmc'].values[0]
mm_percentual = (mm_value / peso_value) * 100
mg_percentual = (mg_value / peso_value) * 100
mo_percentual = (mo_value / peso_value) * 100

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

cabecalho = st.container()
colblank1, collogomaster = cabecalho.columns([1, 30.5])
logo_master = collogomaster.image(Image.open('images/header2.png'), width=1600)

# titulo_label = coltitulo.markdown('## **AVALIAÇÃO FUNCIONAL**')
# img_logos = collogos.image(Image.open('images/logos.png'))

col1, col2 = cabecalho.columns(2)

title_label1 = col1.markdown('## **DADOS PESSOAIS:**')
dadospessoais_label = col1.markdown(f"#### Nome: {nome_value}     \n"
                                    f"#### Data da avaliacão (dd/mm/aa): {data_value}     \n"
                                    f"#### Idade (anos): {idade_value}     \n"
                                    f"#### Peso (kg): {peso_value}     \n"
                                    f"#### Estatura (cm): {estatura_value}     \n")

# nome_label1 = col1.markdown(f" **Nome:** {nome_data['nome'].values[0]}")
# data_label1 = col1.markdown(f"**Data da avaliacão:** {nome_data['data_medida'].values[0]}")
# idade_label1 = col1.markdown(f"**Idade:** {nome_data['idade'].values[0]}")
# peso_label1 = col1.markdown(f"**Peso:** {nome_data['peso'].values[0]}")
# estatura_label1 = col1.markdown(f"**Estatura:** {nome_data['estatura'].values[0]}")

fig_imc = go.Figure()
if float(imc_value) <= 18.4:
    fig_imc.add_trace(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=float(imc_value),
        mode="gauge+number",
        title={'text': "IMC"},
        gauge={'axis': {'range': [10, 40]},
               'steps': [
                   {'name': "Abaixo do peso", 'range': [0, 18.4], 'color': "white", },
                   {'name': "Peso normal", 'range': [18.5, 24.9], 'color': "white", },
                   {'name': "Sobrepeso", 'range': [25, 29.9], 'color': "white", },
                   {'name': "Obesidade", 'range': [30, 40], 'color': "white", }],
               'bar': {'color': "#2887DF", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
               'bgcolor': "black", 'shape': "angular",
               }))
elif 18.5 <= float(imc_value) <= 24.9:
    fig_imc.add_trace(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=float(imc_value),
        mode="gauge+number",
        title={'text': "IMC"},
        gauge={'axis': {'range': [10, 40]},
               'steps': [
                   {'name': "Abaixo do peso", 'range': [0, 18.4], 'color': "white", },
                   {'name': "Peso normal", 'range': [18.5, 24.9], 'color': "white", },
                   {'name': "Sobrepeso", 'range': [25, 29.9], 'color': "white", },
                   {'name': "Obesidade", 'range': [30, 40], 'color': "white", }],
               'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
               'bgcolor': "black", 'shape': "angular",
               }))
elif 25 <= float(imc_value) <= 29.9:
    fig_imc.add_trace(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=float(imc_value),
        mode="gauge+number",
        title={'text': "IMC"},
        gauge={'axis': {'range': [10, 40]},
               'steps': [
                   {'name': "Abaixo do peso", 'range': [0, 18.4], 'color': "white", },
                   {'name': "Peso normal", 'range': [18.5, 24.9], 'color': "white", },
                   {'name': "Sobrepeso", 'range': [25, 29.9], 'color': "white", },
                   {'name': "Obesidade", 'range': [30, 40], 'color': "white", }],
               'bar': {'color': "#f47f20", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
               'bgcolor': "black", 'shape': "angular",
               }))
elif float(imc_value) >= 30:
    fig_imc.add_trace(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=float(imc_value),
        mode="gauge+number",
        title={'text': "IMC"},
        gauge={'axis': {'range': [10, 40]},
               'steps': [
                   {'name': "Abaixo do peso", 'range': [0, 18.4], 'color': "white", },
                   {'name': "Peso normal", 'range': [18.5, 24.9], 'color': "white", },
                   {'name': "Sobrepeso", 'range': [25, 29.9], 'color': "white", },
                   {'name': "Obesidade", 'range': [30, 40], 'color': "white", }],
               'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
               'bgcolor': "black", 'shape': "angular",
               }))

fig_imc.update_layout(height=350, font={'color': "darkblue", 'family': "Arial"})
grafico_imc = col1.plotly_chart(fig_imc, theme="streamlit", use_container_width=True)

colimc1, colimc2 = col1.columns([1.1, 1])
# legendas_perimetros = colperimetros1.color_picker('legenda', value="#ff0000", disabled=False, label_visibility="hidden")
imc_label1 = colimc2.markdown('Pontos de corte:   \n'
                              'Abaixo do peso - abaixo de 18,5;  \n'
                              'Peso normal - entre 18,5 e 25;  \n'
                              'Sobrepeso - entre 25 e 30;  \n'
                              'Obesidade - acima de 30;  \n')

imc_label2 = colimc1.markdown('#### 🟦 Abaixo do peso')
imc_label3 = colimc1.markdown('#### 🟩 Peso normal')
imc_label4 = colimc1.markdown('#### 🟧 Sobrepeso')
imc_label5 = colimc1.markdown('#### 🟥 Obesidade')

title_label2 = col2.markdown('## **PERÍMETROS:**')
# nome_label2 = col2.markdown(f"{nome_data['nome'].values[0]}")
pericol1, pericol2 = col2.columns(2)
if sexo_value == 'Feminino':
    perimetros_img = pericol2.image((Image.open('images/perimetros_img_fem.png')), width=175)
elif sexo_value == 'Masculino':
    perimetros_img = pericol2.image((Image.open('images/perimetros_img_masc.png')), width=175)

# perimetros_label = pericol1.markdown(f"**1. Cintura(cm):** {nome_data['p_cintura'].values[0]}     \n"
#                                     f"**2. Quadril(cm):** {nome_data['p_quadril'].values[0]}     \n"
#                                     f"**3. Coxa(cm):** {nome_data['p_coxamed'].values[0]}     \n"
#                                     f"**4. Perna(cm):** {nome_data['p_perna'].values[0]}     \n")

cintura_label2 = pericol1.markdown(f"#### 1.Cintura(cm): {nome_data['p_cintura'].values[0]}")
quadril_label2 = pericol1.markdown(f"#### 2.Quadril(cm): {nome_data['p_quadril'].values[0]}")
coxa_label2 = pericol1.markdown(f"#### 3.Coxa(cm): {nome_data['p_coxamed'].values[0]}")
perna_label2 = pericol1.markdown(f"#### 4.Perna(cm): {nome_data['p_perna'].values[0]}")

fig_perimetros = go.Figure()

if float(rce_value) >= 0.5:
    fig_perimetros.add_trace(go.Indicator(
        mode="number+gauge", value=float(rce_value),
        domain={'x': [0.2, 1], 'y': [0.6, 1]},
        title={'text': "RCE"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 1]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 0.5},
            'steps': [
                {'range': [0, 0.5], 'color': "white"},
                {'range': [0.5, 1], 'color': "white"}]}))
elif float(rce_value) < 0.5:
    fig_perimetros.add_trace(go.Indicator(
        mode="number+gauge", value=float(rce_value),
        domain={'x': [0.2, 1], 'y': [0.6, 1]},
        title={'text': "RCE"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 1]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 0.5},
            'steps': [
                {'range': [0, 0.5], 'color': "white"},
                {'range': [0.5, 1], 'color': "white"}]}))

if float(rcq_value) >= 0.85:
    fig_perimetros.add_trace(go.Indicator(
        mode="number+gauge", value=float(rcq_value),
        domain={'x': [0.2, 1], 'y': [0, 0.4]},
        title={'text': "RCQ"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 1]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 0.85},
            'steps': [
                {'range': [0, 0.85], 'color': "white"},
                {'range': [0.85, 1], 'color': "white"}]}))
elif float(rce_value) < 0.85:
    fig_perimetros.add_trace(go.Indicator(
        mode="number+gauge", value=float(rcq_value),
        domain={'x': [0.2, 1], 'y': [0, 0.4]},
        title={'text': "RCQ"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 1]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 0.85},
            'steps': [
                {'range': [0, 0.85], 'color': "white"},
                {'range': [0.85, 1], 'color': "white"}]}))

fig_perimetros.update_layout(height=225, margin={'t': 0, 'b': 50, 'l': 0},
                             font={'color': "darkblue", 'family': "Arial"})
graficos_perimetros = col2.plotly_chart(fig_perimetros, theme="streamlit", use_container_width=True)

colperimetros1, colperimetros2 = col2.columns([1, 1])
# legendas_perimetros = colperimetros1.color_picker('legenda', value="#ff0000", disabled=False, label_visibility="hidden")
perimetros_label1 = colperimetros2.markdown('Pontos de corte:   \n'
                                            'Relacao cintura-estatura (RCE) ≥ 0,5;  \n'
                                            'Relacao cintura-quadril (RCQ) ≥ 0,85')
perimetros_label2 = colperimetros1.markdown('#### 🟥 Maior risco cardiovascular')
perimetros_label3 = colperimetros1.markdown('#### 🟩 Menor risco cardiovascular')

cabecalho2 = st.container()
# colblank12, collogomaster2 = cabecalho2.columns([1, 15.5])
# logo_master2 = collogomaster2.image(Image.open('images/header2.png'), width=1500)

col3, col4 = cabecalho2.columns(2)

title_label3 = col3.markdown('### **TESTES:**')
# nome_label3 = col3.markdown(f"{nome_data['nome'].values[0]}")
testes_label = col3.markdown(
    f"##### Forca de Prensão Manual (kg): {fpm_value}     \n"
    f"##### Sentar e levantar (rep): {sl_value}     \n"
    f"##### Ir e vir (s): {iv_value[-9:]}     \n"
    f"##### Marcha usual (5m)(s): {mu_value[-9:]}     \n")

# handgrip_label3 = col3.markdown(
#     f"**Forca de Prensão Manual (kg):** {nome_data[['handgripD1', 'handgripE1', 'handgripD2', 'handgripE2']].max(axis=1).values[0]}")
# senlev_label3 = col3.markdown(f"**Sentar e levantar (rep):** {nome_data[['senlev1', 'senlev2']].max(axis=1).values[0]}")
# irvir_label3 = col3.markdown(f"**Ir e vir (s):** {nome_data[['irvir1', 'irvir2']].min(axis=1).values[0]}")
# marcha_label3 = col3.markdown(f"**Marcha usual (s):** {nome_data[['marcha1', 'marcha2']].min(axis=1).values[0]}")

fig_testes = go.Figure()

if fpm_value >= 16:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=fpm_value,
        domain={'x': [0.2, 1], 'y': [0.7, 0.8], 'row': 3},
        title={'text': "FPM"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 50]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 16},
            'steps': [
                {'range': [0, 16], 'color': "white"},
                {'range': [16, 50], 'color': "white"}]}))

elif fpm_value < 16:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=fpm_value,
        domain={'x': [0.2, 1], 'y': [0.7, 0.8], 'row': 3},
        title={'text': "FPM"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 50]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 16},
            'steps': [
                {'range': [0, 16], 'color': "white"},
                {'range': [16, 50], 'color': "white"}]}))

if sl_value >= 10:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=sl_value,
        domain={'x': [0.2, 1], 'y': [0.5, 0.6], 'row': 1},
        title={'text': "SL"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 10},
            'steps': [
                {'range': [0, 10], 'color': "white"},
                {'range': [10, 40], 'color': "white"}]}))
elif sl_value < 10:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=sl_value,
        domain={'x': [0.2, 1], 'y': [0.5, 0.6], 'row': 1},
        title={'text': "SL"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 10},
            'steps': [
                {'range': [0, 10], 'color': "white"},
                {'range': [10, 40], 'color': "white"}]}))

if float(iv_value[-9:]) >= 20:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=float(iv_value[-9:]),
        domain={'x': [0.2, 1], 'y': [0.3, 0.4], 'row': 2},
        title={'text': "IV"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 20},
            'steps': [
                {'range': [0, 20], 'color': "white"},
                {'range': [20, 40], 'color': "white"}]}))
elif float(iv_value[-9:]) < 20:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=float(iv_value[-9:]),
        domain={'x': [0.2, 1], 'y': [0.3, 0.4], 'row': 2},
        title={'text': "IV"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 20},
            'steps': [
                {'range': [0, 20], 'color': "white"},
                {'range': [20, 40], 'color': "white"}]}))

if float(mu_value[-9:]) >= 6.25:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=float(mu_value[-9:]),
        domain={'x': [0.2, 1], 'y': [0.1, 0.2], 'row': 0},
        title={'text': "MU"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 6.25},
            'steps': [
                {'range': [0, 6.25], 'color': "white"},
                {'range': [6.25, 40], 'color': "white"}]}))
elif float(mu_value[-9:]) < 6.25:
    fig_testes.add_trace(go.Indicator(
        mode="number+gauge", value=float(mu_value[-9:]),
        domain={'x': [0.2, 1], 'y': [0.1, 0.2], 'row': 0},
        title={'text': "MU"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, 40]},
            'bar': {'color': "#6ca443", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 1,
                'value': 6.25},
            'steps': [
                {'range': [0, 6.25], 'color': "white"},
                {'range': [6.25, 40], 'color': "white"}]}))

fig_testes.update_layout(height=405, margin={'t': 0, 'b': 45, 'l': 0},
                         font={'color': "darkblue", 'family': "Arial"})
grafico_testes = col3.plotly_chart(fig_testes, theme="streamlit", use_container_width=True)

coltestes1, coltestes2 = col3.columns([1, 1])
# legendas_perimetros = colperimetros1.color_picker('legenda', value="#ff0000", disabled=False, label_visibility="hidden")
testes_label1 = coltestes2.markdown('Pontos de corte:   \n'
                                    'FPM < 16 kg;  \n'
                                    'SL < 10 rep;  \n'
                                    'IV ≥ 20 s;  \n'
                                    'MU ≥ 6,25 s;  \n')
testes_label2 = coltestes1.markdown('#### 🟥 Desempenho a melhorar')
testes_label3 = coltestes1.markdown('#### 🟩 Desempenho bom')

title_label4 = col4.markdown('### **DEXA:**')

dexa_label = col4.markdown(f"##### Massa magra (kg): {mm_value}     \n"
                           f"##### Massa gorda (kg): {mg_value}     \n"
                           f"##### Massa ossea (kg): {mo_value}     \n"
                           f"##### Percentual de gordura (%): {round(mg_percentual, 1)}     \n"
                           f"##### T-Score: {tscore_value}     \n")

# nome_label4 = col4.markdown(f"{nome_data['nome'].values[0]}")
# dexamm_label4 = col4.markdown(f"**Massa magra:** {nome_data['dexa_mm'].values[0]}")
# dexamg_label4 = col4.markdown(f"**Massa gorda:** {nome_data['dexa_mg'].values[0]}")
# dexapg_label4 = col4.markdown(f"**Massa ossea:** {nome_data['dexa_pg'].values[0]}")
# dexabmc_label4 = col4.markdown(f"**Densidade mineral ossea:** {nome_data['dexa_bmc'].values[0]}")

fig_dexa = go.Figure()

fig_dexa.add_trace(go.Bar(
    y=['CC'],
    x=[round(mm_percentual, 2)],
    name='Massa magra',
    orientation='h',
    text=str(round(mm_percentual, 2)),
    marker=dict(
        color='rgba(209, 57, 46, 0.6)',
        line=dict(color='rgba(209, 57, 46, 1.0)', width=3)
    )
))
fig_dexa.add_trace(go.Bar(
    y=['CC'],
    x=[round(mg_percentual, 2)],
    name='Massa gorda',
    orientation='h',
    text=str(round(mg_percentual, 2)),
    marker=dict(
        color='rgba(250, 198, 46, 0.6)',
        line=dict(color='rgba(250, 198, 46, 1.0)', width=3)
    )
))
fig_dexa.add_trace(go.Bar(
    y=['CC'],
    x=[round(mo_percentual, 2)],
    name='Massa Ossea',
    orientation='h',
    text=str(round(mo_percentual, 2)),
    textposition='inside',
    marker=dict(
        color='rgba(40, 135, 223, 0.6)',
        line=dict(color='rgba(40, 135, 223, 1.0)', width=3)
    )
))

fig_dexa.update_layout(barmode='stack', showlegend=False, height=150, margin={'t': 0, 'b': 50, 'l': 0, 'r': 0},
                       font={'color': "darkblue", 'family': "Arial", 'size': 24})
grafico_dexa = col4.plotly_chart(fig_dexa, theme="streamlit", use_container_width=True)

dexa_label2 = col4.markdown('#### 🟥 Massa magra')
dexa_label3 = col4.markdown('#### 🟨 Massa gorda')
dexa_label4 = col4.markdown('#### 🟦 Massa ossea')

fig_dexatscore = go.Figure()

if tscore_value <= -2.5:
    fig_dexatscore.add_trace(go.Indicator(
        mode="number+gauge", value=tscore_value,
        domain={'x': [0.2, 1], 'y': [0, 0.4]},
        title={'text': "T-Score"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [-5, 5]},
            'bar': {'color': "#d1392e", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'bgcolor': "black",
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 1,
            #     'value': -1},
            'steps': [
                {'range': [-5, -2.5], 'color': "white"},
                {'range': [-2.5, -1], 'color': "white"},
                {'range': [-1, 5], 'color': "white"}]}))
elif -2.5 < tscore_value <= -1:
    fig_dexatscore.add_trace(go.Indicator(
        mode="number+gauge", value=tscore_value,
        domain={'x': [0.2, 1], 'y': [0, 0.4]},
        title={'text': "T-SCORE"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [-5, 5]},
            'bar': {'color': "#f47f20", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'bgcolor': "black",
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 1,
            #     'value': -1},
            'steps': [
                {'range': [-5, -2.5], 'color': "white"},
                {'range': [-2.5, -1], 'color': "white"},
                {'range': [-1, 5], 'color': "white"}]}))
elif tscore_value > -1:
    fig_dexatscore.add_trace(go.Indicator(
        mode="number+gauge", value=tscore_value,
        domain={'x': [0.2, 1], 'y': [0, 0.4]},
        title={'text': "T-SCORE"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [-5, 5]},
            'bar': {'color': "#2887DF", 'thickness': 1, 'line': {'color': "black", 'width': 1}},
            'bgcolor': "black",
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 1,
            #     'value': -1},
            'steps': [
                {'range': [-5, -2.5], 'color': "white"},
                {'range': [-2.5, -1], 'color': "white"},
                {'range': [-1, 5], 'color': "white"}]}))

fig_dexatscore.update_layout(height=150, margin={'t': 0, 'b': 35, 'l': 50},
                             font={'color': "darkblue", 'family': "Arial"})

graficos_dexatscore = col4.plotly_chart(fig_dexatscore, theme="streamlit", use_container_width=True)

coltscore1, coltscore2 = col4.columns([1.2, 1])
# legendas_perimetros = colperimetros1.color_picker('legenda', value="#ff0000", disabled=False, label_visibility="hidden")
tscore_label1 = coltscore2.markdown('Pontos de corte:   \n'
                                    'Osteoporose - abaixo de -2,5;  \n'
                                    'Osteopenia - entre -2,5 e -1;  \n'
                                    'Densidade normal - acima de -1;  \n')

tscore_label2 = coltscore1.markdown('#### 🟥 Pode indicar osteoporose')
tscore_label3 = coltscore1.markdown('#### 🟧 Pode indicar osteopenia')
tscore_label4 = coltscore1.markdown('#### 🟦 Densidade normal')

# botao_pdf = st.sidebar.button('Gerar pdf', on_click=gerar_pdf)
