# Economic-Pulse-App
Economic Pulse: Economic Health &amp; Market Conditions Analyzer

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

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"

# also tell flask where our web app is defined:
FLASK_APP=web_app
```

## Usage

Run RPS game:

```sh
python -m app.rps
```

Run stocks dashboard:

```sh
ALPHAVANTAGE_API_KEY="14SJGKTZQOG2TCYK" python -m app.stocks

python -m app.stocks
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
```
# 'ctrl + c' to stop and 'flask run' to start again when updates made in flask web app, must restart the web server

## Testing

Run tests:

```sh
pytest
```