import datetime

class TimeUtils:
    
    @staticmethod
    def display_current_datetime():
        current_datetime = datetime.datetime.now()
        return f"Текущая дата и время: {current_datetime}"

    @staticmethod
    def calculate_date_difference(date1, date2):
        if isinstance(date1, str):
            date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        if isinstance(date2, str):
            date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        
        difference = date2 - date1
        return f"Разница между датами: {difference.days} дней"

    @staticmethod
    def string_to_datetime(date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return f"Преобразованная дата и время: {date_obj}"