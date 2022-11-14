number = 15
pi = 3.14
name = 'Vladimir'
phrase = 'Hello world'
area = 3.14 * 10 ** 2
print(area)

numbers = [2, 3, 3, 3, 5, 4, 5]
print(
    (sum(numbers) / len(numbers))
)
data = [
    [1, 2, 3],
    'hello',
    3.14
]
print(data[0][1])

data_1 = (1, 2, 3, 5)
data_2 = [1, 2, 3, 5]

size_of_tuple = data_1.__sizeof__()
size_of_list = data_2.__sizeof__()

print(
    size_of_tuple/ (size_of_list- size_of_tuple)
)
