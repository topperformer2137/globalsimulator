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
        """Jak zwykle miałeś rację, bez Ciebie ta firma by upadła!
Jeden dzień wolnego i taka afera.

Rezerwujesz sobie salkę "Ganges". Klient tak bardzo chce pogadać
z Tobą, legendą Mellona, że ustawił tego calla o 4 nad ranem swojego
czasu. Zabierasz laptopa i idziesz do salki. Podłączasz wszystko,
sprawdzasz ustawienie kamery. Wyglądasz zajebiście, jak zawsze.

W międzyczasie dostajesz wiadomość od Pallavi:
> **Pallavi:** My Zoom is not working. Will you handle the client
> alone?
>
> **Ty:** Of course!

Twoja klawiatura, jak i Twoje ręcę są całe mokre, chyba ktoś wyłączył
klimę..."""
    )
)

st.page_link("pages/gs_call_2.py", label="Wdzwoń się na calla", icon="📞")
