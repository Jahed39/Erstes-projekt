from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///tagebuch.db")
SessionLocal = sessionmaker(bind=engine)

class Eintrag(Base):
    __tablename__ = "eintraege"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    stimmung = Column(String)
    score = Column(Float)
    emotion = Column(String)
    datum = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

def save_eintrag(text, analyse):
    db = SessionLocal()
    eintrag = Eintrag(
        text=text,
        stimmung=analyse["stimmung"],
        score=analyse["score"],
        emotion=analyse["emotion"]
    )
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    db.close()
    return {"id": eintrag.id, "stimmung": eintrag.stimmung, "score": eintrag.score, "emotion": eintrag.emotion}

def get_eintraege(limit=50):
    db = SessionLocal()
    eintraege = db.query(Eintrag).order_by(Eintrag.datum.desc()).limit(limit).all()
    db.close()
    return [{"id": e.id, "text": e.text, "stimmung": e.stimmung, "score": e.score, "emotion": e.emotion, "datum": str(e.datum)} for e in eintraege]