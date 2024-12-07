def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        
        for line in data:
            line = line.strip() 
            try:

                if line.isdigit():
                    print(line)
                else:
                    raise TypeError(f"Строка '{line}' не является числом.")
            except TypeError as e:
                print(e)

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")


file_path = 'file.txt'
process_file(file_path)