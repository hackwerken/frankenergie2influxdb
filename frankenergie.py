#!/usr/bin/env python3

import datetime
from python_graphql_client import GraphqlClient


client = GraphqlClient(endpoint="https://graphcdn.frankenergie.nl")


def get_prices(date_start, date_end):

    start_str = date_start.isoformat()
    end_str = date_end.isoformat()

    query = f"""
query MarketPrices {{
marketPricesElectricity(startDate: "{start_str}", endDate: "{end_str}") {{
    till
    from
    marketPrice
    marketPriceTax
    sourcingMarkupPrice
    energyTaxPrice
}}
}}
    """

    prices = client.execute(query)["data"]["marketPricesElectricity"]
    return prices


def get_todays_prices() :
    start = datetime.date.today()
    end = start + datetime.timedelta(days=1)

    return get_prices(start, end)

def get_tomorrows_prices() :
    start = datetime.date.today() + datetime.timedelta(days=1)
    end = start + datetime.timedelta(days=1)
    return get_prices(start, end)
