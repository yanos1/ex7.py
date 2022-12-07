
from ex7_helper import *
from typing import Optional, Any


def mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    else:
        x = add(x, mult(x, subtract_1(y)))

    return x




def is_even(n: int) -> bool:
    if n == 0:
        return True
    if n == 1:
        return False
    else:
        x = is_even(subtract_1(subtract_1(n)))
    return x


def log_mult(x:float, y:int):

    if y == 0:
        return 0
    if y == 1:
        return x

    else:
        x = log_mult(add(x, x), divide_by_2(y)) if not is_odd(y) else add(log_mult(add(x, x),divide_by_2(y)), x)
    return x


def is_power(b: int, x: int) -> bool:
    constant = b

    def is_power_help(b, x, value=True):

        if b > x:
            value = False
            return value
        if b == x:
            value = True
            return value
        else:
            value = is_power_help(log_mult(b,constant), x, False)

        return value
    res = is_power_help(b, x)
    return res

def reverse(s):
    def reverse_h(s, index):
        if index + 1 == len(s):
            return s[index]
        new_s = reverse_h(s, index+1)
        new_s = append_to_end(new_s, s[index])
        return new_s
    return reverse_h(s, 0)




def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> Any:
    if n < 1:
        return
    # if n ==1:
    #     Hanoi.move(src,dst)
    else:
        play_hanoi(Hanoi, n-1, src,dst,temp)
        for i in range(n-1):
            Hanoi.move(src,temp)
        Hanoi.move(src,dst)
        for i in range(n-1):
            Hanoi.move(temp,dst)






















def number_of_ones(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        x = number_of_ones_helper(n)
        return x + number_of_ones(n-1)


def number_of_ones_helper(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        if n % 10 == 1 and n > 10:
            return 1 + number_of_ones_helper(n//10)
        else:
            return number_of_ones_helper(n//10)


def compare_1d_lists(l1, l2, index):
    if len(l1) != len(l2):
        return False
    if index == len(l1):
        return True
    b = compare_1d_lists(l1,l2, index +1)
    if b and l1[index] == l2[index]:
        return True
    return False

def d_helper(l1,l2,index):
    if len(l1) != len(l2):
        return False
    if index == len(l1):
        return True
    b = d_helper(l1,l2, index +1)
    if b and compare_1d_lists(l1,l2,0):
        return True
    return False

def compare_2d_lists(l1,l2):
    x = d_helper(l1,l2, 0)
    return x


def create_deep_copy(lis):
    lis = lis[:]
    print(id(lis))
    return lis


def magic_list(n: int):
    if n == 0:
        return []
    else:
        yp = magic_list(n-1)
        copy = create_deep_copy(yp)
        copy.append(yp)
    return copy

print(magic_list(3))

#
#
#
# def fib(n, dic= {}):
#     if n in dic:
#         return dic[n]
#     if n <= 2:
#         return 1
#     dic[n] = fib(n - 1, dic) + fib(n - 2, dic)
#     return dic[n]
# print(fib(5))
#
#
# def num_of_paths(n, m, dict = {}):
#     key = str(n)+ "," +str(m)
#     if key in dict:
#         return dict[key]
#     if n == 1 and m == 1:
#         return 1
#     if n == 0 or m == 0:
#         return 0
#     dict[key] = num_of_paths(n-1,m,dict) + num_of_paths(n, m-1, dict)
#     return dict[key]
#
# print(num_of_paths(18,18))
#
# def canSum(n, lis,numbers = [], dict = {}, all_paths =[]):
#     if n in dict:
#         return dict[n]
#     if n == 0:
#         return all_paths
#     if n < 0:
#         return None
#     for num in lis:
#         sum = n - num
#         dict[n] = canSum(sum,lis,numbers,dict,all_paths)
#         if dict[n] != None:
#             numbers.append(num)
#         all_paths.append(numbers)
#         return all_paths
#
#     return None
#
# print(canSum(10, [2,3,5]))
#
#
# def short_sum(target_sum, lis, paths = [], numbers = []):
#     if target_sum == 0:
#         return numbers
#
#     if target_sum < 0:
#         return None
#     for num in lis:
#         sum = target_sum - num
#         result = short_sum(sum,lis,paths,numbers)
#         if result != None:
#             paths.append(numbers)
#             return numbers + [num]
#     return paths
#
# print(short_sum(7,[1,2,3]))
#
# def all_construct(target, word_bank):
#     if target == "":
#         return []
#     maybe = []
#     for word in word_bank:
#         if word in target[0:len(word)]:
#             cut_word = target[len(word):]
#             maybe.append(cut_word)
#             one_way_to_cnstrct = all_construct(cut_word, word_bank)
#         if reversed(word) in reversed(target)[0:len(word)]:
#             cut_word = target[len(word)]
#
#
#
#
