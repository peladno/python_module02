def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("../ex2/hola.py")
    elif operation_number == 3:
        "1" + 1
    else:
        return


def test_error_types(num: int) -> None:
    print("Testing ...")
    try:
        garden_operations(num)
    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    except FileNotFoundError as error:
        print(f"Error: {error}")
    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    print("Done")
