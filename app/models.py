# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    sex = Column(Integer)
    birth_day = Column(DateTime)
    joined_at = Column(DateTime)

    def __repr__(self):
        return u"<Customer {}:{}>".format(self.id, self.name)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return u"<Item {}:{}>".format(self.id, self.name)


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    sold_at = Column(DateTime)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    total_price = Column(Integer)

    customer = relationship('Customer', uselist=False)
    details = relationship('SaleDetail')

    def __repr__(self):
        return u"<Sale {}:{}, {}>".format(
            self.id, self.sold_at, self.total_price)


class SaleDetail(Base):
    __tablename__ = 'sale_detail'
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey('sale.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    item_price = Column(Integer)

    sale = relationship('Sale', uselist=False)
    item = relationship('Item', uselist=False)

    def __repr__(self):
        return u"<SaleDetail {}:{}, {}>".format(
            self.id, self.sale_id, self.item_id)
