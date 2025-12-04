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
        """Włączasz Zooma, po chwili wdzwania się ktoś od klieta.

> **Ty:** Hello. _(kaszel)_ How are you doing?
>
> **Klient:** _(imitując hinduski akcent)_ How are you doing?
> _(podnosząc głos)_ How am I doing? You missed the deadline,
> ignored 5 chasers and you're asking me how am I doing? Are you
> serious?
>
> **Ty:** So-so-so-so-sorry, sir!
>
> **Klient:** When can we expect the reports?
>
> **Ty:** Wi-wi-wi-will share reports today, okie?
>
> **Klient:** Good, just make sure data there is correct.
>
> **Ty:** Everything will be krekt, sir!

Rozłączasz się i wychodzisz z salki. Ale im pokazałeś! Właśnie tak
powinno się obchodzić z klientami! Podchodzisz do swojego biurka, Pallavi
jest lekko zdziwiona, że tak szybko poszło, pyta jak było."""
    )
)

st.page_link(
    "pages/the_end.py",
    label="Powiedz jej, że wymieniliście się wymaganiami",
    icon="🤥",
)
st.page_link(
    "streamlit_app.py",
    label="Powiedz jej prawdę (BRAK WYMAGANEGO PRZEDMIOTU: JAJA)",
    icon="🥚",
    disabled=True,
)
