import datetime
from homework_4.task_1.time_utils import TimeUtils

def main():
    
    print("Текущая дата - time.\n")
    print("Вычислить разницу - calc.\n")
    print("Завершения работы программы - exit.\n")
    
    while True:
        user_input = input("Ответ: ")
                
        match user_input:
            case "exit":
                print("Завершение работы программы.")
                break
            case "time":
                print(TimeUtils.display_current_datetime())
            case "calc":
                date_1 = input("Введите первую дату(<год>-<месяц>-<день>): ")
                date_2 = input("Введите вторую дату(<год>-<месяц>-<день>): ")
                
                try:
                    print(TimeUtils.calculate_date_difference(date_1, date_2))
                except ValueError as e:
                    print(f"Ошибка в входных данных: {e}")
                
            case _:
                print(f"Команды({user_input}) нету.")


if __name__ == "__main__":
    main()