class Product:
    
    def __init__(self, name: str, count: int, price: int) -> None:
        self._name = name
        self._price = 1
        self._count = 0
        
        if (price > 0):
            self._price = price
        
        if (count > 0):
            self._count = count
    
    def increase(self, count: int) -> None:
        self._count += count
        
    def decrease(self, count: int) -> None:
        self._count -= count
        
        if (self._count < 0):
            self._count = 0
            
    def get_price(self) -> int:
        return self._price
            
    def get_full_price(self) -> int:
        return self._price * self._count
    
    def get_count(self) -> int:
        return self._count
    
    def get_name(self) -> str:
        return self._name
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.get_name().lower() == other.get_name().lower()
        return False
    
    def __iadd__(self, other):
        if isinstance(other, Product):
            if self.get_name() != other.get_name():
                print("Разные товары нельзя складывать")
                return self
            self.increase(other.get_count())
            
        return self
    
    def __isub__(self, other):
        if isinstance(other, Product):
            if self.get_name() != other.get_name():
                print("Разные товары нельзя вычетать")
                return self
            self.decrease(other.get_count())
            
        return self
    
    def __repr__(self) -> str:
        return f"{self.get_name()}: кол-во: {self.get_count()}; цена: {self.get_price()}"