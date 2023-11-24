#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review

place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")

    amenity_ids = []

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute 
           @amenity_ids that contains all Amenity.id linked to the Place
        """
        from models import storage
        from models import Amenity
        amenity_instances = []
        for (id, obj) in storage.all(Amenity).items():
            if id in self.amenity_ids:
                amenity_instances.append(value)

        return amenity_instances

    @amenities.setter
    def amenities(self, value):
        """handles append method for adding an
           Amenity.id to the attribute amenity_ids
        """
        if isinstance(value, Amenity):
            if value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
