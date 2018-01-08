# Welcome to the Coding Petting Zoo part 2
# In this lesson, we're going to learn a little bit about data types and variables
# This lesson shouldn't be wuite as long as the previous one!

# So let's jump right in:
# 1. Data types
# The computer stores different types of data differently
# Because you can do different things to different types of data
# You can't divide words from eachother but you can divide numbers just fine
# Similarly, if I asked you to uppercase a number, you might think I'm crazy!

# Python has plenty of built in data types but the most important are Strings, numbers, objects and None.
# Let's talk about them!

# a. Strings
# This is just text, just like the way we're talking now
# Text can be added (concatenated)
"This is a string aka text"
"We can add (concatenate) " + "strings"

# All text must be put in quotes, if not you get an error.

# Uncomment this line and run the program and you'll get an error!

# b. Number

# Numbers come in a few flavors:
# First we have integers - This is what you know as whole numbers (both positive and negative), let's look at a few
1
-1
100000000000000

# Unlike other programming languages, Python doesn't really have a maximum number (within reason), feel free to put in some huge numbers here
1000000000000000000000000000000000000000000000

# The other type of number is a floating point number which you may know as a decimal number
# Some examples of that:
1.4
155555.99
-0.15

# In Python these types of numbers are treated the same way, you can add hem together, divide them by each other and whatever other mathematical operations you can think of!
# That's not the case in other languages which you should keep in mind as you go forward!

# c. Booleans
# Booleans are simply true or false
True
False

# They are exactly like they look. There are a few operations you can do with booleans

# AND - this expression looks like BOOLEAN1 and BOOLEAN2
# If BOOLEAN 1 and BOOLEAN2 are both true, the answer will be true - otherwise it's false
# Try and guess what these will print before you run it!
print(True and True)
print(True and False)
print(False and False)

# OR - this expression looks like BOOLEAN1 or BOOLEAN2
# In this case, if either BOOLEAN1 or BOOLEAN2 or both is True this will be true
# Guess what these are!
print(True or True)
print(False or False)

# NOT - this expression looks like not BOOLEAN1
# This just returns the opposite of whatever BOOLEAN1 is!
# Guess what these are!
print(not True)
print(not False)

# You can combine all of these operations too!
print((not True) or True)
print(not (True or (False and False)))

# Go ahead and try your own in the space below!


# There's one more quick aside we should make: There are a few other expressions that evaluate to booleans, <, <=, =>, > and ==
# >, <, <=, >= are just what they look like, They take two numbers NUMBER1 < NUMBER2 and so on
# It evaluates to True if the statement is true, otherwise it evaluates to False
# So what does this return?
print(1 < 4)
print(6 >= 6)

# == is the equality operator (not be confused with = which is the assignment operator - there's a difference!)
# This looks like NUMBERORSTRING1 == NUMBERORSTRING2
# This is true if they're equal and false if they're not
print("EQUAL" == "EQUAL") # True
print("EQUAL" == "NOT EQUAL") # False

# d. Objects
# You can define your own custom data types here but don't worry we'll talk more about this later!

# e. None
# None is a special data type that represents nothing! This may not seem useful but it definitely is!
# Imagine with me for a second that we're getting keyboard input from the user
# We need a way to represent the user not typing anything which is where None comes in!

# 2. Variables
# So now that we know about data how do we save it?
# We definitely don't want to have to type out words or numbers every time we use them!
# We save them with variables
# Variables have two components - their name (which can be any combination of letters or numbers - no spaces! - as long as it starts with a letter)
# And what they hold, which we can assign with the equals sign

# Let's try some!
variableName = "Test"
booleanVar = True
anotherVariable = 4.9
thirdVariable = 1.1

# You try some! Save a number to our number1 and number2 variables and some text to our characters variable
number1 = 
number2 = 
characters = 

# The cool thing about varibles is that we can treat them just like what they hold, which means that they can be added, concatenated and anyhitng else their data type can do!
print(anotherVariable + thirdVariable)
print(anotherVariable + 3)

# We can also save variables into other variables!
# Like this:
addedVariables = anotherVariable + thirdVariable
print(addedVariables)

# Go ahead and add,subtract or divide your variables! 



# Now make a crazy boolean expression and save the result into a variable. Print out your result but try to guess it first!