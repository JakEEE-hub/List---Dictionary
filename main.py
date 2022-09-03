import datetime

some_num = 4 #integer (whole number)
some_decimal = 3.14 #float (decimal number)
some_str = "Hello" #string
human = True #boolean (true false)

some_list = [1, 34, 12, 17, 87]
print(some_list)

another_list = ["tesla", "toyota", "nissan", "bmw"]
print(another_list)

mixed_list = [12, "elon", True, "Smartninja", 3.14]
print(mixed_list)

some_list.append(23)
print(some_list)

some_list.insert(0, 20)
print(some_list)

another_list.pop()
print(another_list)

some_list.sort()
print(some_list)

for item in mixed_list:
    print(item)

box_list = [20, 45, 30]

box_dictionary = {"height": 20, "width": 45, "length": 30}
print(box_dictionary)
print(box_dictionary["height"])
print(box_dictionary.get("width"))
box_dictionary["weight"] = 1
box_dictionary["height"] = 40
print(box_dictionary)
box_dictionary.pop("height")
print(box_dictionary)

some_dics = {"cars": ["bmw", "vw", "tesla"], "city": "Vienna"}
some_lists = [25, "Ninja", {"city": "Vienna"}]

current_time = datetime.datetime.now()
print(current_time)