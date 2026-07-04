import streamlit as st
from quiz_data import compute_style_code, load_questions

st.set_page_config(page_title="Style Test", page_icon="🥊")

st.title("🥊 복싱 스타일 테스트")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("로그인 후 이용할 수 있습니다. 왼쪽 사이드바에서 Login을 진행해주세요.")
    st.stop()

questions = load_questions()

st.write("각 문항을 읽고 자신과 가장 잘 맞는 정도를 선택해 주세요.")
st.write("**(1점: 전혀 그렇지 않다 ~ 5점: 매우 그렇다)**")

if "answers" not in st.session_state:
    st.session_state.answers = {}

submitted = False
with st.form("style_test_form"):
    answers = {}

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['text']}")

        answer = st.radio(
            label="점수 선택",
            options=[1, 2, 3, 4, 5],
            index=2,
            key=f"q_{q['id']}",
            horizontal=True,
            label_visibility="collapsed"
        )
        answers[q["id"]] = answer
        st.write("---")

    submitted = st.form_submit_button("결과 확인하기")

if submitted:
    axes_scores = {"P_D": 0.0, "V_R": 0.0, "S_H": 0.0, "O_K": 0.0}
    stats_scores = {
     "Power": 0.0,
    "Cardio": 0.0,
    "Endurance": 0.0,
    "Balance": 0.0,
    "Flexibility": 0.0,
    "Agility": 0.0,
}

    for q in questions:
        q_id = q["id"]
        user_val = answers[q_id]
        multiplier = user_val - 3

        for axis, weight in q["axes"].items():
            axes_scores[axis] += weight * multiplier

        for stat, weight in q["stats"].items():
            stats_scores[stat] += weight * multiplier

    code = compute_style_code(axes_scores, stats_scores)

    for stat in stats_scores:
        if stats_scores[stat] < 0:
            stats_scores[stat] = 0.0

    st.session_state.result_code = code
    st.session_state.hex_stats = stats_scores
    st.session_state.is_tested = True

    st.success("테스트가 완료되었습니다!")
    st.write("왼쪽 사이드바에서 **Result 페이지**로 이동해 결과를 확인하세요.")