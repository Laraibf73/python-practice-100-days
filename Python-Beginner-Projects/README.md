# Python Beginner Projects

A small collection of beginner-friendly Python projects that demonstrate basic concepts such as dictionaries, functions, loops, and user interaction.

## Projects

- `student-grade-system.py` - A student grade management system with student enrollment, marks entry, average calculation, topper selection, and grade display.
- `contact-book/` - A contact book application for adding, deleting, searching, updating, and listing contacts.
- `todo-list/` - A basic task list manager.
- `library-management-system/` - Starter project for managing books.

## Contact Book Description

The contact book project demonstrates dictionary usage and user input handling. It supports:

- adding new contacts
- deleting existing contacts
- searching contacts by name
- updating phone numbers
- displaying all stored contacts

## Contact Book Preview

<img width="1087" height="717" alt="image" src="https://github.com/user-attachments/assets/693770df-38d1-469e-b1c9-0e3126222189" />

Note: Place your contact book screenshot image at `contact-book/preview.png` in the repository. If you pasted the image earlier, save it with that filename inside the `contact-book` folder so it appears above.

## Student Grade System Preview

<img width="932" height="812" alt="image" src="https://github.com/user-attachments/assets/45adf4da-0330-4c60-a7d0-2ead0da780d1" />

## Usage

Open the project folder and run the Python script for the project you want to use:

```bash
python student-grade-system.py
```

## Notes

- Contact names are stored in uppercase for consistent lookup.
- Invalid input is handled with clear prompts.

## Comprehensive Usage & Details

This section provides explicit commands, example workflows, and the programming concepts practiced in each project.

Requirements

- Python 3.8 or newer installed and available as `python` on your PATH.

Running a project

1. Open a terminal and change to the `Python-Beginner-Projects` folder:

```bash
cd "d:/Python Code Practice/python-practice-100-days/Python-Beginner-Projects"
```

2. Run any script directly with Python, for example:

```bash
python student-grade-system.py
python ../Week2-ControlFlow_Functions/miniProject.py   # Banking system in Week2 folder
```

Student Grade System (`student-grade-system.py`)

- Features:
  - Add student (stores student name normalized to uppercase)
  - Add comma-separated marks for a student
  - Calculate average marks for a student
  - Find the topper (student with highest average)
  - Display all stored grades

- Example workflow:
  1.  Run `python student-grade-system.py`.
  2.  Choose `1` to add a student, enter the name.
  3.  Choose `2` to add marks (enter values like `78,85,90`).
  4.  Choose `3` to calculate and display the average.

- Concepts practiced:
  - Lists and list comprehensions (parsing comma-separated input)
  - Dictionaries for mapping students -> marks
  - Input/output handling and validation
  - Basic control flow (loops and conditionals)

Contact Book (`contact-book/`)

- Features:
  - Add, delete, search, update, and list contacts
  - Case-insensitive lookups via normalized (uppercase) keys

- How to show your screenshot in the README:
  1.  Save your contact-book screenshot as `preview.png` in the `contact-book` folder.
  2.  Commit the image to the repository. The main README references `contact-book/preview.png` and will display it on GitHub.

- Concepts practiced:
  - Using dictionaries for fast lookups
  - Function organization and modular code
  - Simple error handling for user input

Other Projects

- `todo-list/` and `library-management-system/` are starter templates demonstrating lists, file persistence (optionally), and CRUD-style operations.

Contributing

If you'd like to add improvements or images:

1. Place screenshot images in the appropriate project subfolder (e.g. `contact-book/preview.png`).
2. Stage and commit your changes:

```bash
git add .
git commit -m "docs: update Python-Beginner-Projects README with usage and previews"
git push origin main
```

License & Notes

These are practice projects for learning. Feel free to modify them and open PRs if you publish this repository publicly.
