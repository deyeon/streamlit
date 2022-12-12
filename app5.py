import streamlit as st

# 웹 대시보드 프레임워크인, 스트림릿은
# main 함수가 있어야 한다.
# 웹 대시보드에 이미지파일, 동영상 파일 넣는 방법

#이미지 처리를 위한 라이브러리
from PIL import Image


def main() :
    
    #이미지 올리는법

    img = Image.open('streamlit_data/image_03.jpg')
    print(img)

    st.image(img)

    st.image(img, use_column_width=True)

    img_url='https://imgnews.pstatic.net/image/018/2022/12/12/0005385617_001_20221212154901076.jpg?type=w647'

    st.image (img_url)
    
    #영상 올리는법

    video_file=open('streamlit_data/secret_of_success.mp4','rb')
    
    st.video(video_file)

if __name__ == '__main__' :
    print(__name__)
    main()