import streamlit as st
import pandas as pd

def main():
    st.title('Hello World')

    st.markdown('Botão')
    botao = st.button('Botão')
    if botao:
        st.markdown('Clicado')

    st.markdown('Checkbox')   
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicado')

    st.markdown('Radio')
    radio= st.radio('Escolha as opções', ('Opt1', 'Opt2'))
    if radio == 'Opt1':
        st.markdown('Opt1')
    else:
        st.markdown('Opt2')

    st.markdown('SelextBox')
    select = st.selectbox('Escolha as opções', ('Opt1', 'Opt2'))
    if select == 'Opt1':
        st.markdown('Opt1')
    else:
        st.markdown('Opt2')

    st.markdown('Multi')
    multi = st.multiselect('Escolha as opções', ('Opt1', 'Opt2'))
    if multi == 'Opt1':
        st.markdown('Opt1')
    else:
        st.markdown('Opt2')
    if multi == 'Opt1' and multi == 'Opt2':
        st.markdown('Todas opções setadas')

    st.markdown('File Uploader')
    file = st.file_uploader('Escolha o seu arquivo', type= 'csv')
    if file is not None:
        st.markdown('Não está vazio!!!!') 


    
if __name__ == '__main__':
    main()
