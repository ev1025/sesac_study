import streamlit as st

def happy_project():
    st.text('[태블로 시각화]')
    st.title('네이버지도 크롤링을 이용한 강아지 행복 지도')
    st.link_button("Github", "https://github.com/ev1025/happy_dog_map")


    tabs = st.tabs(["Summary","EDA", "Model Training", "Model Evaluation", 'Result'])

    with tabs[0]:   
        st.write('개요')
    
    with tabs[1]:   
        st.write('전처리')

    with tabs[2]:
        st.write('모델 훈련')

    with tabs[3]:
        st.write('모델 평가')

    with tabs[4]:
        st.write('훈련 결과')

