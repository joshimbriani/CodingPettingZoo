# Lesson 6 - Classes

# Welcome to lesson 6 of the Coding Petting Zoo
# This is the last lesson, hope you had some fun and learned something!
# In this lesson we'll learn about classes.
# Classes are another fundamental organization of code
# Objects are all around you, we tend to think of the world in terms of them
# When we think of objects, there are two things we instinctly categorize them by: what they are and what they can do
# What they are includes things like their name, what they look like and more
# On the other hand what they do is do things like quack, speak or even crumple if we're talking about something like a peice of paper

# This is also the two fundamental portions of classes in code
# Properties are the "what they are" - these are variables
# Methods are the "what they do" - these are functions
# Let's jump into the code and it'll make sense!

class Car:
    color = "Red"
    make = "Kia"
    model = "Rondo"

    def revEngine(self):
        print("Vroom Vroom!")

    def roadTrip(self, location):
        print("We're going on vacation!")

# So that's our class! We declare the first line with the class keyword, then after a space we write the name of the class, then a colon
# Then the next few lines are our properties, remember this is just what the car is - attributes of it
# The we get to the methods, what the car does
# These are basically just fundtions declared inside of the class!

# One interesting note: all methods have to take an extra parameter named self that is always the first one
# This lets you access any methods or properties of the class inside itself!

# So now that we have a class how do we use it? Well we have to create an instance of the class. We do this by creating a new object and assigning it to a variable
# We create an object with the constructor which is just the name of the class followed by an open and closed parenthese
myCar = Car()

# Now myCar has an instance of our car. We can create as many instances of a Car as we want and they're all separate!
# So now we can access any properties (as well as change them) and call any methods we want.
# We do this by typing the name of our car variable, followed by a dot and then the name of the property or method
# So for example
print("Your car is " + myCar.color)
myCar.color = "Blue"
print("After a new paint job your car is " + myCar.color)

myCar.revEngine()
myCar.roadTrip("Chicago")

# You create your own Cat class and give it at least two properties and two methods



# There's a ton more things to learn about classes but we're not going to cover it here
# If you want to know more keep your eye on the libaray website since we're starting a full fledged programming 101 class!
# It'll be a lot more guided with me as your instructor - so keep your eye out!
