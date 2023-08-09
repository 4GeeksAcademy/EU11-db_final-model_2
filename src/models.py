import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# From Educative
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)
Base = declarative_base()

# TESTING
# MODEL 1: s-model | Version: Educative - creating the relationship on the Table without FK (the parent)  
# A Favorite can belong only to 1 User  [An Employee can be assiciated with only 1 Department] > FK on Favorite table
# A User can have many Favorites [A Department can have multiple Employees] > relationship on User table 

# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(250), nullable=False)
#     last_name = Column(String(250), nullable=False)
#     user_name = Column(String(250), nullable=False)
#     email = Column(String(250), unique=True, nullable=False)
#     password = Column(String(250), nullable=False)
#     # Added
#     favorites = relationship('Favorites', backref = 'users')

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     id = Column(Integer, primary_key=True)
#     #Added
#     users_id = Column(String, ForeignKey('users.id'), nullable = False)


# TESTING
# MODEL 2 | Version: Star wars template - creating the relationship on the same Table as the FK (the child)

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(250), nullable=False)
#     last_name = Column(String(250), nullable=False)
#     user_name = Column(String(250), nullable=False)
#     email = Column(String(250), unique=True, nullable=False)
#     password = Column(String(250), nullable=False)

# class Favorite(Base):
#     __tablename__ = 'favorite'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     users = relationship('User', backref="favorite")
   

# MODEL 3 | Version: Leo's recommendation - creating the relationship on both Tables (parent and child)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    favorite_table = relationship('Favorite', backref="user")
    visited_table = relationship('Visited', backref="user")
    review_table = relationship('Review', backref="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_table = relationship('User', backref="favorite")
    stadium_id = Column(Integer, ForeignKey("stadium.id"), nullable=False)
    stadium_table = relationship('Stadium', backref="favorite")
    
class Visisted(Base):
    __tablename__ = 'visited'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_table = relationship('User', backref="visited")
    stadium_id = Column(Integer, ForeignKey("stadium.id"), nullable=False)
    stadium_table = relationship('Stadium', backref="visited")

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_table = relationship('User', backref="review")
    stadium_id = Column(Integer, ForeignKey("stadium.id"), nullable=False)
    stadium_table = relationship('Stadium', backref="review")
    review_rating = Column(Integer, nullable=False) # to make it Impossible to send a review witout a rating
    review_text = Column(String(1000), nullable=True) # to make it possible to send a review witout a text

class Stadium(Base):
    __tablename__ = 'stadium'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    address = Column(String(250))
    city = Column(String(250))
    country = Column(String(250))
    surface = Column(String(250))
    image = Column(String(250))
    favorite_table = relationship('Favorite', backref="stadium")
    visited_table = relationship('Visited', backref="stadium")
    review_table = relationship('Review', backref="stadium")



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
