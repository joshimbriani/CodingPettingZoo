# Welcome to the Coding Petting Zoo!
# We're hoping that this serves as a self paced introduction to how to code
# Keep your ear out, we'll be having a more traditional Intro to Programming at the Central Library downtown!

# So let's get started
# In this first lesson, we'll be covering printing and expressions!

# First of all, what you're reading right now is a comment
# Any text that follows a pound/hashtag symbol is a comment
# You can type whatever like and the program won't try to make sense of it
# SGSGHODGSJHISDOIDFNOFDS
# See! That doesn't make any sense but the program will still run fine!

# But generally we use comments to explin our reasonsing
# Although the code in these lessons will be relatively simple, when you get good at programming...
# You'll be able to do some really complicated stuff,
# Stuff that you might not remember how you did in a week or two!
# So make sure you leave comments explaining what you did, if there's anything that's tricky!

# Comments are also how I'll be able to explain coding to you in these lessons!

# 1. Print statements
# So before we learn anything else, we should learn how to have the program print out things
# This way we can see how the program is working!

# So we do this through the print statement
# To print something to the screen, all you have to do is type print("This is something that will be printed to the screen")
# Couple things to note here:
# 1. print is an example of a function (don't worry if that doesn't make sense, we'll go over it in lesson 5!)
# 2. If you want to print out text (so combinations of words and/or numbers), you need to enclose the words in quotes
# (If you want to just print 1 number, feel free to leave the quotes out)
# Let's give it a shot! I'll try one first
print("Hello everyone!")

# If you run the program now by right clicking on the screen and selecting "Run in Terminal", you'll see this line added to the screen
# Now you give it a try! Print out anything you want on the next line
print("This is an example!")


# Give it a run and see if you see it! You should see my text and yours.
# Try printing out just one number without quotes now
print(7)


# Awesome job! You just printed out a string and a number!
# You're basically already a programmer!

# So now onto the next part of our lesson: expressions
# Expressions are basically the arithmetic you learned in 2nd grade
# Coding has all of the ones you're used to: +, -, /, * and a new one %
# So let's go through them! 

# 1. + - Addition
# Addition works just like you'd expect! Type one number, type a plus and type another number and you'll get the sum!
# Let's try one now:
print(3 + 6)

# Try running this and you should see 9, just like we'd expect!

# The + symbol is a little trickier when you try to add text together
# If both sides of our expression is text surrounded by quotes, it will just combine those two pieces of text
# So what do you think that the following print statement will do?
print("What will " + "this do?")

# You guessed it, it'll print out What will this do?
# This is also known as concatenation


# 2. - Subtraction
# Same idea with this one:
# Give it two numbers and it will subtract the second from the first
print(9 - 3)

# 3. * - Multipplication
# This is another easy one- just like you remember from elementary school!
print(9 * 3)

# 4. / - Division
# Division is handled differently in different programming languages but in Python (what you're learning) division removes the remainder
# Remeber in 2nd grade when you learned that the remainder in division is just whatever left over that doesn't fit in the whole number?
# Well Python throws that out and doesn't return it
# So guess what this line will print:
print (7 / 3)

# You guessed it - 2 because 3 goes into 7, 2 1/3 time and then Python throws out the 1/3, giving us an answer of 2!

# So what happens to that 1/3? Well if we want we can get it with our next operator:
# 5. % - Modulus
# Modulus is a little trickier
# Like division, modulus takes two numbers and instead of returning the classic division result,
# It instead returns the remainder, expressed as a whole number!
# Let's look at an example and it'll make more sense
print(7 % 3)

# What does this print? 1. Why? Well let's go through it!
# So what was the answer of 7 / 3? 2, right, just like we did a minute ago.
# So how much of our original number didn't fit into that 2?
# Well 2 * 3 = 6 so there was 7 - 6 = 1 that didn't fit so our answer is 1!
# Let's check this out a few more times:
print(5 % 2) # = 1 because 5 / 2 = 2 => 2*2=4 => 5-4 = 1

# Give a shout if you don't undertand this and we'd be glad to explain it!


# Just like you learned in school, order of operations matters
# Python uses PEMDAS just like we did in school

# Now it's your turn:
# Write a few statemetns using all of the types we learned today! Make them nice and complex!
print(5 * (4 - 7))
print((4 + 6) % 2)
print((5 * 4) / 9)

# When you're done feel free to move to the next station!