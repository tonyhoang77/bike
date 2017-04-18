shops = []
customers = {
    
}

class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.retail_cost = 0
        
class Shop(object):
    def __init__(self, name, margin):
        self.inventory = {
            
        }
        self.name = name
        self.margin = margin
        self.profit = 0
        shops.append(name)
    def add(self, bicycle, amount):
        if bicycle.name in self.inventory:
            count, bicycle.retail_cost = self.inventory[bicycle.name]
            self.inventory[bicycle.name] = (count + amount, bicycle.retail_cost)
        else:
            bicycle.retail_cost = bicycle.cost * self.margin
            self.inventory[bicycle.name] = (amount, bicycle.retail_cost)
    def sell(self, customer, bicycle):
        count, bicycle.retail_cost = self.inventory[bicycle.name]
        if bicycle.retail_cost <= customer.funds:
            customer.funds = customer.funds - bicycle.retail_cost
            self.profit = self.profit + bicycle.retail_cost
            if self.inventory[bicycle.name][0] > 1:
                self.inventory[bicycle.name] = (count - 1, bicycle.retail_cost)
            else:
                del self.inventory[bicycle.name]
            if bicycle.name in customer.owned:
                customer.owned[bicycle.name] = customer.owned[bicycle.name] + 1
            else:
                customer.owned[bicycle.name] = 1
            print("{0} has bought a {1} for ${2}, and has ${3} left".format(customer.name, bicycle.name, bicycle.retail_cost, customer.funds))
            customers[customer.name] = customer.funds
        else:
            print("This customer does not have enough funds.")
            
        
        
class Customer(object):
    def __init__(self, name, funds):
        self.funds = funds
        self.name = name
        self.owned = {
        
    }
        customers[self.name] = self.funds
    
def can_buy(customers, shop):
    for customer in customers.keys():
        print(customer)
        print('Available Funds: {0}'.format(customers[customer]))
        available_bikes = []
        for bicycle in shop.inventory:
            if customers[customer] >= shop.inventory[bicycle][1]:
                available_bikes.append((bicycle, shop.inventory[bicycle][1]))
        print(available_bikes)
        available_bikes = []