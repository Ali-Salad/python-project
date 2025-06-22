import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class ClientVibe:
    def __init__(self, master):
        master.title("ClientVibe")
        master.geometry("400x300")

        ttk.Label(master, text="Add New Client", font=("Roboto", 14, "bold")).pack(pady=5)

        ttk.Label(master, text="Name", font=("Roboto", 12)).pack(pady=5)
        self.Entry_name = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.Entry_name.pack(pady=5)

        ttk.Label(master, text="Phone Number", font=("Roboto", 12)).pack(pady=5)
        self.Entry_Phone = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.Entry_Phone.pack(pady=5)

        ttk.Label(master, text="Email", font=("Roboto", 12)).pack(pady=5)
        self.Entry_Email = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.Entry_Email.pack(pady=5)

        ttk.Button(master, text="ADD", command=self.Add_client).pack(pady=5)
        ttk.Style().configure("TButton", font=("Roboto", 10, "normal"))

    def validate_phone(self, phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone)

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    def Add_client(self):
        name = self.Entry_name.get()
        phone = self.Entry_Phone.get()
        email = self.Entry_Email.get()

        if not self.validate_phone(phone):
            messagebox.showerror("Error", message="Please enter a valid phone number")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", message="Please enter a valid email address")
            return

        print(name)
        print(phone)
        print(email)

root = tk.Tk()
app = ClientVibe(root)
root.mainloop()
