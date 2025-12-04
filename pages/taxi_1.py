import time

import streamlit as st

st.set_page_config(page_title="Global Simulator", page_icon="🎲")


def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


st.header("🌏 Global Simulator", divider="rainbow")

st.write_stream(
    stream_text(
        """Wyciągasz telefon i zamawiasz motorikszę.

W końcu jesteś menedżerem, możesz sobie pozwolić na przyjazd do biura w wielkim stylu!

Szybko jesz śniadanie i wychodzisz. Wsiadasz do taksówki, call zaczął się chwilę temu.
Łączysz się z telefonu.

> **Pallavi:** ...any update on CGM? Think Sharad was going to chase GM.
Patryk, do you know anything? ... Do we have Patryk on call?

**Co robisz?**"""
    )
)

st.page_link("pages/daily_call_1.py", label="Powiedz, że wysłałeś chasera", icon="✉️")
st.page_link("pages/daily_call_1.py", label="Opierdol Patryka", icon="❗")
