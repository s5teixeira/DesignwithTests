from production import Checkout, Item

def test_NJ_Wic():
    checkout = Checkout()
    items = [Item('Apples', 2.5, 'Wic Eligible food')]
    assert checkout.calculate_total('NJ', items) == 2.5

def test_PA_Clothing():
    checkout = Checkout()
    items = [Item('T-shirt', 10.0, 'Clothing')]
    assert checkout.calculate_total('PA', items) == 10.0

def test_DE_Everything_else():
    checkout = Checkout()
    items = [Item('Book', 15.0, 'Books'), Item('Book2', 25.0, 'Books')]
    assert checkout.calculate_total('DE', items) == 40.0

def test_NJ_Fur():
    checkout = Checkout()
    items = [Item('Fur coat', 500.0, 'Clothing')]
    assert checkout.calculate_total('NJ', items) == 533.0
