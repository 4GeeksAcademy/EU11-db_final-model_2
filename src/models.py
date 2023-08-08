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

# MODEL 1: s-model | Version: Educative 
# A Favorite can belong only to 1 User  [An Employee can be assiciated with only 1 Department] > FK on Favorite table
# A User can have many Favorites [A Department can have multiple Employees] > relationship on User table 

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    # Added
    favorites = relationship('Favorites', backref = 'users')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    #Added
    users_id = Column(String, ForeignKey('users.id'), nullable = False)

    # stadiums = relationship('Stadiums', backref = 'favorites')
    # user_id = Column(Integer, ForeignKey("user.id"))
    # stadium_id = Column(Integer, ForeignKey("stadium.id"))
    # stadiums = relationship('Stadiums')
    # users = relationship('User')

# MODEL 2 | Version: Star wars template 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  
    users = relationship('User', backref = 'favorite')
    


# class Visisted(Base):
#     __tablename__ = 'visited'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     stadium_id = Column(Integer, ForeignKey("stadium.id"))

#     # stadiums = relationship('Stadiums')
#     # users = relationship('User')

# class Reviews(Base):
#     __tablename__ = 'reviews'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     stadium_id = Column(Integer, ForeignKey("stadium.id"))
#     review_rating = Column(Integer, nullable=False)
#     review_text = Column(String(1000), nullable=False)
#     # stadiums = relationship('Stadiums')
#     # users = relationship('User')

# class Stadiums(Base):
#     __tablename__ = 'stadiums'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     address = Column(String(250))
#     city = Column(String(250))
#     country = Column(String(250))
#     surface = Column(String(250))
#     image = Column(String(250))
#     # favorites = Column(Integer, ForeignKey('favorites.id'))
#     # reviews = Column(Integer, ForeignKey('reviews.id'))
#     # visited = Column(Integer, ForeignKey('visited.id'))
#     # reviews = Column(Integer, ForeignKey('review.id'))





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
