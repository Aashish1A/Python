def square(x):
    return x ** 2

numbers = [1,3,4,5,6]
squared_numbers = map(square,numbers)
print(list(squared_numbers))