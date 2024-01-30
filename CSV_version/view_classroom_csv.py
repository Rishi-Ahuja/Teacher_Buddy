'''def view_classroom():    
    import csv
    import tkinter as tk
    from tkinter import ttk

    student_data_csv = "students.csv"

    def fetch_students(order_by="roll_num", filters=None):
        with open(student_data_csv, mode='r') as file:
            reader = csv.reader(file)
            students = [row for row in reader]

        if filters:
            students = [student for student in students if all(filter_func(student) for filter_func in filters)]

        order_by_index = {"admission_num": 0, "name": 1, "roll_num": 2, "class": 3, "section": 4, "grade": 5, "assignment": 6, "email": 7}
        students.sort(key=lambda x: x[order_by_index.get(order_by, 2)])
        return students

    def display_classroom():
        def update_display():
            order_by_value = order_by_var.get()
            grade_filter_value = grade_filter_var.get()
            class_filter_value = class_filter_var.get()
            assignment_filter_value = assignment_filter_var.get()

            filters = []
            if grade_filter_value:
                filters.append(lambda student: student[5] == grade_filter_value)
            if class_filter_value:
                filters.append(lambda student: student[3] == class_filter_value)
            if assignment_filter_value:
                if assignment_filter_value == 'Not Missing':
                    filters.append(lambda student: student[6] != '')
                else:
                    filters.append(lambda student: student[6] == '')

            tree.delete(*tree.get_children())
            students = fetch_students(order_by=order_by_value, filters=filters)
            for student in students:
                tree.insert("", "end", values=student)

        root = tk.Tk()
        root.title("Classroom Information")

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), padding=5)
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TEntry", font=("Arial", 12), padding=5)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 12), rowheight=25, padding=5)

        order_by_var = tk.StringVar()
        order_by_var.set("roll_num")
        order_by_menu = ttk.Combobox(root, textvariable=order_by_var, values=("admission_num", "name", "roll_num", "class", "section", "grade", "assignment", "email"))
        order_by_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        order_by_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

        grade_filter_var = tk.StringVar()
        grade_filter_menu = ttk.Combobox(root, textvariable=grade_filter_var, values=("A", "B", "C", "D", "F", ""))
        grade_filter_menu.set("")
        grade_filter_menu.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        grade_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

        class_filter_var = tk.StringVar()
        class_filter_menu = ttk.Combobox(root, textvariable=class_filter_var, values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", ""))
        class_filter_menu.set("")
        class_filter_menu.grid(row=0, column=5, padx=10, pady=10, sticky="w")
        class_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

        assignment_filter_var = tk.StringVar()
        assignment_filter_menu = ttk.Combobox(root, textvariable=assignment_filter_var, values=("Missing", "Not Missing", ""))
        assignment_filter_menu.set("")
        assignment_filter_menu.grid(row=0, column=7, padx=10, pady=10, sticky="w")
        assignment_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

        tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=10)
        tree.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")

        tree.heading(1, text="Admission Number")
        tree.heading(2, text="Name")
        tree.heading(3, text="Roll Number")
        tree.heading(4, text="Class")
        tree.heading(5, text="Section")
        tree.heading(6, text="Grade")
        tree.heading(7, text="Assignment Path")
        tree.heading(8, text="Email")

        for student in fetch_students(order_by=order_by_var.get()):
            tree.insert("", "end", values=student)

        for col in (1, 2, 3, 4, 5, 6, 7, 8):
            tree.column(col, anchor="center")

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
        scrollbar.grid(row=1, column=8, sticky="ns")
        tree.configure(yscrollcommand=scrollbar.set)

        hscrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
        hscrollbar.grid(row=2, column=0, columnspan=8, sticky="ew")
        tree.configure(xscrollcommand=hscrollbar.set)

        ttk.Label(root, text="Order By:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ttk.Label(root, text="Grade Filter:").grid(row=0, column=2, padx=10, pady=10, sticky="e")
        ttk.Label(root, text="Class Filter:").grid(row=0, column=4, padx=10, pady=10, sticky="e")
        ttk.Label(root, text="Assignment Filter:").grid(row=0, column=6, padx=10, pady=10, sticky="e")

        clear_filters_button = ttk.Button(root, text="Clear Filters", command=update_display)
        clear_filters_button.grid(row=3, column=0, columnspan=8, pady=10)

        close_button = ttk.Button(root, text="Close", command=root.destroy)
        close_button.grid(row=4, column=0, columnspan=8, pady=10)

        root.mainloop()

    display_classroom()'''
    

import csv
import tkinter as tk
from tkinter import ttk

student_data_csv = "students.csv"

def fetch_students(order_by="roll_num", filters=None):
    with open(student_data_csv, mode='r') as file:
        reader = csv.reader(file)
        students = [row for row in reader]

    if filters:
        students = [student for student in students if all(filter_func(student) for filter_func in filters)]

    order_by_index = {"admission_num": 0, "name": 1, "roll_num": 2, "class": 3, "section": 4, "grade": 5, "assignment": 6, "email": 7}
    students.sort(key=lambda x: x[order_by_index.get(order_by, 2)])
    return students

def display_classroom():
    def update_display():
        order_by_value = order_by_var.get()
        grade_filter_value = grade_filter_var.get()
        class_filter_value = class_filter_var.get()
        assignment_filter_value = assignment_filter_var.get()

        filters = []
        if grade_filter_value:
            filters.append(lambda student: student[5] == grade_filter_value)
        if class_filter_value:
            filters.append(lambda student: student[3] == class_filter_value)
        if assignment_filter_value:
            if assignment_filter_value == 'Not Missing':
                filters.append(lambda student: student[6] != '')
            else:
                filters.append(lambda student: student[6] == '')

        tree.delete(*tree.get_children())
        students = fetch_students(order_by=order_by_value, filters=filters)
        for student in students:
            tree.insert("", "end", values=student)

    root = tk.Tk()
    root.title("Classroom Information")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), padding=5)
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
    style.configure("Treeview", font=("Arial", 12), rowheight=25, padding=5)

    order_by_var = tk.StringVar()
    order_by_var.set("roll_num")
    order_by_menu = ttk.Combobox(root, textvariable=order_by_var, values=("admission_num", "name", "roll_num", "class", "section", "grade", "assignment", "email"))
    order_by_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    order_by_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

    grade_filter_var = tk.StringVar()
    grade_filter_menu = ttk.Combobox(root, textvariable=grade_filter_var, values=("A", "B", "C", "D", "F", ""))
    grade_filter_menu.set("")
    grade_filter_menu.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    grade_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

    class_filter_var = tk.StringVar()
    class_filter_menu = ttk.Combobox(root, textvariable=class_filter_var, values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", ""))
    class_filter_menu.set("")
    class_filter_menu.grid(row=0, column=5, padx=10, pady=10, sticky="w")
    class_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

    assignment_filter_var = tk.StringVar()
    assignment_filter_menu = ttk.Combobox(root, textvariable=assignment_filter_var, values=("Missing", "Not Missing", ""))
    assignment_filter_menu.set("")
    assignment_filter_menu.grid(row=0, column=7, padx=10, pady=10, sticky="w")
    assignment_filter_menu.bind("<<ComboboxSelected>>", lambda event: update_display())

    tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=10)
    tree.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")

    tree.heading(1, text="Admission Number")
    tree.heading(2, text="Name")
    tree.heading(3, text="Roll Number")
    tree.heading(4, text="Class")
    tree.heading(5, text="Section")
    tree.heading(6, text="Grade")
    tree.heading(7, text="Assignment Path")
    tree.heading(8, text="Email")

    for student in fetch_students(order_by=order_by_var.get()):
        tree.insert("", "end", values=student)

    for col in (1, 2, 3, 4, 5, 6, 7, 8):
        tree.column(col, anchor="center")

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=8, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    hscrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    hscrollbar.grid(row=2, column=0, columnspan=8, sticky="ew")
    tree.configure(xscrollcommand=hscrollbar.set)

    ttk.Label(root, text="Order By:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    ttk.Label(root, text="Grade Filter:").grid(row=0, column=2, padx=10, pady=10, sticky="e")
    ttk.Label(root, text="Class Filter:").grid(row=0, column=4, padx=10, pady=10, sticky="e")
    ttk.Label(root, text="Assignment Filter:").grid(row=0, column=6, padx=10, pady=10, sticky="e")

    clear_filters_button = ttk.Button(root, text="Clear Filters", command=update_display)
    clear_filters_button.grid(row=3, column=0, columnspan=8, pady=10)

    close_button = ttk.Button(root, text="Close", command=root.destroy)
    close_button.grid(row=4, column=0, columnspan=8, pady=10)

    root.mainloop()

display_classroom()
