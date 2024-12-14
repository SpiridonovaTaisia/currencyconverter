# импорт библиотек
import requests
import json
from datetime import datetime


# Эта функция получает актуальный курс доллара к рублю.
# Отправляет GET-запрос к API Центрального банка России. Парсит полученный JSON-ответ. Возвращает текущее значение курса доллара
def get_exchange_rate():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['Valute']['USD']['Value']


# Эта функция выполняет конвертацию валют:
# Если исходная валюта - рубли, делит сумму на курс Если исходная валюта - доллары, умножает сумму на курс
def convert_currency(amount, exchange_rate, from_currency, to_currency):
    if from_currency == "RUB":
        return amount / exchange_rate
    else:
        return amount * exchange_rate


# main Выводит заголовок конвертера валют.
def main():
    print("Конвертер валют (RUB <-> USD)")
    print("------------------------------")

    # Запускает бесконечный цикл.
    while True:
        try:
            exchange_rate = get_exchange_rate()
            print(f"\nТекущий курс: 1 USD = {exchange_rate:.4f} RUB")
            print(f"Дата и время обновления: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            amount = float(input("\nВведите сумму: "))
            currency = input("Введите валюту (RUB или USD): ").upper()

            if currency == "RUB":
                result = convert_currency(amount, exchange_rate, "RUB", "USD")
                print(f"\n{amount:.2f} RUB = {result:.2f} USD")
            elif currency == "USD":
                result = convert_currency(amount, exchange_rate, "USD", "RUB")
                print(f"\n{amount:.2f} USD = {result:.2f} RUB")
            else:
                print("Неверная валюта. Пожалуйста, введите RUB или USD.")

            continue_choice = input("\nХотите продолжить? (да/нет): ").lower()
            if continue_choice != "да":
                break

        # Обрабатывает возможные ошибки.
        except ValueError:
            print("Ошибка: Введите корректное числовое значение.")
        except requests.RequestException:
            print("Ошибка: Не удалось получить данные о курсе валют. Проверьте подключение к интернету.")

    # Завершает работу, если пользователь не хочет продолжать.
    print("\nСпасибо за использование конвертера валют!")


# Выполняет запуск программы.
if __name__ == "__main__":
    main()
