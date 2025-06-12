from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PlayBase(BaseModel):
    title: str
    date: datetime
    genre: Optional[str] = None
    synopsis: Optional[str] = None


class PlayCreate(PlayBase):
    pass


class Play(PlayBase):
    id: int

    class Config:
        from_attributes = True


class ActorBase(BaseModel):
    name: str
    gender: str
    date_of_birth: datetime


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        from_attributes = True


class DirectorBase(BaseModel):
    name: str
    date_of_birth: datetime
    citizenship: str


class DirectorCreate(DirectorBase):
    pass


class Director(DirectorBase):
    id: int

    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    name: str
    telephone_no: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True


class ShowTimeBase(BaseModel):
    date_time: datetime
    play_id: int


class ShowTimeCreate(ShowTimeBase):
    pass


class ShowTime(ShowTimeBase):
    id: int

    class Config:
        from_attributes = True


class TicketBase(BaseModel):
    ticket_no: str
    seat_id: int
    showtime_id: int
    customer_id: int
    price: float


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int

    class Config:
        from_attributes = True
