# Student GPA Calculator

A Python command-line tool that calculates a credit-weighted GPA on the standard 4.0 scale from letter grades, including plus/minus grades.

## Features

- Supports A+ through F, with plus/minus grades (A- = 3.7, B+ = 3.3, and so on)
- Weights each course by its credit hours
- Rejects invalid grades and credit hours and asks again instead of crashing
- `calculate_gpa()` can be imported and used in other scripts
- Includes unit tests

## Tech

Python 3 · `unittest`

## Run it

```bash
git clone https://github.com/hi0012/Student_GPA_Calculator.git
cd Student_GPA_Calculator
python gpa_calculator.py
```

## Example

```
Course 1 grade (e.g. A, B+, C-): A
  Credit hours: 4
Course 2 grade (e.g. A, B+, C-): B+
  Credit hours: 3
Course 3 grade (e.g. A, B+, C-): C
  Credit hours: 3
Course 4 grade (e.g. A, B+, C-):

Courses: 3 | Credits: 10
GPA: 3.19
```

## Run the tests

```bash
python -m unittest -v
```
