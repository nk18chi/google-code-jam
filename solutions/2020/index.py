from typing import List, Set

# Note
# If you want to run the following code in google code jam, you need to remove type variable in all code.
# It is beacuse google code jam does not support "typing" library.
# ex.) testcases: int = int(input()) -> testcases = int(input())

# Also, you don't need to wrap by function statement when you submit your code in google code jam.
# This is not my actual code when I submitted. I refactored to make me and others understandable


# Vestigium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c


def vestigium():
    testcases: int = int(input())
    for i in range(testcases):
        s: str = input()
        prev: int = 0
        res: str = ""
        for c in s:
            if int(c) < prev:
                res += ")" * (prev - int(c))
            if int(c) > prev:
                res += "(" * (int(c) - prev)
            res += c
            prev = int(c)
        res += ")" * prev
        print("Case #{}: {}".format(i + 1, res))


# Nesting Depth
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
def nesting_depth():
    testcases: int = int(input())
    for i in range(testcases):
        square: int = int(input())
        matrix: List[List[int]] = [[0 for _ in range(square)] for _ in range(square)]
        for j in range(square):
            arrStr: List[str] = input().split(" ")
            for k, a in enumerate(arrStr):
                matrix[j][k] = int(a)

        trace: int = 0
        for j in range(len(matrix)):
            trace += matrix[j][j]

        row: int = 0
        for m in matrix:
            row += 0 if len(set(m)) == square else 1

        col: int = 0
        for j in range(square):
            unique: Set[int] = set()
            for k in range(square):
                unique.add(matrix[k][j])
            col += 0 if len(unique) == square else 1

        print("Case #{}: {} {} {}".format(i + 1, trace, row, col))


# Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

def parenting_partnering_returns():
    testcases: int = int(input())
    for i in range(testcases):
        count: int = int(input())
        activities: List[List[int]] = []
        res: List[str] = ["" for _ in range(count)]
        for j in range(count):
            activity: List[str] = input().split(" ")
            activities.append([int(activity[0]), int(activity[1]), j])
        activities.sort(key=lambda x: x[0])
        cameron: int = -1
        jamie: int = -1
        possible: bool = True
        for a in activities:
            if a[0] >= cameron:
                cameron = a[1]
                res[a[2]] = "C"
            elif a[0] >= jamie:
                jamie = a[1]
                res[a[2]] = "J"
            else:
                possible = False
                break
        if possible:
            print("Case #{}: {}".format(i + 1, "".join(res)))
        else:
            print("Case #{}: {}".format(i + 1, "IMPOSSIBLE"))
