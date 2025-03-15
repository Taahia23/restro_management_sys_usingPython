import tkinter as tk
from tkinter import messagebox

# Menu items and their prices
menu = {
    'Pizza': 280,
    'Pasta': 180,
    'Chawmin': 150,
    'Fried Rice': 190,
    'Coffee': 40,
}

# Function to calculate total
def calculate_total():
    total = 0
    selected_items = []
    
    for item in menu:
        if checkboxes[item].get() == 1:
            total += menu[item]
            selected_items.append(item)
    
    if not selected_items:
        messagebox.showwarning("No Selection", "Please select at least one item.")
        return
    
    another_order = messagebox.askyesno("Order More", "Do you want to order another item?")
    if another_order:
        return
    
    messagebox.showinfo("Order Summary", f"You ordered: {', '.join(selected_items)}\nTotal: {total} Tk\nEnjoy your meal!")

# Creating main window
root = tk.Tk()
root.title("Restaurant Order System")
root.geometry("350x350")

# Heading Label
tk.Label(root, text="Welcome to Our Restaurant", font=("Arial", 14)).pack(pady=10)

# Dictionary to store checkbox variables
checkboxes = {}

# Creating checkboxes for each menu item
for item in menu:
    var = tk.IntVar()
    checkboxes[item] = var
    tk.Checkbutton(root, text=f"{item} - {menu[item]} Tk", variable=var).pack(anchor='w')


# Order Button
tk.Button(root, text="Place Order", command=calculate_total, font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=10)


# Run the Tkinter event loop
root.mainloop()