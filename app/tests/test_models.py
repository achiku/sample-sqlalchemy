# -*- coding: utf-8 -*-
from ..models import Sale


def test_sales(sale_data):
    for i in sale_data:
        print i
    print Sale.query.all()
    assert False
