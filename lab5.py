""" 1 """
""" start = int(input("Введіть початкове значення: "))
end = int(input("Введіть кінцеве значення: "))

arr = list(range(start, end+1))

print("Original Array: ", arr)

replace_num = 99 
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = replace_num

print("Updated Array: ", arr) """
""" 2 """
""" import array
import binascii


string = input("Введіть машинні значення у вигляді шістнадцяткового рядка: ")


bytes = binascii.unhexlify(string)


array1 = array.array("i")
array1.frombytes(bytes)


print("array1:", array1)
print("Bytes:", bytes)


array2 = array.array("i", array1)
print("array2:", array2) """

""" 3 """
""" def remove_duplicates(arr):
   
    unique_set = set()

    
    for elem in arr:
        
        if elem not in unique_set:
            unique_set.add(elem)

    
    return list(unique_set)


arr1 = [1, 3, 5, 1, 3, 7, 9]
arr2 = [2, 4, 2, 6, 4, 8]
print("Оригінальний масив:", " ".join(str(x) for x in arr1))
print("After removing duplicate elements from the said array:", " ".join(str(x) for x in remove_duplicates(arr1)))
print("Оригінальний масив:", " ".join(str(x) for x in arr2))
print("After removing duplicate elements from the said array:", " ".join(str(x) for x in remove_duplicates(arr2))) """

""" 4 """
""" arr = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
n = len(arr) + 1
sum_of_arr = sum(arr)
expected_sum = (n * (10 + 20)) // 2
missing_number = expected_sum - sum_of_arr
print(f"Оригінальний масив: {arr}")
print(f"Missing number in the said array (10-20): {missing_number}")

arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
n = len(arr) + 1
sum_of_arr = sum(arr)
expected_sum = (n * (10 + 20)) // 2
missing_number = expected_sum - sum_of_arr
print(f"Оригінальний масив: {arr}")
print(f"Відсутнє число у вказаному масиві (10-20): {missing_number}") """

""" 5 """
"""  string = 'w3resource'

# Initialize an empty dictionary
dict = {}

# Loop through each character in the string
for char in string:

    # If the character is already in the dictionary, increment its count
    if char in dict:
        dict[char] += 1

    # Otherwise, add the character to the dictionary with a count of 1
    else:
        dict[char] = 1

# Print the resulting dictionary
print(dict) """
