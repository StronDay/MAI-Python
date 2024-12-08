import itertools

# Cоздание бесконечного генератора чисел
def infinite_counter(start=0, step=1):
    return itertools.count(start=start, step=step)

# Применение функции к каждому элементу в итераторе
def apply_function_to_iterator(iterator, func):
    return map(func, iterator)

# Объединение нескольких итераторов в один
def combine_iterators(*iterators):
    return itertools.chain(*iterators)

def main():
    counter = infinite_counter(1, 2)
    numbers = []
    
    print("Генератор бесконечных чисел:")
    for _ in range(5):
        numbers.append(next(counter))
    
    print(numbers)

    doubled = apply_function_to_iterator(numbers, lambda x: x * 2)
    print("Сгенерированные числа, умноженные на 2:")
    print(list(doubled))

    some_iter = [7, 7, 7]
    combined = combine_iterators(numbers, some_iter)
    print("Объединенные итераторы:")
    print(list(combined))

    # Обработка исключений при попытке доступа к пустым итераторам
    try:
        empty_iter = iter([]) 
        print(next(empty_iter))
    except StopIteration:
        print("Ошибка: Итератор пуст!")

if __name__ == "__main__":
    main()