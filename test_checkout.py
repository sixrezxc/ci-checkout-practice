def calculate_total(items_total, delivery_price):
    return items_total


def test_total_includes_delivery():
    assert calculate_total(2000, 300) == 2300
