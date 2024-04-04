import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

st.title('시인')

content = st.text_input("엔터로 주제어 입력")

if st.button('시 작성'):
    with st.spinner("시 작성 중"):
        result = llm.predict(content + "에 대한 시를 써줘")
        st.write(result)
