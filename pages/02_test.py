import streamlit as st
from quiz_data import load_questions

st.set_page_config(page_title="Style Test", page_icon="🥋")

st.title("🥋 주짓수 스타일 테스트")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("로그인 후 이용할 수 있습니다. 왼쪽 사이드바에서 Login을 진행해주세요.")
    st.stop()

questions = load_questions()
total_questions = len(questions)

st.write("각 문항을 읽고 자신과 가장 잘 맞는 정도를 선택해 주세요.")
st.write("**(1점: 전혀 그렇지 않다 ~ 5점: 매우 그렇다)**")

# 진행률을 위한 State
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 전체 질문 렌더링
with st.form("style_test_form"):
    answers = {}
    
    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['text']}")
        
        # 가로형 라디오 버튼 활용
        answer = st.radio(
            label="점수 선택",
            options=[1, 2, 3, 4, 5],
            index=2, # 기본값: 3 (보통이다)
            key=f"q_{q['id']}",
            horizontal=True,
            label_visibility="collapsed"
        )
        answers[q["id"]] = answer
        st.write("---")
        
    submitted = st.form_submit_button("결과 확인하기")

if submitted:
    # 점수 계산 초기화
    axes_scores = {"P_M": 0.0, "P_F": 0.0, "C_A": 0.0, "F_R": 0.0}
    stats_scores = {
        "Pressure": 0.0, 
        "Mobility": 0.0, 
        "Submission": 0.0, 
        "Control": 0.0, 
        "Creativity": 0.0, 
        "Aggression": 0.0
    }
    
    for q in questions:
        q_id = q["id"]
        # 응답 값: 1~5 -> 승수 변환: -2, -1, 0, 1, 2
        user_val = answers[q_id]
        multiplier = user_val - 3
        
        # 메인 지표 계산
        for axis, weight in q["axes"].items():
            axes_scores[axis] += weight * multiplier
            
        # 육각 스탯 계산
        for stat, weight in q["stats"].items():
            stats_scores[stat] += weight * multiplier

    # 최종 코드 도출
    code = ""
    # P_M: P(양수/0) or M(음수)
    code += "P" if axes_scores["P_M"] >= 0 else "M"
    # P_F: P(양수/0) or F(음수)
    code += "P" if axes_scores["P_F"] >= 0 else "F"
    # C_A: C(음수) or A(양수/0) - C_A 가중치가 C쪽에 음수, A쪽에 양수로 설정되었다면..
    # quiz_data.py 기준: C_A가 음수면 C(Calculated), 양수면 A(Aggressive)
    code += "A" if axes_scores["C_A"] > 0 else "C"
    # F_R: F(양수/0) or R(음수)
    code += "F" if axes_scores["F_R"] >= 0 else "R"

    # 스탯 스케일링 (음수가 나오지 않게 보정)
    for stat in stats_scores:
        if stats_scores[stat] < 0:
            stats_scores[stat] = 0.0

    st.session_state.result_code = code
    st.session_state.hex_stats = stats_scores
    st.session_state.is_tested = True

    st.success("테스트가 완료되었습니다!")
    st.write("왼쪽 사이드바에서 **Result 페이지**로 이동해 결과를 확인하세요.")