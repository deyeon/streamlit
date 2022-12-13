import streamlit as st
#다른 파일의 함수를 호출하고 싶으면, 함수를 임포트 한다.
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main() :
    st.title('파일 분리 앱')

    #Exploratory Data Analysis
    menu = ['Home','EDA','ML','About']


    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()
    elif choice == 'About':
        pass


if __name__ == '__main__' :
    main()