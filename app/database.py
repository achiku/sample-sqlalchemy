# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


session = scoped_session(sessionmaker())
engine = create_engine('sqlite://')
session.configure(bind=engine, autoflush=False)
Base = declarative_base()
Base.query = session.query_property()
