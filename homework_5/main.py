from warehouse import Warehuse, WarehuseError
import os

def init_base_values(warehouse: Warehuse):
    warehouse.append_category("столы")
    warehouse.append_category("стулья")
        
    warehouse.append_supplier("ООО ГорСтрой")
    warehouse.append_supplier("ИП Алексеев")
        
    warehouse.append_products("Гармония", 1000, "столы", "ИП Алексеев")
    warehouse.append_products("Мезон-4", 1240, "столы", "ООО ГорСтрой")
    warehouse.append_products("Ретро-Классик", 950, "столы", "ИП Алексеев")
        
    warehouse.append_products("Комфорт-5", 850, "стулья", "ИП Алексеев")
    warehouse.append_products("Элегантный Стул", 1120, "стулья", "ООО ГорСтрой")
    warehouse.append_products("Модерн 2000", 1980, "стулья", "ООО ГорСтрой")
    

def main():
    try:
        
        if not os.path.exists("warehouse.db"):
            warehouse = Warehuse("warehouse.db")
            
            warehouse.init_db()
            init_base_values(warehouse)
            
        warehouse = Warehuse("warehouse.db")

        print(f"Навания товаров с ценой от 1000 до 1500: {", ".join(warehouse.get_products_name(1000, 1500))}")
        print()
        print(f"Минимальная цена категории 'столы': {warehouse.get_min_cost_category("столы")}")
        print()
        
        print("Поставщики:")
        suppliers = warehouse.get_suppliers()
        for supplier in suppliers:
            print(f"ID поставщика: {supplier['id поставщика']}, "
                f"Название: {supplier['Название']}, "
                f"Максимальная цена товара: {supplier['максимальная цена товара']}")
        
    except WarehuseError as e:
        print(f"WarehuseError: {e}")


if __name__ == "__main__":
    main()