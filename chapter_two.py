#assignment for chapter two

def main():
    integer = 17
    string = "This is a flipping string"
    
    print(integer)
    print(string)

    x = 33
    y = 66

    if x < y:
        print("{} is less than {}" .format(x, y))

    elif x > y:
        print("{} is greater than {}" .format(x, y))

    else:
        print("{} is equal to {}" .format(x, y))

    print("\r")
    new_function(1,10)
    
    print("\r")
    new_function(34,29)

    print("\r")
    pet_one()
    
def new_function(first, second):
    if second > first:
        firstnumber = first
        while firstnumber < second:
            print(firstnumber)
            firstnumber += 1
        print(firstnumber)
        
    elif second < first:
        firstnumber = second
        while firstnumber < first:
            print(firstnumber)
            firstnumber += 1
        print(firstnumber)

    else:
        print("The two numbers are equal/invalid. Please enter a valid pair of numbers that are not equal.")

class HousePet:
    bestpet = "Brown Bear"
    petsound = "I'm going to eat you now."

    def pet_type(self):
        print(self.bestpet)

    def pet_sound(self):
        print(self.petsound)

def pet_one():
    pet_one = HousePet()
    pet_one.pet_type()
    pet_one.pet_sound()

if __name__ == "__main__" : main()


