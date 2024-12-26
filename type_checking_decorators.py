import functools
import inspect
import io
import contextlib
from typing import get_type_hints, Union


def print_types(func):
    """Decorator that prints the types of the formal parameters, actual parameters and their values and finally the return type of the function"""

    @functools.wraps(func)
    def wrapper(*args):
        signature = inspect.signature(func)
        params = signature.parameters
        args = list(args)
        for i, (name, param) in enumerate(params.items()):
            print(
                f"Formal par '{name}':{param.annotation}; actual par '{args[i]}':{type(args[i])}"
            )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = func(*args)

        output = stdout.getvalue()
        if output:
            print(output.strip())
        else:
            print(output, end="")  # Print the captured output
        print(
            f"Result type {signature.return_annotation}; actual result '{result}':{type(result)}"
        )

        return result  # Return the captured result

    return wrapper


def type_check(func):
    """Decorator that checks the types of the formal parameters and the return type against the actual parameters and return type"""

    @functools.wraps(func)
    def wrapper(*args):
        signature = inspect.signature(func)
        params = signature.parameters
        args = list(args)
        for i, (name, param) in enumerate(params.items()):
            if param.annotation == inspect.Parameter.empty:
                continue
            type_hints = get_type_hints(func)
            if hasattr(type_hints[name], "__args__"):
                arg_type_hint = type_hints[name].__args__
                if not isinstance(args[i], arg_type_hint):
                    print(
                        f"Parameter '{i}' has value '{args[i]}', not of type '{type_hints[name]}'"
                    )
            else:
                if not isinstance(args[i], param.annotation):
                    print(
                        f"Parameter '{i}' has value '{args[i]}', not of type '{param.annotation}'"
                    )
        result = func(*args)
        if (
            signature.return_annotation == None
            or signature.return_annotation == inspect.Parameter.empty
        ):
            return result
        elif not isinstance(result, signature.return_annotation):
            print(f"Result is '{result}', not of type '{signature.return_annotation}'")
        return result

    return wrapper


def bb_type_check(arg):
    """Decorator factory that accepts an argument and returns a decorator that is bounded to that argument"""
    arg_list = [arg]

    def decorator(func):
        """Decorator that does a bounded-blocking type checking of the formal parameters and the return type against the actual parameters and return type"""

        @functools.wraps(func)
        def wrapper(*args):
            signature = inspect.signature(func)
            params = signature.parameters
            args = list(args)
            check = False
            for i, (name, param) in enumerate(params.items()):
                if param.annotation == inspect.Parameter.empty:
                    continue
                type_hints = get_type_hints(func)
                if hasattr(type_hints[name], "__args__"):
                    arg_type_hint = type_hints[name].__args__
                    if arg_list[0] > 0:
                        if not isinstance(args[i], arg_type_hint):
                            print(
                                f"Parameter '{i}' has value '{args[i]}', not of type '{type_hints[name]}'"
                            )
                            check = True
                    elif arg_list[0] == 0:
                        if not isinstance(args[i], arg_type_hint):
                            print(
                                f"Parameter '{i}' has value '{args[i]}', not of type '{type_hints[name]}'"
                            )
                            continue
                else:
                    if arg_list[0] > 0:
                        if not isinstance(args[i], param.annotation):
                            print(
                                f"Parameter '{i}' has value '{args[i]}', not of type '{param.annotation}'"
                            )
                            check = True
                    elif arg_list[0] == 0:
                        if not isinstance(args[i], param.annotation):
                            print(
                                f"Parameter '{i}' has value '{args[i]}', not of type '{param.annotation}'"
                            )
                            continue
            if check:
                arg_list[0] -= 1
                print(f"Function blocked. Remaining blocks: {arg_list[0]}")
                return None

            result = func(*args)
            if (
                signature.return_annotation == None
                or signature.return_annotation == inspect.Parameter.empty
            ):
                return result
            elif not isinstance(result, signature.return_annotation):
                print(
                    f"Result is '{result}', not of type '{signature.return_annotation}'"
                )
                return result
            return result

        return wrapper

    return decorator


# def f(x: int | float | str, y: int | float, z) -> int:
#     pass


# sig = inspect.signature(f)
# print(sig)
# params = sig.parameters
# print(params)
# for name, param in enumerate(params.items()):
#     print(param)

# for param in params.values():
#     print(param.kind.description)

# type_hints = get_type_hints(f)
# print(type_hints)

# x_type_hint = type_hints["x"]
# print(x_type_hint)
# print(sig.return_annotation)

# if hasattr(x_type_hint, "__args__"):
#     x_type_hint_tuple = x_type_hint.__args__
#     print(x_type_hint_tuple)
#     for t in x_type_hint_tuple:
#         print(t)


# def f(x, y) -> None:
#     pass


# sig = inspect.signature(f)
# print(sig.return_annotation)
# print(inspect.Parameter.empty)
# print(sig.return_annotation == None)


# def f(x, y):
#     return x + y


# sig = inspect.signature(f)
# print(sig.return_annotation)
