from datetime import datetime
import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (
    math.pi
    * width**2
    * aspect_ratio
    * (width * aspect_ratio + 2540 * wheel_diameter)
    / 10_000_000_000
)

print(f"The approximate volume is {volume:.2f} liters")

current_date = datetime.now().strftime("%Y-%m-%d")
with open("volumes.txt", "at", encoding="utf-8") as volumes_file:
    print(
        f"{current_date}, {width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}",
        file=volumes_file,
    )