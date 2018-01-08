# Lesson 4 - Loops

# Welome to lesson 4 of the coding petting zoo: in this lesson we're going to talk about looping
# Humans and computers are good at different kinds of things, humans are amzing at things luje seeing hidden patterns or recognizing faces or objects
# Those tasks are really hard for computers however. But on the other hand, computers are happy to repeat the same thing hunderds of times
# Let's talk abut how to do that!
# In Python there are two main kinds of loops: while loop and a for loop
# Let's talk about while loops first
# While loops keep repeating the code beneath it until a certain condition is met. They look like the following:
# while CONDITION:
#   Do some code

# And now a practical example:
var = 1
while var < 10:
    print("Your variable is less than 10")
    var = var + 1

# If you try to run this you will see that the statement prints 10 times
# We can go through it intuitiveley. We start at line 15. What is the value of var at that point? 1 since we jsut set it.
# Then since the condition is true, we do the code that's indented, so print the message and add 1 to var, then we check the condition again.
# In this case var equals 2 which is still less than 10 so we run it again. This continues until var equals 10. In this case, 10 is not less than 10
# So when we check the condition, it fails meaning we go to the next non indented line

# Set your name on the next line and try typing in a few names. MAke sure you understand how this works!
myName = "Josh"
while input("What's your name? ") != myName:
    print("That's not your name!")

#Now try writing your own while statements! Get creative with your conditions!


# The second part of our lesson will be the for loop:
# The for loop runs one time for every element in a collection of objects (be that numbers or characters)
# So let's say we want to individually print out every character in a string. The for loop is perfect for that!
for char in "My name is Josh":
    print(char)

# Change the name into your name and run it!

# What if you just want to get your for loop to run a fixed amount of times?
# That's where the range function comes in!
# If you call a for loop like so: 
# for number in range(6):
# print(number)
# This will run exactly 6 times and give you every number from 0 to 6 exclusive
# Don't forget youdon't have to use the number that this function gives you!
# I've written part of a 99 bottles of beer on the wall program. Try to finsih it!

for i in ___:
    print((99-i)," bottles of beer on the wall, take them down pass them around...")

# Now you have the basics of loops! Combine all you've learned and try to write a program that has a for loop inside of a four loop!
# Try to generate an x,y coordinate system with both x and y going from 0 to 10