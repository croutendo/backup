#requests two number and put them into variables
x = input("What is your first number? ")
try:
    x = int(x)
except ValueError:
    print("ValueError: Please restart the program and input an integer.")
    quit()
y = input("What is your second number? ")
try:
    y = int(y)
except ValueError:
    print("ValueError: Please restart the program and input an integer.")
    quit()

#perform and display addition, subtraction, multiplication, division and r division
print("\r")
print("OPERATIONS")
print("Added together, your numbers sum to: " + str(x + y))
print("The difference between your numbers is: " + str(x - y))
print("Multipled together, the product of your numbers is: " + str(x * y))
print("When your first number is divided by your second number, we get " + str(x // y))
print("But this time dividing with floats: " + str(x / y))

#use comparison operators to determine which number is greater and display results
print("\r")
print("COMPARISONS")
if x > y:
    print("Your first number is greater than your second.")

elif x < y:
    print("Your first number is less than your second number.")

elif x == y:
    print("Your numbers are equal.")

else:
    print("Something went wrong. Try again and make sure you use two integers.")

#create a list from 0 to 99 and determine if the numbers are on the list
n = 0
li = []
while n <= 99:
    li.append(n)
    n += 1
print(li) 

print("\r")
print("LIST BETWEEN 1 and 99")
if (x in li) and (y in li):
    print("Both of your numbers are on the list.")

elif x in li:
    print("Your first number is on the list.")

elif y in li:
    print("Your second number is on the list.")

elif (x not in li) and (y not in li):
    print("Neither of your numbers are on the list.")

else:
    print("Something went wrong. Try again and make sure you use two integers.")

