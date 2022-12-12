#판다스의 데이터프레임을, 웹화면으로 보여주는 방법

import streamlit as st
import pandas as pd

# UI 요소들을 처리하는 방법
# 버튼, 라디오버튼, 셀렉트 박스, 멀티셀렉트, 슬라이더
def main():
    
    st.title('아이리스 꽃 데이터')

    df=pd.read_csv('streamlit_data/iris.csv')
   
    st.dataframe(df)

    species = df['species'].unique()

    st.text('아이리스 꽃은'+species+'으로 되어있다.')

if __name__ == '__main__' :
    main()
