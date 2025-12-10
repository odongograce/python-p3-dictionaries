my_dict = {
    "key_one": "value one"
}

# passing in an array of arrays
my_dict.update([["key_one", "new value one"], ["key_two", "value two"]])

# passing in an array of tuples
my_dict.update([("key_two", "new value two"), ("key_three", "value three")])

# passing in a tuple of arrays
my_dict.update((["key_three", "new value three"], ["key_four", "value four"]))

# passing in a tuple of tuples
my_dict.update((("key_four", "new value four"), ("key_five", "value five")))

# using assignment operation
my_dict.update(key_five="new value five", key_six="value six")

print(my_dict)