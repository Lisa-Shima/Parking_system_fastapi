from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ParkingLot(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    available_spots: int

    class Config:
        from_attributes = True

class ParkingLotDetails(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    available_spots: int
    description: Optional[str] = None  # Example of additional field

    class Config:
        from_attributes = True

class ReservationRequest(BaseModel):
    lot_id: int
    user_id: int
    start_time: datetime
    end_time: datetime

class ReservationResponse(BaseModel):
    reservation_id: int
    lot_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    status: str  # e.g., "Confirmed", "Pending"

    class Config:
        from_attributes = True
        
        
class ParkingLotResponse(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    available_spots: int

    class Config:
        orm_mode = True
        
        
class ReservationResponse(BaseModel):
    id: int
    user: str
    spot_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        orm_mode = True