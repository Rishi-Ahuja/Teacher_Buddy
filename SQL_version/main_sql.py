def main_sql():
    import tkinter as tk
    from tkinter import ttk
    import add_student_sql as add
    import view_classroom_sql as vc
    import compare_text as ct
    import score as sc

    def open_add_student_window():
        add.add_student_sql()

    def open_view_classroom_window():
        vc.view_classroom()

    def open_plagiarism_check_window():
        ct.compare_assignments()

    def open_score_assignment_window():
        sc.score()

    root = tk.Tk()
    root.title("Teacher Buddy (SQL Edition)")

    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    heading_label = tk.Label(root, text="Teacher Buddy App", font=("Arial", 24))
    heading_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack()

    style = ttk.Style()
    style.configure("TButton", relief=tk.RAISED, padding=(15, 10))  # Increase the button padding

    button_width = 40
    button_height = 3

    add_student_button = ttk.Button(button_frame, text="Add Student", command=open_add_student_window, width=button_width, style="TButton")
    add_student_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    view_classroom_button = ttk.Button(button_frame, text="View Classroom", command=open_view_classroom_window, width=button_width, style="TButton")
    view_classroom_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    plagiarism_check_button = ttk.Button(button_frame, text="Plagiarism Check", command=open_plagiarism_check_window, width=button_width, style="TButton")
    plagiarism_check_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    score_assignment_button = ttk.Button(button_frame, text="Score Assignment", command=open_score_assignment_window, width=button_width, style="TButton")
    score_assignment_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    root.mainloop()
