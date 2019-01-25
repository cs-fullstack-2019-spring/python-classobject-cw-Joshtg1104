def main():

    # problem1()
    # problem2()
    # problem3()
    problem4()



# ### Problem 1:
# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

def problem1():
    class Dog:
        def __init__(self, name, breed, color, gender):
            self.name = name
            self.breed = breed
            self.color = color
            self.gender = gender

        def printDoggo(self):
            print(f"This dog's name is {self.name}, it is a {self.breed} with {self.color} fur and is a {self.gender}.")
    newDog1 = Dog("Melo", "Shiba", "black", "male")
    newDog2 = Dog("Seiba", "Golden Retriever", "golden blond", "female")
    newDog1.printDoggo()
    newDog2.printDoggo()


# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.

def problem2():

    woop = input("Type me something. Enter the equal sign(=) to leave me alone.")

    while(woop != "="):
        woop = input("Enter some more. Don't forget, equal sign(=) to leave me alone.")
        continue


# ### Problem 3:
# In your main file create three Person objects. Change the weight and height of each one.
# Afterwards, print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.
# <strong>Hint</strong>: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
# <strong>Extra</strong>:Put the three person objects in an array and use a loop to print out their BMIs.

def problem3():
    class Size:
        def __init__(self,weight, height):
            self.weight = weight
            self.height = height

        def weightUpdate(self, amount):
            self.weight += amount
        def heightUpdate(self, amount):
            self.height += amount

        def bmi(self):
            print(f"This person's weight is {self.weight}lbs and their height is {self.height} inches\nWhich gives them a BMI of\n{(self.weight / (self.height * self.height) * 703)}")
    person1 = Size(164, 66)
    person2 = Size(138, 49)
    person3 = Size(208, 76)
    # person1.bmi()
    # person2.bmi()
    # person3.bmi()
    person1.weightUpdate(23)
    person2.heightUpdate(10)
    person2.weightUpdate(-5)
    person3.weightUpdate(-30)
    person1.bmi()
    person2.bmi()
    person3.bmi()

# ### Problem 4:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
# The class should have changeProduct:
# a) If changeProduct has one parameter, it can change the name of the product.
# b) If changeProduct has two parameters it can change the name and price of the product.
# c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
# Create an object of Product in your problem4 function and print all of it's attributes.

def problem4():

    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity
        def changeProduct1(self, name = ""):
            self.name = name
        def changeProduct2(self,name = "", price = 0):
            self.name = name
            self.price = price
        def changeProduct3(self, name = "", price = 0, quantity = 0):
            self.name = name
            self.price = price
            self.quantity = quantity
        def printProduct(self):
            print(f"Our new product is {self.name} with a price of ${self.price} and we have {self.quantity} in stock.")
    # I tried to get it to replace the first parameter without changing the others but found it difficult.
    newProduct1 = Product("Deluxe Deo-D", 4.58, 200)
    newProduct1.printProduct()
    newProduct1.changeProduct1("Jimmy's Ice Cream")
    newProduct1.printProduct()
    newProduct1.changeProduct2("Robin's Diapers",24)
    newProduct1.printProduct()
    newProduct1.changeProduct3("Raven's Hampers",12, 40)
    newProduct1.printProduct()
#     Settled for just creating 3 seperate functions.









if __name__ == '__main__':
    main()