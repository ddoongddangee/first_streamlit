import streamlit as st
from quiz_data import load_questions

st.set_page_config(page_title="Style Test", page_icon="🥋")

st.title("🥋 주짓수 스타일 테스트")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("로그인 후 이용할 수 있습니다.")
    st.stop()

questions = load_questions()

st.write("각 상황에서 본인과 가장 가까운 선택지를 고르세요.")

scores = {
    "pressure": 0,
    "speed": 0,
    "leglock": 0,
    "backtake": 0
}

with st.form("style_test_form"):
    answers = []

    for i, q in enumerate(questions):
        st.subheader(q["question"])

        selected = st.radio(
            label="선택지",
            options=list(q["options"].keys()),
            key=f"question_{i}"
        )

        answers.append(q["options"][selected])

    submitted = st.form_submit_button("결과 확인하기")

if submitted:
    for answer in answers:
        scores[answer] += 1

    result_style = max(scores, key=scores.get)

    st.session_state.scores = scores
    st.session_state.result_style = result_style

    st.success("테스트가 완료되었습니다!")
    st.write("왼쪽 사이드바에서 **Result 페이지**로 이동해 결과를 확인하세요.")

    st.subheader("점수 요약")
    st.write(scores)