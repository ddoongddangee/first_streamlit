import streamlit as st

@st.cache_data
def load_questions():
    # 총 24개의 질문. 각 문항은 메인 지표 4축과 육각 스탯 6축에 영향을 줍니다.
    # 5점 척도 응답에 따라 가중치가 곱해집니다. (1점: -2, 2점: -1, 3점: 0, 4점: 1, 5점: 2)
    # 긍정 응답(4, 5점)일 경우 가중치 그대로 적용.
    questions = [
        {
            "id": 1,
            "text": "나는 라운드 초반부터 상대를 뒤로 밀어붙이며 압박하는 편이다.",
            "axes": {"P_D": 1.5, "V_R": 0.5, "S_H": 0.0, "O_K": -0.5},
            "stats": {"Power": 2.0, "Cardio": 1.5, "Endurance": 1.0, "Balance": 0.5, "Flexibility": -0.5, "Agility": -0.5}
        },
        {
            "id": 2,
            "text": "나는 먼저 들어가기보다 상대가 들어오게 유도한 뒤 받아치는 편이다.",
            "axes": {"P_D": -1.5, "V_R": -0.5, "S_H": 0.0, "O_K": 0.5},
            "stats": {"Power": -1.0, "Cardio": -0.5, "Endurance": -0.5, "Balance": 1.0, "Flexibility": 0.5, "Agility": 0.5}
        },
        {
            "id": 3,
            "text": "강한 한 방보다 잽과 콤비네이션을 많이 던져 흐름을 가져가는 것이 좋다.",
            "axes": {"P_D": 0.5, "V_R": 1.5, "S_H": 0.5, "O_K": 0.5},
            "stats": {"Power": 0.5, "Cardio": 2.0, "Endurance": 1.0, "Balance": 0.5, "Flexibility": 0.0, "Agility": 0.5}
        },
        {
            "id": 4,
            "text": "펀치를 많이 던지기보다 확실히 맞출 수 있는 순간을 기다리는 편이다.",
            "axes": {"P_D": -0.5, "V_R": -1.5, "S_H": 0.0, "O_K": 0.5},
            "stats": {"Power": -0.5, "Cardio": -1.0, "Endurance": -0.5, "Balance": 1.5, "Flexibility": 0.5, "Agility": 1.0}
        },
        {
            "id": 5,
            "text": "상대의 공격을 피할 때 상체 움직임보다 발로 거리를 빼는 편이다.",
            "axes": {"P_D": -0.5, "V_R": 0.0, "S_H": 1.5, "O_K": 1.0},
            "stats": {"Power": -0.5, "Cardio": 0.0, "Endurance": 0.0, "Balance": 2.0, "Flexibility": -0.5, "Agility": 1.5}
        },
        {
            "id": 6,
            "text": "나는 슬립, 더킹, 위빙처럼 머리 움직임으로 상대 펀치를 피하는 것을 선호한다.",
            "axes": {"P_D": 0.5, "V_R": 0.0, "S_H": -1.5, "O_K": -1.0},
            "stats": {"Power": 0.5, "Cardio": 0.0, "Endurance": 0.0, "Balance": -0.5, "Flexibility": 2.0, "Agility": 1.0}
        },
        {
            "id": 7,
            "text": "나는 긴 잽 거리에서 상대를 컨트롤하는 것이 가장 편하다.",
            "axes": {"P_D": -0.5, "V_R": 0.5, "S_H": 1.0, "O_K": 1.5},
            "stats": {"Power": -0.5, "Cardio": 0.5, "Endurance": 0.5, "Balance": 1.5, "Flexibility": -0.5, "Agility": 2.0}
        },
        {
            "id": 8,
            "text": "나는 가까운 거리에서 훅과 어퍼를 주고받는 상황이 편하다.",
            "axes": {"P_D": 1.0, "V_R": 0.0, "S_H": -1.0, "O_K": -1.5},
            "stats": {"Power": 1.5, "Cardio": 0.5, "Endurance": 0.5, "Balance": -1.0, "Flexibility": 1.5, "Agility": -1.0}
        },
        {
            "id": 9,
            "text": "상대가 물러나면 나는 따라가며 계속 압박을 유지한다.",
            "axes": {"P_D": 1.5, "V_R": 0.5, "S_H": 0.0, "O_K": -0.5},
            "stats": {"Power": 2.0, "Cardio": 1.5, "Endurance": 1.5, "Balance": 0.0, "Flexibility": 0.0, "Agility": 0.0}
        },
        {
            "id": 10,
            "text": "나는 상대가 공격하도록 일부러 빈틈을 보여주는 편이다.",
            "axes": {"P_D": -1.5, "V_R": -0.5, "S_H": -0.5, "O_K": 0.0},
            "stats": {"Power": -1.0, "Cardio": -0.5, "Endurance": -0.5, "Balance": 0.5, "Flexibility": 1.5, "Agility": 0.5}
        },
        {
            "id": 11,
            "text": "나는 잽, 원투, 잽-바디처럼 기본 콤비네이션을 계속 쌓는 스타일이다.",
            "axes": {"P_D": 0.5, "V_R": 1.5, "S_H": 1.0, "O_K": 1.0},
            "stats": {"Power": 0.5, "Cardio": 2.0, "Endurance": 1.5, "Balance": 1.0, "Flexibility": 0.0, "Agility": 1.0}
        },
        {
            "id": 12,
            "text": "나는 한 번의 카운터나 강한 스트레이트로 흐름을 뒤집는 것을 좋아한다.",
            "axes": {"P_D": -0.5, "V_R": -1.5, "S_H": 0.0, "O_K": 0.0},
            "stats": {"Power": 0.0, "Cardio": -1.0, "Endurance": -0.5, "Balance": 1.0, "Flexibility": 1.0, "Agility": 0.5}
        },
        {
            "id": 13,
            "text": "위험한 교환 상황이 오면, 나는 발을 써서 각도를 바꾸고 빠져나간다.",
            "axes": {"P_D": -0.5, "V_R": 0.0, "S_H": 1.5, "O_K": 1.0},
            "stats": {"Power": -0.5, "Cardio": 0.0, "Endurance": 0.0, "Balance": 2.0, "Flexibility": -0.5, "Agility": 1.5}
        },
        {
            "id": 14,
            "text": "상대 펀치가 날아오면 뒤로 빠지기보다 안쪽에서 숙이고 파고드는 편이다.",
            "axes": {"P_D": 1.0, "V_R": 0.0, "S_H": -1.5, "O_K": -1.0},
            "stats": {"Power": 1.0, "Cardio": 0.5, "Endurance": 0.5, "Balance": -1.0, "Flexibility": 2.0, "Agility": -0.5}
        },
        {
            "id": 15,
            "text": "나는 상대가 닿기 어려운 거리에서 잽과 스트레이트로 경기를 운영하고 싶다.",
            "axes": {"P_D": -0.5, "V_R": 0.5, "S_H": 1.0, "O_K": 1.5},
            "stats": {"Power": -0.5, "Cardio": 0.5, "Endurance": 0.5, "Balance": 1.5, "Flexibility": -0.5, "Agility": 2.0}
        },
        {
            "id": 16,
            "text": "나는 상대와 가까운 거리에서 짧은 훅, 바디샷, 어퍼를 섞는 것이 좋다.",
            "axes": {"P_D": 1.0, "V_R": 0.5, "S_H": -1.0, "O_K": -1.5},
            "stats": {"Power": 1.0, "Cardio": 1.0, "Endurance": 0.5, "Balance": -1.0, "Flexibility": 1.0, "Agility": -1.0}
        },
        {
            "id": 17,
            "text": "나는 상대가 쉬지 못하게 계속 펀치를 던져 압박하는 편이다.",
            "axes": {"P_D": 1.5, "V_R": 1.5, "S_H": 0.0, "O_K": -0.5},
            "stats": {"Power": 2.0, "Cardio": 2.0, "Endurance": 1.5, "Balance": 0.0, "Flexibility": 0.5, "Agility": -0.5}
        },
        {
            "id": 18,
            "text": "나는 상대의 실수를 기다렸다가 정확하게 한 방을 꽂는 편이다.",
            "axes": {"P_D": -1.0, "V_R": -1.5, "S_H": 0.0, "O_K": 0.0},
            "stats": {"Power": -0.5, "Cardio": -1.0, "Endurance": -0.5, "Balance": 1.0, "Flexibility": 1.0, "Agility": 0.5}
        },
        {
            "id": 19,
            "text": "내 방어의 핵심은 풋워크와 거리 조절이다.",
            "axes": {"P_D": -0.5, "V_R": 0.0, "S_H": 1.5, "O_K": 1.0},
            "stats": {"Power": -0.5, "Cardio": 0.0, "Endurance": 0.0, "Balance": 2.0, "Flexibility": -1.0, "Agility": 1.5}
        },
        {
            "id": 20,
            "text": "내 방어의 핵심은 슬립, 롤링, 위빙 같은 상체 움직임이다.",
            "axes": {"P_D": 0.5, "V_R": 0.0, "S_H": -1.5, "O_K": -0.5},
            "stats": {"Power": 0.5, "Cardio": 0.0, "Endurance": 0.0, "Balance": -1.0, "Flexibility": 2.0, "Agility": 0.5}
        },
        {
            "id": 21,
            "text": "나는 긴 거리에서 포인트를 쌓는 경기보다 안쪽으로 들어가 흐름을 흔드는 경기가 더 좋다.",
            "axes": {"P_D": 1.0, "V_R": 0.5, "S_H": -0.5, "O_K": -1.5},
            "stats": {"Power": 1.0, "Cardio": 1.0, "Endurance": 0.5, "Balance": -0.5, "Flexibility": 1.0, "Agility": -1.0}
        },
        {
            "id": 22,
            "text": "나는 근거리 난타전보다 거리를 유지하며 깨끗하게 맞히는 경기를 선호한다.",
            "axes": {"P_D": -0.5, "V_R": -0.5, "S_H": 1.0, "O_K": 1.5},
            "stats": {"Power": -0.5, "Cardio": -0.5, "Endurance": 0.5, "Balance": 1.5, "Flexibility": -0.5, "Agility": 2.0}
        },
        {
            "id": 23,
            "text": "상대가 강하게 들어와도 나는 물러서기보다 맞불을 놓는 편이다.",
            "axes": {"P_D": 1.0, "V_R": 0.5, "S_H": -0.5, "O_K": -1.0},
            "stats": {"Power": 1.5, "Cardio": 1.0, "Endurance": 1.0, "Balance": -0.5, "Flexibility": 1.0, "Agility": -0.5}
        },
        {
            "id": 24,
            "text": "나는 무리하게 들어가기보다 상대가 스스로 들어오는 순간을 기다리는 편이다.",
            "axes": {"P_D": -1.5, "V_R": -0.5, "S_H": 0.5, "O_K": 1.0},
            "stats": {"Power": -1.0, "Cardio": -0.5, "Endurance": -0.5, "Balance": 1.0, "Flexibility": 0.0, "Agility": 1.0}
        },
    ]
    return questions


def compute_style_code(axes_scores, stats_scores):
    """질문 데이터 기준으로 스타일 코드를 계산합니다."""
    first = "P" if axes_scores["P_D"] >= 0 else "D"
    second = "C" if stats_scores["Power"] >= stats_scores["Cardio"] else "V"
    third = "S" if stats_scores["Balance"] >= stats_scores["Flexibility"] else "H"
    fourth = "O" if stats_scores["Agility"] >= stats_scores["Endurance"] else "P"
    return first + second + third + fourth


# 16개 스타일 정의
STYLE_INFO = {
    "PCSO": {
        "name": "Predator",
        "title": "사냥꾼",
        "description": "상대를 압박하면서도 무작정 들어가지 않고, 상대의 반응을 끌어낸 뒤 카운터로 사냥하는 스타일입니다.",
        "features": ["압박 중심", "카운터 지향", "풋워크 활용", "오픈 레인지 선호"],
        "skills": ["압박 잽", "카운터 스트레이트", "스텝 인-아웃", "거리 압박"],
        "training": ["압박 후 빠지기", "상대 반응 유도", "잽 카운터 드릴"]
    },
    "PCSP": {
        "name": "Executioner",
        "title": "끝내는 자",
        "description": "압박으로 상대를 몰아넣고, 근거리에서 정확한 카운터와 강한 펀치로 끝내는 토투토 피니셔입니다.",
        "features": ["압박", "정확한 카운터", "풋워크 진입", "포켓 피니시"],
        "skills": ["숏 훅", "카운터 어퍼", "바디샷", "원투 후 포켓 진입"],
        "training": ["포켓 콤비네이션", "카운터 후 마무리", "바디-헤드 연계"]
    },
    "PCHO": {
        "name": "Sentinel",
        "title": "침착한 수호자",
        "description": "압박을 하면서도 가드를 단단히 유지하고, 머리 움직임과 거리 조절로 안정적으로 경기를 운영합니다.",
        "features": ["침착한 압박", "카운터", "헤드무브먼트", "오픈 레인지"],
        "skills": ["슬립 카운터", "잽 컨트롤", "체크 훅", "가드 리셋"],
        "training": ["슬립 후 카운터", "디펜스 중심 스파링", "거리 유지 드릴"]
    },
    "PCHP": {
        "name": "Pitbull",
        "title": "핏불",
        "description": "한 번 붙으면 놓지 않는 근거리 압박형입니다. 상대를 포켓에 가두고 머리 움직임으로 피하면서 계속 물고 늘어집니다.",
        "features": ["강한 압박", "카운터", "헤드무브먼트", "포켓 싸움"],
        "skills": ["위빙 진입", "숏 훅", "바디 훅", "인파이트 카운터"],
        "training": ["포켓 디펜스", "위빙-훅 연계", "근거리 압박 스파링"]
    },
    "PVSO": {
        "name": "General",
        "title": "경기 지휘관",
        "description": "압박과 활동량을 바탕으로 링을 넓게 쓰며 경기를 지휘하는 운영형 스타일입니다.",
        "features": ["압박", "볼륨", "풋워크", "오픈 레인지"],
        "skills": ["더블 잽", "원투", "각도 전환", "링 커팅"],
        "training": ["잽 볼륨 드릴", "링 커팅", "풋워크 압박"]
    },
    "PVSP": {
        "name": "Relentless",
        "title": "끊임없는 돌격",
        "description": "끊임없이 들어가며 펀치를 쏟아붓는 스워머형입니다. 쉬지 않는 전진과 연타로 상대를 무너뜨립니다.",
        "features": ["압박", "볼륨", "풋워크 진입", "포켓"],
        "skills": ["연속 잽", "바디-헤드 콤보", "러시", "포켓 연타"],
        "training": ["고강도 콤비네이션", "압박 체력 훈련", "러시 후 가드 복귀"]
    },
    "PVHO": {
        "name": "Rhino",
        "title": "돌진하는 코뿔소",
        "description": "머리 움직임으로 상대 공격을 뚫고 들어가며 볼륨으로 밀어붙이는 전진형 스타일입니다.",
        "features": ["압박", "볼륨", "헤드무브먼트", "오픈 운영"],
        "skills": ["더킹 진입", "오버핸드", "바디잽", "러시 콤보"],
        "training": ["더킹 후 진입", "헤드무브먼트 러시", "전진 압박 드릴"]
    },
    "PVHP": {
        "name": "Bulldozer",
        "title": "불도저",
        "description": "압박과 연타로 상대를 밀어버리는 스타일입니다. 근거리에서 계속 펀치를 쌓아 상대의 리듬을 부숩니다.",
        "features": ["강한 압박", "볼륨", "헤드무브먼트", "포켓"],
        "skills": ["숏 콤비네이션", "바디샷", "훅 연타", "클로즈 레인지 압박"],
        "training": ["포켓 연타", "바디샷 체인", "압박 스파링"]
    },
    "DCSO": {
        "name": "Sniper",
        "title": "저격수",
        "description": "상대를 끌어들인 뒤 긴 거리에서 정확한 한 방을 꽂는 스타일입니다.",
        "features": ["유도", "정확도", "풋워크", "오픈 레인지"],
        "skills": ["카운터 스트레이트", "체크 훅", "잽 페인트", "스텝백 카운터"],
        "training": ["스텝백 카운터", "정확도 미트", "페인트 후 스트레이트"]
    },
    "DCSP": {
        "name": "Assassin",
        "title": "암살자",
        "description": "상대를 유도한 뒤 근거리에서 조용히 치명타를 넣는 암살자형 스타일입니다.",
        "features": ["유도", "정확도", "풋워크", "포켓"],
        "skills": ["스텝인 카운터", "숏 어퍼", "체크 훅", "바디 카운터"],
        "training": ["거리 좁히기", "카운터 타이밍", "포켓 정확도 훈련"]
    },
    "DCHO": {
        "name": "Phantom",
        "title": "보이지 않는 카운터",
        "description": "상대가 치는 순간 사라지고, 보이지 않는 각도에서 카운터를 꽂는 회피형 스타일입니다.",
        "features": ["유도", "정확도", "헤드무브먼트", "오픈 레인지"],
        "skills": ["슬립 카운터", "롤 카운터", "풀 카운터", "앵글 체인지"],
        "training": ["슬립백 카운터", "롤링 후 반격", "방어 후 각도 이동"]
    },
    "DCHP": {
        "name": "Viper",
        "title": "독사",
        "description": "상대가 들어오는 순간 짧고 날카로운 한 방으로 물어버리는 스타일입니다.",
        "features": ["유도", "정확도", "헤드무브먼트", "포켓"],
        "skills": ["숏 카운터", "리드 훅", "어퍼컷", "바디 카운터"],
        "training": ["근거리 카운터", "헤드무브먼트 후 반격", "숏 펀치 정확도"]
    },
    "DVSO": {
        "name": "Matador",
        "title": "투우사",
        "description": "상대를 끌어들이고, 거리와 스텝으로 흘려보내며 볼륨으로 점수를 쌓는 스타일입니다.",
        "features": ["유도", "볼륨", "풋워크", "오픈 레인지"],
        "skills": ["잽 앤 무브", "사이드 스텝", "원투", "각도 전환"],
        "training": ["잽 앤 무브", "사이드 스텝 드릴", "거리 유지 스파링"]
    },
    "DVSP": {
        "name": "Maestro",
        "title": "리듬의 지휘자",
        "description": "리듬과 스텝으로 상대를 무너뜨리는 스타일입니다. 포켓에 들어가더라도 정면 난타가 아니라 리듬으로 흔듭니다.",
        "features": ["유도", "볼륨", "풋워크", "포켓"],
        "skills": ["리듬 잽", "스텝 인 훅", "바디-헤드 연결", "앵글 펀치"],
        "training": ["리듬 체인지", "스텝 인-아웃", "콤비네이션 후 각도 이동"]
    },
    "DVHO": {
        "name": "Ghost",
        "title": "유령",
        "description": "맞지 않고 움직이며 경기를 운영하는 스타일입니다. 상대는 따라오지만 제대로 맞히지 못합니다.",
        "features": ["유도", "볼륨", "헤드무브먼트", "오픈 레인지"],
        "skills": ["풀 카운터", "잽 앤 슬립", "롤링", "거리 리셋"],
        "training": ["노히트 스파링", "슬립 후 거리 벌리기", "잽-회피 반복"]
    },
    "DVHP": {
        "name": "Artist",
        "title": "아티스트",
        "description": "리듬, 움직임, 상체 회피, 근거리 감각을 모두 섞어 아름답게 경기를 풀어가는 기술파입니다.",
        "features": ["유도", "볼륨", "헤드무브먼트", "포켓"],
        "skills": ["숄더롤", "슬립 앤 리턴", "리듬 콤보", "근거리 앵글"],
        "training": ["리듬 스파링", "숄더롤 드릴", "헤드무브먼트 콤비네이션"]
    }
}