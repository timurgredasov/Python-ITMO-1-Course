from csv import reader

def search_author(table, search_line):
    flag = 0
    for row in table:
        if string_find(row[2], search_line) != -1 and price_limit(row[6]):
            flag += 1
            print(f"Название: '{row[1]}' | Цена: {row[6]} руб.")
            
    if flag == 0:
        print("Ничего не найдено!")
    else:
        print(f"\nВсего найдено книг: {flag}")

def generator(table, search_line):
    output = open('result.txt', 'w')
    number = 0
    for row in table[30:50]:
        number += 1
        output.write(f"{number}) {row[2]}. '{row[1]}' - {row[3]}\n")
    output.close()
        

def string_find(string, search_line):
    lower_case = string.lower()
    return lower_case.find(search_line.lower())

def price_limit(price):
    if "," in price:
        if int(price[:price.index(",")]) >= 150:
            return True
    else:
        if int(price) >= 150:
            return True

def additional_task(table):
    publishers = []
    popular_books = []
    for row in table:
        if row[4] not in publishers:
            publishers.append(row[4])
        if row[5] != 'Downloads' and int(row[5]) > 24:
            popular_books.append([row[5], row[2], row[1]])
    popular_books = sorted(popular_books, reverse=True)
    print('Перечень издательств:\n')
    for i in publishers[:20]:
        print(i)
    print('\nСамые популярные 20 книг:\n')
    for i in range(20):
        print(f"Количество скачиваний: {popular_books[i][0]} | Автор: {popular_books[i][1]} | Название: {popular_books[i][2]}")



while True:
    search_line = input("Введите имя автора: ")
    if search_line in ['0', '', ' ']:
        break
    try:
        with open('books-en.csv', 'r', encoding='cp1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            search_author(table, search_line)
            generator(table, search_line)
            print('\n')
            additional_task(table)
            counter = 0
            for row in table:
                if len(row[1]) > 30:
                    counter += 1
            print(f"\nКоличество записей, у которых в поле Название строка длиннее 30 символов: {counter}")
            

    except FileNotFoundError:
        print("Файл не найден!")
    
        