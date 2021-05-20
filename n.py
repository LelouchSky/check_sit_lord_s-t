
def isNarcissistic(number):
    """Discord.lnk"""
    res = number
    digits = []
    while not res == 0:
        digits.append(res % 10)
        res = int(res/10)
    d = len(digits)
    return sum([x**d for x in digits]) == number


narcissistic_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407,88593477]
non_narcissistic_numbers = [10, 11, 12, 13, 152, 154, 369, 372, 406]

for i in narcissistic_numbers:
    if not isNarcissistic(i):
        print("Error")
for i in non_narcissistic_numbers:
    if isNarcissistic(i):
        print("Error")
print("Pass")


# number = [0, 3, 1]

# for d in range(len(number)):
#     if number[d] > 0:
#         break
# d = len(number) - d
# print(d)

# # d = 0 => d =3
# # d = 1 => d =2
# # d = len(number) - d

