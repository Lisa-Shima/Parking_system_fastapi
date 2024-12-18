# app/crud/parking_crud.py
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.parking_model import ParkingLot, ParkingSpot, Reservation
from app.schemas.parking_schemas import ReservationRequest, ReservationResponse
from fastapi import HTTPException

def list_parking_lots(db: Session):
    """List all parking lots."""
    return db.query(ParkingLot).all()

def get_lot_details(lot_id: int, db: Session):
    """Get details of a parking lot, including available spots."""
    lot = db.query(ParkingLot).filter(ParkingLot.id == lot_id).first()  
    if not lot:
        raise HTTPException(status_code=404, detail="Parking lot not found")
    spots = db.query(ParkingSpot).filter(ParkingSpot.lot_id == lot_id, ParkingSpot.is_available == True).all()
    return {"parking_lot": lot, "available_spots": spots}

def reserve_spot(request: ReservationRequest, db: Session, user: str):
    """Reserve a parking spot."""
    spot = db.query(ParkingSpot).filter(
        ParkingSpot.lot_id == request.lot_id, 
        ParkingSpot.is_available == True
    ).first()

    print(request.lot_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Spot not available")

    # Mark spot as reserved
    spot.is_available = False
    db.add(spot)

    # Create reservation
    reservation = Reservation(
        user=user,
        spot_id=spot.id,
        start_time=datetime.utcnow(),
        end_time=request.end_time,
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    # Return the reservation data in the expected format
    return ReservationResponse.from_orm(reservation)
