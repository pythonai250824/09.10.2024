

#################################### all AND
result1: list[bool] = [True, False, False, True]
print(result1, 'all()', all(result1)) # is everything in this list is True /
# if result[0] and result[1] ... result[4]

result2 = [True, True, True, True]
print(result2, 'all()', all(result2)) # is everything in this list is True ?

# >>> all([1, 1, 0])
# False
# >>> all([1, 1, 2 > 1])
# True
# >>>

#################################### any OR
result3: list[bool] = [True, False, False, True]
print(result3, 'any()', any(result3)) # is anything in this list is True ?
# if result[0] or result[1] ... result[4]

result4: list[bool] = [False, False, False, False]
print(result4, 'any()', any(result4)) # is anything in this list is True ?

#          F  F  F  F
# >>> any([0, 0, 0, 0])
# False
#          F  F  F  T
# >>> any([0, 0, 0, 1])
# True

# targil -- use any/all
# check if a list [True, False, False, True] contains at least 1 False
#   if yes -- print 'At least 1 False' else print '0 False'
if not all([True, False, False, True]):  # is all true? == False
    print('At least 1 False')
else:
    print('0 False')

# check if a list [False, False, False, False] contains all False
#   if yes -- print 'All False' else print 'not All False'
if not any([False, False, False, False]):  # is any true? == False
    print('All False')
else:
    print('not All False')

# *Bonus: check if a list [3, 9, 12, 15, 16] contains only numbers divided by 3 no reminder
#   if yes -- print 'All 3 divided' else print 'not All3 divided'
list3: list[int] = [3, 9, 12, 15, 16]
list_div3: list[bool] = []
for number in list3:
    if number % 3 == 0:
        list_div3.append(True)
    else:
        list_div3.append(False)
print(list3)
print(list_div3)
if all(list_div3):
    print('all divided by 3')


#list3: list[int] = [3, 9, 12, 15, 16]
#list_div3: list[bool] = [number % 3 == 0 for number in list3]  # [True, True, True, True, False]
#if all(list_div3):
    pass

if all([number % 3 == 0 for number in [3, 9, 12, 15, 16]]):
    print('all divided by 3')
else:
    print('not divided by 3')

if any([number % 3 == 0 for number in [3, 9, 12, 15, 16]]):
    print('at least 1 divided by 3')
else:
    print('none divided by 3')

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
print('all bool1', bool1, all(bool1))  # True
print('all bool2', bool2, all(bool2))  # False
print('all bool3', bool3, all(bool3))  # False

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
bool4: list[bool] = [False, False]
bool5: list[int] = [0, 0, 0, 0, 0]
print('any bool1', bool1, any(bool1))  # True
print('any bool2', bool2, any(bool2))  # True
print('any bool3', bool3, any(bool3))  # True
print('any bool4', bool4, any(bool4))  # False
print('any bool5', bool5, any(bool5))  # False

nums: list[int] = [100, 200, 1, 2, 3, -2, 400, 999, 1001]
if all([num > 0 for num in nums]):
    print(nums, 'all positive')
else:
    print(nums, 'not all positive')

word = 'aaaaaaaaaaaaaaba'
if all([char=='a' for char in word]):
#if not any([char != 'a' for char in word]):
    print(word, 'all a')
else:
    print(word, 'not all a')

#                    1   2   3  4  5    6    7     8   9
nums: list[int] = [100, 200, 1, 2, 3, 400, 999, 1001, -2]
#if ([num for num in nums if num > 0] == nums):  # [100, 200, 1, 2, 3, 400, 999, 1001] 8 len
if len([num for num in nums if num > 0]) == len(nums):   # [100, 200, 1, 2, 3, 400, 999, 1001]
    print(nums, 'all positive')
else:
    print(nums, 'not all positive')








