
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from openai import OpenAI

#
chat_model = ChatOpenAI(model_name='gpt-3.5-turbo',
                        api_key = st.secrets["OPENAI_API_KEY"],
                        temperature = 0.5
)

prompt = PromptTemplate(input_variables = ["chat_history", "question"],
                        template = """You are a AI assistant.
                                      You are currently haing a conversation with a human.
                                      Answer the Question.
                                      chat_history : {chat_history},
                                      Human : {question},
                                      AI assistant : 
                                      """
                       )

# 일반적인 코드에서는 memory객체를 생성하면 대화 내용들을 자동으로 기억하지만 
# streamlit에서는 웹에서 요청, 답을 수행하기 때문에 따로 지정해두지 않으면 다 초기화 됨

# session_state : 딕셔너리와 유사한 구조로 모든 자료형 및 객체를 지정할 수 있고 []외에 .으로도 key에 접근 가능
#                  앱을 재실행해도 사용자 입력이나 계산결과 등 변수의 상태를 지속적으로 관리해야 할 때 사용함


# 처음부터 지정하지 않고 not in을 쓰는 이유는 코드 재실행 시 지정된 값이 초기화 되는 것을 방지하기 위함
if "pre_memory" not in st.session_state:
    st.session_state.pre_memory = ConversationBufferMemory(memory_key="chat_history",
                                                           return_messages=True
                                                          )

llm_chain = LLMChain(llm=chat_model,
                     prompt=prompt,
                     memory=st.session_state.pre_memory # CBMemory객체가 입력 됨
                    )

# LLM에 요청하고 응답받을 수 있는 chat형태로 messages를 관리
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role" : "assistant", "content" : "안녕하세요 저는 AI Assistant입니다."}
    ]

# ------------------------ 웹표시 부분 -----------------------------------
st.title("나의 작고 소중한 GPT 챗봇😊")

# 반복문으로 session_state.messages에 있는 모든 대화 기록에 접근
for message in st.session_state.messages:
    # chat_message : 메세지의 발신자 role(assistant, user)에 따라 UI를 구분하여 출력
    #                assistant, user는 디폴트로 설정되어 있으며 다른 role을 추가하려면 html 코드 작성이 필요
    with st.chat_message(message["role"]):
        st.write(message["content"])

# chat_input : 채팅메세지 입력 UI가 생성되며 사용자가 입력한 텍스트를 받아오는 함수
user_prompt = st.chat_input()

# 사용자가 텍스트를 입력한다면!
if user_prompt is not None:
    st.session_state.messages.append({"role" : "user", "content" : user_prompt})
    with st.chat_message("user"):  # user형태로 메세지 창 UI 출력
        st.write(user_prompt)      # 사용자가 입력한 질문 출력

# 마지막 메세지의 role이 assistant가 아니라면 새로운 답변을 생성하고 session_state에 추가
# (assistant가 본인의 응답에도 계속 대답하는 자문자답을 방지하기 위함)
if st.session_state.messages[-1]["role"] != "assistant" :
    # assistant 메세지 UI 생성
    with st.chat_message("assistant") :
        # 
        with st.spinner("Loading..") :
            try :
                ai_response = llm_chain.predict(question=user_prompt)
                st.write(ai_response)
                # 모델의 응답도 세션의 messages에 추가하여 관리
                st.session_state.messages.append({"role" : "assistant", "content" : ai_response})
            except Exception as e:
                st.error(f"LLM 에러 발생 : {e}")

                 
#------------------------------------------------------------------------
