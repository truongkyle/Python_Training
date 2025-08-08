my_list1 = [1,4,3,1]
my_list2 = ["a", "b", "c"]
for i, v in zip(my_list1, my_list2):
    print(f"value i: {i}, value v: {v}")
checked_item = 6
try:
    print(f"index of {checked_item} in my_list1 is {my_list1.index(checked_item)}")
except Exception as e:
    print(f"Exception occured: {e}")

checked_item2 = 1
print(f"{checked_item2} account of {my_list1.count(checked_item2)}")

my_dict_list = [
    {"name": "ky", "age": "28"},
    {"name": "nam", "age": "18"},
    {"name": "Han", "age": "22"},
    {"name": "Bao", "age": "28"},
    ]
sorted_list = sorted(my_dict_list, key=lambda e: -int(e["age"]))
print(sorted_list)