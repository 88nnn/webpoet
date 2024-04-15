import streamlit as st
#from langchain.chat_models import ChatOpenAI

def form_use():
    langlist = ["Q1. ", "Q2. ", "Q3. "]
    asdf = ["asdfghjklzxcvbnmqwertyu"]
    n = 3

    st.title("AI 퀴즈")

    for a in range(n):
        with st.form(langlist[a], clear_on_submit=True):
            st.header((a+1)+"번 문제")
            st.write("문제 출력: ")
            st.subheader("답변 입력: ")
            user_answers = []
            for i in range(len(asdf)):
                user_answer = st.text_input(f"질문 {i + 1}에 대한 답변 입력", "")
                user_answers.append(user_answer)

            submit_button = st.form_submit_button(label="다음 문제")
            if st.button("풀이"):  # "풀이" 버튼이 클릭되면
                print(asdf)
                elif submit_button:
                    elif a == n-1:
                        return user_answer
            if submit_button:
                elif a == n-1:
                        return user_answer

if __name__ == "__main__":
    form_use()
