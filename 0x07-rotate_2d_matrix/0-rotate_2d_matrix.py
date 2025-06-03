#!/usr/bin/python3
"""rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """function to do the job"""
    # temp array that will transfer its
    # content to the original matrix
    temp_list = []
    # temp array that will push to temp_list
    temp_temp_list = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            temp_temp_list.insert(0, matrix[j][i])
        temp_list.append(temp_temp_list)
        temp_temp_list = []

    # when temp list operation is complete,
    # temp_list will be the matrix in 90 degrees
    # so remove everything in the matrix and append temp list content
    del matrix[:]
    for i in temp_list:
        matrix.append(i)
