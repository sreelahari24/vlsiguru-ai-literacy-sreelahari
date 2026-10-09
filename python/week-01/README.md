# Practical Activity B — Start Python with CS50P

1. Objective

The objective of this activity is to learn the fundamentals of Python programming through CS50P Week 0. The activity focuses on variables, functions, input/output, basic data types, and simple debugging. I will apply these concepts by writing and running a small Python program.

2. Learning Resource

Course: CS50's Introduction to Programming with Python (CS50P)

Week: Week 0 — Functions, Variables

Course link: [https://cs50.harvard.edu/python/weeks/0/](https://cs50.harvard.edu/python/weeks/0/)

Python execution environment: Google Colab

Link: [https://colab.research.google.com/](https://colab.research.google.com/)

## 3. Concepts Learned

Variables

Variables are used to store values that can be accessed and modified during program execution.

Example:

```python
voltage = 5
current = 2
```

Here, `voltage` and `current` store numerical values.

### Basic Data Types

Python provides different data types for representing information.

- `int`: Stores whole numbers, such as `10`.
- `float`: Stores decimal numbers, such as `3.3`.
- `str`: Stores text, such as `"Python"`.
- `bool`: Represents Boolean values, `True` or `False`.

Input and Output

The `input()` function accepts information entered by the user, while `print()` displays information on the screen.

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Functions

Functions are reusable blocks of code that perform specific tasks. They are defined using the `def` keyword.

Example:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

### Simple Debugging

Debugging is the process of identifying and correcting errors in a program. Common errors include syntax errors, runtime errors, and logical errors.

For example, a missing closing parenthesis in a `print()` statement causes a syntax error. Correcting the statement allows the program to execute properly.

 4. Python Program — Electrical Power Calculator

### Objective

To write a Python program that accepts voltage and current as inputs and calculates electrical power using the formula:

P = V × I

Where:

- P is electrical power in watts.
- V is voltage in volts.
- I is current in amperes.

Source Code

Filename: `electrical_power.py`

```python
voltage = float(input("Enter voltage in volts: "))
current = float(input("Enter current in amperes: "))

power = voltage * current

print("Voltage:", voltage, "V")
print("Current:is th", current, "A")
print("Electrical Power:", power, "W")
```

5. Program Explanation

1. The program accepts voltage and current from the user.
2. The `float()` function converts the entered values into floating-point numbers.
3. The program multiplies voltage by current to calculate electrical power.
4. The `print()` function displays the input values and calculated power.

This program demonstrates variables, floating-point data types, user input, arithmetic operations, and output.

## 6. Testing and Expected Output

Example test inputs:

- Voltage: 5 V
- Current: 2 A

Expected output:

```text
Enter voltage in volts: 5
Enter current in amperes: 2
Voltage: 5.0 V
Current: 2.0 A
Electrical Power: 10.0 W
```

The expected power is 10 watts because 5 × 2 = 10.

The expected output should be compared with the actual output after running the program.

7. What I Learned

Through this activity, I learned the basic structure of a Python program and how variables store values. I practised accepting user input, converting data types, performing arithmetic calculations, and displaying results. I also learned the importance of debugging errors and checking program output.

The electrical power calculator demonstrates how Python can be applied to a simple engineering problem.

 8. Conclusion

This activity provides an introduction to Python programming through a practical engineering example. Writing and testing the electrical power calculator helps reinforce the fundamental programming concepts needed for future work in automation, data analysis, and AI applications.

The next step is to continue learning through CS50P and practise writing, executing, and debugging more Python programs.
