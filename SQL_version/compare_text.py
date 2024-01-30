def compare_assignments():
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import ttk

    def load_file_or_display_contents(entry, text_widget, name_var):
        file_path = entry.get()

        if not file_path:
            file_path = filedialog.askopenfilename()

        if file_path:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, file_contents)
                name_var.set(file_contents)

    def compare_text():
        text1 = text_textbox1.get("1.0", tk.END)
        text2 = text_textbox2.get("1.0", tk.END)

        words1 = set(text1.split())
        words2 = set(text2.split())

        common_words = words1.intersection(words2)

        similarity_percentage = len(common_words) / len(words1) * 100

        highlight_text(text_textbox1, common_words, "red", "bold")
        highlight_text(text_textbox2, common_words, "red", "bold")

        progress_bar['value'] = similarity_percentage

    def reset_text():
        text_textbox1.delete("1.0", tk.END)
        text_textbox2.delete("1.0", tk.END)
        progress_bar['value'] = 0
        name_var1.set("")
        name_var2.set("")

    def close_app():
        root.destroy()

    def highlight_text(text_widget, words, color, style):
        text_widget.tag_configure("highlight", foreground=color, font=("Helvetica", 10, style))

        for word in words:
            start = "1.0"
            while True:
                start = text_widget.search(word, start, stopindex=tk.END)
                if not start:
                    break

                end = f"{start}+{len(word)}c"
                text_widget.tag_add("highlight", start, end)
                start = end

    root = tk.Tk()
    root.title("Text Comparison Tool")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    text_label1 = tk.Label(frame, text="Student 1 Name:")
    text_label1.grid(row=0, column=0, padx=5, pady=5)
    name_var1 = tk.StringVar()
    name_entry1 = tk.Entry(frame, width=20, textvariable=name_var1)
    name_entry1.grid(row=0, column=1, padx=5, pady=5)
    text_textbox1 = tk.Text(frame, wrap=tk.WORD, width=30, height=10)
    text_textbox1.grid(row=0, column=2, padx=5, pady=5)

    text_label2 = tk.Label(frame, text="Student 2 Name:")
    text_label2.grid(row=1, column=0, padx=5, pady=5)
    name_var2 = tk.StringVar()
    name_entry2 = tk.Entry(frame, width=20, textvariable=name_var2)
    name_entry2.grid(row=1, column=1, padx=5, pady=5)
    text_textbox2 = tk.Text(frame, wrap=tk.WORD, width=30, height=10)
    text_textbox2.grid(row=1, column=2, padx=5, pady=5)

    load_button1 = tk.Button(frame, text="Load Text 1", command=lambda: load_file_or_display_contents(name_entry1, text_textbox1, name_var1))
    load_button1.grid(row=0, column=3, padx=5, pady=5)
    load_button2 = tk.Button(frame, text="Load Text 2", command=lambda: load_file_or_display_contents(name_entry2, text_textbox2, name_var2))
    load_button2.grid(row=1, column=3, padx=5, pady=5)

    compare_button = tk.Button(root, text="Compare", command=compare_text)
    compare_button.pack(pady=5)
    reset_button = tk.Button(root, text="Reset", command=reset_text)
    reset_button.pack(pady=5)
    close_button = tk.Button(root, text="Close", command=close_app)
    close_button.pack(pady=5)

    progress_frame = tk.Frame(root)
    progress_frame.pack(pady=10)
    progress_label = tk.Label(progress_frame, text="Similarity:")
    progress_label.pack(side=tk.LEFT, padx=5)
    progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(side=tk.LEFT, padx=5)

    root.mainloop()

compare_assignments()
