import os
import math
import uuid
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Float, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, sessionmaker

# -------------------------------------------------
# ENV
# -------------------------------------------------
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# -------------------------------------------------
# APP
# -------------------------------------------------
app = FastAPI(
    title="ProQee Engineering Core",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# DB
# -------------------------------------------------
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class LiftRecord(Base):
    __tablename__ = "lift_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    load_t = Column(Float)
    sling_angle_deg = Column(Float)
    number_of_legs = Column(Integer)
    daf = Column(Float)
    sling_wll_t = Column(Float)
    factored_load_t = Column(Float)
    tension_per_leg_t = Column(Float)
    utilization = Column(Float)
    status = Column(String)
    messages = Column(JSONB)
    advisory = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# MODELS
# -------------------------------------------------
class LiftSummaryRequest(BaseModel):
    load_t: float
    sling_angle_deg: float
    number_of_legs: int
    daf: float
    sling_wll_t: float

class LiftSummaryResponse(BaseModel):
    factored_load_t: float
    tension_per_leg_t: float
    utilization: float
    status: str
    messages: List[str]
    advisory: List[str]

class EnvelopeRequest(BaseModel):
    load_t: float
    number_of_legs: int
    daf: float
    sling_wll_t: float

# -------------------------------------------------
# ROUTES
# -------------------------------------------------
@app.get("/")
def health():
    return {"status": "ok"}

# -------------------------------------------------
# LIFT SUMMARY (SAVE TO DB)
# -------------------------------------------------
@app.post("/calculate/lift-summary", response_model=LiftSummaryResponse)
def calculate_lift_summary(data: LiftSummaryRequest):
    angle_rad = math.radians(data.sling_angle_deg)
    messages, advisory = [], []

    factored_load = data.load_t * data.daf
    tension = factored_load / (data.number_of_legs * math.cos(angle_rad))
    utilization = tension / data.sling_wll_t

    if utilization > 1:
        status = "FAIL"
        messages.append("❌ Sling utilization exceeds 100%")
        advisory.append(f"Increase sling WLL to ≥ {round(tension * 1.1,1)} t")
        advisory.append("Or add an additional sling leg")
    elif utilization >= 0.8:
        status = "WARNING"
        messages.append("⚠ Sling utilization above 80%")
        advisory.append("Consider higher WLL or angle")
    else:
        status = "OK"
        messages.append("✅ Lift within acceptable limits")
        advisory.append("No action required")

    db = SessionLocal()
    db.add(
        LiftRecord(
            load_t=data.load_t,
            sling_angle_deg=data.sling_angle_deg,
            number_of_legs=data.number_of_legs,
            daf=data.daf,
            sling_wll_t=data.sling_wll_t,
            factored_load_t=factored_load,
            tension_per_leg_t=tension,
            utilization=utilization,
            status=status,
            messages=messages,
            advisory=advisory,
        )
    )
    db.commit()
    db.close()

    return LiftSummaryResponse(
        factored_load_t=round(factored_load, 3),
        tension_per_leg_t=round(tension, 3),
        utilization=round(utilization, 2),
        status=status,
        messages=messages,
        advisory=advisory,
    )

# -------------------------------------------------
# ENGINEERING ENVELOPE (NO DB WRITE)
# -------------------------------------------------
@app.post("/calculate/angle-envelope")
def calculate_angle_envelope(data: EnvelopeRequest):
    points = []
    factored_load = data.load_t * data.daf

    for angle in range(30, 91, 2):
        rad = math.radians(angle)
        tension = factored_load / (data.number_of_legs * math.cos(rad))
        utilization = tension / data.sling_wll_t

        points.append({
            "angle": angle,
            "utilization": round(utilization, 3)
        })

    return {
        "points": points,
        "limits": {
            "warning": 0.8,
            "fail": 1.0
        }
    }

# -------------------------------------------------
# HISTORY
# -------------------------------------------------
@app.get("/lifts")
def list_lifts():
    db = SessionLocal()
    records = db.query(LiftRecord).order_by(LiftRecord.created_at.desc()).all()
    db.close()
    return records

