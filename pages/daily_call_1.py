import time

import streamlit as st

st.set_page_config(page_title="Global Simulator", page_icon="🎲")


def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


st.header("🌏 Global Simulator", divider="rainbow")

st.write_stream(
    stream_text("""Włączasz mikrofon i zaczynasz tyradę.
Wiesz, że twoi niewolnicy... znaczy się pracownicy je lubią.

> **Pallavi:** Sharad, you're not audible.""")
)

st.page_link("pages/daily_call_2.py", label="Hello?", icon="📞")
