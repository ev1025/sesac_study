import streamlit as st
st.set_page_config(page_title = "이진우 포트폴리오입니다.", page_icon = ":sunglasses:")

from state import initialize_state
from project import intro, alter_credit, math_teacher, happy_dog_map, certi, resume

# cd desktop/sesac_study/포트폴리오

# 네비게이션 로고, 기본 로고
st.logo("images/horizontal_blue.png", 
        icon_image="images/icon_blue.png")

# 연도, 상단 탭 CSS
css = '''
<style>
    .stElementContainer {
    display: flex;
    justify-content: flex-end; /* 연도 오른쪽 정렬*/
    }

    .stButtonGroup [data-baseweb="button-group"] button [data-testid="stMarkdownContainer"] p {
    font-size: 20px;         /* 텍스트 크기 조정 */
    font-weight: light;      /* 텍스트 굵기 조정 */
    padding: 12px 0px;       /* 버튼의 패딩 조정 */
    height: 60px;            /* 버튼의 높이 */
    width : 50px;
    }

    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.3rem; /* 연도 크기 조정 */
    font-wegiht:bold;
    }


    /* 사이드바 섹션 헤더 스타일링 */
    [data-testid="stNavSectionHeader"] {
        font-size: 1.3rem;
        color: #333;

    }

    /* 사이드바 링크 텍스트 스타일링 */
    .st-emotion-cache-6tkfeg {
        font-size: 1.1rem;
        font-weight: 400;
    }

    /* 활성화된 링크 스타일링 */
    .st-emotion-cache-xtjyj5 {
        font-size: 1.1rem;
        display: flex;
        color: #272727;
    }

    /* 활성화된 링크 내부 아이콘 스타일링 */
    .st-emotion-cache-xtjyj5 svg {
        flex-shrink: 0;
        position: static;
    }


</style>
'''
st.markdown(css, unsafe_allow_html=True)

# state 초기화 / 연도 생성 / 네비게이션 생성
initialize_state()
options = ["2023", "2024", "2025"]
year = st.pills("", options, selection_mode="single", default="2025")


# 자기 소개
intro = st.Page("project/intro.py", title="소개", icon=":material/person:", default=True)
resume = st.Page("project/resume.py", title="이력사항", icon=":material/lab_profile:")
certi = st.Page("project/certi.py", title="경력사항", icon=":material/license:")


# 프로젝트
alter_credit_scording = st.Page("project/alter_credit.py", title="대안 신용 평가", icon=":material/dashboard:")
math_teacher = st.Page("project/math_teacher.py", title="나만의 수학 선생님 만들기", icon=":material/bug_report:")
happy_dog_map = st.Page("project/happy_dog_map.py", title="강아지 행복 지도", icon=":material/notification_important:")

project_list = {
"2025": [alter_credit_scording],
"2024": [math_teacher],
"2023": [happy_dog_map],
}

# page_dict 생성
page_dict = {
    "자기소개": [intro, resume, certi, ],
    f"{year}년 프로젝트": project_list.get(year, []),  # year에 해당하는 프로젝트만 선택
}

page = st.navigation(page_dict,)
page.run()
