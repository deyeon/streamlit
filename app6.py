# 스트림릿 라이브러리를 사용하기 위한 임포트문 작성

import streamlit as st

#유저한테 데이터를 입력받는 방법

def main() :
    # 텍스트를 입력받는 방법
    name = st.text_input('이름을 입력하세요')

    st.title(name)

    name2 = st.text_input('이름 입력:!', max_chars=5)
    st.title(name2)

    message = st.text_area('매세지를 입력하세요',height=2)
    st.text(message)

    # 숫자를 입력받는 방법
    year=st.number_input("출생년도를 입력하세요",1000,3000)
    st.text(year)

    st.number_input('실수를 입력하세요',0.5,100.0,step=0.3)

    #날짜 입력받는 방법
    my_date=st.date_input('약속 잡는 방법')

    st.write(my_date)

    st.text(my_date.strftime('%Y년 %m월 %d일'))

    #시간 입력받는 방법
    my_time=st.time_input('약속 시간 선택')

    st.write(my_time)

    #비밀번호 입력받는 방법
    password=st.text_input('비밀번호 입력',type='password')

    st.text(password)

    #색깔입력 
    st.color_picker("색깔을 입력")



if __name__ == '__main__' :
    main()