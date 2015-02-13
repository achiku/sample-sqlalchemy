# -*- coding: utf-8 -*-
import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Factory as FakerFactory
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from ..models import (
    Base, Customer, Item, Sale, SaleDetail,
)

session = scoped_session(sessionmaker())
engine = create_engine('sqlite://')
session.configure(bind=engine)
Base.metadata.create_all(engine)
faker = FakerFactory.create()


class CustomerFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Customer
    FACTORY_SESSION = session

    id = factory.Sequence(lambda n: n)
    screen_name = factory.Sequence(lambda n: u'user{}'.format(n))
    sex = factory.Iterator([1, 2])
    birth_day = factory.LazyAttribute(lambda x: faker.date())


class ItemFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Item
    FACTORY_SESSION = session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: u'item{}'.format(n))
    price = factory.Iterator([100, 200, 500, 1000])


class SaleFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Sale
    FACTORY_SESSION = session

    id = factory.Sequence(lambda n: n)
    sold_at = factory.LazyAttribute(lambda x: faker.date())
    customer_id = factory.SubFactory(CustomerFactory)
    total_price = factory.Iterator([100, 200, 500, 1000])


class SaleDetailFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = SaleDetail
    FACTORY_SESSION = session

    id = factory.Sequence(lambda n: n)
    sale_id = factory.SubFactory(SaleFactory)
    item_id = factory.SubFactory(ItemFactory)
    item_price = factory.Iterator([100, 200, 500, 1000])
