def multiply(*args):
    result = 1
    print(args[1])
    for value in args:
        result *= value
    return result

result = multiply(2,3,4,5,6)
print(result)
