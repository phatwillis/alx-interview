#!/usr/bin/python3
"""pascal's triangle interview challenge"""

def pascal_triangle(n):
    """will return the triangle list which can now be iterated
     to be printed however. the list will be a list of lists.
     each list (i) in the triangle list will be each row of the triangle
     and each number (j) will be each number present in the row as expected."""

    if n <= 0:
        return []
    else:
        triangle_list = []
        for i in range(n):  # i represents row, j, column
            """temp list is a temporary list that will be pushed
            to the triangle list. it will contain the numbers/columns
            of the triangle for a particular row."""
            temp_list = []
            for j in range(i + 1):
                """if j is the first position/column or it is equal to
                 i which is the current extreme, then append 1.
                 this is to have 1s by the sides"""
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    """num to be appended in a nested list will be an
                     addition of the previous list's j-1(which is
                     the number at its immediate top, by the left)
                     and the previous lists j (right hand side). e.g:
                          1
                        1 2 1
                       1 3 3 1
                    here, to get the first '3'
                    (which its i/row[j/column], will be = position 1)
                    you add 1 and 2 from the prev row,
                    (i - 1[j - 1] where j-1 is 0 and i-1[0] is 1, and i-1[j]
                    which is i-1[1] and that is 2). remember, i is always
                    current row so position i-1 is prev row"""
                    num = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
                    temp_list.append(num)
            triangle_list.append(temp_list)
        return triangle_list
