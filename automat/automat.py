# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:17:13 2022

@author: tzielinski
"""

import streamlit as st
import pandas as pd
import openpyxl


st.set_page_config(page_title='Porównanie RKMH', page_icon = ':bar_chart:', layout='wide')

st.set_option('deprecation.showfileUploaderEncoding',False)

st.title('Wszystkie pliki')

st.sidebar.subheader('Dodawanie plików')

uploaded_file = st.sidebar.file_uploader(label='Wprowadź pliki', type=['xlsx'],accept_multiple_files=True)
uploaded_file1 = st.sidebar.file_uploader(label='Wprowadź plik z ostatniego miesiąca', type=['xlsx'])


global df, l, zl, df1, z1
#zl = pd.DataFrame()
l = []
if uploaded_file is not None:
    print(uploaded_file)
    try:
        for i in range(len(uploaded_file)):
            df = pd.read_excel(uploaded_file[i],usecols='C,K')
            l.append(df)
    except Exception as e:
        st.write(str(e))
        st.write('Złe rozszerzenie pliku. Może być tylko .xlsx!')
        

    try:
        st.subheader('Złączone pliki')
        zl = pd.concat(l,ignore_index=True)
        st.write(zl)
    except Exception as e:
        st.write('Czekam na dane')
        
    
    try:
        st.header('Unikatowi producenci i ich RKMH')
        z = zl.drop_duplicates('Producent',ignore_index=True)
        st.download_button(label = 'Pobierz plik', data = z.to_csv(index=False,encoding = 'utf-8'),file_name = 'Porównanie_IPRA.csv', mime = "text/csv")
        st.write(z)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')   
        
    if uploaded_file1 is not None:
        try:
            df1 = pd.read_excel(uploaded_file1,usecols='C,K')
        except Exception as e:
            print(e)
            st.write('Złe rozszerzenie pliku. Może być tylko .xlsx!')
            
    try:
        st.subheader('Plik z ostatniego miesiąca')
        st.write(df1)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')
        
    try:
        st.header('dane o producentach co byli, a nie ma ich w pliku z ostatniego miesiąca')
        z1 = z[~z['Producent'].isin(df1.Producent)].reset_index().iloc[:,1:3]
        st.download_button(label = 'Pobierz plik', data = z1.to_csv(index=False,encoding = 'utf-8'),file_name = 'Odeszli.csv', mime = "text/csv")
        st.write(z1)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')
    
    

