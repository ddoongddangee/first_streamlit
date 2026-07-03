import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from quiz_data import STYLE_INFO

st.set_page_config(page_title="Result", page_icon="📊", layout="wide")

st.title("📊 진단 결과")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("로그인 후 이용할 수 있습니다. 왼쪽 사이드바에서 Login을 진행해주세요.")
    st.stop()

if "is_tested" not in st.session_state or not st.session_state.is_tested:
    st.warning("아직 테스트를 완료하지 않았습니다. Style Test 페이지에서 진단을 진행하세요.")
    st.stop()

code = st.session_state.result_code
hex_stats = st.session_state.hex_stats

# 예외 처리: 코드가 STYLE_INFO에 없을 경우 방어 코드
if code not in STYLE_INFO:
    st.error("알 수 없는 코드입니다. 다시 테스트를 진행해 주세요.")
    st.stop()

result = STYLE_INFO[code]

st.markdown(f"## 당신의 플레이 스타일 코드는 **{code}** 입니다.")
st.markdown(f"### 💡 별칭: **{result['name']}**")
st.write(f"> {result['description']}")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("육각 스탯 분석")
    
    # 육각 그래프(Radar Chart) 그리기
    categories = list(hex_stats.keys())
    values = list(hex_stats.values())
    
    # 닫힌 도형을 위해 첫 값을 끝에 추가
    categories_plot = categories + [categories[0]]
    values_plot = values + [values[0]]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values_plot,
        theta=categories_plot,
        fill='toself',
        name='Stats',
        line_color='indigo'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(max(values) + 1, 5)] # 최대값 유동적 조정
            )),
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("훈련 및 추천")
    
    st.markdown("**🛡️ 추천 기술 (Recommended Skills):**")
    for skill in result["skills"]:
        st.write(f"- {skill}")
        
    st.markdown("**🥋 추천 선수 (Reference Players):**")
    for player in result["players"]:
        st.write(f"- {player}")
        
    st.markdown("**💪 추천 훈련 방향 (Training Direction):**")
    for training in result["training"]:
        st.write(f"- {training}")

st.divider()

if st.button("테스트 다시 하기"):
    st.session_state.is_tested = False
    del st.session_state.result_code
    del st.session_state.hex_stats
    st.success("결과가 초기화되었습니다. Style Test 페이지에서 다시 진행하세요.")