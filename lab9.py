""" 1 """
""" import re

pattern = r'^[a-z0-9]+$'
input_string = "hello123"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False") """

""" 2 """
""" import re

pattern = r'[A-Z]+'
input_string = "Hello"

match = re.search(pattern, input_string)

if match:
    print("True")
else:
    print("False") """

""" 3 """
""" import re

pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
input_string = "192.168.1.1"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
"""

""" 4 """
""" import re

pattern = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
input_string = "12:34:56"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
"""

""" 5 """
""" import re

pattern = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
input_string = "12:34:56"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
"""
""" 6 """
""" import re

pattern = r'^[a-z0-9_-]{6,12}$'
input_string = "john_doe-123"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
 """

""" 7 """
""" import re

pattern = r'^(4|5|6)\d{3}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$'
input_string = "4512-3456-7890-1234"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
"""

""" 8 """
""" import re

pattern = r'^\d{3}-\d{2}-\d{4}$'
input_string = "123-45-6789"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
"""

""" 9 """
""" import re

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
input_string = "Passw0rd#"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
 """

""" 10 """

"""  import re

pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
input_string = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

match = re.match(pattern, input_string)

if match:
    print("True")
else:
    print("False")
 """