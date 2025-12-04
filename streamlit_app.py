import streamlit as st

st.set_page_config(page_title="Global Simulator", page_icon="🎲")

st.header("🌏 Global Simulator", divider="rainbow")
st.subheader("Przygodowa gra przeglądarkowa")
st.markdown(
    "Wciel się w najlepszego hinduskiego menedżera i podejmuj decyzje globalnej skali!"
)
st.page_link("pages/start.py", label="Rozpocznij grę", icon="▶️")
st.markdown("_Pomysł i wykonanie: Top Performer_")
