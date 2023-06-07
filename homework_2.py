def find_indexes(lst, min_val, max_val):
    result = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            result.append(i)
    return result

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_val = int(input())
max_val = int(input())

print(find_indexes(lst, min_val, max_val))
