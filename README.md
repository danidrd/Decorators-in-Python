# Decorators-in-Python

This repository contains three decorators implemented in Python, along with tests to demonstrate their usage. The decorators are defined in the `type_checking_decorators.py` file and include `print_types`, `type_check`, and `bb_type_check`.

## Decorators

### `print_types`

The `print_types` decorator prints the types of the formal parameters, actual parameters, their values, and the return type of the function. It helps in introspecting the function's behavior by displaying detailed type information.

### `type_check`

The `type_check` decorator checks the types of the formal parameters and the return type against the actual parameters and return type. It ensures that the function is called with the correct types and prints a message if there is a mismatch.

### `bb_type_check`

The `bb_type_check` decorator is a decorator factory that accepts an argument and returns a decorator. This decorator performs bounded-blocking type checking of the formal parameters and the return type against the actual parameters and return type. If the types do not match, the function call is blocked a specified number of times before allowing it to proceed.

## Tests

The repository includes three test files (test1.py, test2.py, test3.py) that demonstrate the usage of the decorators with various functions. Each test file contains multiple function definitions and calls to showcase the behavior of the decorators.

## Log

The repository includes three log files (log1.txt, log2.txt, log3.txt) provided in the log folder, each logN file is useful only for comparing to the correspondent execution of testN.py.

## Example Usage

`print_types` is useful only for printing actual, formal parameters and result types.
```bash
@print_types
def foo(...)
```

`type_check` is a way to check the difference between actual and formal parameters and result types.
```bash
@type_check
def foo(...)
```

`bb_type_check` bounded-blocking `type_check` extension, has actually the same behavior as `type_check` but includes blocking capability.
```bash
@bb_type_check(N)
def foo(...)
```

## Installation

To install and run the code, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/danidrd/Decorators-in-Python.git
cd Decorators-in-Python
```

2. How to check the execution of testN.py against a file:

```bash
echo $ python3 testN.py > temp.txt && python3 testN.py >> temp.txt

diff temp.txt log/logN.txt
```

replacing N with:
1. for testing `print_types`
2. for testing
`type_check`
3. for testing 
`bb_type_check`

