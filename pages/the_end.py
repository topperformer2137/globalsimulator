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
        """Mówisz Pallavi, że call był spokojny i powiedziałeś
klientowi, że dostarczycie EMSĘ jak tylko przyślą dane, a obiecali,
że zrobią to jeszcze dzisiaj. Kryzys zażegnany, dzięki Twojej
interwencji. Pallavi nie komentuje, jesteś pewien, że to łyknęła.

No, już 16:00. To był kolejny udany dzień! Czas wracać do domu.

**Ciąg dalszy nastąpi...**"""
    )
)

st.page_link("streamlit_app.py", label="Wróć do menu", icon="🔁")
