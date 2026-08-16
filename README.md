# Economic-Pulse-App
Economic Pulse: Economic Health &amp; Market Conditions Analyzer

## Project Overview

Economic Pulse analyzes U.S. economic conditions using Inflation, Unemployment, GDP, and Interest Rates.
The application generates an Economic Health Score and provides investor guidance based on a selected risk profile.

## Features
- Economic Health Score
- Personalized Investor Guidance
- Plotly Visualizations
- Alpha Vantage API Integration
- Automated Testing with Pytest
- GitHub Actions Continuous Integration

## Technologies Used
- Python
- Flask
- Jinja2
- Bootstrap 5
- Pandas
- Plotly
- Alpha Vantage API
- Pytest
- GitHub Actions
- GitHub
- Conda
- Python Dotenv

## Running the Application 

```sh
cd ~/Documents/economic-pulse-app
```

Create a virtual environment:

```sh
conda create -n economic-pulse-app python=3.11
```

Activate the virtual environment:

```sh
conda activate economic-pulse-app
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The app's functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key)

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"

# also tell flask where our web app is defined:
FLASK_APP=web_app
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run

# Use 'ctrl + c' to stop and 'flask run' to start again when updates made in flask web app, must restart the web server
```
## Testing

Run tests:

```sh
pytest
```