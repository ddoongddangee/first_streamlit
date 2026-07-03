import streamlit as st
from quiz_data import STYLE_INFO

st.set_page_config(page_title="Result", page_icon="📊")

st.title("📊 테스트 결과")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("로그인 후 이용할 수 있습니다.")
    st.stop()

if "result_style" not in st.session_state:
    st.warning("아직 테스트를 풀지 않았습니다. Style Test 페이지에서 먼저 테스트를 진행하세요.")
    st.stop()

result_style = st.session_state.result_style
scores = st.session_state.scores

result = STYLE_INFO[result_style]

st.header(f"당신의 주짓수 스타일은: {result['name']}")

st.write(result["description"])

st.subheader("추천 기술")
for skill in result["skills"]:
    st.write(f"- {skill}")

st.subheader("스타일별 점수")
st.bar_chart(scores)

if st.button("테스트 다시 하기"):
    del st.session_state.result_style
    del st.session_state.scores
    st.success("결과가 초기화되었습니다. Style Test 페이지에서 다시 테스트하세요.")