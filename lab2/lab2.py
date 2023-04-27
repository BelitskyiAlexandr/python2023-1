def task_1(lst):
    return [2 * x for x in lst]

def task_2(lst):
    return [x for x in lst if x**2 <= 30]

def task_3(lst):
    return [x for i, x in enumerate(lst) if x not in lst[:i]]

def task_4():
    return {str(i): i**2 for i in range(20, 31) if i % 3 == 0 and i % 5 != 0}

from collections.abc import Hashable

def task_5(lst):
    new_set = set()

    for elem in lst:
        if isinstance(elem, Hashable):
            new_set.add(elem)
    
    return new_set

task1_lst = [1,2,3,4,5]
print(task_1(task1_lst))

task2_lst = [1,2,3,4,5,6,7]
print(task_2(task2_lst))

task3_lst = [1,2,2,2,3,3,3,4,4,5,5,5]
print(task_3(task3_lst))

print(task_4())

task5_lst = [3, 'ok', [1, 2], (True, False), {'flag': 1}]
print(task_5(task5_lst))