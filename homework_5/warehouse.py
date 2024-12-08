from sql import Sql, SqlColumn, SqlType, SqlForeignKey
import sqlite3

class WarehuseError(Exception):
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class Warehuse():
    
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        
    def init_db(self):
        columns = [
            SqlColumn("product_id", SqlType.INTEGER, is_primary=True),
            SqlColumn("produt_name", SqlType.TEXT),
            SqlColumn("product_cost", SqlType.INTEGER),
            SqlColumn("category_id", SqlType.INTEGER, f_key=SqlForeignKey("categories", "category_id")),
            SqlColumn("supplier_id", SqlType.INTEGER, f_key=SqlForeignKey("suppliers", "supplier_id"))
        ]
        
        Sql.create_table(self.connection, "products", columns)
        
        columns = [
            SqlColumn("category_id", SqlType.INTEGER, is_primary=True),
            SqlColumn("category_name", SqlType.TEXT)
        ]
        
        Sql.create_table(self.connection, "categories", columns)
        
        columns = [
            SqlColumn("supplier_id", SqlType.INTEGER, is_primary=True),
            SqlColumn("supplier_name", SqlType.TEXT)
        ]
        
        Sql.create_table(self.connection, "suppliers", columns)
        
    def append_products(self, name: str, cost: int, category: str, supplier: str):
        search_category = Sql.search_first(self.connection, "categories", f"category_name = '{category}'")
        if not search_category:
            raise WarehuseError(f"Категории {category} не существует.")
        
        search_supplier = Sql.search_first(self.connection, "suppliers", f"supplier_name = '{supplier}'")
        if not search_supplier:
            raise WarehuseError(f"Поставщика {supplier} не существует.")
        
        columns = {
            "produt_name": name,
            "product_cost": cost,
            "category_id": search_category[0],
            "supplier_id": search_supplier[0],
        }
        
        Sql.append(self.connection, "products", list(columns.keys()), list(columns.values()))
        
    def append_category(self, name: str):
        Sql.append(self.connection, "categories", ["category_name"], [name])
    
    def append_supplier(self, name: str):
        Sql.append(self.connection, "suppliers", ["supplier_name"], [name])
        
    # 
    # ЗАДАНИЕ 1
    # 
    def get_products_name(self, cost_min: int, cost_max: int):
        if cost_min >= cost_max:
            raise WarehuseError("Минимальное значение должно быть меньше максимального")
        
        response = Sql.search_all(
            self.connection, 
            "products", 
            f"product_cost >= {cost_min} AND product_cost < {cost_max}"
        )
        
        if not response:
            return []
        
        product_names = [product[1] for product in response]
        return product_names
    
    # 
    # ЗАДАНИЕ 2
    # 
    def get_min_cost_category(self, category: str):
        search_category = Sql.search_first(self.connection, "categories", f"category_name = '{category}'")
        if not search_category:
            raise WarehuseError(f"Категории {category} не существует.")
        
        response = Sql.search_min(
            self.connection, 
            "products",
            "product_cost",
            f"category_id = {search_category[0]}"
        )
        
        if not response:
            return []
        
        return response
    
    # 
    # ЗАДАНИЕ 3
    # 
    def get_suppliers(self):
        result_suppliers = []
        
        suppliers = Sql.search_all(
            self.connection, 
            "suppliers",
        )
        
        for supplier in suppliers:
            max_cost = Sql.search_max(self.connection, "products", "product_cost", f"supplier_id = {supplier[0]}")

            result_suppliers.append({
                "id поставщика": str(supplier[0]),
                "Название": str(supplier[1]),
                "максимальная цена товара": str(max_cost if max_cost is not None else 0)
            })
        
        if not result_suppliers:
            return []
        
        return result_suppliers
    
    