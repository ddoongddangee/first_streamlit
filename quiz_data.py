import streamlit as st

@st.cache_data
def load_questions():
    # 총 24개의 질문. 각 문항은 메인 지표 4축과 육각 스탯 6축에 영향을 줍니다.
    # 5점 척도 응답에 따라 가중치가 곱해집니다. (1점: -2, 2점: -1, 3점: 0, 4점: 1, 5점: 2)
    # 긍정 응답(4, 5점)일 경우 가중치 그대로 적용.
    questions = [
        {
            "id": 1,
            "text": "나는 스파링을 시작할 때, 상대방을 묵직하게 누르면서 시작하는 것을 선호한다.",
            "axes": {"P_M": 1.0, "P_F": 0.5, "C_A": -0.5, "F_R": 0.0}, 
            "stats": {"Pressure": 2.0, "Mobility": -1.0, "Submission": 0.0, "Control": 1.0, "Creativity": 0.0, "Aggression": -0.5}
        },
        {
            "id": 2,
            "text": "위험을 감수하더라도 화려하고 빠른 스크램블 상황을 만드는 것을 좋아한다.",
            "axes": {"P_M": -1.5, "P_F": -0.5, "C_A": 1.5, "F_R": 0.5},
            "stats": {"Pressure": -1.0, "Mobility": 2.0, "Submission": 0.5, "Control": -1.0, "Creativity": 1.0, "Aggression": 1.5}
        },
        {
            "id": 3,
            "text": "유리한 포지션(예: 마운트, 백)을 잡았다면 서브미션보다는 포지션을 유지하며 점수를 확실히 지키는 것이 먼저다.",
            "axes": {"P_M": 0.0, "P_F": 1.5, "C_A": -1.0, "F_R": 0.5},
            "stats": {"Pressure": 0.5, "Mobility": 0.0, "Submission": -1.5, "Control": 2.0, "Creativity": -0.5, "Aggression": -1.0}
        },
        {
            "id": 4,
            "text": "스파링 중 기회가 보이면 포지션을 잃을 수 있더라도 과감하게 서브미션을 시도한다.",
            "axes": {"P_M": 0.0, "P_F": -1.5, "C_A": 1.5, "F_R": 0.0},
            "stats": {"Pressure": -0.5, "Mobility": 0.5, "Submission": 2.0, "Control": -1.5, "Creativity": 0.5, "Aggression": 1.5}
        },
        {
            "id": 5,
            "text": "나는 평소 새로운 인스타그램 릴스나 유튜브에서 본 최신 기술을 스파링에서 자주 실험해 본다.",
            "axes": {"P_M": 0.0, "P_F": 0.0, "C_A": 0.5, "F_R": -1.5}, # F(양수) R(음수) -> 음수가 Creative
            "stats": {"Pressure": 0.0, "Mobility": 0.5, "Submission": 0.0, "Control": -0.5, "Creativity": 2.0, "Aggression": 0.0}
        },
        {
            "id": 6,
            "text": "화려한 기술보다는 검증된 기본적인 기술(예: 클로즈 가드 암바, 크로스 칼라 초크)을 가장 신뢰한다.",
            "axes": {"P_M": 0.0, "P_F": 0.0, "C_A": -0.5, "F_R": 1.5},
            "stats": {"Pressure": 0.5, "Mobility": 0.0, "Submission": 0.5, "Control": 1.0, "Creativity": -1.5, "Aggression": -0.5}
        },
        {
            "id": 7,
            "text": "가드 패스를 할 때, 좌우로 빠르게 움직이며 상대방의 반응을 이끌어내는 토레안도 패스 류를 주로 사용한다.",
            "axes": {"P_M": -1.5, "P_F": 0.0, "C_A": 0.5, "F_R": -0.5},
            "stats": {"Pressure": -1.0, "Mobility": 2.0, "Submission": 0.0, "Control": 0.0, "Creativity": 0.5, "Aggression": 1.0}
        },
        {
            "id": 8,
            "text": "패스 시 무릎이나 골반을 이용해 상대방의 다리를 묶어두고 천천히 진입하는 스매시 패스나 니컷을 선호한다.",
            "axes": {"P_M": 1.5, "P_F": 0.5, "C_A": -0.5, "F_R": 0.5},
            "stats": {"Pressure": 2.0, "Mobility": -1.5, "Submission": 0.0, "Control": 1.5, "Creativity": 0.0, "Aggression": 0.0}
        },
        {
            "id": 9,
            "text": "상대가 터틀 자세로 방어할 때, 억지로 백을 잡으려 하기보다는 먼저 눌러서 체력을 갉아먹는 것을 택한다.",
            "axes": {"P_M": 1.0, "P_F": 1.0, "C_A": -1.0, "F_R": 0.0},
            "stats": {"Pressure": 1.5, "Mobility": -0.5, "Submission": -1.0, "Control": 1.5, "Creativity": 0.0, "Aggression": -0.5}
        },
        {
            "id": 10,
            "text": "하체 관절기(Leg lock) 상황이 오면 피하지 않고 오히려 적극적으로 얽히려고 한다.",
            "axes": {"P_M": -0.5, "P_F": -1.0, "C_A": 1.0, "F_R": -1.5},
            "stats": {"Pressure": -0.5, "Mobility": 1.0, "Submission": 1.5, "Control": -1.0, "Creativity": 1.5, "Aggression": 1.0}
        },
        {
            "id": 11,
            "text": "나의 주짓수는 한 턴, 한 턴 계산된 움직임으로 상대를 늪에 빠뜨리는 느낌에 가깝다.",
            "axes": {"P_M": 1.0, "P_F": 1.0, "C_A": -1.5, "F_R": 0.5},
            "stats": {"Pressure": 1.0, "Mobility": -1.0, "Submission": -0.5, "Control": 2.0, "Creativity": -0.5, "Aggression": -1.5}
        },
        {
            "id": 12,
            "text": "불리한 포지션에 깔려 있을 때, 기술적인 이스케이프보다는 폭발적인 움직임(브릿지, 새우빼기)으로 순식간에 벗어나는 편이다.",
            "axes": {"P_M": -1.0, "P_F": -0.5, "C_A": 1.0, "F_R": 0.0},
            "stats": {"Pressure": -1.0, "Mobility": 1.5, "Submission": 0.0, "Control": -1.0, "Creativity": 0.0, "Aggression": 1.0}
        },
        {
            "id": 13,
            "text": "아무리 좋은 서브미션 기회가 있어도, 내가 깔릴(스윕 당할) 위험이 조금이라도 있다면 시도하지 않는다.",
            "axes": {"P_M": 0.0, "P_F": 1.5, "C_A": -1.5, "F_R": 1.0},
            "stats": {"Pressure": 0.0, "Mobility": -0.5, "Submission": -1.5, "Control": 1.5, "Creativity": 0.0, "Aggression": -2.0}
        },
        {
            "id": 14,
            "text": "나는 스파링 파트너가 누구든 간에 내 템포(속도)를 빠르게 올려 상대를 지치게 만드는 것을 즐긴다.",
            "axes": {"P_M": -1.0, "P_F": 0.0, "C_A": 1.5, "F_R": -0.5},
            "stats": {"Pressure": -0.5, "Mobility": 1.5, "Submission": 0.5, "Control": -0.5, "Creativity": 0.5, "Aggression": 1.5}
        },
        {
            "id": 15,
            "text": "주짓수는 결국 '누가 더 상대의 목과 팔다리를 먼저 꺾거나 조르냐'의 싸움이라고 생각한다.",
            "axes": {"P_M": 0.0, "P_F": -1.5, "C_A": 1.0, "F_R": -0.5},
            "stats": {"Pressure": 0.0, "Mobility": 0.5, "Submission": 2.0, "Control": -1.0, "Creativity": 0.5, "Aggression": 1.5}
        },
        {
            "id": 16,
            "text": "나는 클래식한 도복 주짓수 기술들(라펠, 스파이더 가드 등)보다 노기(No-Gi) 스타일이나 현대적인 주짓수가 더 흥미롭다.",
            "axes": {"P_M": 0.0, "P_F": 0.0, "C_A": 0.0, "F_R": -1.5},
            "stats": {"Pressure": -0.5, "Mobility": 1.0, "Submission": 0.5, "Control": -0.5, "Creativity": 1.5, "Aggression": 0.0}
        },
        {
            "id": 17,
            "text": "시합에 나간다면 어드밴티지나 2점 차이로라도 안전하게 이기는 것이 화끈하게 하다가 지는 것보다 훨씬 낫다.",
            "axes": {"P_M": 1.0, "P_F": 1.5, "C_A": -1.5, "F_R": 1.0},
            "stats": {"Pressure": 0.5, "Mobility": -1.0, "Submission": -1.5, "Control": 1.5, "Creativity": -0.5, "Aggression": -1.5}
        },
        {
            "id": 18,
            "text": "가드에 있을 때 상대를 가둬두는 클로즈가드나 하프가드보다는 델라히바, 리버스 델라히바처럼 움직임이 많은 오픈가드를 선호한다.",
            "axes": {"P_M": -1.5, "P_F": -0.5, "C_A": 0.5, "F_R": -0.5},
            "stats": {"Pressure": -1.5, "Mobility": 1.5, "Submission": 0.0, "Control": -1.0, "Creativity": 1.0, "Aggression": 0.5}
        },
        {
            "id": 19,
            "text": "나는 패스 상황에서 1cm씩 전진하며 상대의 숨을 조여가는 크로스페이스(Cross-face) 압박을 사랑한다.",
            "axes": {"P_M": 1.5, "P_F": 1.0, "C_A": -0.5, "F_R": 1.0},
            "stats": {"Pressure": 2.0, "Mobility": -1.0, "Submission": 0.0, "Control": 1.5, "Creativity": -1.0, "Aggression": 0.0}
        },
        {
            "id": 20,
            "text": "스파링 중 불리한 포지션에 처하면, 차분하게 프레임을 만들고 하나씩 해제하는 정석적인 방어를 한다.",
            "axes": {"P_M": 1.0, "P_F": 1.0, "C_A": -1.0, "F_R": 1.5},
            "stats": {"Pressure": 0.5, "Mobility": -1.0, "Submission": -0.5, "Control": 1.5, "Creativity": -1.0, "Aggression": -1.0}
        },
        {
            "id": 21,
            "text": "상대방의 백을 잡는 것(Back take)이 가드 패스 후 마운트를 점유하는 것보다 훨씬 좋고 매력적이라 느낀다.",
            "axes": {"P_M": -0.5, "P_F": -1.0, "C_A": 0.5, "F_R": -1.0},
            "stats": {"Pressure": -0.5, "Mobility": 1.0, "Submission": 1.0, "Control": 0.5, "Creativity": 1.0, "Aggression": 0.5}
        },
        {
            "id": 22,
            "text": "쉬는 시간 없이 계속해서 공격을 퍼부어 상대방의 정신을 빼놓는 '무한 공격' 스타일을 지향한다.",
            "axes": {"P_M": -1.0, "P_F": -1.0, "C_A": 1.5, "F_R": 0.0},
            "stats": {"Pressure": 0.0, "Mobility": 1.0, "Submission": 1.5, "Control": -1.0, "Creativity": 0.0, "Aggression": 2.0}
        },
        {
            "id": 23,
            "text": "새로운 서브미션 시스템(예: 다스 초크 연계, 이너 힐훅 시스템)을 배우고 적용하는 것이 주짓수의 가장 큰 즐거움이다.",
            "axes": {"P_M": 0.0, "P_F": -1.0, "C_A": 0.0, "F_R": -1.5},
            "stats": {"Pressure": -0.5, "Mobility": 0.5, "Submission": 1.0, "Control": -0.5, "Creativity": 2.0, "Aggression": 0.0}
        },
        {
            "id": 24,
            "text": "서브미션은 내가 억지로 만들어내는 것이 아니라, 포지션을 굳건히 하면 상대가 발버둥치다 스스로 내어주는 것이라 믿는다.",
            "axes": {"P_M": 1.0, "P_F": 1.5, "C_A": -1.5, "F_R": 1.0},
            "stats": {"Pressure": 1.0, "Mobility": -1.0, "Submission": -1.0, "Control": 2.0, "Creativity": -0.5, "Aggression": -1.0}
        }
    ]
    return questions

# 16개 스타일 정의
STYLE_INFO = {
    "PPCF": {
        "name": "Iron Tank",
        "description": "무너지지 않는 압박형 플레이어. 정석적이고 견고한 포지션 유지로 상대를 천천히 질식시킵니다. 위험을 감수하기보다는 완벽한 컨트롤을 추구합니다.",
        "skills": ["Knee Cut", "Over-Under Pass", "Cross Face", "Mount Control"],
        "players": ["Roger Gracie", "Bernardo Faria"],
        "training": ["압박 패스 드릴", "기본 이스케이프", "포지션 유지 훈련"]
    },
    "PPCR": {
        "name": "Chess Master",
        "description": "계산적이고 창의적인 전략가. 압박과 컨트롤을 기반으로 하면서도 상대의 허를 찌르는 독창적인 기술 셋을 보유하고 있습니다.",
        "skills": ["Lapel Guard", "Smash Pass", "Ezekiel Choke", "Modern Half Guard"],
        "players": ["Keenan Cornelius", "Mikey Musumeci"],
        "training": ["라펠 시스템", "가드 리텐션", "체인 컨트롤"]
    },
    "PPAF": {
        "name": "Bruiser",
        "description": "묵직하면서도 저돌적인 브루저. 기본기를 바탕으로 거칠게 압박하며 템포를 높여 상대를 지치게 만듭니다.",
        "skills": ["Double Leg Takedown", "Pressure Passing", "Americana", "Kimura"],
        "players": ["Marcus 'Buchecha' Almeida", "Erberth Santos"],
        "training": ["테이크다운 후 압박", "연속 패스", "체력 훈련"]
    },
    "PPAR": {
        "name": "Predator",
        "description": "공격적이고 창의적인 압박형 포식자. 상대의 움직임을 억제하면서 예상치 못한 각도에서 공격을 쏟아붓습니다.",
        "skills": ["Body Lock Pass", "Darce Choke", "Guillotine", "Front Headlock System"],
        "players": ["Gordon Ryan", "Nicholas Meregali"],
        "training": ["프론트 헤드락 컨트롤", "바디락 패스", "다스/아나콘다 연계"]
    },
    "PFCF": {
        "name": "Technician",
        "description": "정확도 높은 피니셔. 압박과 정석적인 움직임을 통해 실수 없이 완벽한 타이밍에 서브미션을 성공시킵니다.",
        "skills": ["Bow and Arrow Choke", "Armbar", "Cross Collar Choke", "Closed Guard"],
        "players": ["Rickson Gracie", "Kron Gracie"],
        "training": ["기본기 서브미션 피니시", "클로즈 가드 서브미션", "타이밍 스파링"]
    },
    "PFCR": {
        "name": "Trap Setter",
        "description": "창의적인 덫을 놓는 사냥꾼. 묵직하게 누르면서 상대를 방심하게 만든 뒤, 독특한 피니시로 경기를 끝냅니다.",
        "skills": ["Buggy Choke", "Tarikoplata", "Wrist Lock", "Sneaky Triangles"],
        "players": ["Roberto Jimenez", "Braulio Estima"],
        "training": ["변칙 서브미션", "그립 싸움", "함정 파기 드릴"]
    },
    "PFAF": {
        "name": "Executioner",
        "description": "자비 없는 처형자. 강한 압박을 유지한 채 맹렬하게 피니시를 노리는 킬러입니다. 한 번 물면 놓지 않습니다.",
        "skills": ["Kimura Trap", "Ezekiel Choke", "Heavy Knee on Belly", "Arm Triangle"],
        "players": ["Rodolfo Vieira", "Ronaldo 'Jacare' Souza"],
        "training": ["키무라 트랩 시스템", "니온벨리 공격", "서브미션 체인"]
    },
    "PFAR": {
        "name": "Snake",
        "description": "유연하고 치명적인 뱀. 기발한 서브미션과 저돌적인 압박을 섞어 상대를 숨 막히게 하고 빠르게 항복을 받아냅니다.",
        "skills": ["Heel Hook", "Leg Entanglements", "Darce Choke", "Calf Slicer"],
        "players": ["Craig Jones", "Garry Tonon"],
        "training": ["하체관절기 시스템", "스크램블 중 서브미션", "다양한 그립 연구"]
    },
    "MPCF": {
        "name": "Controller",
        "description": "안정적인 플로우 라이더. 부드러운 움직임과 스크램블 능력을 통해 포지션을 유지하고 안전하게 점수를 땁니다.",
        "skills": ["Toreando Pass", "De La Riva Guard", "Berimbolo", "Back Take"],
        "players": ["Mendes Brothers", "Paulo Miyao"],
        "training": ["베림볼로 셋업", "가드 리텐션 드릴", "가벼운 패스 드릴"]
    },
    "MPCR": {
        "name": "Flow Master",
        "description": "예측 불가한 흐름의 지배자. 계산된 움직임과 현대적인 테크닉을 활용해 마찰 없이 상대를 제압합니다.",
        "skills": ["K-Guard", "Crab Ride", "Matrix", "50/50 Guard"],
        "players": ["Levi Jones-Leary", "Thalison Soares"],
        "training": ["K-가드 연계", "크랩 라이드", "리텐션 및 인버전"]
    },
    "MPAF": {
        "name": "Berserker",
        "description": "지치지 않는 광전사. 빠른 기동성을 바탕으로 끊임없이 상대를 몰아붙이고 공격적으로 포지션을 빼앗습니다.",
        "skills": ["Flying Triangle", "Wrestling Takedowns", "Scramble Passing", "Back Takes"],
        "players": ["JT Torres", "Lucas Lepri"],
        "training": ["레슬링 연계", "고강도 스크램블", "체력 훈련"]
    },
    "MPAR": {
        "name": "Trickster",
        "description": "어디서든 나타나는 트릭스터. 창의적인 움직임과 폭발적인 스피드로 상대를 혼란에 빠뜨리고 유리한 고지를 선점합니다.",
        "skills": ["Cartwheel Pass", "Flying Armbar", "Imanari Roll", "Rubber Guard"],
        "players": ["Geo Martinez", "Jeff Glover"],
        "training": ["플라잉 서브미션", "체조 훈련", "유연성 극대화"]
    },
    "MFCF": {
        "name": "Professor",
        "description": "이론과 실전을 겸비한 교수. 정석적인 기술을 완벽한 타이밍에 스피디하게 성공시켜 피니시합니다.",
        "skills": ["Armdrag", "Guillotine Choke", "Triangle Choke", "Back Mount Finishes"],
        "players": ["Marcelo Garcia", "Demian Maia"],
        "training": ["백테이크 셋업", "암드래그 타이밍", "X-가드 시스템"]
    },
    "MFCR": {
        "name": "Innovator",
        "description": "새로운 메타를 창조하는 혁신가. 뛰어난 움직임과 최신 피니시 기술을 융합하여 상대를 무력화시킵니다.",
        "skills": ["Leg Lock System", "Saddle", "Ashi Garami", "Inverted Guard"],
        "players": ["Lachlan Giles", "Ryan Hall"],
        "training": ["에스테틱스 및 인버전", "50/50 피니시", "하체 관절기 깊은 연구"]
    },
    "MFAF": {
        "name": "Showman",
        "description": "관중을 매료시키는 쇼맨. 빠른 템포와 정석적인 강한 공격으로 상대를 압도하며 폭발적인 피니시를 만듭니다.",
        "skills": ["Jumping Guard", "Explosive Sweeps", "Fast Submissions", "Kimura"],
        "players": ["Mica Galvao", "Leandro Lo"],
        "training": ["폭발력 훈련", "서브미션 타이밍", "빠른 전환"]
    },
    "MFAR": {
        "name": "Phantom",
        "description": "순식간에 숨통을 끊는 유령. 눈에 보이지 않는 빠른 스크램블 속에서 창의적인 서브미션으로 탭을 받아냅니다.",
        "skills": ["Darce Choke", "Japanese Necktie", "Rolling Back Attacks", "Heel Hook"],
        "players": ["Tye Ruotolo", "Kade Ruotolo"],
        "training": ["스크램블 중 서브미션 캐치", "다스/볼라 연계", "변칙적 움직임"]
    }
}