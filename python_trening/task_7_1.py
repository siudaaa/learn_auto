def func1(s: str = '') -> int:
    return len(s)

def func2(a: list, b: list) -> int:
    return max(len(a), len(b))


def func_list(a: list):
    a.append('test')
    return a

print (func_list(['один', 2, 3]))

def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print (sum_list([1, 2, 3]))
