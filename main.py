# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = "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"

llm = ChatOpenAI(OPENAI_API_KEY)

"""prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a poet."),
    ("user", "{input}")
])

"""
content = st.text_input("엔터로 주제어 입력")
#output_parser = StrOutputParser()

#chain = prompt | llm | output_parser
st.title('시인')

if st.button('시 작성'):
    result = llm.predict(content + "에 대한 시를 써줘")
    st.write('result')













# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

unsafe_allow_html=True)

st.title("uploading Files")
st.markdown("---")
images=st.file_uploader("Please upload an image", type=["png", "jpg"], accept_multiple)
if images is not None:
    for image in images:
        st.image(image)

val=st.text_input("엔터로 시의 주제를 입력해주세요.", max_chars=50)
#slider("This is slider", min_value=50, max_value=150, value=70)
"""


