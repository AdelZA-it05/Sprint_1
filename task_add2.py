def digit_root(num):
    print(num)
    if num > 9:
        print(num // 10 + num % 10)
        return digit_root(num // 10 + num % 10)
    return num
