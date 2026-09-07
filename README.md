# Python Module 02: Exception Handling & Robustness

Welcome to **Python Module 02** of the 42 Tokyo Python curriculum. This module focuses on error handling, designing resilient programs, and handling unexpected runtime scenarios gracefully.

## 🎯 Objectives

- Understand exception propagation and runtime errors.
- Intercept and handle errors using `try` and `except` blocks.
- Explicitly trigger exceptions using `raise`.
- Catch and discriminate between different built-in exception types (`ValueError`, `TypeError`, `ZeroDivisionError`, etc.).
- Design custom exception hierarchies extending `Exception`.
- Ensure proper resource and state cleanup using `finally` blocks.

---

## 📁 Directory Structure & Exercises

| Exercise | Directory | File(s)                  | Description                                                                                  |
| :------- | :-------- | :----------------------- | :------------------------------------------------------------------------------------------- |
| **ex0**  | `ex0/`    | `ft_first_exception.py`  | Basic `try`/`except` block handling invalid user input (e.g. converting strings to numbers). |
| **ex1**  | `ex1/`    | `ft_raise_exception.py`  | Validating input bounds and raising built-in exceptions manually.                            |
| **ex2**  | `ex2/`    | `ft_different_errors.py` | Handling multiple distinct exception types individually.                                     |
| **ex3**  | `ex3/`    | `ft_custom_errors.py`    | Creating and using custom exception classes for domain-specific errors.                      |
| **ex4**  | `ex4/`    | `ft_finally_block.py`    | Guaranteeing cleanup and finalization logic with the `finally` construct.                    |

---

## 🚀 How to Run

Execute individual exercise scripts using:

```bash
python ex0/ft_first_exception.py
python ex3/ft_custom_errors.py
```
