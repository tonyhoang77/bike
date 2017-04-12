from bike import *

#initialize bike shop
bikeshop = Shop('The Only Bike Shop', 1.20)

#initialize bikes
turbo = Bicycle('Turbo 3000', 50, 300)
nasbike = Bicycle('Daytona Nasbike', 100, 500)
schwepps = Bicycle('Schweppcycle', 74, 200)
dirt = Bicycle('Dirt Cheap Bike', 10, 50)
trike = Bicycle('Trike', 20, 100)
nvidia = Bicycle('Nvidia GeForce GTX 1080', 30, 799)

#initialize customers
bob = Customer('Billy Bob', 200)
mike = Customer('Michael Vanderwinkle', 500)
elonmusk = Customer('Elon Fricken Musk', 1000)

#add bikes to inventory, i know it's redundant 
#i'll put code to set quantity in class later
bikeshop.add(turbo)
bikeshop.add(turbo)
bikeshop.add(nasbike)
bikeshop.add(schwepps)
bikeshop.add(schwepps)
bikeshop.add(schwepps)
bikeshop.add(schwepps)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(dirt)
bikeshop.add(trike)
bikeshop.add(trike)
bikeshop.add(trike)
bikeshop.add(nvidia)