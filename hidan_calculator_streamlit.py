import streamlit as st

# ひな段の板の枚数を計算する関数
def calculate_boards(n, s):
    if n < 1 or s < 1:
        return "1以上の値を入力してください"
    total_boards = (s * n) + ((n - 1) * s)
    return total_boards

# Streamlit の UI
st.title("ひな段の板計算ツール")

# ユーザー入力
n = st.number_input("ひな段の数 (n)", min_value=1, step=1)
s = st.number_input("段数 (s)", min_value=1, step=1)

# 計算ボタン
if st.button("計算"):
    result = calculate_boards(n, s)
    st.success(f"必要な板の枚数: {result} 枚")
