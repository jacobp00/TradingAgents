import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- SIDKONFIG ---
st.set_page_config(page_title="TradingAgents Dashboard", layout="wide")

# --- DUMMYDATA (byt ut mot riktig data senare) ---
portfolio = pd.DataFrame({
    "Aktie": ["AAPL", "MSFT", "NVDA", "TSLA"],
    "Status": ["hold", "sell", "buy", "hold"]
})

transactions = pd.DataFrame({
    "Aktie": ["AAPL", "MSFT"],
    "Typ": ["sold", "bought"],
    "Belopp (USD)": [5.56, 70.0]
})

dates = pd.date_range("2025-10-01", periods=30)
values = [10000 + i**1.5 * 50 for i in range(30)]  # enkel fejkdata

reports = [
    {"Datum": "2025-10-18", "Fil": "report_2025-10-18.txt"},
    {"Datum": "2025-10-17", "Fil": "report_2025-10-17.txt"}
]

# --- RUBRIK över hela sidan ---
st.markdown(
    "<h1 style='text-align:center; font-size:48px; margin-bottom:0px;'>TradingAgents</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr style='margin-top:10px; margin-bottom:30px;'>", unsafe_allow_html=True)

# --- LAYOUT ---
col1, col2 = st.columns([1.2, 1.8], gap="large")

with col1:
    st.markdown("### 📊 Portfölj")
    st.dataframe(portfolio, use_container_width=True, height=150, hide_index=True)

    st.markdown("### 💰 Transaction")
    st.dataframe(transactions, use_container_width=True, height=120, hide_index=True)

with col2:
    st.markdown("### 📈 Growth")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(dates, values, color="black")
    ax.set_xlabel("Datum")
    ax.set_ylabel("Portföljvärde (USD)")
    st.pyplot(fig, use_container_width=True)

    st.markdown("### 🧾 Reports")
    for r in reports:
        st.markdown(f"- 📄 **{r['Datum']}** — {r['Fil']}")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Data simulerad – koppla CLI senare för riktig analys")
