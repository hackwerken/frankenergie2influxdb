# Frank energie to InfluxDB scraper

This simple script get's tomorrows prices from Frank Energie's GraphQL API, and writes them to InfluxDB.

This repo is mainly intended for my own documentation uses. But feel free to use / adapt it to your needs.

## Setup
Tested on Ubuntu 20.04. All commands must be executed as root.


    adduser --system frankenergie
    cd /home/frankenergie/
    git clone https://github.com/hackwerken/frankenergie2influxdb.git
    cd frankenergie2influxdb

    apt install python3-virtualenv
    virtualenv virtenv
    source virtenv/bin/activate
    pip3 install -r requirements.txt
    deactivate

    cp systemd/frankenergie.* /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable frankenergie.timer


