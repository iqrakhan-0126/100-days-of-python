print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m, or l \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25

else:
    print('you typed the wrong letter.')        


if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3   


if extra_cheese == 'y':
    bill += 1
print(f'Your final bill is: ${bill}.')        