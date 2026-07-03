class GardenError(Exception):
    default_message = "Unknown garden error"

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.default_message
        super().__init__(self.message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def demo_specific_catches() -> None:
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print("Caught WaterError:", e)


def demo_catch_all() -> None:
    print("Testing catching all garden errors...")
    for func in (test_plant_error, test_water_error):
        try:
            func()
        except GardenError as e:
            print("Caught GardenError:", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    demo_specific_catches()
    demo_catch_all()
    print("All custom error types work correctly!")
