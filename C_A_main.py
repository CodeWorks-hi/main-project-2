import streamlit as st
import importlib
import pandas as pd
import base64

# ▶️ 이미지 base64 인코딩 함수
def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def app():
    logo_base64 = get_base64_image("images/hyundae_kia_logo.png")

    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 20px;">
            <img src="data:image/png;base64,{logo_base64}" alt="로고" width="60" style="width: 120px; height: auto; border-radius: 8px;">
            <h1 style="margin: 0; font-size: 28px;"> 관리자 콘솔 </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    tabs = st.tabs([
        "수출입 데이터 분석",
        "재고·공급망",
        "생산·제조",
        "탄소 배출 모니터링",
        "콘솔 관리"
    ])

    tab_modules = [
        ("modules.C_A_analytics", "analytics_ui"),
        ("modules.C_A_inventory", "inventory_ui"),
        ("modules.C_A_production", "production_ui"),
        ("modules.C_A_eco", "eco_ui"),
        ("modules.C_A_settings", "settings_ui"),
    ]

    for i, (module_path, function_name) in enumerate(tab_modules):
        with tabs[i]:
            # try:
                module = importlib.import_module(module_path)
                getattr(module, function_name)()
            # except Exception as e:
            #     st.error(f"모듈 로딩 오류: `{module_path}.{function_name}`\\n\n**{e}**")

    st.markdown("---")
    col11, col12, col13 =  st.columns([1, 6, 1])
    # ✔ 안전한 방식: 세션 상태로 페이지 전환
    with col13:
        pass
    with col11:
        if st.button("← 메인으로 돌아가기"):
            st.session_state.current_page = "home"
            st.rerun()
    with col12:
        st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 0.9rem; margin-top: 30px;'>
        © 2025 Hyundai & Kia Export Dashboard. All rights reserved.
        </div>
        """,
        unsafe_allow_html=True
        )

