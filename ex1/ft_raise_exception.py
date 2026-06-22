def input_temperature(temp : str) -> int:
    return int(temp)

def test_temperature() -> int | None:
    print("=== Garden Temperature ===")

    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
        return temp
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
        return temp
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    
#     try:
#     if value > 100:
#         raise ValueError(f"Invalid Value: {value} is out of bounds.")
# except ValueError as error:
#     print(f"Caught an error! Details: {error}")
    data = "100"
    max = 40
    
    try:
        temp = input_temperature(data)
        if temp < max:
              print(f"Temperature is now {temp}°C")
    except:
        print(f"Caught input_temperature error: {data}°C is too hot for plants (max {max}°C)")
    
    data = "-50"
    min = 0
    try:
        temp = input_temperature(data)
        if temp < min:
              print(f"Temperature is now {temp}°C")
    except:
        print(f"Caught input_temperature error: {data}°C is too hot for plants (max {max}°C)")

    print("All tests completed - program didn't crash!")

    if __name__ == "__name":
        test_temperature()