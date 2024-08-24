import tkinter as tk
import random

def generate_password():
    length = length_var.get()
    include_capital_letters = capital_letters_var.get()
    include_special_symbols = special_symbols_var.get()
    include_numbers = numbers_var.get()
    include_small_letters = small_letters_var.get()

    password = ""
    for i in range(length):
        if include_capital_letters and random.random() > 0.5:
            password += chr(random.randint(65, 90))
        elif include_small_letters and random.random() > 0.5:
            password += chr(random.randint(97, 122))
        elif include_special_symbols and random.random() > 0.5:
            password += chr(random.randint(33, 47))
        elif include_numbers and random.random() > 0.5:
            password += chr(random.randint(48, 57))
        else:
            password += chr(random.randint(97, 122))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")
root.configure(bg='aqua')

length_var = tk.IntVar()
length_var.set(8) 

capital_letters_var = tk.BooleanVar()
capital_letters_var.set(True)

small_letters_var = tk.BooleanVar()
small_letters_var.set(True)

special_symbols_var = tk.BooleanVar()
special_symbols_var.set(True)

numbers_var = tk.BooleanVar()
numbers_var.set(True)

length_label = tk.Label(root, text="Length:", font=("Helvetica", 20), bg='aqua')
length_label.pack()

length_entry = tk.Entry(root, textvariable=length_var, font=("Helvetica", 20))
length_entry.pack()

capital_letters_checkbox = tk.Checkbutton(root, text="Include capital letters", variable=capital_letters_var, font=("Helvetica", 20), bg='aqua')
capital_letters_checkbox.pack()

small_letters_checkbox = tk.Checkbutton(root, text="Include small letters", variable=small_letters_var, font=("Helvetica", 20), bg='aqua')
small_letters_checkbox.pack()

special_symbols_checkbox = tk.Checkbutton(root, text="Include special symbols", variable=special_symbols_var, font=("Helvetica", 20), bg='aqua')
special_symbols_checkbox.pack()

numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var, font=("Helvetica", 20), bg='aqua')
numbers_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 20), bg='aqua')
generate_button.pack()

password_entry = tk.Entry(root, font=("Helvetica", 20), bg='aqua')
password_entry.pack()

root.mainloop()