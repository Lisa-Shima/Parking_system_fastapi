from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.config.config import get_db
from app.models.parking_model import ParkingSpot

# Importing ParkingLot schema correctly from the parking_schemas.py file
from app.schemas.parking_schemas import ParkingLot, ParkingLotDetails, ReservationRequest, ReservationResponse, ParkingLotResponse

# Ensure the correct import path for CRUD operations
from app.crud.parking_crud import list_parking_lots, get_lot_details, reserve_spot

router = APIRouter()

# Get all parking lots
@router.get("/parking-lots", response_model=list[ParkingLotResponse])
def get_parking_lots(db: Session = Depends(get_db)):
    lots = list_parking_lots(db)

    # Transform lots to include available spots
    response = [
        ParkingLotResponse(
            id=lot.id,
            name=lot.name,
            location=lot.location,
            capacity=lot.capacity,
            available_spots=db.query(ParkingSpot)
                .filter(ParkingSpot.lot_id == lot.id, ParkingSpot.is_available == True)
                .count(),
        )
        for lot in lots
    ]
    return response

# Get details for a specific parking lot
@router.get("/parking-lots/{lot_id}", response_model=ParkingLotDetails)
def get_parking_lot_details(lot_id: int, db: Session = Depends(get_db)):
    lot_data = get_lot_details(lot_id, db)

    # Construct the response object
    parking_lot = lot_data["parking_lot"]
    available_spots = len(lot_data["available_spots"])
    response = ParkingLotDetails(
        id=parking_lot.id,
        name=parking_lot.name,
        location=parking_lot.location,
        capacity=parking_lot.capacity,
        available_spots=available_spots,
        description=f"{parking_lot.name} located at {parking_lot.location} has {available_spots} spots available."
    )
    return response


# Reserve a parking spot
@router.post("/reserve", response_model=ReservationResponse)
def reserve_parking_spot(
    request: ReservationRequest, 
    db: Session = Depends(get_db), 
    user: str = "test_user"
):
    return reserve_spot(request, db, user)
    