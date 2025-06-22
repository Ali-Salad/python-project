import tkinter as tk
from tkinter import ttk, Frame
from tkinter import messagebox
import re
from tkinter.ttk import Treeview, Style
import Database
from Database_handling import cursor


class Clients:
    def __init__(self, name, phone_number, Email):
        self.name = name
        self.phone_number = phone_number
        self.Email = Email

    def create(self):
        cursor = Database.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS client_vibe")
        cursor.execute("USE client_vibe")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clients(name VARCHAR(100) NOT NULL, phone_number CHAR(10) NOT NULL, Email VARCHAR(100) NOT NULL)")
        cursor.execute("INSERT INTO clients VALUES(%s, %s, %s)", (self.name, self.phone_number, self.Email))
        Database.connection.commit()
        cursor.close()

    @staticmethod
    def fetchall():
        cursor = Database.connection.cursor()
        cursor.execute("USE client_vibe")
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
        cursor.close()
        return clients


class ClientVibe:
    def __init__(self, master):
        self.master = master
        master.title("ClientVibe")
        master.geometry("400x300")

        self.Notebook = ttk.Notebook(master)
        self.Notebook.pack(expand=True, fill="both")
        self.add_client_tab()
        self.view_client_tab()

    def add_client_tab(self):
        frame = ttk.Frame(self.Notebook)
        self.Notebook.add(frame, text="Add Client")

        ttk.Label(frame, text="Add New Client", font=("Roboto", 14, "bold")).pack(pady=5)
        ttk.Label(frame, text="Name", font=("Roboto", 12)).pack(pady=5)
        self.Entry_name = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.Entry_name.pack(pady=5)

        ttk.Label(frame, text="Phone Number", font=("Roboto", 12)).pack(pady=5)
        self.Entry_Phone = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.Entry_Phone.pack(pady=5)

        ttk.Label(frame, text="Email", font=("Roboto", 12)).pack(pady=5)
        self.Entry_Email = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.Entry_Email.pack(pady=5)

        ttk.Button(frame, text="ADD", command=self.Add_client).pack(pady=5)
        ttk.Style().configure("TButton", font=("Roboto", 10, "normal"))

    def view_client_tab(self):
        frame = ttk.Frame(self.Notebook)
        frame.pack(fill="both", padx=10, pady=10)
        treeview = ttk.Treeview(frame, columns=("name", "phone_number", "Email"), show="headings")
        treeview.heading("name", text="Name", anchor="center")
        treeview.heading("phone_number", text="Phone Number", anchor="center")
        treeview.heading("Email", text="Email", anchor="center")
        treeview.pack(expand=True, fill="both")
        treeview.column("name", width=130)
        treeview.column("phone_number", width=100)
        treeview.column("Email", width=130)

        clients_list = Clients.fetchall()
        for client in clients_list:
            treeview.insert("", "end", values=client)
        self.Notebook.add(frame, text="View Clients")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Roboto", 10, "bold"))
        style.configure("Treeview", font=("Roboto", 10, "normal"))

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

        client = Clients(name, phone, email)
        client.create()
        messagebox.showinfo("Success", "Client successfully added")


root = tk.Tk()
app = ClientVibe(root)
root.mainloop()
