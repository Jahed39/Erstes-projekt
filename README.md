# AI-Tagebuch mit Stimmungsanalyse

Ein persönliches Tagebuch das mithilfe von KI automatisch die Stimmung deiner Einträge analysiert.

## Was das Projekt macht

- Tagebucheinträge schreiben und speichern
- KI analysiert automatisch deine Stimmung (positiv, neutral, negativ)
- Gibt dir einen Score von 1-10 und die Hauptemotion
- Alle Einträge werden in einer Datenbank gespeichert

## Technologien

- **Backend:** Python, FastAPI
- **KI:** Ollama (llama3.2) / Anthropic Claude API
- **Datenbank:** SQLite
- **Frontend:** Streamlit

## Installation

1. Pakete installieren:
   pip install fastapi uvicorn sqlalchemy streamlit requests

2. Ollama installieren: https://ollama.com
   ollama pull llama3.2

3. Backend starten:
   cd backend
   uvicorn main:app --reload

4. Frontend starten:
   cd frontend
   streamlit run app.py

5. Browser öffnen: http://localhost:8501
