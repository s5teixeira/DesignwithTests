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
        if state not in ['DE', 'NJ', 'PA']:
            raise ValueError('Invalid state')

        for item in items:
            if item.item_type == 'Wic Eligible food':
                total += item.price  # tax exempt in all three states
            elif item.item_type == 'Clothing':
                if 'Fur' in item.name and state == 'NJ':
                    total += item.price * (1 + tax_rate)  # fur is taxable
                else:
                    total += item.price  # clothing exempt in pa nj
            else:
                total += item.price * (1 + tax_rate)  # everything else in default tax rates

        return float(total)
