

def mountains_weight(weight):
    count = 0
    empty = (2 * weight) - 2
    for i in range(0, weight, 2):
        nums_array_row = []
        number_1 = weight - i
        for j in range(0, empty):
            print(end='  ')
        empty = empty - 1
        for j in range(0, i + 1):
            nums_array_row.append(number_1)
            print(number_1, end=' ')
            if j < count:
                number_1 += 1
            else:
                number_1 -= 1
        count += 1
        nums_array.append(sum(nums_array_row))
        print(' ')

    return sum(nums_array)


# Проверка вводимых данных на то, что это нечетное число
def input_number():
    number = input("Enter an odd weight: ")
    if number.isdecimal() and int(number) % 2 != 0 and int(number) > 0:
        print(f"You enter: {number}")
        return int(number)
    else:
        print("You enter not positive odd weight! Please try again.")
        return input_number()


if __name__ == '__main__':
    odd_number = input_number()
    nums_array = []
    print(mountains_weight(odd_number))
