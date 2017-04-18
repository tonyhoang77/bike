from bike import *

#initialize bike shop
bikeshop = Shop('The Only Bike Shop', 1.20)

#initialize bikes
turbo = Bicycle('Turbo 3000', 50, 300)
nasbike = Bicycle('Daytona Nasbike', 100, 400)
schwepps = Bicycle('Schweppcycle', 74, 200)
dirt = Bicycle('Dirt Cheap Bike', 10, 50)
trike = Bicycle('Trike', 20, 100)
nvidia = Bicycle('Nvidia GeForce GTX 1080', 30, 799)

#initialize customers
bob = Customer('Billy Bob', 200)
mike = Customer('Michael Vanderwinkle', 500)
elonmusk = Customer('Elon Fricken Musk', 1000)
john = Customer('John Smith', 500)
jake = Customer('Jake Gylenhaal', 1000)
joe = Customer('Joe Dirt', 400)

bikeshop.add(turbo, 2)
bikeshop.add(nasbike, 1)
bikeshop.add(schwepps, 4)
bikeshop.add(dirt, 7)
bikeshop.add(trike, 3)
bikeshop.add(nvidia, 2)
    
print(bikeshop.inventory)

bikeshop.sell(bob, dirt)
bikeshop.sell(mike, nasbike)
bikeshop.sell(elonmusk, nvidia)

print("{0} has made ${1} in profit from these sales. Below is the remaining inventory.".format(bikeshop.name, bikeshop.profit))
print(bikeshop.inventory)
can_buy(customers, bikeshop)