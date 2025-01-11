import streamlit as st

# 상단 네비게이션탭
tabs = st.tabs(["EDA", "Model Training", "Model evaluation", 'Result'])

with tabs[0]:   
    st.write('전처리')

with tabs[1]:
    st.write('모델 훈련')

with tabs[2]:
    st.write('모델 평가')

with tabs[3]:
    st.write('훈련 결과')
