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

# Taking first order

total_order = 0
item1 = input("Enter any item you want order: ")

if item1 in menu:
    print(f'Entered item {item1} is available')
    total_order += menu[item1]
    print(f'Your item {item1} has been added to your order')
else:
    print(f'Sorry! Entered item {item1} is currently unavailable')


# Taking another order
another_item = input('Do you want to order any other item? (Yes/No)')

if another_item == 'Yes':
    item2 = input("Enter another item you want order: ")
    print(f'Your item {item2} has been added to your order')

    if item2 in menu:
        total_order+=menu[item2]
        print(f'Your total bill is {total_order}')
else: 
    print(f'Okey! Enjoy our item!')
    print(f'Your bill is {total_order}')


