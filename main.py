
#from dotenv import load_dotenv
#load_dotenv()


#from streamlit.cli import main

# OpenAI API 키를 환경 변수에서 불러오기
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API 키를 직접 설정하기
# OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"


"""
from langchain_openai.llms import OpenAI
model = OpenAI()
word = input()
result = model.invoke(word+"에 대한 시를 써줘.")
print(result)
#from langchain_openai import ChatOpenAI
#llm = ChatOpenAI()
"""

# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
#from langchain_openai.llms import OpenAI

from langchain_openai.llms import ChatOpenAI


llm = ChatOpenAI

st.title('시인')
content = st.text_input("엔터로 주제어 입력")

if st.button('시 작성'):
    with st.spinner("시 작성 중"):
        result = llm.predict(content + "에 대한 시를 써줘")
        st.write(result)
