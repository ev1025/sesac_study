import streamlit as st
# 타이틀 적용 예시
st.title('이것은 타이틀 입니다.')
# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses:')
# Header 적용 (마크다운 헤더 개념)
st.header('헤더를 입력할 수 있어요! :반짝임:')
# SubHeader
st.subheader('이것은 subheader 입니다.')
# 캡션 적용
st.caption('캡션을 넣어 봤습니다.')
# 코드 표시
sample_code = '''
df function():
    print('hello, world')
'''
st.code(sample_code, language='python')
# 일반 텍스트
st.text('일반 텍스트를 입력해봤습니다.')
# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 구분선 생성
st.divider()