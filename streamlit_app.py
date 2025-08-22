import streamlit as st
import random

st.title("🎈 랜덤 대답 사이트")

answers = [
    "네",
    "아니요",
    "조금 더 생각해보세요.",
    "확실히 할 수 있어요.",
    "아직 결정 내릴 단계가 아닙니다.",
    "확실한가요?.",
    "냉면.",
    "큰 결심.",
    "주변에 위험한 사람이 있다.",
    "도망가라.",
    "넌 할 수 있어.",
    "잡아라.",
    "눈 조심해.",
    "아래.",
    "위.",
    "옆.",
    "뒤.",
    "사랑해.",
    "죽어라.",
    "때로는 쉬어가요.",
    "실패는 성공의 어머니.",
    "너 자신을 알라.",
    "오늘의 노력이 내일의 기적을 만든다.",
    "맛있겠다.",
    "짜장면",
    "브론즈",
    "실버",
    "챌린저"

]

if "answer" not in st.session_state:
    st.session_state["answer"] = ""

def generate_answer():
    question = st.session_state["question_input"].strip()
    if question != "":
        st.session_state["answer"] = random.choice(answers)
    else:
        st.session_state["answer"] = "질문을 입력해주세요."

# 질문 입력창에 on_change 활용
st.text_input("궁금한 점을 입력하세요", key="question_input", on_change=generate_answer, placeholder="여기에 질문을 써 주세요.")

# 질문하기 버튼도 동일 기능 (엔터 못 누르는 상황 대비)
if st.button("질문하기"):
    generate_answer()

# 대답칸 (크게)
if st.session_state["answer"]:
    st.markdown(
        f"<div style='font-size: 2em; font-weight: bold; color: #4169e1; margin: 30px 0;'>{st.session_state['answer']}</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<div style='height: 2em; margin: 30px 0;'></div>",  # 빈 공간 유지
        unsafe_allow_html=True
    )