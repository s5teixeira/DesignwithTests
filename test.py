from production import Checkout, Item

def test_NJ_WIC():
    checkout = Checkout()
    items = [Item('Apples', 2.5, 'Wic Eligible food')]
    assert checkout.calculate_total('NJ', items) == 2.5

