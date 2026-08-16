def calculate_score(inflation, unemployment, gdp,interest_rate):
    
    score = 0 
    
    if inflation <= 2:
        score += 25
    elif inflation <= 4:
        score += 15
    else: 
        score += 5

    if unemployment <= 4:
        score += 25
    elif unemployment <= 6:
        score += 15
    else: 
        score += 5

    if gdp >= 25000:
        score += 25
    elif gdp >= 20000:
        score += 15
    else:
        score += 5
    
    if interest_rate <= 3:
        score += 25
    elif interest_rate <= 5:
        score += 15
    else:
        score += 5
    
    return score

def determine_assessment(score, risk_tolerance):
    if risk_tolerance == "Conservative":
        if score >= 85:
            return "Healthy"
        elif score >= 65:
            return "Stable"
        elif score >= 45:
            return "Weak"
        else:
            return "High Risk"

    elif risk_tolerance == "Moderate":
        if score >= 75:
            return "Healthy"
        elif score >= 55:
            return "Stable"
        elif score >= 35:
            return "Weak"
        else:
            return "High Risk"

    else:
        if score >= 65:
            return "Healthy"
        elif score >= 45:
            return "Stable"
        elif score >= 25:
            return "Weak"
        else:
            return "High Risk"
                