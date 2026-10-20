all_items = [['r', 3, 25, 25/3], ['p', 2, 15, 15/2], ['a', 2, 15, 15/2], ['m', 2, 20, 10], ['i', 1, 5, 5],\
              ['k', 1, 15, 15], ['x', 3, 20, 20/3], ['t', 1, 25, 25], ['f', 1, 15, 15], ['s', 2, 20, 10],\
                ['c', 2, 20, 10]]

# добавляю элемент 'd'
all_items_with_d = [['d', 1, 15, 15]] + all_items
all_items_sorted = sorted(all_items_with_d, key=lambda x: x[3], reverse=True)

total_weight = 8
result = []
summ = 20

# жадный алгоритм
for item in all_items_sorted:
    if total_weight >= item[1]:
        result.append(item)
        total_weight -= item[1]
        summ += item[2]

inventory = [[' ' for _ in range(2)] for _ in range(4)]
current_row, current_col = 0, 0

# формирую сетку 2х4
for item in result:
    name, weight, value, _ = item
    for _ in range(weight):
        if current_col >= 2:
            current_col = 0
            current_row += 1
        if current_row < 4:
            inventory[current_row][current_col] = name
            current_col += 1

# считаю итоговые очки выживания
all_items_names = [item[0] for item in all_items_with_d]
taken_items_names = [item[0] for item in result]
not_taken_items = [item for item in all_items_with_d if item[0] not in taken_items_names]
total_survival_points = summ - sum(item[2] for item in not_taken_items)
print(f"[{inventory[0][0]}] [{inventory[0][1]}]")
print(f"[{inventory[1][0]}] [{inventory[1][1]}]")
print(f"[{inventory[2][0]}] [{inventory[2][1]}]")
print(f"[{inventory[3][0]}] [{inventory[3][1]}]")
print(f"Итоговые очки выживания: {total_survival_points}")