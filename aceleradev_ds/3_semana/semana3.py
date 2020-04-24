import streamlit as st
import pandas as pd
import base64
import altair as alt

def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y='count()', tooltip=[coluna, 'count()']
    ).interactive()
    return chart

def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width=600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()
    return bars

def criar_boxplot(coluna_num, coluna_cat, df):
    boxplot = alt.Chart(df, width=600).mark_boxplot().encode(
        x=coluna_num,
        y=coluna_cat
    )
    return boxplot


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.image('logo.png', width= 200)
    st.title('AceleraDev Data Science')
    st.subheader('Semana 3 - Análise de dados Exploratória')
    st.image('https://media.giphy.com/media/KyBX9ektgXWve/giphy.gif', width=200)
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        st.subheader('Estatística Descritiva Univariada')
        df = pd.read_csv(file)

        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])

        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])

        st.markdown('**Visualizando o dataframe**')
        number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
        st.dataframe(df.head(number))
        
        st.markdown('**Nome das colunas:**')
        st.markdown(list(df.columns))

        aux = pd.DataFrame({"colunas": df.columns, "tipos": df.dtypes})
        colunas_numericas = list(aux[aux["tipos"] != "object"]["colunas"])
        colunas_object = list(aux[aux["tipos"] == "object"]["colunas"])
        colunas = list(df.columns)
        col = st.selectbox('Selecione a coluna: ', colunas_numericas)
        if col is not None:
            st.markdown('Selecione o que deseja analisar: ')

            mean = st.checkbox('Média')
            if mean:
                st.markdown(df[col].mean())
            
            median = st.checkbox('Mediana')
            if median:
                st.markdown(df[col].median())

            desvio_pad = st.checkbox('Desvio padrão')
            if desvio_pad:
                st.markdown(df[col].std())

            kurtosis = st.checkbox('Kurtosis')
            if kurtosis:
                st.markdown(df[col].kurtosis())
            
            skewness = st.checkbox('Skewness')
            if skewness:
                st.markdown(df[col].skew())

            describe = st.checkbox('Describe')
            if describe:
                st.table(df['IDADE'].describe().transpose())

        st.subheader('Visualização dos Dados')
        st.image('https://i.kym-cdn.com/photos/images/original/001/333/670/35c.gif', width=200)
        st.markdown('Selecione a Visualização')

        histograma = st.checkbox('Histograma')
        if histograma:
            col_num = st.selectbox('Selecione a Coluna Numérica: ', colunas_numericas)
            st.markdown('Histograma da coluna: ' + str(col_num))
            st.write(criar_histograma(col_num, df))
        
        barras = st.checkbox('Gráfico de Barras')
        if barras:
            col_num_barras = st.selectbox('Selecione a Coluna numérica: ', colunas_numericas)
            col_cat_barras = st.selectbox('Selecione uma Coluna categórica: ', colunas_object)
            st.markdown('Gráfico de barras da coluna ' + str(col_cat_barras + ' pela coluna ' + col_num_barras))
            st.write(criar_barras(col_num_barras, col_cat_barras, df))

        boxplot = st.checkbox('Boxplot')
        if boxplot:
            col_num_box = st.selectbox('Selecione a Coluna numérica: ', colunas_numericas)
            col_cat_box = st.selectbox('Selecione uma Coluna categórica: ', colunas_object)    
            st.markdown('Boxplot ' + str(col_cat_box) + ' pela coluna ' + col_num_box)          
            st.write(criar_boxplot(col_num_box, col_cat_box, df)) 

if __name__ == '__main__':
	main()