my_dict = {
    "key_one": "value one",
    "key_two": "value two",
}
#using dict
# my_dict.update({"key_one":"I've changed", "key_three":"value three"})
#using list
# my_dict.update({"key_one":"I've changed", "key_three":"value three"})
my_dict.update([["key_one","I've changed"], ["key_three","value three"]])
my_dict.update([("key_two", "new value two"), ("key_three", "value three")])
print(my_dict)