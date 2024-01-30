import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import time
from io import StringIO
import sys

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.configure(state="normal")
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        file_entry.configure(state="readonly")

def create_checkboxes():
    rules = [
        "Minimum 150 words should be used. The limit is capped at 200 words.",
        "Stop words will not be counted as words.",
        "The paragraph should always begin with the phrase 'Once upon a time.'",
    ]

    for idx, rule in enumerate(rules, start=1):
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(root, text=rule, variable=var)
        checkbox.grid(row=idx, column=0, columnspan=3, padx=10, pady=5, sticky="w")
        checkboxes[rule] = var

def check_paragraph():
    paragraph_path = file_entry.get()

    try:
        # Redirect stdout to capture print statements
        sys.stdout = StringIO()

        # Execute the provided code with the redirected stdout
        execute_paragraph_checker(paragraph_path)

        # Retrieve the captured output
        output = sys.stdout.getvalue()

        # Display the output in a messagebox
        messagebox.showinfo("Output", output)

    finally:
        # Reset stdout to its original state
        sys.stdout = sys.__stdout__

def execute_paragraph_checker(paragraph_path):
    with open('tags.txt', 'r') as file:
        l = file.read()
    lines = l.split('\n')

    user = []
    score = 1

    with open(paragraph_path, 'r') as file:
        paragraph = file.read()

    def StopWords(x):
        nonlocal user
        x = re.sub(r"[^a-zA-Z0-9]", " ", x.lower())
        token = word_tokenize(x)
        for j in range(0, len(token)):
            match = 'rishi'
            for z in range(0, len(stop_words)):
                if token[j] == stop_words[z]:
                    match = 'nitin'
                    break
            if match == 'rishi':
                user.append(token[j])

    def WordCount(y):
        nonlocal score
        length = len(y)
        if length < 150:
            print('The length of the paragraph is less than 150.\n +1 denied.\n\n')
        elif length >= 150:
            score = score + 1
            print('The length of the paragraph is greater than 150 words.\n +1 awarded\n\n')
        else:
            print('You exceeded the word limit of the paragraph.\n +1 denied\n\n')

    def Regular(o):
        nonlocal score
        match_result = re.search('^Once upon a time', o)
        if match_result and match_result.group():
            score = score + 1
            print('Correct starting phrase.\n +1 awarded\n\n')
        else:
            print('Did not start with the required phrase.\n +1 denied.\n\n')


    def types(v):
        tags = {}
        for e in range(0, len(lines)):
            line = lines[e]
            a = line.split(':')
            if len(a) >= 2:  # Check if there are at least two elements after the split
                tags[a[0]] = a[1]

        for words in v:
            j = nltk.pos_tag([words])
            p = j[0][1]
            ok = list(j[0])
            if p in tags:
                ok[1] = tags[p]
                print(ok)
    fd = nltk.FreqDist(user)
    print(fd)
    fd.plot(20)



    def calculate():
        print('Calculating Marks and Grade:\n')
        print('\nMarks: ', score)
        if score == 3:
            print('Grade: A')
            global grade
            grade = 'A'
        elif score == 2:
            print("Grade: B")
            grade = 'B'
        else:
            print("Grade: C")
            grade = 'C'

    StopWords(paragraph)
    WordCount(user)
    Regular(paragraph)
    types(user)
    calculate()
    score_value_label.config(text=f"{score}/3\n{grade}")

root = tk.Tk()
root.title("Paragraph Checker")
root.geometry("600x300")

stop_words = stopwords.words('english')
checkboxes = {}

file_label = ttk.Label(root, text="Upload File:")
file_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

file_entry = ttk.Entry(root, width=40, state="readonly")
file_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

browse_button = ttk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

create_checkboxes()

score_label = ttk.Label(root, text="Final Score:\nGrade:")
score_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="e")


score_value_label = ttk.Label(root, text="")
score_value_label.grid(row=6, column=2, padx=10, pady=10, sticky="w")

check_button = ttk.Button(root, text="Check Paragraph", command=check_paragraph)
check_button.grid(row=7, column=0, columnspan=3, pady=10)

root.mainloop()
