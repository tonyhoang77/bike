shops = []
customers = []

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
    def add(self, bicycle):
        if bicycle.name in self.inventory:
            count, cost = self.inventory[bicycle.name]
            self.inventory[bicycle.name] = (count + 1, cost)
        else:
            bicycle.retail_cost = bicycle.cost * self.margin
            self.inventory[bicycle.name] = (1, bicycle.retail_cost)
    def sell(self, customer, bicycle):
        _, cost = self.inventory[bicycle.name]
        if cost <= customer.funds:
            customer.funds = customer.funds - cost
            self.profit = self.profit + cost
            print(self.profit)
            if bicycle.name in customer.owned:
                customer.owned[bicycle.name] = customer.owned[bicycle.name] + 1
            else:
                customer.owned[bicycle.name] = 1
        else:
            print("This customer does not have enough funds.")
            
        
        
class Customer(object):
    def __init__(self, name, funds):
        self.funds = funds
        self.name = name
        self.owned = {
        
    }
    #customers.append(self)
    
#    def can_buy(self, shops):
#        print(self.funds)
#        for shop in shops:
#            available_bikes = []
#            for bikes in shop.price:
#                if self.funds >= shop.price[bikes]:
#                    available_bikes.append((shop, bikes, shop.price[bikes]))

def can_buy(customers):
    for x in customers:
        print(x.name)
        print('Available Funds: ' + x.funds)
        for y in shops:
            available_bikes = []
            for z in y.inventory:
                if x.funds >= z[1]:
                    available_bikes.append((z[0],y.name))
        print(available_bikes)
        available_bikes = []