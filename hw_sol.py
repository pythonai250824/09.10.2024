import random
from webbrowser import Error

'''

# list_95_105: list[int] = []
# for i in range(95, 105 + 1):
#     list_95_105.append(i)

list_95_105: list[int] = [i for i in range(95, 105 + 1)]
print(list_95_105)

list_10_20_even: list[int] = [i for i in range(10, 20 + 2, 2)]
print(list_10_20_even)

list_5_bool: list[bool] = [random.choice([True, False]) for _ in range(5)]
print(list_5_bool)

list_100_rnd: list[int] = [random.randint(1, 100) for _ in range(10)]
print(list_100_rnd)

#list1 = [1, 2, 5, 100]

# for i in range(10):
#     number: int = list1[i]
#
# for number in list1:
#     number

list_100_rnd_bigger_50: list[int] = [number for number in list_100_rnd if number > 50]
print(list_100_rnd_bigger_50)

list_rnd_big50: list[int] = [number for number in [random.randint(1, 100) for _ in range(10)] if number > 50]
print(list_rnd_big50)

sentence: str = input('enter a sentence')
# Hello -> ['H', 'e', 'l', 'l', 'o']
#list_char: list[str] = [char for char in sentence if char != 't' and char != ' ']
list_char: list[str] = [char for char in sentence if char not in ['t', ' ']]
print(list_char)

list_10: list[int] = [random.randint(10, 99) for _ in range(10)]
print(list_10)
list_ahadot: list[int] = [num % 10 for num in list_10]
print(list_ahadot)

# 98 / 10 = 9.8
# 98 % 10 = 8
'''

#88 / 0
y: int = 1
try:
    x: int = 88
    print(x / 0)
except ZeroDivisionError as e:
    print(e)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

try:
    raise KeyError("test key error")
except KeyError as e:
   print(e)


list_4 = [5, 11, 99, -12]

SENTINEL: int = -999
while True:
    try:
        index: int = int(input('enter an index- '))
        if index == SENTINEL:
            break
        print(list_4[index])
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

