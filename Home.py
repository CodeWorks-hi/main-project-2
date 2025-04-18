# 실행: streamlit run Home.py
# 서버 주소: https://main-project-codeworks.streamlit.app/
# 대표 이미지: https://m.ddaily.co.kr/2022/07/28/2022072820411931122_l.png

import streamlit as st
import os
import logging
import traceback
import datetime
import base64



# ✅ 접속 로그 기록
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logging.info(f"[접속 기록] 페이지 접속 시각: {datetime.datetime.now()}")

# ✅ 페이지 설정
st.set_page_config(
    page_title="Hyundai CRM",
    layout="wide",
    page_icon="https://i.namu.wiki/i/uNKzeN4J5LmcBr_4EbF2D6ObllziCSQWNo8inXP6F2vS1zIb1UtVws-7AzkP0qOUrm40Um6xekuoFUYDMtFT3w.webp"
)

# ✅ 페이지 상태 초기화
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# ✅ 페이지 전환 함수
def switch_page(page):
    st.session_state.current_page = page
    st.rerun()

# ✅ 홈 페이지
if st.session_state.current_page == "home":
    def get_image_base64(path):
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()

    image_base64 = get_image_base64("images/hyundai_logo.png")

    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 40px;">
            <img src="data:image/png;base64,{image_base64}" width="80"/>
            <h1 style="margin-bottom: 0;">Hyundai CRM </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.subheader("")
    col4, col1,col6, col2,col7, col3, col5 = st.columns([1.5, 1,0.1, 1,0.1, 1, 1])
    with col4:
        st.markdown("<div style='height:100%; border-left:1px solid #ddd;'></div>", unsafe_allow_html=True)
    with col5:
        st.markdown("<div style='height:100%; border-left:1px solid #ddd;'></div>", unsafe_allow_html=True)
    with col6:
        st.markdown("<div style='height:100%; border-left:1px solid #ddd;'></div>", unsafe_allow_html=True)
    with col7:
        st.markdown("<div style='height:100%; border-left:1px solid #ddd;'></div>", unsafe_allow_html=True)

    with col1:
        st.image("images/user_icon.png", width=80)
        st.markdown("### 일반회원\n개인 사용자 전용 서비스")
        if st.button("접속하기", key="btn_user"):
            switch_page("A_U_main")

    with col2:
        st.image("images/shop_icon.png", width=80)
        st.markdown("### 딜러 허브\n대리점 및 가맹점 서비스")
        if st.button("접속하기", key="btn_dealer"):
            switch_page("dealer_main")

    with col3:
        st.image("images/admin_icon.png", width=80)
        st.markdown("### 관리자 콘솔\n운영 및 데이터 관리")
        if st.button("접속하기", key="btn_admin"):
            switch_page("admin_main")

# ✅ 라우팅 처리
else:

    page = st.session_state.get("current_page")

    if page == "A_U_main":
        import A_U_main as auto
        auto.app()       
    
    # 딜러 페이지 전환 ( 수정하면 안됩니다.) - 수정시 페이지 전환 안됨
    elif page == "dealer_main":  
        import B_D_main as dealer
        dealer.app()
    # 어드민 페이지 전환 ( 수정하면 안됩니다.) - 수정시 페이지 전환 안됨
    elif page == "admin_main":  
        import C_A_main as admin
        admin.app()
