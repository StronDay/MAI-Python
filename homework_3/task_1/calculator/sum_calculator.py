class SumCalculator:
    
    def calculate_sum(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Все элементы списка должны быть числами.")
        return sum(numbers)