
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from openai import OpenAI

# -------------------------- 사전 설정 ------------------------------
# 질의가 적저한 콘텐츠인지 확인하는 사용자 정의 함수(moderation 적용 모델)
def moderate_message(message):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.moderations.create(model="text-moderation-latest",
                                        input=message
                                        )
    moderation_result = response.results[0]

    # 메세지가 유해하다고 판단되는 경우(flagged가 True인 경우!)
    if moderation_result.flagged :
        category_type = dict(moderation_result.categories)            # 딕셔너리 변환
        categories = [i for i,j in category_type.items() if j==True]  # 딕셔너리에서 True값 추출
        return False, categories
        
    return True, None
    # None은 없어도 되지만 return이 여러개인 경우 반환 값의 크기를 맞춰주는 것


# LLMChain 클래스를 상속받은 사용자 정의 클래스인 ModeratedLLMChain 선언
# LLMChain 내부에서 Moderation을 지원하지 않기 때문에 상속 받아서 추가코드 작성)
class ModeratedLLMChain(LLMChain) :
    # 전달 메세지가 적절한지 확인하기 위해 moderate_message함수를 호출하고 응답 생성 및
    # 상황에 따른 출력 문구 작성
    def moderate_and_generate(self, user_input):
        # 사용자의 정의에 대한 Moderation
        is_safe, categories = moderate_message(user_input)

        # moderate_message결과로 유해하다고 판단되면 is_safe에 False값 반환
        # 즉, 유해하다고 판단이 된다면 아래 조건문 실행
        if not is_safe:
            st.write(f"사용자의 메세지가 부적절하여 차단되었습니다.😒 : {categories}")
            return "" # return값이 없으면 None이 화면에 출력되기 때문에 이를 방지하기 위한 코드

        # 상속받은 LLMChain클래스의 predict 메소드로 응답 실행
        response = self.predict(question=user_input)

        # 모델 응답에 대한 Moderation
        is_safe_ai, categories_ai = moderate_message(response)
        if not is_safe_ai:
            st.write(f"AI의 응답이 부적절하여 차단되었습니다.😒 : {categories}")
            return " "
            
        return response

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

if "pre_memory" not in st.session_state:
    st.session_state.pre_memory = ConversationBufferMemory(memory_key="chat_history",
                                                           return_messages=True
                                                          )

# 위에서 정의한 클래스
moderated_chain = ModeratedLLMChain(llm=chat_model,
                                    prompt=prompt,
                                    memory=st.session_state.pre_memory # CBMemory객체가 입력 됨
                                   )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role" : "assistant", "content" : "안녕하세요 저는 좀 더 향상된 AI Assistant입니다."}
    ]

# ------------------------ 웹표시 부분 -----------------------------------
st.title("나의 작고 소중한 GPT 챗봇😊")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role" : "user", "content" : user_prompt})
    with st.chat_message("user"):  # user형태로 메세지 창 UI 출력
        st.write(user_prompt)      # 사용자가 입력한 질문 출력


if st.session_state.messages[-1]["role"] != "assistant" :
    # assistant 메세지 UI 생성
    with st.chat_message("assistant") :
        # 
        with st.spinner("Loading..") :
            try :
                ai_response = moderated_chain.moderate_and_generate(user_prompt) # 클래스에서 가져오기
                st.write(ai_response)
                st.session_state.messages.append({"role" : "assistant", "content" : ai_response})
            except Exception as e:
                st.error(f"LLM 에러 발생 : {e}")

#------------------------------------------------------------------------
