# -*- coding: utf-8 -*-
from ..models import Sale


def test_sales(sale_data):
    top_sales = Sale.query.filter(
       Sale.total_price >= 400
    )
    print "# of sales above 400: {}".format(top_sales.count())
    for sale in top_sales.all():
        print sale.sold_at, sale.customer.name, sale.total_price

    assert False
