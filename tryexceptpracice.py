class NegativeValueError(Exception):
    pass



try:
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість товару: "))

    if price < 0 or quantity < 0:
        raise NegativeValueError("Ціна та кількість не можуть бути відємними")

    total = price * quantity
    print(f"Загальна сума: {total} грн")


except ValueError:
    print("Помилка! Ціна або кількість має бути числом!")

except ZeroDivisionError:
    print("Помилка кількість товару не може бути 0")

except NegativeValueError as e:
    print(f"Помилка: {e}")


finally:
    print("Дякуємо за користування нашим калькулятором товару!")