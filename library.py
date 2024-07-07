import tkinter as tk
from tkinter import messagebox

inventory = {
    'jeans': 5000,
    'hoodies': 1000,
    'tie': 400,
    'trouser': 900,
    'tuxedo': 10000,
    'bow': 300,
    'blazer': 6000,
    'windcheater': 3000
}

def add_to_cart():
    item = item_var.get().lower()
    if item not in inventory:
        messagebox.showerror("Error", "Please select a valid item.")
        return
    
    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return
    
    price = inventory[item] * quantity
    cart_listbox.insert(tk.END, f"{item.capitalize()} - Quantity: {quantity} - Price: Rs. {price}")
    total_var.set(total_var.get() + price)
    item_var.set("")
    quantity_entry.delete(0, tk.END)

def process_payment():
    total_bill = float(total_var.get())
    if total_bill == 0:
        messagebox.showwarning("Warning", "Your cart is empty.")
        return
    
    payment_method = payment_var.get()
    if payment_method == "Cash":
        cash_given = cash_entry.get()
        try:
            cash_given = float(cash_given)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return
        
        if cash_given < total_bill:
            messagebox.showerror("Error", "Insufficient amount provided.")
        else:
            change = cash_given - total_bill
            messagebox.showinfo("Payment Successful", f"Change to be returned: Rs. {change}")
            reset_ui()
    
    elif payment_method == "Card":
        messagebox.showinfo("Payment Successful", f"Total amount paid: Rs. {total_bill} (via Card)")
        reset_ui()

def reset_ui():
    cart_listbox.delete(0, tk.END)
    total_var.set(0)
    item_var.set("")
    quantity_entry.delete(0, tk.END)
    cash_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chitkara Fashion Arena")
root.geometry("600x400")

title_label = tk.Label(root, text="Welcome to Chitkara Fashion Arena", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

inventory_label = tk.Label(root, text="Available Items:")
inventory_label.pack()

item_var = tk.StringVar()
item_options = tk.OptionMenu(root, item_var, *inventory.keys())
item_options.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_to_cart_button = tk.Button(root, text="Add to Cart", command=add_to_cart)
add_to_cart_button.pack(pady=10)

cart_label = tk.Label(root, text="Cart:")
cart_label.pack()

cart_listbox = tk.Listbox(root, height=5, width=50)
cart_listbox.pack()

total_var = tk.DoubleVar()  # Changed to DoubleVar to handle floating-point values
total_label = tk.Label(root, textvariable=total_var)
total_label.pack()

payment_label = tk.Label(root, text="Select Payment Method:")
payment_label.pack()

payment_var = tk.StringVar()
payment_var.set("Cash")
payment_options = tk.OptionMenu(root, payment_var, "Cash", "Card")
payment_options.pack()

payment_button = tk.Button(root, text="Process Payment", command=process_payment)
payment_button.pack(pady=10)

cash_label = tk.Label(root, text="Cash Given:")
cash_label.pack()

cash_entry = tk.Entry(root)
cash_entry.pack()

root.mainloop()
