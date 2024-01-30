import tkinter as tk
from tkinter import ttk
import main_sql as ms
import main_csv as mc

def open_csv_version():
    mc.main_csv()
    print("Opening CSV version")

def open_sql_version():
    ms.main_sql()
    print("Opening SQL version")

root = tk.Tk()
root.title("Teacher Buddy")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 14, "bold"))

logo_image = tk.PhotoImage(file="/Users/rishiahuja/Desktop/buddy/logo.png")
logo_label = ttk.Label(root, image=logo_image)
logo_label.grid(row=0, column=0, columnspan=2, pady=20)

csv_button = ttk.Button(root, text="CSV Version", command=open_csv_version)
csv_button.grid(row=1, column=0, padx=20, pady=10)

sql_button = ttk.Button(root, text="SQL Version", command=open_sql_version)
sql_button.grid(row=1, column=1, padx=20, pady=10)

instructions_label = ttk.Label(root, text="Select the version you want to use.", style="TLabel")
instructions_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
