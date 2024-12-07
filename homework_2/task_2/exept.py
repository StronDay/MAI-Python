class BufferError(Exception):
    
    def __init__(self, message="Ошибка буфера", error_type="full"):
        if error_type == "full":
            message = "Буфер переполнен, невозможно записать данные!"
        elif error_type == "empty":
            message = "Буфер пуст, невозможно получить данные!"
            
        self.message = message
        super().__init__(self.message)