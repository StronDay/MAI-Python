from clipboard import ClipBoard
from exept import BufferError

def main():
    buff = ClipBoard()

    while True:
        input_data = input("Введите данные в буфер (get - для получения, exit - для завершения): ")
        
        if input_data == "exit":
            print("Завершение работы программы.")
            break
        
        try:
            if input_data == "get":
                print(buff.get_data())
            else:
                buff.add_data(input_data)
        
        except BufferError as e:
            print(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()