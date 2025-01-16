# Easy Python Project

Welcome to this simple Python project! This guide will walk you through creating a beginner-friendly Python script that introduces you to essential programming concepts.

## Project: Even or Odd Checker

This project is a simple script where you can pass a number as a parameter, and the program determines whether the number is even or odd.

### Features:
- Accepts a parameter instead of user input.
- Checks if the number is even or odd using basic logic.
- Provides instant feedback via function output.

---

## Example Code
```python
def even_or_odd_checker(number):
    """
    Determines if a number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Example usage
if __name__ == "__main__":
    test_numbers = [10, 15, 0, -4, -7]
    for num in test_numbers:
        print(even_or_odd_checker(num))
```

---

## How to Run the Code
1. Make sure you have Python installed on your computer.
2. Copy and paste the code into a file named `even_or_odd_checker.py`.
3. Open your terminal or command prompt, navigate to the folder containing the file, and run the command:
   ```bash
   python even_or_odd_checker.py
   ```
4. Observe the outputs for the test numbers included in the script.

---

## Learning Outcomes
By completing this project, you will:
- Learn how to use functions to handle inputs.
- Understand how to use conditional statements for decision-making.
- Practice writing reusable code.
- Gain experience running Python scripts in the terminal.

---

Feel free to customize and enhance this project! Happy coding!
