from product import Product 
from warehouse import Warehouse
from seller import Seller

product_1 = Product("Блокнот", 10, 120)
product_2 = Product("Ручка", 200, 15)
product_3 = Product("Вода", 30, 150)
product_4 = Product("Портфель", 5, 500)
product_5 = Product("Линейка", 100, 25)

storage = Warehouse()

storage.add(product_1)
storage.add(product_2)
storage.add(product_3)
storage.add(product_4)
storage.add(product_5)

print(f"Магазин до начала работы продавца\n{storage}\n")

seller = Seller("Иван", storage)

seller.sell("Линейка", 100)
seller.sell("Вода", 40)
seller.sell("Ручка", 132)

print(f"Магазин после начала работы продавца\n{storage}\n")
print(seller.get_report())