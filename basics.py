#list traversal
filenames = ["1.awe" , "2.frfw" , "3.fdefew"]
filenames  = [fn.replace('.' , '-') + '.txt' for fn in filenames]
print (filenames)

##sum of number in list
user_entries = ['10', '19.1', '20']

# Use list comprehension to convert each item to a float
user_numbers = [float(item) for item in user_entries]

# Print the sum of the numbers
print(sum(user_numbers))

## all keywprd
list56 = ['a' , 'a' , 'a']
if all(list56) == 'a':
    print ("All a")
else:
    print ("All now a")
file = open('todo.txt', 'r')
toDos = file.readlines()
file.close()

#with..as
with open('todo.txt', 'r') as file:
    toDos = file.readlines()
# file.close()   --- not required


#####Switch match Case Stamement

def process_data(option):
    match option:
        case 1:
            print("Option 1 selected. Performing action 1.")
        case 2:
            print("Option 2 selected. Performing action 2.")
        case 3:
            print("Option 3 selected. Performing action 3.")
        case _:
            print("nothing selected")


# Example usage
process_data(2)


##string manupulation
#slice
str1 = "abcd"
str2 = str1[1:] #str will be bcd

# "abs" in "absaass" => True

# Creating a dictionary
person = {
    'name': 'John',
    'age': 30,
    'city': 'Exampleville',
    'is_student': False
}
# Creating a tuple
fruits = ('apple', 'banana', 'orange')

# Accessing dictionary elements
print("Name:", person['name'])
print("Age:", person['age'])
print("City:", person['city'])
print("Is Student:", person['is_student'])

# Modifying dictionary values
person['age'] = 31
person['is_student'] = True

# Adding a new key-value pair
person['occupation'] = 'Engineer'

# Accessing all keys and values
print("\nAll keys:", person.keys())
print("All values:", person.values())

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")


# Simple example with try-except

try:
    # Attempting to convert user input to an integer
    user_input = input("Enter a number: ")
    number = int(user_input)

    # Dividing 10 by the entered number
    result = 10 / number

    # Printing the result
    print("Result:", result)

except ValueError:
    # Handling the ValueError if the user doesn't enter a valid integer
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    # Handling the ZeroDivisionError if the user enters 0
    print("Error: Cannot divide by zero.")

except Exception as e:
    # Handling other unexpected exceptions
    print(f"An unexpected error occurred: {e}")

else:
    # Executed if no exception occurs
    print("No errors occurred.")

finally:
    # Always executed, whether an exception occurred or not
    print("This block is always executed.")



#functions in python
# Simple example of a function in Python

def add_numbers(a, b):
    """
    This function takes two numbers as parameters and returns their sum.
    """
    result = a + b
    return result

# Using the function
num1 = 5
num2 = 7

sum_result = add_numbers(num1, num2)


sentence = "This;is;a;simple;example."

# Splitting the string into a list of words
words = sentence.split(';')

# Printing the result
print("Original sentence:", sentence)
print("List of words:", words)

#defaults argument
def greet(name, greeting="Hello"):
    """
    This function takes a 'name' parameter and an optional 'greeting' parameter.
    If 'greeting' is not provided, it defaults to "Hello".
    """
    print(f"{greeting}, {name}!")

# Calling the function with both parameters
greet("Alice")

# Calling the function with a custom greeting
greet("Bob", "Good morning")
