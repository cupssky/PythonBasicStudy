my_dict = {}
print(type(my_dict))

my_dict[0] = 'a'
print(my_dict)

my_dict['b'] = 1

print(my_dict)

my_dict['동물'] = '돼지'
print(my_dict)

del my_dict[0]
print(my_dict)

for value in my_dict.values():
    print(value)

for keys in my_dict.keys():
    print(keys)

for key, value in my_dict.items():
    print(key, value)
