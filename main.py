import streamlit as st
from langchain-openai import ChatOpenAI
import os
#from streamlit.cli import main

# OpenAI API 키를 환경 변수에서 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API 키를 직접 설정하기
# OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"

if OPENAI_API_KEY is None:
    st.error("OpenAI API 키를 설정해야 합니다.")
else:
    llm = ChatOpenAI(OPENAI_API_KEY)

    st.title('시인')
    content = st.text_input("엔터로 주제어 입력")
    if st.button('시 작성'):
        with st.spinner("시 작성 중"):
            result = llm.predict(content + "에 대한 시를 써줘")
            st.write(result)

