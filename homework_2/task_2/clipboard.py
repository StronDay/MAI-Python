from exept import BufferError

class ClipBoard():
    
    def __init__(self):
        self.data_list = []
    
    def add_data(self, data: str):

        if len(self.data_list) == 5:
            raise BufferError(error_type="full")
        
        self.data_list.append(data)
    
    def get_data(self):
        
        if len(self.data_list) == 0:
            raise BufferError(error_type="empty")
        
        return_data = self.data_list[:]
        self.data_list.clear()
        
        return return_data