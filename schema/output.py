from pydantic import BaseModel
from typing import List,Optional

class UserRequest(BaseModel):
    origin: str
    destination: str
    number_of_days: int
    travel_style: str
    departure_date: str
    return_date: Optional[str]
    interests: List[str]
    pace: str


class Flight(BaseModel):
    airline: str
    currency: str
    total_price: float
    duration: int
    stops: int

class Recommendation(BaseModel):
    name: str
    area: str

class Activity(BaseModel):
    category: str
    area: str
    time_of_day: str

class Budget(BaseModel):
    total_estimated_budget: float
    currency:str