class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None, total=0, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
        
    def add_item(self, name, price, quantity=1):
        self.total += price * quantity
        [self.items.append((name,price)) for i in range(quantity)]
        return self.total
    
    def mean_item_price(self):
        item_prices = []
        for item in self.items:
            item_prices.append(item[1])
        return sum(item_prices)/len(item_prices)

    def median_item_price(self):
        num_items = len(self.items)
        sorted_prices = [x[1] for x in self.items]
        sorted_prices.sort()
        if num_items % 2 == 0:
            return sorted_prices[num_items/2 - 1] + sorted_prices[num_items/2] / 2
        else:
            return sorted_prices[int((num_items-1)/2)]

    def apply_discount(self):
        if self.employee_discount:
            return self.total * (1 - (self.employee_discount/100))
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        self.total -= self.items.pop()[1]
        