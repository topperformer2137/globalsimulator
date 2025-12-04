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
        """Przewracasz się na drugi bok i zamykasz oczy. Po co masz się męczyć, przecież jesteś na szczycie.
Zespół z Pune sobie poradzi, a Pallavi jakoś pogoni tych debili z Wroklaw i wieśniaków z Chennai.

_Czujesz silne uderzenie w głowę_

> Wstawaj nierobie jeden! Zamówiłam Ci taksówkę!

Zwlekasz się z łóżka i dziękujesz żonie za pomoc w podjęciu tej trudnej acz słusznej decyzji.
Bez Ciebie cały bank mógłby upaść, nie możesz na to pozwolić.

Szybko jesz śniadanie i wychodzisz. Wsiadasz do taksówki, call zaczął się chwilę temu.
Łączysz się z telefonu.

> **Pallavi:** ...any update on CGM? Think Sharad was going to chase GM.
Patryk, do you know anything? ... Do we have Patryk on call?

**Co robisz?**"""
    )
)

st.page_link("pages/daily_call_1.py", label="Powiedz, że wysłałeś chasera", icon="✉️")
st.page_link("pages/daily_call_1.py", label="Opierdol Patryka", icon="❗")
