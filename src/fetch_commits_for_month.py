#!/usr/bin/env python3
import sys

from urllib.error import HTTPError
from time import gmtime, strftime
from fetch_commits import fetch_and_parse_commits


def fetch_and_parse_commits_for_month(year, month):
    """
    Fetch and parse commits for a given month.
    :param year: year in yyyy format
    :param month: month in mm format
    """
    for day in range(1, 31):
        for hour in range(0, 24):
            time = strftime("%H:%M:%S", gmtime())
            print(f"[{time}] Downloading commits for {year}-{month}-{day}-{hour}")
            try:
                fetch_and_parse_commits(f"{year}-{month}-{day:02}-{hour}")
            except HTTPError:
                print("Error, skipping.")


fetch_and_parse_commits_for_month(sys.argv[1], sys.argv[2])
