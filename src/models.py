import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username= Column(String(20), nullable=False)
    email= Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name= Column(String(250), nullable=False)
    gender = Column(String(250))
    height = Column(String)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name= Column(String(250), nullable=False)
    climate = Column(String(250))
    population = Column(Integer)
    diameter = Column(Float)
    terrain = Column(String(250))
    surface_water = Column(Integer)
    orbital_period = Column(Integer)

class Vehicles(Base):
    __tablename__= 'vehicles'

    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name= Column(String(250), nullable=False)
    model_name = Column(String(250))
    manufacturer= Column(String(250))
    price = (Integer)     

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))
    vehicles_id= Column(Integer, ForeignKey('vehicles.id'))

class Comments(Base):
    __tablename__='comments'

    id = Column(Integer, primary_key=True)
    comments = Column(Text)
    post_id = (Integer, ForeignKey('post.id'))
    user_id= (Integer, ForeignKey('user.id'))

# Python program to illustrate
# enumerate function
l1 = ["characters.id", "vehicles.id", "planets.id"]

class Post(Base):
    __tablename__='post'
    
    id = Column(Integer, primary_key=True)
    description = (Column, Text)
    body = Column(Text)
    type = enumerate(l1)
    type_id = (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))

 

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e