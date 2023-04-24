from typing import List


class Item:
    def __init__(self, name: str, price: float, item_type: str):
        self.name = name
        self.price = price
        self.item_type = item_type



class Checkout:
    def calculate_total(self, state: str, items: List[Item]):
        tax_rate = 0.0
        total = 0.0
        if state == 'NJ':
            tax_rate = 0.066
        elif state == 'PA':
            tax_rate = 0.06
        if state not in ['DE','NJ','PA']:
            raise ValueError('Invalid State, please try again')












