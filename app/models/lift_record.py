import uuid
from sqlalchemy import Column, Float, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
from app.database import Base

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
