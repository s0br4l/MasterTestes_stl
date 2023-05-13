from datetime import datetime, date, time, timedelta
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Avaliacoes", page_icon='images/avaliacoes.ico', layout="centered",
                   initial_sidebar_state="auto", menu_items=None)

container1 = st.container()
container1.image(Image.open('images/large_master_image_avaliacoes.png'))

avaliacoes = pd.read_excel('tables/db_avaliacoes.xlsx', index_col=0)
avaliacoes_exib = avaliacoes[['nome', 'data_medida', 'idade', 'sexo', 'peso', 'estatura', 'p_cintura',
                              'p_quadril', 'p_coxamed', 'p_perna', 'handgripD1', 'handgripE1', 'handgripD2',
                              'handgripE2', 'irvir1', 'irvir2', 'senlev1', 'senlev2', 'marcha1', 'marcha2',
                              'dexa_mm', 'dexa_mg', 'dexa_pg', 'dexa_bmc',
                              'pergunta_1', 'pergunta_2', 'pergunta_3', 'pergunta_4', 'pergunta_5']]
listanomes_geral = avaliacoes['nome'].unique().astype(str)


container2 = st.container()
data_exp = container2.expander('Prévia dos dados')
data_exp.dataframe(avaliacoes_exib, use_container_width=True)

updateuser = st.container()
data_exib = updateuser.date_input('Data da medição', min_value=date.today(), key='data medida', disabled=True)
data_medida = data_exib.strftime("%d/%m/%y")
update_nome = updateuser.selectbox('Selecionar Nome', listanomes_geral)
nomeselecionado = avaliacoes.loc[avaliacoes['nome'] == update_nome]
idade_value = nomeselecionado['idade'].values[0]
sexo_value = nomeselecionado['sexo'].values[0]
peso_value = nomeselecionado['peso'].values[0]
estatura_value = nomeselecionado['estatura'].values[0]
pcintura_value = nomeselecionado['p_cintura'].values[0]
pquadril_value = nomeselecionado['p_quadril'].values[0]
coxamed_value = nomeselecionado['p_coxamed'].values[0]
perna_value = nomeselecionado['p_perna'].values[0]
handgripD1_value = nomeselecionado['handgripD1'].values[0]
handgripE1_value = nomeselecionado['handgripE1'].values[0]
handgripD2_value = nomeselecionado['handgripD2'].values[0]
handgripE2_value = nomeselecionado['handgripE2'].values[0]
irvir1_value = datetime.strptime((nomeselecionado['irvir1'].values[0]), '%H:%M:%S.%f').time()
irvir2_value = datetime.strptime((nomeselecionado['irvir2'].values[0]), '%H:%M:%S.%f').time()
senlev1_value = nomeselecionado['senlev1'].values[0]
senlev2_value = nomeselecionado['senlev2'].values[0]
marcha1_value = datetime.strptime((nomeselecionado['marcha1'].values[0]), '%H:%M:%S.%f').time()
marcha2_value = datetime.strptime((nomeselecionado['marcha2'].values[0]), '%H:%M:%S.%f').time()
dexamm_value = nomeselecionado['dexa_mm'].values[0]
dexamg_value = nomeselecionado['dexa_mg'].values[0]
dexapg_value = nomeselecionado['dexa_pg'].values[0]
dexabmc_value = nomeselecionado['dexa_bmc'].values[0]
pergunta1_value = nomeselecionado['pergunta_1'].values[0]
pergunta2_value = nomeselecionado['pergunta_2'].values[0]
pergunta3_value = nomeselecionado['pergunta_3'].values[0]
pergunta4_value = nomeselecionado['pergunta_4'].values[0]
pergunta5_value = nomeselecionado['pergunta_5'].values[0]

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2 = updateuser.columns(2)
antropometria_label = col1.subheader('Antropometria')
antropometria_label2 = col2.subheader('-')
idade = col1.number_input('Idade', min_value=0, max_value=999, value=int(idade_value), key='idade input',
                          help='Idade em anos')
if sexo_value == 'Feminino':
    sexo_opt = col2.radio('Sexo', ['Feminino', 'Masculino'], horizontal=True, index=0)
elif sexo_value == 'Masculino':
    sexo_opt = col2.radio('Sexo', ['Feminino', 'Masculino'], horizontal=True, index=1)

peso = col1.number_input('Peso', min_value=0.00, max_value=999.99, value=float(peso_value), key='peso input', help='Peso em kg')
estatura = col2.number_input('Estatura', min_value=0.00, max_value=999.99, value=float(estatura_value), key='estatura input',
                             help='Estatura em cm')

colperi1, colperi2 = updateuser.columns(2)
perimetria_label = colperi1.subheader('Perimetros')
perimetria_label2 = colperi2.subheader('-')
pcintura = colperi1.number_input('Perímetro cintura', min_value=0.00, max_value=999.99, value=float(pcintura_value),
                                 key='pcintura input', help='Perímetro cintura em cm')
pquadril = colperi2.number_input('Perímetro quadril', min_value=0.00, max_value=999.99, value=float(pquadril_value),
                                 key='pquadril input', help='Perímetro quadril em cm')
coxamed = colperi1.number_input('Perímetro coxa média', min_value=0.00, max_value=999.99, value=float(coxamed_value),
                                key='coxamed input', help='Perímetro coxa média em cm')
perna = colperi2.number_input('Perímetro panturrilha', min_value=0.00, max_value=999.99, value=float(perna_value),
                              key='perna input', help='Perímetro panturrilha em cm')

coldexa1, coldexa2 = updateuser.columns(2)
dexa_label = coldexa1.subheader('Dados DEXA')
dexa_label2 = coldexa2.subheader('-')
dexamm = coldexa1.number_input('Massa Magra', min_value=0.000, max_value=999.999, value=float(dexamm_value),
                               key='mm input', help='Massa Magra em g')
dexamg = coldexa2.number_input('Massa Gorda', min_value=0.000, max_value=999.999, value=float(dexamg_value),
                               key='mg input', help='Massa Gorda em g')
dexapg = coldexa1.number_input('Massa ossea', min_value=0.00, max_value=999.99, value=float(dexapg_value),
                               key='pg input', help='Percentual de gordura (%)')
dexabmc = coldexa2.number_input('T-Score', min_value=-999.999, max_value=999.999, value=float(dexabmc_value),
                               key='bmc input', help='BMD (g/cm²)')

coltest1, coltest2 = updateuser.columns(2)
testes_label = coltest1.subheader('Testes')
testes_label2 = coltest2.subheader('-')
handgripD1 = coltest1.number_input('Handgrip mão direita 1', min_value=0.00, max_value=999.99, value=float(handgripD1_value),
                                   key='handgripD1 input', help='Handgrip em kg')
handgripE1 = coltest2.number_input('Handgrip mão esquerda 1', min_value=0.00, max_value=999.99, value=float(handgripE1_value),
                                   key='handgripE1 input', help='Handgrip em kg')
handgripD2 = coltest1.number_input('Handgrip mão direita 2', min_value=0.00, max_value=999.99, value=float(handgripD2_value),
                                   key='handgripD2 input', help='Handgrip em kg')
handgripE2 = coltest2.number_input('Handgrip mão esquerda 1', min_value=0.00, max_value=999.99, value=float(handgripE2_value),
                                   key='handgripE2 input', help='Handgrip em kg')
senlev1 = coltest1.number_input('Sentar e levantar 1', min_value=0, max_value=999, value=int(senlev1_value),
                                key='senlev1 input', help='N repeticoes em 30s')
senlev2 = coltest2.number_input('Sentar e levantar 2', min_value=0, max_value=999, value=int(senlev2_value),
                                key='senlev2 input', help='N repeticoes em 30s')
irvir1 = coltest1.slider('Ir e vir 1', value=time(irvir1_value.hour, irvir1_value.minute, irvir1_value.second, irvir1_value.microsecond),
                         key='irvir1 input', help='Ir e vir em ssms', min_value=time(0, 0, 0, 0),
                         max_value=time(0, 0, 59, 0), step=timedelta(milliseconds=1), format='ss:SS')
irvir2 = coltest2.slider('Ir e vir 2', value=time(irvir2_value.hour, irvir2_value.minute, irvir2_value.second, irvir2_value.microsecond),
                         key='irvir2 input', help='Ir e vir em ssms', min_value=time(0, 0, 0, 0),
                         max_value=time(0, 0, 59, 0), step=timedelta(milliseconds=1), format='ss:SS')
marcha1 = coltest1.slider('Marcha usual 1', value=time(marcha1_value.hour, marcha1_value.minute, marcha1_value.second, marcha1_value.microsecond),
                          key='marcha1 input', help='Marcha usual em ssms', min_value=time(0, 0, 0, 0),
                          max_value=time(0, 0, 59, 0), step=timedelta(milliseconds=1), format='ss:SS')
marcha2 = coltest2.slider('Marcha usual 2', value=time(marcha2_value.hour, marcha2_value.minute, marcha2_value.second, marcha2_value.microsecond),
                          key='marcha2 input', help='Marcha usual em ssms', min_value=time(0, 0, 0, 0),
                          max_value=time(0, 0, 59, 0), step=timedelta(milliseconds=1), format='ss:SS')


colperg1, colperg2 = updateuser.columns([100, 1])
perguntas_label = colperg1.subheader('Perguntas')
perguntas_label2 = colperg2.subheader('-')
if pergunta1_value == ' ':
    pergunta1_opt = colperg1.radio('Você está satisfeito com a vida?', [' ', 'Sim', 'Não'], horizontal=True, index=0)
elif pergunta1_value == 'Sim':
    pergunta1_opt = colperg1.radio('Você está satisfeito com a vida?', [' ', 'Sim', 'Não'], horizontal=True, index=1)
elif pergunta1_value == 'Não':
    pergunta1_opt = colperg1.radio('Você está satisfeito com a vida?', [' ', 'Sim', 'Não'], horizontal=True, index=2)

if pergunta2_value == ' ':
    pergunta2_opt = colperg1.radio('Você se aborrece facilmente?', [' ', 'Sim', 'Não'], horizontal=True, index=0)
elif pergunta2_value == 'Sim':
    pergunta2_opt = colperg1.radio('Você se aborrece facilmente?', [' ', 'Sim', 'Não'], horizontal=True, index=1)
elif pergunta2_value == 'Não':
    pergunta2_opt = colperg1.radio('Você se aborrece facilmente?', [' ', 'Sim', 'Não'], horizontal=True, index=2)

if pergunta3_value == ' ':
    pergunta3_opt = colperg1.radio('Você se sente desamparado(a)?', [' ', 'Sim', 'Não'], horizontal=True, index=0)
elif pergunta3_value == 'Sim':
    pergunta3_opt = colperg1.radio('Você se sente desamparado(a)?', [' ', 'Sim', 'Não'], horizontal=True, index=1)
elif pergunta3_value == 'Não':
    pergunta3_opt = colperg1.radio('Você se sente desamparado(a)?', [' ', 'Sim', 'Não'], horizontal=True, index=2)

if pergunta4_value == ' ':
    pergunta4_opt = colperg1.radio('Você prefere ficar em casa a sair e fazer coisas diferentes?', [' ', 'Sim', 'Não'],
                                   horizontal=True, index=0)
elif pergunta4_value == 'Sim':
    pergunta4_opt = colperg1.radio('Você prefere ficar em casa a sair e fazer coisas diferentes?', [' ', 'Sim', 'Não'],
                                   horizontal=True, index=1)
elif pergunta4_value == 'Não':
    pergunta4_opt = colperg1.radio('Você prefere ficar em casa a sair e fazer coisas diferentes?', [' ', 'Sim', 'Não'],
                                   horizontal=True, index=2)

if pergunta5_value == ' ':
    pergunta5_opt = colperg1.radio('Atualmente você se sente inútil?', [' ', 'Sim', 'Não'], horizontal=True, index=0)
elif pergunta5_value == 'Sim':
    pergunta5_opt = colperg1.radio('Atualmente você se sente inútil?', [' ', 'Sim', 'Não'], horizontal=True, index=1)
elif pergunta5_value == 'Não':
    pergunta5_opt = colperg1.radio('Atualmente você se sente inútil?', [' ', 'Sim', 'Não'], horizontal=True, index=2)


def salvaratualizacao():
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'data_medida'] = data_medida
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'idade'] = idade
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'peso'] = peso
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'estatura'] = estatura
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'p_cintura'] = pcintura
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'p_quadril'] = pquadril
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'p_coxamed'] = coxamed
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'p_perna'] = perna
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'handgripD1'] = handgripD1
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'handgripE1'] = handgripE1
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'handgripD2'] = handgripD2
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'handgripE2'] = handgripE2
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'irvir1'] = irvir1
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'irvir2'] = irvir2
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'senlev1'] = senlev1
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'senlev2'] = senlev2
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'marcha1'] = marcha1
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'marcha2'] = marcha2
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'dexa_mm'] = dexamm
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'dexa_mg'] = dexamg
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'dexa_pg'] = dexapg
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'dexa_bmc'] = dexabmc
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'pergunta_1'] = pergunta1_opt
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'pergunta_2'] = pergunta2_opt
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'pergunta_3'] = pergunta3_opt
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'pergunta_4'] = pergunta4_opt
    avaliacoes.loc[avaliacoes['nome'] == update_nome, 'pergunta_5'] = pergunta5_opt

    with pd.ExcelWriter('tables/db_avaliacoes.xlsx') as writer:
        avaliacoes.to_excel(writer, index=True)


updateuser.button('Salvar', on_click=salvaratualizacao)
