import time

import streamlit as st

st.set_page_config(page_title="Global Simulator", page_icon="🎲")


def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


st.header("🌏 Global Simulator", divider="rainbow")

st.write_stream(
    stream_text(""">**Ty:** Hello?
>
> **Pallavi:** Think Sharad got disconnected. Will check with him later.

Rozłączasz się, w sumie to nie powinieneś tracić swojego cennego czasu
na takie pierdoły jak calle z ludźmi z niższej kasty niż Ty.

Spokojnie dojeżdżasz do biura. Wchodzisz do środka, odbijasz się na bramce
i czekasz na windę. Kiedy podchodzisz do biurka, Pallavi Cię zagaduje i mówi,
że w piątek, kiedy Cię nie było, Mark i Patryk byli na callu z dyrektorami
w sprawie CGM, a chwilę temu klient ustawił calla. Forwardowała Ci go, bo Cię
nie zaprosili. Myślisz sobie, że to pewnie przez błąd Outlooka.

**Co jej odpowiadasz?**""")
)

st.page_link(
    "pages/gs_call_1.py",
    label="Upewniasz się, że ona też się wdzwoni i rezerwujesz sobie salkę na calla",
    icon="📠",
)
st.page_link(
    "streamlit_app.py",
    label="Mówisz jej, że sam sobie z tym poradzisz (WYMAGANE: CHARYZMA 1)",
    icon="🤚🏾",
    disabled=True,
)
