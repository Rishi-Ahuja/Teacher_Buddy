def add_student_csv():    
    import csv
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
    from tkinter import ttk

    student_data_csv = "students.csv"

    student_admission_numbers = []   # Admission number
    student_names = []               # Name
    student_roll_numbers = []        # Roll number
    student_classes = []             # Class
    student_sections = []            # Section
    student_grades = []              # Grade
    student_assignments = []         # Assignment path
    student_emails = []              # Email


    def add_student():
        try:
            admission_number = int(admission_number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Admission Number must be a unique integer.")
            return

        name = name_entry.get()
        roll_number = roll_number_entry.get()
        class_name = class_entry.get()
        section = section_entry.get()
        grade = grade_entry.get()
        assignment = file_path_label["text"] or "missing"  # Default value if no assignment is provided
        email = email_entry.get() or "missing"  # Default value if no email is provided

        if admission_number in student_admission_numbers:
            messagebox.showerror("Error", "Admission Number must be unique.")
            return

        student_admission_numbers.append(admission_number)
        student_names.append(name)
        student_roll_numbers.append(roll_number)
        student_classes.append(class_name)
        student_sections.append(section)
        student_grades.append(grade)
        student_assignments.append(assignment)
        student_emails.append(email)

        admission_number_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        roll_number_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        section_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        file_path_label.config(text="")

        messagebox.showinfo("Success", "Student information added successfully.")


    def browse_file():
        file_path = filedialog.askopenfilename()
        file_path_label.config(text=file_path)


    def save_to_csv():
        with open(student_data_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(student_admission_numbers)):
                writer.writerow([
                    student_admission_numbers[i],
                    student_names[i],
                    student_roll_numbers[i],
                    student_classes[i],
                    student_sections[i],
                    student_grades[i],
                    student_assignments[i],
                    student_emails[i]
                ])
        messagebox.showinfo("Success", f"Data saved to {student_data_csv} successfully.")


    def close_window():
        root.destroy()


    root = tk.Tk()
    root.title("Student Information")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))

    fields = [
        ("Admission Number:", "admission_number_entry"),
        ("Name:", "name_entry"),
        ("Roll Number:", "roll_number_entry"),
        ("Class:", "class_entry"),
        ("Section:", "section_entry"),
        ("Grade:", "grade_entry"),
        ("Upload Assignment:", "file_path_label"),
        ("Email:", "email_entry"),
    ]

    for i, (label_text, widget_name) in enumerate(fields):
        label = ttk.Label(root, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        if widget_name == "file_path_label":
            widget = ttk.Label(root, text="")
            browse_button = ttk.Button(root, text="Browse", command=browse_file)
            widget.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            browse_button.grid(row=i, column=2, padx=10, pady=5)
        else:
            widget = ttk.Entry(root)
            widget.grid(row=i, column=1, columnspan=2, padx=10, pady=5)

        globals()[widget_name] = widget

    submit_button = ttk.Button(root, text="Add Student", command=add_student)
    submit_button.grid(row=len(fields), column=0, columnspan=3, padx=10, pady=10)

    save_csv_button = ttk.Button(root, text="Save to CSV", command=save_to_csv)
    save_csv_button.grid(row=len(fields) + 1, column=0, columnspan=3, padx=10, pady=10)

    close_button = ttk.Button(root, text="Close", command=close_window)
    close_button.grid(row=len(fields) + 2, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()
