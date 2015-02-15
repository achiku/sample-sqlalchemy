# -*- coding: utf-8 -*-
import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Factory as FakerFactory
from ..database import session, engine
from ..models import (
    Base, Customer, Item, Sale, SaleDetail,
)

Base.metadata.create_all(engine)
faker = FakerFactory.create()


class CustomerFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session = session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: u'user{}'.format(n))
    sex = factory.Iterator([1, 2])
    birth_day = factory.LazyAttribute(lambda x: faker.date_time())
    joined_at = factory.LazyAttribute(lambda x: faker.date_time())


class ItemFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Item
        sqlalchemy_session = session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: u'item{}'.format(n))
    price = factory.Iterator([100, 200, 500, 1000])


class SaleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Sale
        sqlalchemy_session = session

    id = factory.Sequence(lambda n: n)
    sold_at = factory.LazyAttribute(lambda x: faker.date_time())
    customer = factory.SubFactory(CustomerFactory)
    total_price = factory.Iterator([100, 200, 500, 1000])


class SaleDetailFactory(SQLAlchemyModelFactory):
    class Meta:
        model = SaleDetail
        sqlalchemy_session = session

    id = factory.Sequence(lambda n: n)
    sale = factory.SubFactory(SaleFactory)
    item = factory.SubFactory(ItemFactory)
    item_price = factory.Iterator([100, 200, 500, 1000])
