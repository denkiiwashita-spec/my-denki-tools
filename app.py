import streamlit as st
import cmath

# ページの設定
st.set_page_config(page_title="岩下電気管理事務所 - 複素数計算機", layout="centered")

st.title("⚡ 複素数・%Z 計算ツール")
st.write("電験2種・実務向けの複素数計算機です。")

# 入力エリア
col1, col2 = st.columns(2)

with col1:
    st.subheader("直交形式で入力")
    real_part = st.number_input("実数部 (R)", value=0.0, step=0.1, format="%.4f")
    imag_part = st.number_input("虚数部 (X)", value=0.0, step=0.1, format="%.4f")
    z = complex(real_part, imag_part)

with col2:
    st.subheader("極形式で入力")
    r = st.number_input("絶対値", value=0.0, step=0.1)
    deg = st.number_input("角度 (deg)", value=0.0, step=0.1)
    if r != 0:
        z = cmath.rect(r, cmath.radians(deg))

# 計算結果の表示
st.divider()
r_res, phi_res = cmath.polar(z)
deg_res = cmath.degrees(phi_res)

st.metric(label="直交形式", value=f"{z.real:.4f} + j{z.imag:.4f}")
st.metric(label="極形式", value=f"{r_res:.4f} ∠ {deg_res:.2f}°")

# 独立後の実務向け機能（おまけ）
with st.expander("％インピーダンス換算（開発中）"):
    st.write("ここに基準容量換算のロジックを追加予定です！")

st.info("💡 iPadのApple Pencilで数字をタップして入力できます。")