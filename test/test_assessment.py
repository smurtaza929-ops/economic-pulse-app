from app.scoring import determine_assessment

def test_conservative_healthy():

    result = determine_assessment(
        90,
        "Conservative"
    )

    assert result == "Healthy"

def test_conservative_stable():
    result = determine_assessment(
        70,
        "Conservative"
    )

    assert result == "Stable"

def test_aggressive_healthy():
    result = determine_assessment(
        70,
        "Aggressive"
    )

    assert result == "Healthy"