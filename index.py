menu = {
    'Pizza' : 280,
    'Pasta' : 180,
    'Chawmin' : 150,
    'Fried rice' : 190,
    'Coffee' : 40,
}

# Greeting our customer
print("Welcome to our restro")
print("-------------------------------------")

# Printing our menu
print(" Pizza : 280tk\n Pasta : 180tk\n Chawmin : 150tk\n Fried rice : 190tk\n Coffee : 40tk\n")

# 

total_order = 0
item1 = input("Enter any item you want order: ")

if item1 in menu:
    print('Entered item is available')
else:
    print('Sorry! Entered item is currently unavailable')