
#Language ---> Python 2.7

# Task--1
#Creating a Calculator
while True:

      print("================Options:==================")
      print("Enter '+' to add two numbers")
      print("Enter '-' to subtract two numbers")
      print("Enter '*' to multiply two numbers")
      print("Enter '/' to divide two numbers")
      print("Enter 'quit' to end the program")

      user_input = raw_input(": ")

      if user_input == "quit":
         break
      elif user_input == "+":
           a = float(raw_input("Enter a number: "))
           b = float(raw_input("Enter another number: "))
           result = str(a + b)
           print("The answer is " + result)
      elif user_input == "-":
           a = float(raw_input("Enter a number: "))
           b = float(raw_input("Enter another number: "))
           result = str(a - b)
           print("The answer is " + result)
      elif user_input == "*":
           a = float(raw_input("Enter a number: "))
           b = float(raw_input("Enter another number: "))
           result = str(a * b)
           print("The answer is " + result)
      elif user_input == "/":
           a = float(raw_input("Enter a number: "))
           b = float(raw_input("Enter another number: "))
           result = str(a / b)
           print("The answer is " + result)
      else:
           print("Unknown input")



        
















