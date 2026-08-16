# this is the "web_app/routes/economic_routes.py" file...
import time 
import plotly.express as px
from flask import Blueprint, request, render_template
from app.economic_service import (
    get_indicator,
    get_gdp,
    get_federal_funds_rate
)

economic_routes = Blueprint("economic_routes", __name__)

@economic_routes.route("/economic/form")
def form():
    print("ECONOMIC FORM...")
    return render_template("economic_form.html")

@economic_routes.route('/economic/results', methods=['POST'])
def results():
    print("ECONOMIC RESULTS...")
    print(dict(request.form))
    
    # Get the user's choice from the form data
    risk_tolerance = request.form.get('risk_tolerance')
    
    inflation_df = get_indicator(
        "INFLATION"
    )

    inflation_fig = px.line(
        inflation_df,
        x="date",
        y="value",
        title="US Inflation Rate Over Time",
        labels={
            "date": "Year",
            "value": "Inflation Rate (%)"
        }
    )
    inflation_chart = inflation_fig.to_html(
        full_html=False
    )

    time.sleep(1)

    unemployment_df = get_indicator(
        "UNEMPLOYMENT"
    )   
    
    unemployment_fig = px.line(
        unemployment_df,
        x="date",
        y="value",
        title="US Unemployment Rate Over Time",
        labels={
            "date": "Year",
            "value": "Unemployment Rate (%)"
        }
    )
    unemployment_chart = unemployment_fig.to_html(
        full_html=False
    )

    time.sleep(1)

    gdp_df = get_gdp()

    gdp_fig = px.line(
        gdp_df,
        x="date",
        y="value",
        title="US Real GDP Over Time",
        labels={
            "date": "Year",
            "value": "GDP ($)"
        }
    )
    gdp_chart = gdp_fig.to_html(
        full_html=False
    )  

    time.sleep(1)

    fed_funds_df = get_federal_funds_rate()
    
    interest_fig = px.line(
        fed_funds_df,
        x="date",
        y="value",
        title="Federal Funds Rate Over Time",
        labels={
            "date": "Year",
            "value": "Interest Rate (%)"
        }
    )
    interest_chart = interest_fig.to_html(
        full_html=False
    )  

    latest_inflation=round(
        inflation_df.iloc[-1]["value"], 
        2
    )

    latest_unemployment=round(
        unemployment_df.iloc[-1]["value"], 
        2
    )

    latest_gdp=round(
        gdp_df.iloc[-1]["value"], 
        2
    )

    latest_interest_rate=round(
        fed_funds_df.iloc[-1]["value"],
        2
    )

    score = 0 
    if latest_inflation <= 2:
        score += 25
    elif latest_inflation <= 4:
        score += 15
    else: 
        score += 5

    if latest_unemployment <= 4:
        score += 25
    elif latest_unemployment <= 6:
        score += 15
    else: 
        score += 5

    if latest_gdp >= 25000:
        score += 25
    elif latest_gdp >= 20000:
        score += 15
    else:
        score += 5
    
    if latest_interest_rate <= 3:
        score += 25
    elif latest_interest_rate <= 5:
        score += 15
    else:
        score += 5
    
    if risk_tolerance == "Conservative":
        if score >= 85:
            assessment = "Healthy"
        elif score >= 65:
            assessment = "Stable"
        elif score >= 45:
            assessment = "Weak"
        else:
            assessment = "High Risk"
        
    elif risk_tolerance == "Moderate":
        if score >= 75:
            assessment = "Healthy"
        elif score >= 55:
            assessment = "Stable"
        elif score >= 35:
            assessment = "Weak"
        else:
            assessment = "High Risk"

    else: # Aggressive
        if score >= 65:
            assessment = "Healthy"
        elif score >= 45:
            assessment = "Stable"
        elif score >= 25:
            assessment = "Weak"
        else:
            assessment = "High Risk"

    if risk_tolerance == "Conservative":
        if assessment == "Healthy":
            guidance = (
                "Economic conditions appear strong. As a conservative "
                "investor, you may consider gradually increasing market "
                "exposure while maintaining diversification and risk controls."
            )
        
        elif assessment == "Stable":
            guidance = (
                "The economy appears stable. As a conservative investor, "
                "maintaining a balanced portfolio and avoiding excessive "
                "risk may be appropriate."
            )

        elif assessment == "Weak":
            guidance = (
                "Economic conditions are showing signs of weakness. "
                "Conservative investors may prefer defensive investments "
                "and a more cautious strategy."
            )

        else:
            guidance = (
                "Economic risk appears elevated. Conservative investors "
                "may wish to prioritize capital preservation and limit "
                "exposure to highly volatile assets."
            )

    elif risk_tolerance == "Moderate":
        if assessment == "Healthy":
            guidance = (
                "Economic conditions are healthy. A balanced approach with "
                "a mix of growth and defensive investments may be suitable."
            )

        elif assessment == "Stable":
            guidance = (
                "The economy appears stable. Moderate investors may benefit "
                "from maintaining a diversified portfolio aligned with "
                "long-term objectives."
            )
        
        elif assessment == "Weak":
            guidance = (
                "Economic conditions are weakening. Moderate investors may "
                "wish to review portfolio allocations and monitor risk levels."
            )
        
        else:
            guidance = (
                "Economic uncertainty is elevated. A more selective approach "
                "to investing may help manage potential downside risks."
            )

    else: # Aggressive
        if assessment == "Healthy":
            guidance = (
                "Strong economic conditions may create opportunities for "
                "growth-oriented investments. Aggressive investors may be " 
                "comfortable pursuing higher-return opportunities."
            )

        elif assessment == "Stable":   
            guidance = (
                "The economy appears stable. Aggressive investors may still "
                "find attractive growth opportunities while remaining aware "
                "of potential market fluctuations."
            )

        elif assessment == "Weak":
            guidance = (
                "Economic conditions are weak. Aggressive investors may "
                "identify opportunities during periods of market weakness, "   
                "but should be prepared for increased volatility."
        )
        
        else:
            guidance = (
                "Economic risk is high. While aggressive investors may seek "
                "opportunities in distressed markets, significant downside "
                "risk remains and careful analysis is important."
            )

    return render_template("economic_results.html",
        risk_tolerance=risk_tolerance,
        score=score,
        assessment=assessment,
        guidance=guidance,

        inflation=latest_inflation,
        unemployment=latest_unemployment,
        gdp=latest_gdp,
        interest_rate=latest_interest_rate,

        inflation_chart=inflation_chart,
        unemployment_chart=unemployment_chart,
        gdp_chart=gdp_chart,
        interest_chart=interest_chart
    )