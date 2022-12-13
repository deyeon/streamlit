# 스트림릿 라이브러리를 사용하기 위한 임포트문 작성
import streamlit as st
import numpy as np
import pandas as pd
#plotly 라이브러리
import plotly.express as px

#altair 라이브러리
import altair as alt

def main() :
    df = pd.read_csv('streamlit_data/lang_data.csv')

    st.dataframe(df.head())

    column_menu= df.columns[1:]

    choice_list=st.multiselect('프로그래밍 언어를 선택하세요',column_menu)

    if len(choice_list) != 0:
        #유저가 선택한 언어만, 차트를 그린다.
        df_selected = df[choice_list]

        ##스트림릿에서 제공하는 라인차트
        st.line_chart(df_selected)

        ##스트림릿에서 제공하는 영역차트
        st.area_chart(df_selected)

        ##스트림릿에서 제공하는 바차트
        st.bar_chart(df_selected)

        df2 = pd.read_csv('streamlit_data/iris.csv')

        ### altair 라이브러리 mark_cicle 함수 사용법
        chart=alt.Chart(df2).mark_circle().encode(
            x='petal_length',
            y='petal_width',
            color = 'species'
        )
        st.altair_chart(chart)

        ###위치 정보를 지도에 표시하는 방법
        ### 스트림릿의 map차트

    df3 = pd.read_csv('streamlit_data/location.csv')

    st.dataframe(df3.head(3))

    st.map(df3,zoom=5)

    df4 = pd.read_csv('streamlit_data/prog_languages_data.csv')

    st.dataframe(df4.head(3))

    ##plotly의 pie 차트 그리는 방법
    fig6 = px.pie(df4, 'lang','Sum',title='각 언어별 파이차트')
    st.plotly_chart(fig6)

    ##plotly의 bar차트 그리는 방법
    fig7 = px.bar(df4.sort_values('Sum',ascending=False),x='lang',y='Sum')
    st.plotly_chart(fig7)

if __name__ == '__main__' :
    main()
