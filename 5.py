# Lesson 5 - functions

# In this lesson we'll learn about functions!
# Functions are an important building block of programs and not as scary as they look!
# After all we've already looked at a few (print, range etc)

# So what are functions? Well really simply, they are a way to organize code that takes some inputs (called parameters) and returns an output
# So in the case of the range function, our parameter is the number we want it to count to and it returns all of the numbers between 0 and that number when the for loop asks
# You might remember functions from your math classes, lots of problems started with f(x)=x+2
# Same idea here! You feed in a parameter which stands in for x and you get back the value plus 2!
# Let's write up what that looks like in code and then we'll go over the syntax

def basicFunction(x):
    temporaryVariable = x + 2
    return temporaryVariable

# So every function has a first line that has 3 components: first the "def" stands for define: all functions must start with it
# Then there's the name of the function, same rules apply with variables, it must be alphanumeric and it can't start with a number
# Finally you have zero or any number of parameters enclosed by variables seperated by commas. In this case we only have one parameter named x
# Imagine parameters as a temporary variable that only lives inside of the function, you can't use it anywhere else!
# You can have any number or no parameters

# Then you can add any amount of code you like (indented with a tab of course)
# The last line of the function is the return. We want to be able to use the value we calculate in the body of the loop outside of the program.
# Since we return it, if we save it to a variable we can use it elsewhere. That would look like
result = basicFunction(5)
print(result)

# In this case, we give the function a 5, we return a (5+2) and save it into the result variable
# There can be multiple return statements in a function but whenever the code hits a return statement, it leaves the function
# Can you think of time when that might be useful?

# In if statements! We might want to do different calculations based on what the user enters!

# So let's let you get a try here. I made a basic function but am having trouble getting the first line right.
# I know I want it to be called "myCustomFunction" and I know I want the user to pass in two parameters. Can you write that for me and run the program to make sure it works?
___ ______________________
    temporaryVariable = x * y + x * x + y * y
    return temporaryVariable


# Check the answers file if you're not sure!

# You got it! Functions aren't that bad! I have a task for you: write a function that uses a loop to continually prompt the user for their name.
# If they enter the name of your favorite celebrity return a happy message otherwise return a sad message