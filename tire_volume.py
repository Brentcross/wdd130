from datetime import datetime

import math
width = int(input("What is the width of the tire?: "))
aspect_ratio = int(input("What is the aspect ratio of the tire?: "))
diameter = int(input("What is the diameter of the tire?: "))

volume_1 = (math.pi * width**2)
volume_2 = volume_1 * (aspect_ratio * ((2540 * diameter) + (width * aspect_ratio)))
volume_3 = int(10000000000)
volume = round(volume_2 / volume_3, 2)

print("\n"f"Your tire size is {width}/{aspect_ratio}/R{diameter}.")
print(f"The volume of your tires is {volume:.2f} liters.")

current_date_and_time = datetime.now()

with open("wdd130/volumes.txt", "at") as volumes_file:
    print("The current date is", current_date_and_time, file=volumes_file)
    print("The Width is", width, file=volumes_file)
    print("The Aspect Ratio is", aspect_ratio, file=volumes_file)
    print("The Diameter is", diameter, file=volumes_file)
    print("The Volume is", volume, file=volumes_file)
print("File is now closed")