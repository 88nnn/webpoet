import streamlit as st
from check import quiz_questions

# Display generated quiz
st.header("생성된 퀴즈")
for question in quiz_questions:
    st.write(question)

# Collect user answers
st.header("답변 입력")
user_answers = []
for i in range(len(quiz_questions)):
    user_answer = st.text_input(f"질문 {i+1}에 대한 답변 입력", "")
    user_answers.append(user_answer)
