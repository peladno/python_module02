def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
