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
        """_Przedmieścia Pune, poniedziałek, środek peaku_

Z cudownego snu, w którym przeżywałeś ponownie wspaniałe przygody z wyprawy do Wroklaw budzi Cię dźwięk budzika.
Obroża z lokalizatorem lekko uwiera Cię w szyję, żona założyła Ci ją po powrocie z tej wycieczki...

Jest 13:45, za 15 minut Twój zespół ma daily calla a ci idioci z którymi pracujesz pewnie nie poradzą sobie bez Ciebie.

**Co robisz?**"""
    )
)

st.page_link("pages/taxi_1.py", label="Wstajesz i zamawiasz taksówkę", icon="🚕")
st.page_link("pages/taxi_2.py", label="Chuj z tym, Pallavi to ogarnie", icon="🛌🏾")
