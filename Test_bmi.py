import Lab2.bmi as bmi


def test_bmi_normal_weight():
    bmi_range = bmi.calculate_bmi(1.73, 57)

    assert (bmi_range == 0)


def test_bmi_over_weight():
    bmi_range = bmi.calculate_bmi(1.8, 150)

    assert (bmi_range == 1)


def test_bmi_under_weight():
    bmi_range = bmi.calculate_bmi(1.8, 50)

    assert (bmi_range == -1)
