from app.scoring import calculate_score

def test_calculate_score_returns_int():
    score = calculate_score(
        2,
        4,
        26000,
        3
    )

    assert isinstance(score,int)

def test_healthy_economy_score():
    score = calculate_score(
        2,
        4,
        26000,
        3
    )

    assert score == 100

def test_weak_economy_score():

    score = calculate_score(
        8,
        8,
        15000,
        7
    )

    assert score == 20

