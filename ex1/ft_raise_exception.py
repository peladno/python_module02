def input_temperature(temp: str) -> int:
    num = int(temp)
    if num > 40 :
        raise ValueError(f"{num} is too hot for plants")
    if num < 0:
        raise ValueError(f"{num} is too cold for plants")
    return num

def testing(data : str) -> None :
        try:
            print(f"Input data is '{data}'")
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as error:
            print(f"Cought input_temperature error: {error}")
        print("")
        
def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    testing("25")
    testing("abc")
    testing("100")
    testing("-50")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
