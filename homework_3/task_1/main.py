from calculator import SumCalculator

def main():
    calculator = SumCalculator()
    
    numbers = [1, 2, 3, 4, 5]
    total = calculator.calculate_sum(numbers)
    
    print(f"Сумма чисел {numbers} равна {total}")

if __name__ == "__main__":
    main()