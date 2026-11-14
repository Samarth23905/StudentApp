from app import calculate_grade, calculate_total, check_result


def test_calculate_total():
    assert calculate_total([80, 75, 90]) == 245


def test_calculate_grade():
    assert calculate_grade(95) == "A"


def test_check_pass():
    assert check_result(75) == "PASS"


def test_check_fail():
    assert check_result(35) == "FAIL"
