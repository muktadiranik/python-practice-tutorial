# Python Practice Tutorial

A collection of runnable examples for practicing Python fundamentals. The
examples live in a single script, making it easy to experiment with the code
and compare the printed results.

## Topics

- Loops, `range()`, conditionals, and the modulo operator
- Lists, indexing, slicing, comprehensions, and nested lists
- Strings, formatting, character checks, and a simple Caesar cipher
- Functions, return values, variable scope, and variable-length arguments
- Prime numbers, basic geometry, and sorting
- Dictionaries and iteration over keys and values
- Recursion with factorial and Fibonacci examples

## Getting started

Install Python 3.8 or newer and Git, then clone the repository:

```sh
git clone https://github.com/muktadiranik/python-practice-tutorial.git
cd python-practice-tutorial
```

Run the tutorial from the repository root:

```sh
python Tutorial/tutorial.py
```

Use `python3` instead of `python` if that is how Python is installed on your
system. The script prints example results to the terminal; examples using
random numbers produce different output on each run. It uses only the Python
standard library, so no additional packages are needed to run it.

## Development tools (optional)

Create an isolated environment:

```sh
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

Install the formatting and style-checking tools:

```sh
python -m pip install -r requirements.txt
```

Check formatting and style without changing the script:

```sh
python -m black --check Tutorial/tutorial.py
python -m pycodestyle Tutorial/tutorial.py
```

## Project structure

```text
Tutorial/
    tutorial.py       # Python practice examples
requirements.txt      # Development tools and their dependencies
README.md             # Project overview and setup instructions
```

To practice, change an example, run the script again, and observe how the
output changes. You can also copy a smaller section into a separate scratch
file to focus on one concept at a time.
