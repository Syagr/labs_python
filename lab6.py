""" 1 """
""" my_tuple = (5, 10)
print(my_tuple[0] + my_tuple[1]) """

""" 2 """
""" my_tuple = (1, 2, "three", 4, "five")
print(len(my_tuple)) """

""" 3 """
""" my_tuple = ((1, 2), (3, 4, 5), (6, 7, 8, 9))
last_tuple = my_tuple[-1]
last_element = last_tuple[-1]
print(last_element) """

""" 4 """
""" my_list = [5, 2, 8, 1, 9]
my_tuple = tuple(my_list)
sorted_tuple = sorted(my_tuple, reverse=True)
print(sorted_tuple[0]) """

""" 5 """
""" my_dict = {"name": "Pasha", "age": 18, "city": "Kiev"}
my_tuple = (my_dict,)
print(my_tuple[0]["name"])
"""

""" 6 """
""" my_list = [("a", 1), ("ab", 2, 3), ("abc", 4, 5, 6)]
my_tuple = tuple(my_list)
sorted_tuple = sorted(my_tuple, key=lambda x: len(x[0]))
print(sorted_tuple[-1][-1]) """

""" 7 """
""" my_list = ["apple", "banana", "orange"]
my_tuple = tuple(my_list)
joined_string = ",".join(my_tuple)
print(joined_string[-1]) """

""" 8 """
""" my_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
flat_list = [item for sublist in my_tuple for item in sublist]
filtered_list = list(filter(lambda x: x % 2 == 0, flat_list))
product = 1
for num in filtered_list:
    product *= num

print(product) """

""" 9 """
""" my_tuple = ((1, 2), (3, 4), (5, 6))
sum_second_elements = sum([t[1] for t in my_tuple])
print(sum_second_elements)
"""

""" 10 """
""" my_list = [(1, 5, 3), (2, 4, 1), (3, 2, 7)]
my_tuple = tuple(my_list)
sorted_tuple = sorted(my_tuple, key=lambda x: x[1])
print(sorted_tuple[-1][-1]) """

""" 11 """
""" def filter_tuple(tuple_of_numbers, k):
    filtered_list = [num for num in tuple_of_numbers if num > k]
    return tuple(filtered_list)
my_tuple = (1, 3, 5, 7, 9)
k = 4
result = filter_tuple(my_tuple, k)
print(result)
"""