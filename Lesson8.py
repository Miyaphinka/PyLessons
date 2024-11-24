# name = input("What is your name?")
# location = input("Please enter where are you from: ")

# print(f"Your name is {name} and you are from {location}")
 

# name = input("What is your name?")
# location = input("Please enter where are you from: ")

# user = {
# name: name,
# location:location
# }
# print(f"Your name is {user[name]} and you are from {user[location]}") 

prompt = "Tell me something and i'll repeat "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# prompt += "\nWhat is your name? "

# name = input(prompt)

# a relation give tru or false basen on a condition
# a boolean is a type that includes True or False
# age = int(input("How old are you? "))
# age = int(age)
# is_legal = age >= 18

# if is_legal:
#     print("Welcome")
# if age >= 18:
#     print("welcome")

# def is_even(number):
#     return number % 2 == 0

# # print(f"Is 6 even? {is_even(6)}")
# # print(f"Is 7 even? {is_even(7)}")
# # while False:
# #     print("sorry, you are not legal")
# #     age = int(input("How old are you? "))

# while True:
#     try:
#         prompt = "Give me a number: "
#         number = int(input(prompt))
#         if number == 0:
#             print("0 is not allowed")
#             continue
#         if is_even(number):
#             print(f"Number {number} is even.")
#         else:
#             print(f"Number {number} is odd.")
#         if number > 100:
#             print("stopping, number is too large")
#             break
#     except ValueError:
#         print("value not number, stopping")