import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Error: Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Your generated password is: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#F0F0F0")

# Create a frame for input options
input_frame = tk.Frame(root, bg="#F0F0F0")
input_frame.grid(row=0, column=0, padx=20, pady=20)

# Create labels and entries for password length and character types
length_label = tk.Label(input_frame, text="Password Length:", bg="#F0F0F0", fg="#333333", font=("Arial", 14))
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(input_frame, font=("Arial", 14), width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(input_frame, text="Include Letters", variable=letters_var, onvalue=True, offvalue=False, bg="#F0F0F0", fg="#333333", font=("Arial", 12))
letters_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(input_frame, text="Include Numbers", variable=numbers_var, onvalue=True, offvalue=False, bg="#F0F0F0", fg="#333333", font=("Arial", 12))
numbers_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(input_frame, text="Include Symbols", variable=symbols_var, onvalue=True, offvalue=False, bg="#F0F0F0", fg="#333333", font=("Arial", 12))
symbols_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
generate_button.grid(row=1, column=0, padx=20, pady=10)

# Create a frame for the result
result_frame = tk.Frame(root, bg="#F0F0F0")
result_frame.grid(row=2, column=0, padx=20, pady=20)

# Create a label to display the generated password
result_label = tk.Label(result_frame, text="", bg="#F0F0F0", fg="#333333", font=("Arial", 14))
result_label.pack()

# Run the main event loop
root.mainloop()
