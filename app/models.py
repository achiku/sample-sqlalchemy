# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from .database import Base


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    screen_name = Column(String, primary_key=True)
    sex = Column(Integer)
    birth_day = Column(DateTime)
    joined_at = Column(DateTime)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    sold_at = Column(DateTime)
    customer_id = Column(Integer, ForeignKey(Customer.id))
    total_price = Column(Integer)


class SaleDetail(Base):
    __tablename__ = 'sale_detail'
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey(Sale.id))
    item_id = Column(Integer, ForeignKey(Item.id))
    item_price = Column(Integer)
