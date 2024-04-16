import streamlit as st
from langchain.chat_models import ChatOpenAI
from PIL import Image
import pytesseract
from PyPDF2 import PdfReader
import io

# ChatOpenAI 모델 초기화
chat_model = ChatOpenAI()

# 퀴즈 채점 함수
def grade_quiz_answers(user_answers, quiz_answers):
    graded_answers = []
    for user_answer, quiz_answer in zip(user_answers, quiz_answers):
        if user_answer.lower() == quiz_answer.lower():
            graded_answers.append("정답")
        else:
            graded_answers.append("오답")
    return graded_answers

# 파일 처리 함수
def process_file(uploaded_file):
    if uploaded_file is None:
        st.warning("파일을 업로드하세요.")
        return None

    # 업로드된 파일 처리
    if uploaded_file.type == "text/plain":
        text_content = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type.startswith("image/"):
        image = Image.open(uploaded_file)
        text_content = pytesseract.image_to_string(image)
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
    else:
        st.error("지원하지 않는 파일 형식입니다.")
        return None

    return text_content

# 퀴즈 생성 함수
def generate_quiz(quiz_type, text_content):
    # Generate quiz prompt based on selected quiz type
    if quiz_type == "다중 선택 (객관식)":
        prompt = "객관식 퀴즈를 생성합니다."
    elif quiz_type == "주관식":
        prompt = "주관식 퀴즈를 생성합니다."
    else:
        prompt = "OX 퀴즈를 생성합니다."

    prompt += f'''
    다음 텍스트를 기반으로 퀴즈를 생성합니다:

    {text_content}

    다양한 유형의 문제를 포함하여 퀴즈를 생성하세요. 객관식, 주관식, OX 퀴즈 등을 포함하여 참가자의 이해도와 지식 깊이를 테스트하세요.
    '''

    # Generate quizzes using ChatOpenAI model
    quiz_questions = chat_model.predict(prompt)

    # Convert quiz_questions to a list
    quiz_questions = quiz_questions.split("\n")

    return quiz_questions

# 메인 함수
def main():
    with st.form("AI 퀴즈 생성기", clear_on_submit=True):
        # 퀴즈 유형 선택
        quiz_type = st.radio("생성할 퀴즈 유형을 선택하세요:", ["다중 선택 (객관식)", "주관식", "OX 퀴즈"])

        # 파일 업로드 옵션
        st.header("파일 업로드")
        uploaded_file = st.file_uploader("텍스트, 이미지, 또는 PDF 파일을 업로드하세요.", type=["txt", "jpg", "jpeg", "png", "pdf"])

        text_content = process_file(uploaded_file)

        if text_content is not None:
            submit_button = st.form_submit_button(label="퀴즈 생성")
            if submit_button:
                with st.form("생성된 퀴즈", clear_on_submit=True):
                    quiz_questions = generate_quiz(quiz_type, text_content)
                    # Display generated quiz

                    for question in quiz_questions:
                        st.write(question)

                        # Collect user answers
                        st.header("답변 입력")
                        user_answers = []
                        for i in range(len(quiz_questions)):
                            user_answer = st.text_input(f"질문 {i + 1}에 대한 답변 입력", "")
                            user_answers.append(user_answer)
                        # Button to grade the quiz
                        checkbt = st.form_submit_button(label="채점")
                        if checkbt:  # Grade the quiz answers
                            quiz_answers = [answer.split(": ")[1] for answer in quiz_questions]
                            graded_answers = grade_quiz_answers(user_answers, quiz_answers)

                            # Display grading results
                            st.header("퀴즈 채점 결과")
                            for i, (question, user_answer, graded_answer) in enumerate(
                                    zip(quiz_questions, user_answers, graded_answers), start=1):
                                st.write(f"질문 {i}: {question}")
                                st.write(f"사용자 답변: {user_answer}")
                                st.write(f"채점 결과: {graded_answer}")

                                # Open a new window to show the quiz result

            

# 메인 함수 실행
if __name__ == "__main__":
    main()
