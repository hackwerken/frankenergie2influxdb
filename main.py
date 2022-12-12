#!/usr/bin/env python3


import argparse
import toml
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import frankenergie

parser = argparse.ArgumentParser()
parser.add_argument('-f', metavar='config file', required=True, type=str)


def main():

    args = parser.parse_args()
    config = toml.load(args.f)
    config_influx = config["influxdb"]

    influxdb = influxdb_client.InfluxDBClient(
        url=config_influx["url"],
        token=config_influx["token"],
        org=config_influx["org"])

    influx_api = influxdb.write_api(write_options=SYNCHRONOUS)

    prices = frankenergie.get_tomorrows_prices()

    for entry in prices:
        time = entry["from"]
        market_price = entry["marketPrice"]
        market_price_tax = entry["marketPriceTax"]
        sourcing_markup_price = entry["sourcingMarkupPrice"]
        energy_tax_price = entry["energyTaxPrice"]
        all_in = market_price + \
            market_price_tax +  \
            sourcing_markup_price + \
            energy_tax_price

        point = influxdb_client.Point(config_influx["measurement"]) \
            .time(time) \
            .tag("provider", "Frank Energie") \
            .field("marketPrice", market_price) \
            .field("marketPriceTax", market_price_tax) \
            .field("sourcingMarkupPrice", sourcing_markup_price) \
            .field("energyTaxPrice", energy_tax_price) \
            .field("allIn", all_in)

        influx_api.write(config_influx["bucket"], config_influx["org"], point)

        print("Writing", time, all_in)

if __name__ == "__main__":
    main()