#Jaunel Deans
# October 23, 2023
# We used comments to answer the investigate questions on the example code.

# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  ## Answer: The condition guess < number, will run because it is true. Therefore, the if statement "Too Low!" will be outputed.

# What happens if you input the guess '6'?
  ## Answer: The condition guess > number, will run because it is true. Therefore, the if statement "Too High!" will be outputed.

# What happens if you input the guess '5'?
  ## Answer: The condition guess == number, will run because it is true. Therefore, the if statement "Correct" will be outputed.

# What happens if you input the guess '-5'?
  ## Answer: The condition guess < number, will run because it is true. Therefore, the if statement "Too Low!" will be outputed.

# What happens if you input the guess '0'?
  ## Answer: The condition guess < number, will run because it is true. Therefore, the if statement "Too Low!" will be outputed.

# What do the symbols '<' and '>' mean on lines 9 and 11?
  ## Answer < means "less than" and > means "greater than".

# What happens if you change line 5 to if guess = number: ?
  ## Answer: There would be a syntax error because you can not assign a value to a variable in an if statement

# What do you notice about each line that FOLLOWS each IF statement?
  ## Answer: The value that will be output is indented. 


