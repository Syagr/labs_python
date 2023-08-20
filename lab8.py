""" 1 """
""" import re
from collections import Counter


with open('C:\\Users\\pasha\\Downloads\\text.txt', 'r') as f:
    text = f.read()


words = re.findall(r'\w+', text.lower())


word_counts = Counter(words)


top_words = word_counts.most_common(10)


for word, count in top_words:
    print(f"{word}: {count}") """

""" 2 """
""" import csv


with open('filename.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)


num_rows = len(data)
num_cols = len(data[0])


print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}") """

""" 3 """
""" with open('C:\\Users\\pasha\\Downloads\\binary_file.bin', 'rb') as f:
    binary_data = f.read()


hex_data = binary_data.hex()


with open('0', 'w') as f:
   
    f.write(hex_data) """

""" 4 """
""" input_file = 'C:\\Users\\pasha\\Downloads\\text.txt'
output_file = 'new.txt'
old_word = 'Tony Soprano'
new_word = 'head of mafia'


with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
    
    for line in f_input:
        
        new_line = line.replace(old_word, new_word)
        
        f_output.write(new_line) """

""" 5 """
""" import json


with open('C:\\Users\\pasha\\Downloads\\weather_data.json', 'r') as f:
    data = json.load(f)


print(json.dumps(data, indent=4)) """

""" 6 """
"""import json


with open('C:\\Users\\pasha\\Downloads\\weather_data.json', 'r') as f:
    data = json.load(f)


keys = []
for item in data:
    keys.extend(item.keys())


keys = list(set(keys))


print(keys)  """