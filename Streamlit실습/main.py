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