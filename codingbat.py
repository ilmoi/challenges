import itertools

# ==============================================================================
# https://codingbat.com/prob/p118406

# ALL OF THE BELOW WORK HERE AND DON'T FUCKING WORK ON THE BAT FOR VARIOUS REASONS. FUCKING STUPID.


# def make_bricks(small, big, goal):
#     # using itertools, which codingbat doesn't allow
#     L = []
#     L.extend([1 for i in range(small)])
#     L.extend([5 for i in range(big)])
#     # print(L)
#     for i in range(1, len(L)+1):
#         combos = itertools.combinations(L, i)
#         for combo in combos:
#             if sum(list(combo)) == goal:
#                 return True
#     return False
#
#
# print(
#     make_bricks(3, 2, 10)
# )


# def n_length_combo(lst, n):
# from geeks for geeks - "timeout" whatever the fuck that means on bat
#     if n == 0:
#         return [[]]
#
#     l = []
#
#     for i in range(0, len(lst)):
#
#         # fix the ith element
#         m = lst[i]
#         # take everything to the right of that element
#         remLst = lst[i+1:]
#
#         for p in n_length_combo(remLst, n-1):
#             l.append([m]+p)
#
#     return l


# def n_length_combo(iterable, r):
#     # another geeks for geeks - bat doesn't accept yield
#
#     char = tuple(iterable)
#     n = len(char)
#
#     if r > n:
#         return
#
#     index = list(range(4))
#
#     # retruns the first sequence
#     yield tuple(char[i] for i in index)
#
#     while True:
#
#         for i in reversed(range(r)):
#             if index[i] != i + n - r:
#                 break
#         else:
#             return
#
#         index[i] += 1
#
#         for j in range(i + 1, r):
#
#             index[j] = index[j-1] + 1
#
#         yield tuple(char[i] for i in index)


# def combinations(iterable, r):
#     # this is the source code for the itertools thing - bat doesn't accept yield
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable) #(ABCD)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r)) #0 1 2
#     yield tuple(pool[i] for i in indices) #A B C -->
#     while True:
#         for i in reversed(range(r)): # 2 1 0
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)


# def make_bricks(small, big, goal):
#
#     L = []
#     L.extend([1 for i in range(small)])
#     L.extend([5 for i in range(big)])
#     # print(L)
#
#     for i in range(1, len(L)+1):
#         combos = n_length_combo(L, i)
#         for combo in combos:
#             if sum(list(combo)) == goal:
#                 return True
#     return False


# def make_bricks(small, big, goal):
#     # this works but is still brute force and crashes when ran on the below large numbers
#     L = []
#     L.extend([1 for i in range(small)])
#     L.extend([5 for i in range(big)])
#
#     try:
#         while goal != 0:
#             # prepare p
#             p = L.pop()
#             print(f'preparing p, which is {p}')
#
#             # if goal is above p
#             if goal >= p:  # 9 > 5
#                 # subtract p
#                 goal -= p
#                 print(f'subtracting {p}, goal is now {goal}')
#     except IndexError:
#         return False
#     return True


ddef make_bricks(small, big, goal):
    # I FUCKING DID IT. NO LOOPS. CONSTANT TIME.

    how_many_fives_fit = goal // 5

    if big <= how_many_fives_fit:
        goal -= big*5
    else:
        goal -= how_many_fives_fit*5

    if goal <= small:
        return True
    else:
        return False


print(
    make_bricks(2, 1000000, 100003)
)
