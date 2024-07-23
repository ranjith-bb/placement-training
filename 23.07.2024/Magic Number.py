def is_magic_number(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num == 1

number = 1234
print(f"Is Magic Number: {is_magic_number(number)}")
