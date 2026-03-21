import streamlit as st
import requests

st.title("Mein AI-Tagebuch")

st.subheader("Neuer Eintrag")
text = st.text_area("Was war heute?", height=150)

if st.button("Speichern & Analysieren"):
    if text:
        res = requests.post("http://127.0.0.1:8000/eintrag", json={"text": text})
        data = res.json()
        
        st.success("Eintrag gespeichert!")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Stimmung", data["stimmung"])
        col2.metric("Score", f"{data['score']}/10")
        col3.metric("Emotion", data["emotion"])
    else:
        st.warning("Bitte erst etwas schreiben!")

st.subheader("Alle Einträge")
eintraege = requests.get("http://127.0.0.1:8000/eintraege").json()

for e in eintraege:
    with st.expander(f"{e['datum']} — {e['stimmung']} ({e['score']}/10)"):
        st.write(e["text"])
        st.caption(f"Emotion: {e['emotion']}")