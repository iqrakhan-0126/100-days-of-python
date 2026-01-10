# Debugging Practice

# ❌ Type Error
# print("Age: " + 21)

# ✅ Fixed
print("Age:", 21)

# ❌ Zero Division Error
# print(10 / 0)

# ✅ Fixed
print(10 / 2)

# ❌ Wrong data type from input
age = input("Enter your age: ")
print(f"Next year you will be {int(age) + 1}")
