#Task1
lessernumbers = [10, 3, 15, 7, 20, 5, 8]
numbers_tuple = tuple(lessernumbers)
n = int(input("Введіть число n для першого завдання: "))
lesserresult = [num for num in numbers_tuple if num < n]
print("Числа менші за", n, ":", lesserresult)

#Task2
tuple_of_strings = ("Надія", "Любов", "Радість")
stringsresult = ",".join(tuple_of_strings)
print(stringsresult)

#Task3
library = {
    "Гаррі Поттер і філософський камінь": {
        "Автор": "Дж. К. Роулінг",
        "Рік": 1869,
        "Кількість сторінок": 223
    },
    "Дон Кіхот": {
        "Автор": "Мігель де Сервантес",
        "Рік": 1605,
        "Кількість сторінок": 863
    },
    "Майстер і Маргарита": {
        "Автор": "Михайло Булгаков",
        "Рік": 1967,
        "Кількість сторінок": 384
    }
}
book_name = input("Введіть назву книги: ")
if book_name in library:
    book_info = library[book_name]
    print(f"Інформація про книгу '{book_name}':")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print("Такої книги немає в бібліотеці.")

#Task4
students = {
    "Мардєєва": ("Діна", 20, "ІЕЛІІТ"),
    "Коваленко": ("Анастасія", 19, "ІЕЛІІТ"),
    "Лашко": ("Іван", 20, "ІЕЛІІТ")
}
surname = input("Введіть прізвище студента: ")
if surname in students:
    name, age, faculty = students[surname]
    print(f"Інформація про студента '{surname}':")
    print(f"Ім'я: {name}")
    print(f"Вік: {age}")
    print(f"Факультет: {faculty}")
else:
    print("Студента з таким прізвищем немає в базі.")

#Task5
phone_book = {
    "Анастасія": ["+380687476805"],
    "Женя": ["+380684809140"],
    "Олександр": ["+380505444235"]
}
def add_phone_number(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
    else:
        phone_book[contact_name] = [phone_number]
    print(f"Додано номер {phone_number} до контакту '{contact_name}'.")
contact_name = input("Введіть ім'я контакту: ")
phone_number = input("Введіть номер телефону для додавання: ")
add_phone_number(contact_name, phone_number)
print("\nТелефонна книга:")
for contact, numbers in phone_book.items():
    print(f"{contact}: {', '.join(numbers)}")