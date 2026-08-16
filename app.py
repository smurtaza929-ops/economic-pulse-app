from dotenv import load_dotenv
import os

import requests
import pandas as pd
import plotly.express as px

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")