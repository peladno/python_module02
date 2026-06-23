class GardenError(Exception):
    default_message = "Unknown garden error"

    def __init__(self, message=None):
        self.message = message or self.default_message
        super().__init__(self.message)

class PlantError(GardenError):
    default_message = "Unknown plant error"

class WaterError(GardenError):
    default_message = "Unknown plant error"

def water_plant(plant_name : str) -> None:
    if plant_name == plant_name.capitalize():
      print(f"Watering {plant_name}: [OK]")
    else:
      raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(garden : list[str]) -> None:
  print("Opening watering system")
  try:
    for plant in garden:
      water_plant(plant)
  except PlantError as error:
    print(f"Caught PlantError: {error}")
    print(".. ending test and returning to main")
  finally:
    print("Closing watering system")
      
if __name__ == "__main__":
  print("=== Garden Watering System ===")
  print("")
  print("Testing valid plants")
  garden = ["Tomato", "Lettuce", "Carrots"]
  test_watering_system(garden)
  print("")
  print("Testing invalid plants")
  garden = ["Tomato", "lettuce", "Carrots"]
  test_watering_system(garden)
      