# Create a new window with the title "Address Entry Form"

# def input_num():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
# def add():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
# def substract():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"

# def funcadd():
#     pass
#
# def funcsub():
#     pass
#
# def func_None():
#     print("cannot find func")
#
# func_dict = {"a": funcadd, "b": funcsub}
#
# def func(x):
#     return func_dict.get(x, func_None)()

# def  fun_a():
#
#     print 'a'
#
# def  fun_b():
#
#     print 'b'
#
# def  fun_z():
#
#     print 'z'
#
# def  test_function(input_key):
#
#     function_map = {
#                      'a': fun_a,
#                      'b': fun_b,
#                      'z': fun_z,
#                     }
#     return function_map[input_key]()

# string formatting
# name = "Eric"
# age = 74
# "Hello, %s. You are %s." % (name, age)
# "Hello, {1}. You are {0}.".format(age, name)
# person = {'name': 'Eric', 'age': 74}
# "Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
# f"Hello, {name}. You are {age}."
# f"{2 * 37}"
# >> >
#
# def to_lowercase(input):
#     ...
#     return input.lower()
#
# >> > name = "Eric Idle"
# >> > f"{to_lowercase(name)} is funny."
# 'eric idle is funny.'
#
# class Comedian:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}."
#
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
#
#     >> > new_comedian = Comedian("Eric", "Idle", "74")
#     >> > f"{new_comedian}"
#     'Eric Idle is 74.'