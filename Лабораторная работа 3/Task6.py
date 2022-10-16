list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maximum_element = 0
maximum_order = 0

for i in range(len(list_numbers)):
    if list_numbers[i] > maximum_element:
        maximum_element = list_numbers[i]
        maximum_order = i

list_numbers[maximum_order], list_numbers[-1] = list_numbers[-1], list_numbers[maximum_order]
# TODO Оформить решение

print(list_numbers)

