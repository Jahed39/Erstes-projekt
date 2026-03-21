from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from claude import analyse_stimmung
from database import save_eintrag, get_eintraege

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class EintragRequest(BaseModel):
    text: str

@app.post("/eintrag")
def neuer_eintrag(eintrag: EintragRequest):
    analyse = analyse_stimmung(eintrag.text)
    return save_eintrag(eintrag.text, analyse)

@app.get("/eintraege")
def alle_eintraege():
    return get_eintraege()