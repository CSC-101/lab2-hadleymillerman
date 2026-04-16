# def smallest(n:float, m:float) -> float:
#     if n < m:
#         return n    # This statement is not evaluated for either call below
#     else:
#         return m
# first = smallest(3, 2)  # The value of first is 2
# second = smallest(2, 2) # The value of second is 2. This is reasonable because both numbers are equal so either one will be the smallest.
# print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, a call to this function evaluate this statement when a is the largest value
    elif b > c:
        return b + c             # In general, a call to this function evaluate this statement when b is the largest value
    else:
        return 2 * c             # In general, a call to this function evaluate this statement when c is the largest value

answer1 = function2(3, 2, 1)     # The value of answer1 is 1
answer2 = function2(2, 3, 1)     # The value of answer2 is 4
answer3 = function2(2, 1, 3)     # The value of answer3 is 6
print()