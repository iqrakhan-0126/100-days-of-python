# String manipulation examples

# String Manipulation and Debugging Practice

# ❌ Example 1: Missing quotes (Syntax Error)
# print(Hello World)

# ✅ Fixed
print("Hello World")


# ❌ Example 2: String + Number (TypeError)
age = 21
# print("I am " + age + " years old")

# ✅ Fixed using type conversion
print("I am " + str(age) + " years old")


# ❌ Example 3: Missing space in string concatenation
first_name = "Iqra"
last_name = "Khan"
print(first_name + last_name)

# ✅ Fixed
print(first_name + " " + last_name)


# ❌ Example 4: New line mistake
# print("Python is fun
# Learning strings")

# ✅ Fixed using escape character
print("Python is fun\nLearning strings")


# ❌ Example 5: Wrong indentation (IndentationError)
# print("Start")
#     print("Middle")

# ✅ Fixed
print("Start")
print("Middle")


# ✅ Final Output
print("String manipulation and debugging practice completed!")
