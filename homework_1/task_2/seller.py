from warehouse import Warehouse
from product import Product

class Seller:
    
    def __init__(self, name: str, store: Warehouse) -> None:
        self._name = name
        self._store = store
        self._sales = Warehouse()
        
    def sell(self, product_name: str, count: int) -> bool:
        product_in_store = self._store.find_product(product_name)
        count_for_sale = count
        
        if self._store.find_product(product_name):
            
            if product_in_store.get_count() < count_for_sale:
                print("Недостаточно продуктов")
                return False
            
            price = product_in_store.get_price()
            selling_product = Product(product_name, count_for_sale, price)
            
            self._store.pop(selling_product)
            self._sales.add(selling_product)
            
            return True
        else:
            print("Продукт отсутствует")
            return False
    
    def get_name(self):
        return self._name
    
    def get_sell_list(self):
        return repr(self._sales)
    
    def get_sell_amount(self):
        return self._sales.get_products_price()
    
    def get_report(self):
        report = f"Отчет продавца: {self.get_name()}\n"
        report += "Список проданных товаров:\n" + self.get_sell_list() + "\n"
        report += f"Общая сумма продаж: {self.get_sell_amount()} руб.\n"
        return report