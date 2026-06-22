def input_temperature(temp: str) -> int:
    return int(temp)


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
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    data = "100"
    max_temp = 40
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        if temp > max_temp:
            print(
                f"Caught input_temperature error: {temp}°C is too hot "
                f"for plants (max {max_temp}°C)")
        else:
            print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    data = "-50"
    min_temp = 0
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        if temp < min_temp:
            print(
                f"Caught input_temperature error: {temp}°C is too cold "
                f"for plants (min {min_temp}°C)")
        else:
            print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
