import sqlite3
from enum import Enum

class SqlType(Enum):
    INTEGER = "INTEGER"
    TEXT = "TEXT"
    REAL = "REAL"
    BLOB = "BLOB"
    BOOLEAN = "BOOLEAN"
    NUMERIC = "NUMERIC"
    
class SqlForeignKey():
    def __init__(self, reference_table: str, reference_column: str):
        self.reference_table = reference_table
        self.reference_column = reference_column

    def to_sql(self):
        return f"REFERENCES {self.reference_table}({self.reference_column})"

class SqlColumn():
    
    def __init__(self, name: str, type: SqlType, is_primary: bool = False, f_key: SqlForeignKey = None):
        self._name = name
        self._type = type
        self._is_primary = is_primary
        self._foreign_key = f_key
        
    def to_sql(self):
        column_def = f"{self._name} {self._type.value}"
        
        if self._is_primary:
            column_def += " PRIMARY KEY"
            
        if self._foreign_key:
            column_def += " " + self._foreign_key.to_sql()
            
        return column_def
    
def handle_db_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except sqlite3.Error as e:
            print(f"Ошибка при выполнении запроса {func}: {e}")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")
            
    return wrapper

class Sql():
    
    @handle_db_errors
    def create_table(connection, table_name: str, columns: list[SqlColumn]):
        cursor = connection.cursor()
            
        columns_definition = ", ".join([column.to_sql() for column in columns])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition});"
            
        cursor.execute(query)
        connection.commit()
            
        print(f"Таблица {table_name} успешно создана или уже существует.")
        
    @handle_db_errors
    def append(connection, table_name: str, columns: list[str], values: list[str]):
        cursor = connection.cursor()
    
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?" for _ in values])
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
    
        cursor.execute(query, values)
        connection.commit()
            
    @handle_db_errors
    def search_all(connection, table_name: str, condition: str = None):
        cursor = connection.cursor()
        if condition:
            query = f"SELECT * FROM {table_name} WHERE {condition};"
        else:
            query = f"SELECT * FROM {table_name};"
        
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            return result
        else:
            return None
        
    @handle_db_errors
    def search_first(connection, table_name: str, condition: str):
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name} WHERE {condition};"
        
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result
        else:
            return None
        
    def search_min(connection, table_name: str, column: str, condition: str = None):
        cursor = connection.cursor()
        
        if condition:
            query = f"SELECT MIN({column}) FROM {table_name} WHERE {condition};"
        else:
            query = f"SELECT MIN({column}) FROM {table_name};"
        
        cursor.execute(query)
        result = cursor.fetchone()[0]
        if result:
            return result
        else:
            return None
        
    def search_max(connection, table_name: str, column: str, condition: str = None):
        cursor = connection.cursor()
        
        if condition:
            query = f"SELECT MAX({column}) FROM {table_name} WHERE {condition};"
        else:
            query = f"SELECT MAX({column}) FROM {table_name};"
        
        cursor.execute(query)
        result = cursor.fetchone()[0]
        if result:
            return result
        else:
            return None
        