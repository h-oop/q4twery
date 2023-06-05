# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

# 1)
for colour in color_data:
    print(colour["name"], colour["family"])

# 2)
for colour in color_data:
    if colour["brightness"] >= 200:
        print(colour["name"], colour["brightness"])

# 3)
count = 0
for colour in color_data:
    if colour["family"] == "Red" or colour["family"] == "Pink":
        count += 1
print(f"# of red/pink = {count}")

# 4)
search = input("what colour family?:")
count = 0
for colour in color_data:
    if colour["family"] == search:
        print(colour["name"], colour["family"])
        count +=1
print(f"# of {search} = {count}")

# 5)
search = input("what letter?:").lower()
count = 0
for colour in color_data:
    if colour["name"].lower()[0] == search:
        print(colour["name"], colour["family"])
        count +=1
print(f"# of {search} = {count}")