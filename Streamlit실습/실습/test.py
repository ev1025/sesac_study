# 경로 /Desktop/새싹 코드/Streamlit실습
# 터미널 경로 맞추고 streamlit run main.py

import streamlit as st
import pandas as pd

# ------------- 1. streamlit 설치 ----------------------
# 앱 제목 설정
st.title('첫 번째 Streamlit 앱')
# 텍스트 출력
st.write('안녕하세요! Streamlit입니다.')
st.write('오늘은 스트림릿을 배울거에요.')
# 이미지 출력
st.image('streamlit_logo.png', width=200)
# 데이터 프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]}
df = pd.DataFrame(data)
# 데이터 프레임 출력
st.dataframe(df)
# 막대 그래프 생성
st.bar_chart(df['age'])



"""
데이터프레임 생성
"""

st.title('데이터 프레임 튜토리얼')

data ={
    'first_column' : [1,2,3,4],
    'second column' : [10,20,30,40]
}
df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.table(df)

# value = 값, delta = 변화율
st.metric(label = '온도', value='10C', delta='1.2C')
st.metric(label = '삼성전자', value='61,000원', delta ='-12.00원')
st.metric(label = '일본jpy(100엔)', value = '958.63 원', delta = "-7.44 원")

# 합쳐서 한 줄에 표현하기
col1, col2, col3 = st.columns(3)
col1.metric(label = '달러USD', value='1,228 원', delta='-12.00 원')
col2.metric(label = '일본JPY(100엔)', value = '958.63원', delta = "-7.44원")
col3.metric(label = '유럽연함EUR', value = '1,335.82 원', delta = '11.44원')





"""
마크다운사용
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# 한글 폰트 설정 (전역)
plt.rcParams['font.family'] = 'Malgun Gothic'
# 마이너스 폰트 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
# 앱 제목 설정
st.title("첫 번째 Streamlit 앱")
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'Emma'],
        'age': [30, 25, 22, 21],
        'gender': ['Female', 'Male', 'Male', 'Female']}
df = pd.DataFrame(data)
# 데이터 프레임 출력
st.dataframe(df)
# 데이터 프레임 정렬
sorted_df = df.sort_values(by="age")
# 데이터 프레임 집계
average_age = sorted_df["age"].mean()
st.write("")
# 정렬된 데이터 프레임 출력
st.write('정렬된 데이터 프레임')
st.dataframe(sorted_df)
# 평균 연령 출력
# unsafe_allow_html=True HTML을 작성할 수 있게 함
st.write("평균 연령:", round(average_age, 4))
st.markdown(
    f"""
    <h1 style='font-size:32px; color:white;'>
        평균 연령: <span style='color:yellow;'>{round(average_age, 4)}</span>
    </h1>
    """,
    unsafe_allow_html=True
)
# 성별별 연령 분포 그래프
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="gender", y="age", ci=None, palette="Set2")
plt.xlabel("성별")
plt.ylabel("나이")
plt.title("성별별 평균 연령 분포")
st.pyplot(plt)


"""
폰트 조절

"""

import streamlit as st
# 타이틀 적용 예시
st.title('이것은 타이틀 입니다.')
# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :선글라스:')
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