#data.py
#structured data assignment

#create a list
li = ["apples", "pears", "oranges", "peaches"]
for x in li:
    print(x)
print()

#add a fruit to the list
x = input("Please add another fruit: ")
li.append(x)
print()

for x in li:
    print(x)
print()

#display based off number
x = input("Please give me a number to display the corresponding fruit of: ")
print()

print(li[int(x)-1])
print()

#add a fruit to the begginning of the list
li.insert(0, "pineapple")
for x in li:
    print(x)
print()

#create a dictionary
di = dict(name = "Chris", city = "Seattle", cake = "Chocolate")
print(di)
print()

#delete an entry
di.pop("cake")

print(di)
print()

#add an entry
di["fruit"] = "Mango"
print(di)
print()

for k in di.keys():
    print(k)
print()
for v in di.values():
    print(v)
print()

print("True" if "cake" in di.keys() else "False")
print()

print("True" if "Mango" in di.values() else "False")
print()

#create sets
s = set(range(0,21))
"""for x in s:
    print(x)
print()"""

s2 = set(x for x in s if x % 2 == 0)
s3 = set(x for x in s if x % 3 == 0)
s4 = set(x for x in s if x % 4 == 0)

for x in s2:
    print(x, end = ", ")
print()
for x in s3:
    print(x, end = ", ")
print()
for x in s4:
    print(x, end = " ")
print()

#display union and intersections of sets
print()
print(s2 | s3)
print(s3 & s4)
print()







