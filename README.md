# Teacher Buddy - README

![Paragraph Checker Logo](/images/Logo.png)  
A powerful, user-friendly tool for evaluating and grading paragraphs based on predefined rules.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
The **Paragraph Checker** application evaluates a paragraph for:
1. Minimum word count (150 words).
2. Proper starting phrase ("Once upon a time...").
3. Presence of stop words.
4. Word types and frequencies.

It provides real-time feedback, scoring, and visualizes word usage.

---

## Features
- **File Upload:** Easily upload text files for analysis.
- **Real-Time Evaluation:** Automatic scoring as rules are satisfied.
- **Dynamic Filters:** Filter text using stop words.
- **Frequency Visualization:** Visualize word frequency using a bar chart.
- **Database Integration:** Store and fetch student data (SQL support).

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Paragraph-Checker.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download NLTK corpora:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    ```

4. Run the application:
    ```bash
    python main.py
    ```

---

## Usage
1. Launch the application and upload a `.txt` file containing your paragraph.
2. View real-time evaluation with checkboxes indicating rule compliance.
3. Review the final score displayed at the bottom.

---

## Screenshots
### Home Screen
![Home Screen](/images/homee.png)

### Paragraph Evaluation
![Evaluation Screen](/images/score.png)

### Word Frequency Visualization
![Word Frequency](/images/plagiarism.png)

---

## Tech Stack
- **Programming Language:** Python
- **Libraries:**
  - `nltk`
  - `tkinter`
  - `matplotlib`
- **Database:** MySQL

---

## Contributing
We welcome contributions! Here's how you can help:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Added YourFeature"
    ```
4. Push to your branch:
    ```bash
    git push origin feature/YourFeature
    ```
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
Special thanks to the following resources:
- [Stack Overflow](https://stackoverflow.com)
- [GitHub](https://github.com)
- [W3Schools](https://www.w3schools.com)
- [Khan Academy](https://www.khanacademy.org)
