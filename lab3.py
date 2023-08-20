""" 1 """
""" a = [1,2,3,4,5,6]
a[1]=-5
print(a)
print(max(a))
print(min(a))
b=[1,2,3]
a.append(b[-1::-1])
print(a)
a.append('Сягровський Павло')
print(a)
print(len(a)) """

""" 2 """
""" a = [1058, 1387]
b = [26, 33]
c = ['coca-cola', 'pepsi']
x = [a[i]*b[i] for i in range(len(a))]
print(x)
print(f'''
   загальна ціна : {sum(x)},
   середня ціна : {int(sum(x)/len(x))},
   найбільше : {c[a.index(max(a))]}
      ''')
"""
""" 3 """
""" numbers = list(range(-50,51))


a= []
b= []


for num in numbers:
    if num >= 0:
        a.append(num)
    else:
        b.append(num)


print("список додатніх ",a)
print("список від'ємних ",b) """