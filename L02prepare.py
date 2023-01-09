import math

items = int(input(f"Enter the number of items you have: "))
box_capacity = int(input(f"Enter how many items per box: "))

boxes = math.ceil(items / box_capacity)


print("\n"f"For {items} item(s), packing {box_capacity} items in each box you will need {boxes} box(es).")