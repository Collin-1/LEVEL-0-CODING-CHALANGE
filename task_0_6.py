def maximum(*numbers):
    max_num = 0
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


print(maximum(1, 22, 3, 2))
