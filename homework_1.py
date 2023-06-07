first_num = int(input("Введите первое число: "))
difference = int(input("Введите разницу между каждым следующим числом: "))
num_of_elements = int(input("Введите количество элементов: "))

array = []

array.append(first_num)

for i in range(num_of_elements - 1):
    next_num = array[-1] + difference
    array.append(next_num)

print("Массив: ", *array)