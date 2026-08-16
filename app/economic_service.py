from dotenv import load_dotenv
import os

import requests
import pandas as pd
import plotly.express as px
import time

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

def get_indicator(function_name):
    url = (
        f"https://www.alphavantage.co/query?"
        f"function={function_name}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    time.sleep(1)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])

    return df.sort_values("date")


def get_gdp():
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=REAL_GDP"
        f"&interval=annual"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    time.sleep(1)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])

    return df.sort_values("date")

def get_federal_funds_rate():
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=FEDERAL_FUNDS_RATE"
        f"&interval=monthly"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    time.sleep(1)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])

    return df.sort_values("date")



# test code
#print(
#    get_indicator(
#        "INFLATION"
#    ).tail()
#)    
