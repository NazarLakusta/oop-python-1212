# try:
#     number = int(input("Введіть ціле число: "))
#
# except ValueError:
#     print("Помилка! Це не ціле число")
#
# else:
#     print(f"Ви ввели число {number}")
#
# finally:
#     print("Кінець програми")


# код який може викликати помилку
try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))

    result = a / b

# обробка помилки, винятку
except (ZeroDivisionError,ValueError):
    print("Помилка, ти що, тут ділення на 0!!!!!")

except ValueError:
     print("Помилка! Це не ціле число")


else:
    print(f"Результат ділення: {result}")


finally:
    print("Дякую за використання програми!")