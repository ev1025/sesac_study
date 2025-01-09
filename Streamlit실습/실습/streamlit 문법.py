# 경로로 이동 /Desktop/새싹 코드/Streamlit실습
# 터미널 경로 맞추고 streamlit run main.py


# """ 
# 출력 
# """

import streamlit as st
import pandas as pd

# 제목표시줄 이름, 아이콘(무조건 제일 위에 넣을 것)
st.set_page_config(page_title = "홈페이지",
                   page_icon = ":sunglasses")

st.markdown('# 출력')

st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.caption('캡션')

# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')

# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(':sunglasses:')

# 구분선 생성
st.divider()

# 모두 문자 형태로 출력
st.text(1234)
st.text(True)
st.text({'test':1})

# 타입에 맞춰서 출력
st.write(123)
st.write(True)
st.write({'test' : 1})

# 이미지 출력
st.image('streamlit_logo.png', width=200)

# 함수 리턴값 출력(변수에 넣어서 실행시켜줘야 됨)
def get_user_name():
    return 'John'

greeting = 'Hi'
user_name = get_user_name()

st.write(greeting, user_name)


# 코드만 출력
sample_code = '''
df function():
    print('hello, world')
'''
st.code(sample_code, language='python')

# 코드 + 실행값 출력
def get_user_name():
    return 'John'

with st.echo():
    def get_punctuation():
        return '!!!'

    greeting = 'Hi there'
    user_name = get_user_name()
    punctuation = get_punctuation()

    st.write('이 윗 부분의 함수 정의부는 화면에 출력되지 않습니다.')
    st.write(greeting, user_name, punctuation)




st.divider()
# """
# 표출력
# """
st.markdown('# 표')

data ={
    'first_column' : [1,2,3,4],
    'second column' : [10,20,30,40]
}
df = pd.DataFrame(data)

# dataframe : 상호작용 가능
# use_container_width 표 사이즈 자동 조정
st.dataframe(df, use_container_width=True)

# table : 상호작용 불가
st.table(df)




st.divider()
# """
# 개체 생성
# """
st.markdown('# 개체')

# value = 값, delta = 변화율
st.metric(label = '온도', value='10C', delta='1.2C')
st.metric(label = '삼성전자', value='61,000원', delta ='-12.00원')
st.metric(label = '일본jpy(100엔)', value = '958.63 원', delta = "-7.44 원")

# 합쳐서 한 줄에 표현하기
col1, col2, col3 = st.columns(3)
col1.metric(label = '달러USD', value='1,228 원', delta='-12.00 원')
col2.metric(label = '일본JPY(100엔)', value = '958.63원', delta = "-7.44원")
col3.metric(label = '유럽연함EUR', value = '1,335.82 원', delta = '11.44원')





st.divider()
# """
# 그래프
# """
st.markdown('# 그래프')

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (전역)
plt.rcParams['font.family'] = 'Malgun Gothic'
# 마이너스 폰트 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'Emma'],
        'age': [30, 25, 22, 21],
        'gender': ['Female', 'Male', 'Male', 'Female']}
df = pd.DataFrame(data)

# 막대 그래프 생성
st.bar_chart(df['age'])

"""----------------------------------------------------------------------------------------------"""

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





st.divider()
# """
# 슬라이더
# """
st.markdown('# 슬라이더')

import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 슬라이더 생성
age_range = (18, 65)
selected_age = st.slider("나이 선택:",  # 라벨
                         age_range[0], # 시작값
                         age_range[1]) # 끝값

# 선택된 값 출력
st.write("선택된 나이:", selected_age)
# 데이터 불러오기
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 22]}

df = pd.DataFrame(data)

# 조건부 실행
if  selected_age in df["age"].values:
    st.dataframe(df[df['age']==selected_age])
else:
    st.write(f"{selected_age}살에 대한 데이터는 존재하지 않습니다.")
st.divider()


"""------------------------------------------------------"""

# 슬라이더
st.slider("날짜 슬라이더", # 라벨
          min_value = datetime(2024,1,1),    # 시작값
          max_value = datetime(2024,12,31),  # 끝값
          value=(datetime(2024,3,1),datetime(2024,4,1)))  # 기본값


#
# 파일 업로더
#
st.markdown('# 파일업로더')

file = st.file_uploader("파일 선택(csv or excel)",     # 라벨
                       type = ['csv', 'xls', 'xlsx'])  # 업로드 확장자(화면에도 표시됨)

# 업로드된 파일 띄우기
if file is not None:
    ext = file.name.split('.')[-1] # 파일이 있으면, 파일 이름 뒤의 확장자 가져오기
    if ext == 'csv':
        df = pd.read_csv(file) 
    elif 'xls' in ext:
        df = pd.read_excel(file, engine='openpyxl')
    st.dataframe(df)






st.divider()
#
# 라디오 버튼
#
st.markdown('# 라디오 버튼')
import streamlit as st

#
st.title('라디오 버튼 페이지')

# 라디오버튼 만들기
add_radio = st.radio(
    "Choose a shipping method",
    ("Standar (5-15 days)","Express (205 days)")
)

st.write(f"당신은 \"{add_radio}\"를 선택하셨습니다.")
st.write("안녕하세요! 이곳은 홈페이지입니다.")





st.divider()
#
# 세션
#
st.markdown('# 세션')
import streamlit as st
import uuid

# 세션 ID 생성 및 유지
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())  # 고유 세션 ID 생성

# 일반 변수와 세션 상태 변수 비교
if "normal_counter" not in st.session_state:
    normal_counter = 0  # 일반 변수 초기화
if "session_counter" not in st.session_state:
    st.session_state["session_counter"] = 0  # 세션 상태 변수 초기화

# 버튼 생성
increment_normal = st.button("일반 변수 증가")
increment_session = st.button("세션 상태 증가")

# 각 버튼 누르면 +1
if increment_normal:
    normal_counter += 1
if increment_session:
    st.session_state["session_counter"] += 1


# 출력
st.write("### 일반 변수 카운터 (normal_counter)")
st.write(f"Normal Counter: {locals().get('normal_counter', 0)}")
st.write("### 세션 상태 카운터 (st.session_state)")
st.write(f"Session State Counter: {st.session_state['session_counter']}")
st.write("### 일반 변수와 세션 상태 차이점")
st.write("""
1. **일반 변수**: 앱이 매번 재실행될 때마다 초기화됩니다. 버튼 클릭 후에도 값이 저장되지 않고 사라집니다.
2. **세션 상태 (`st.session_state`)**: 앱이 재실행되어도 같은 세션 내에서 값을 유지합니다. 버튼을 클릭하면 이전 값이 유지되며 계속 증가합니다.
""")

# 세션 스테이트 확인
st.write(st.session_state)




st.divider()
#
# 탭 만들기
#
st.markdown("# 탭 만들기")

import streamlit as st

st.title('머신러닝 프로젝트')

tab_titles = ['데이터 전처리', '모델 훈련', '모델 평가', '결과 시각화']
tabs = st.tabs(tab_titles)

with tabs[0]:
    st.header('데이터 전처리')
    st.write('데이터 전처리를 수행하는 곳입니다.')

with tabs[1]:
    st.header('모델 훈련')
    st.write('모델 훈련을 하는 곳입니다.')

with tabs[2]:
    st.header('모델 평가')
    st.write('모델을 평가하는 곳입니다.')

with tabs[3]:
    st.header('모델 시각화')
    st.write('모델을 시각화하는 곳입니다.')


st.divider()
#
# 시각화
#
st.markdown('# 시각화 고도화')

import streamlit as st
import pandas as pd
import time
# 앱 제목
st.title("My Interactive Dashboard")
# 세션 상태 초기화
for key, value in {
    "data": [],
    "message": None,
    "message_time": None,
    "current_name": "",
    "current_age": 0,
    "current_score": 0.0,
}.items():
    if key not in st.session_state:
        st.session_state[key] = value
# 데이터 추가 함수
def add_data():
    if (st.session_state.current_name and
    st.session_state.current_age > 0 and
    st.session_state.current_score > 0):
        new_entry = {
            "Name": st.session_state.current_name,
            "Age": st.session_state.current_age,
            "Score": st.session_state.current_score,
        }
        st.session_state.data.append(new_entry)
        st.session_state.message = f"Data Added: {new_entry}"
    else:
        st.session_state.message = "Please fill all fields correctly!"
    st.session_state.message_time = time.time()
    st.session_state.current_name, st.session_state.current_age, st.session_state.current_score = "", 0, 0.0
# 메시지 초기화 함수
def clear_message():
    if (st.session_state.message and
        time.time() - st.session_state.message_time > 3):
        st.session_state.message, st.session_state.message_time = None, None
# 탭 생성
tabs = st.tabs(["User Inputs",
                "Data Display",
                "Data Analysis"])
# 1. User Inputs 탭
with tabs[0]:
    st.header("User Inputs")
    st.text_input("Enter Name", key="current_name")
    st.number_input("Enter Age", min_value=0, max_value=120, step=1, key="current_age")
    st.number_input("Enter Score", min_value=0.0, max_value=100.0, step=0.1, key="current_score")
    st.button("Add Data", on_click=add_data)
    if st.session_state.message:
        st.success(st.session_state.message)
        clear_message()
# 2. Data Display 탭
with tabs[1]:
    st.header("Data Display")
    if st.session_state.data:
        st.table(pd.DataFrame(st.session_state.data))
    else:
        st.write("No data available. Please add data in the 'User Inputs' tab.")
# 3. Data Analysis 탭
with tabs[2]:
    st.header("Data Analysis")
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        # 나이와 점수 구간화
        bins_age = list(range(0, 130, 10))  # 나이 구간: 0-9, 10-19, ...
        bins_score = list(range(0, 110, 10))  # 점수 구간: 0-9, 10-19, ...
        df["Age Group"] = pd.cut(df["Age"], bins=bins_age, right=False, labels=[f"{i}-{i+9}" for i in bins_age[:-1]])
        df["Score Group"] = pd.cut(df["Score"], bins=bins_score, right=False, labels=[f"{i}-{i+9}" for i in bins_score[:-1]])
        # 사용자 선택: Age 또는 Score
        option = st.selectbox("Select Data to Analyze", ["Age", "Score"])
        if option == "Age":
            # 나이대별 카운트
            age_counts = df["Age Group"].value_counts(sort=False)
            st.subheader("Age Group Counts")
            st.bar_chart(age_counts)
        elif option == "Score":
            # 점수 구간별 카운트
            score_counts = df["Score Group"].value_counts(sort=False)
            st.subheader("Score Group Counts")
            st.bar_chart(score_counts)
    else:
        st.write("No data available. Please add data in the 'User Inputs' tab.")





st.divider()
#
# 다른 파일 실행 시키기(같은 경로의 파일)
#

st.markdown('# 같은 경로의 다른 파일 실행시키기')

import streamlit as st
import subprocess

if st.button("다른 Python 파일 실행"):
    result = subprocess.run(['python',         # 파이썬인
                             'other.py'],      # 해당 파일을
                             capture_output=True, text=True)
    st.write('### 실행 결과')
    st.write(result.stdout) # 실행결과 출력

    if result.stderr:
        st.write("### 에러")
        st.write(result.stderr)



