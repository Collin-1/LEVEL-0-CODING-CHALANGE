def maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(maximum(1, 2, 3))

# BONUS
def maximum2(*numbers):
    max_num = 0
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


print(maximum2(1, 22, 3, 2))
