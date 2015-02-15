# -*- coding: utf-8 -*-
import pytest
from .factories import SaleFactory, SaleDetailFactory


@pytest.fixture()
def sale_data():
    sales = SaleFactory.create_batch(4)
    for sale in sales:
        SaleDetailFactory.create_batch(2, sale=sale)
    return sales
