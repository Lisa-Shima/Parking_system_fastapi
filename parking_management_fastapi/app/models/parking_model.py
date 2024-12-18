# app/models/parking_model.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.config import Base

class ParkingLot(Base):
    __tablename__ = 'parking_lots'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity = Column(Integer)

    spots = relationship("ParkingSpot", back_populates="lot")
    


class ParkingSpot(Base):
    __tablename__ = 'parking_spots'

    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(Integer, ForeignKey('parking_lots.id'))
    is_available = Column(Boolean, default=True)
    number = Column(Integer)

    lot = relationship("ParkingLot", back_populates="spots")
    reservations = relationship("Reservation", back_populates="spot")


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user = Column(String)
    spot_id = Column(Integer, ForeignKey('parking_spots.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    spot = relationship("ParkingSpot", back_populates="reservations")
