from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base


class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    date = Column(DateTime)
    genre = Column(String(20))
    synopsis = Column(Text)
    showtimes = relationship("ShowTime", back_populates="play")


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    gender = Column(String(1))
    date_of_birth = Column(DateTime)
    actor_plays = relationship("ActorPlay", back_populates="actor")


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    date_of_birth = Column(DateTime)
    citizenship = Column(String(100))
    director_plays = relationship("DirectorPlay", back_populates="director")


class ShowTime(Base):
    __tablename__ = "showtimes"
    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
    play_id = Column(Integer, ForeignKey("plays.id"))
    play = relationship("Play", back_populates="showtimes")


class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    row_no = Column(Integer)
    seat_no = Column(Integer)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    telephone_no = Column(String(100))
    tickets = relationship("Ticket", back_populates="customer")


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    ticket_no = Column(String(100))
    seat_id = Column(Integer, ForeignKey("seats.id"))
    showtime_id = Column(Integer, ForeignKey("showtimes.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    price = Column(Numeric(10, 2))
    customer = relationship("Customer", back_populates="tickets")


class ActorPlay(Base):
    __tablename__ = "actor_play"
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)
    actor = relationship("Actor", back_populates="actor_plays")


class DirectorPlay(Base):
    __tablename__ = "director_play"
    director_id = Column(Integer, ForeignKey("directors.id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)
    director = relationship("Director", back_populates="director_plays")
