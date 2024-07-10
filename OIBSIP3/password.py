import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import pyperclip

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator -shaik hassan ahmed")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self, padding="10 10 10 10")
        self.frame.pack(fill="both", expand=True)

        self.length_label = ttk.Label(self.frame, text="Password Length")
        self.length_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.length_entry = ttk.Entry(self.frame, width=25)
        self.length_entry.grid(column=1, row=0, padx=5, pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = ttk.Checkbutton(self.frame, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(column=0, row=1, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = ttk.Checkbutton(self.frame, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(column=0, row=2, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.digits_var = tk.BooleanVar()
        self.digits_check = ttk.Checkbutton(self.frame, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(column=0, row=3, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.symbols_var = tk.BooleanVar()
        self.symbols_check = ttk.Checkbutton(self.frame, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(column=0, row=4, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.exclude_label = ttk.Label(self.frame, text="Exclude Characters")
        self.exclude_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.exclude_entry = ttk.Entry(self.frame, width=25)
        self.exclude_entry.grid(column=1, row=5, padx=5, pady=5)

        self.generate_button = ttk.Button(self.frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=0, row=6, columnspan=2, pady=10)

        self.password_label = ttk.Label(self.frame, text="Generated Password")
        self.password_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.frame, width=25)
        self.password_entry.grid(column=1, row=7, padx=5, pady=5)

        self.copy_button = ttk.Button(self.frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(column=0, row=8, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid password length.")
            return

        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        exclude_chars = self.exclude_entry.get()
        for char in exclude_chars:
            characters = characters.replace(char, "")

        if not characters:
            messagebox.showerror("Input Error", "No characters available for password generation. Please adjust your settings.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password to copy.")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
