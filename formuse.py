import streamlit as st
#from langchain.chat_models import ChatOpenAI

def form_use():
    langlist = ["Q1. ", "Q2. ", "Q3. "]
    asdf = ["asdfghjklzxcvbnmqwertyu"]
    submit_button = st.form_submit_button(label="채점")
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

            for a in range(n):
                if a == (n-1):  # 마지막 반복일 때
                    if submit_button:
                        st.write("수고하셨습니다")
            break  # 반복 종료
    else:
        if st.button("풀이"):  # "풀이" 버튼이 클릭되면
            print(asdf)
            if st.button("다음 문제"):  # "다음 문제" 버튼을 띄워줌
                continue  # 다음 반복문으로 넘어감
        elif st.button("다음 문제"):  # "다음 문제" 버튼이 클릭되면
            continue  # 다음 반복문으로 넘어감


if __name__ == "__form_use()__":
    form_use()
