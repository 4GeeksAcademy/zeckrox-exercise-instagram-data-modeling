import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20))
    email = Column(String, nullable=False, unique=True)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    followed_id = Column(Integer, ForeignKey("user.id"), nullable= False)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum("Video", "Image"))
    url = Column(String(200), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id =  Column(Integer, ForeignKey("post.id"), nullable=False)

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    liked = Column(Boolean())



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
