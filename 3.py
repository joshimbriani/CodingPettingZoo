# Lesson 3 - user input and if statements

# Welcome to lesson 3 of the coding petting zoo!
# In this lesson we're going to be learning about how to get user input and if statements.
# Without user input, our programs would be pretty boring so we definitely want to have ways to get user input!

# So let's do that first! 
# It's accom[plished via the input function. Don't worry too much about what functions are, we'll talk about it later!
# The easiest way to figure this out is just by looking at an example
userinput = input("Enter your statement: ")
print("You said '" + userinput + "'")

# You can give this input function one string in between the parenthesis, this is the prompt it asks you
# In our example we save what the user inputs into a variable
# If we didn't we would just lose what the user inputs!
# You try it here! I've created a variable and set it to None. Go ahead and set that variable to get the input and then print it out!

userInput = None
# Your code here!

# That was easy! Now let's get to the second part of this lesson: if statements
# So until now our programs haven't been very smart
# Ideally we'll be able to create programs where the computer does different things based on what the user enters
# We do this via the if statement!
# The if statement looks like the following: 
# if EXPRESSION:
#   Some other code
# Some things to note: EXPRESSION is any collection of variables or numbers that evaluate to true or false
# So in this case think of all of the boolean expressions (and, equality, or and not) that we worked on last lesson!
# The code that you want to be run if the EXPRESSION is met _needs_ to be tabbed over. This is how Python tells what you want to be run!
# Let's look at an example

ourVariable = 6
if ourVariable > 5:
    print("It's greater than 5!")

# Create your own variable and test it with the if statement and the operators we know!


# We also have else statements: these can only be used with an if statements and only get run if the if condition is false
# It looks pretty similar to the if statement but doesn't take an expressison, don't forget to tab on the line after the else!
# else:
#   Code here
userVariable = 7
if userVariable == 8:
    print("You guessed my number!")
else:
    print("Try again!")

# The last if statenebt idea we'll cover this lesson is the elif statement
# Let's say if a variable is 5 we want to print a message, if it's 6 we want to print a different one and if it's 7 we want to print yet another one
# And if it's none of the above, we want to print something else
# How would we do this? Well we could create a bunch of if statements like the following
variable = 5
if variable == 5:
    print("It's 5!")
if variable == 6:
    print("It's 6!")
if variable == 7:
    print("It's 7!")
else:
    print("It's something else")

# Try running it and see what goes wrong!

# It prints both "It's 5" and "It's something else", that's not right!
# What's the issue here? Well each new if statement is an entirely new check
# We want to combine a bunch of if statements into one check, we do this with the elif statement
# Elif stands for else if
# It looks pretty similar to a mixture of the if and else:
# elif EXPRESSION:
#   Code to execute
# Like the if it takes an expression
# Like the else it can only be used with an if
# Let's check out an example
variable = 5
if variable == 5:
    print("It's 5!")
elif variable == 6:
    print("It's 6!")

# Ifs, Elses and ELifs can all be combined!
# Go ahead and try to rewrite our complicated statement we did on line 54 with if, elif and elses!
variable = 5 
# Your code here!