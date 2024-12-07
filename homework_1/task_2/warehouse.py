from product import Product

class Warehouse:
    
    def __init__(self) -> None:
        self._products = []
        
    def find_product(self, product_name) -> Product:
        for product in self._products:
            if product.get_name() == product_name:
                return product
        return None
        
    def add(self, new_product: Product) -> None:
        product = self.find_product(new_product.get_name())
        if product:
            product += new_product
        else:
            self._products.append(new_product)
            
    def pop(self, removed_product) -> None:
        product = self.find_product(removed_product.get_name())
        if product:
            product -= removed_product
            if product.get_count() == 0:
                self._products.remove(product)
            
    def get_products_price(self) -> int:
        amount = 0
        for product in self._products:
            amount += product.get_full_price()
            
        return amount
            
            
    def __repr__(self) -> str:
        product_list = []
        for product in self._products:
            product_list.append(repr(product))
            
        return "\n".join(product_list) if product_list else "Пусто"
            
        
    