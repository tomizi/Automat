# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:17:13 2022

@author: tzielinski
"""

import streamlit as st
import pandas as pd
import plotly_express as px

st.set_option('deprecation.showfileUploaderEncoding',False)

st.title('Wizualizacja danych')

st.sidebar.subheader('Ustawienia')

st.sidebar.file_uploader(label='Wprwadź pliki', type=['csv','xlsx'], accept_multiple_files)

global df
if uploaded_file is not None:
    print(uploaded_file)
    print('hello')
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
        
st.write(df)
try:
    st.write(df)
except Exception as e:
    print(e)
    str.write('Odswież plik')