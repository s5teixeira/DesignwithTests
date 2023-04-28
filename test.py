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

def test_EmptyCart():
    checkout = Checkout()
    assert checkout.calculate_total('NJ', []) == 0
    assert checkout.calculate_total('PA', []) == 0
    assert checkout.calculate_total('DE', []) == 0


def test_MultipleItemsInCart():
    checkout = Checkout()
    assert checkout.calculate_total('NJ', [Item('Apple', 0.75, 'Wic Eligible food'), Item('Milk', 2.50, 'Wic Eligible food')]) == 3.25
    assert checkout.calculate_total('PA', [Item('Shirt', 20.00, 'Clothing'), Item('Pants', 30.00, 'Clothing')]) == 50.00
    assert checkout.calculate_total('DE', [Item('Shirt', 15.00, 'everything else'), Item('Mug', 5.00, 'everything else')]) == 20.00

