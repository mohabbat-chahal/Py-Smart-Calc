# Python Project to create a simple calculator

#Three steps to build a calculator
#  1. Functions for operations
#  2. Displaying operations to user
#  3. User input
#  4. Print result

print("Welcome to the Calculator, powered by: \t Python\t and developed by:\t Ravnoor Kaur ")
# Step1:
def add(num1 , num2):
    return num1 + num2

def sub(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    return num1 / num2

def average(num1 , num2):
    return(num1 + num2) / 2

def percentage(num1 , num2):
    return((num1 + num2) / 200) * 100

# Step2:
print("Please select an operation:\n " \
      "1. Addition\n " \
      "2. Subtraction\n " \
      "3. Multiplication\n " \
      "4. Division\n " \
      "5. Average\n " \
      "6. Percentage\n" )

# Step3:
select = int(input("Select an operation from 1,2,3,4,5,6: "))

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

# Step4:
if select == 1:
    print(number1, "+", number2, "=", add(number1 , number2))
elif select == 2:
    print(number1, "-", number2, "=", sub(number1 , number2))
elif select == 3:
    print(number1, "*", number2, "=", multiply(number1 , number2))
elif select == 4:
    print(number1, "/", number2, "=", divide(number1 , number2))
elif select == 5:
    print("(" ,number1, "+", number2, ")" , "/" , "2" , "=", average(number1 , number2))
elif select == 6:
    print("(" , "(",number1, "+", number2, ")", "/", "200",")", "*", "100", "=", percentage(number1 , number2))
else:
    print("Invalid operation!!! please select again.")
