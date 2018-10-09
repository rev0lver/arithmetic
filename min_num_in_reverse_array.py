# -*- coding:utf-8 -*-

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

array = [6,7,8,9,12,15,17,1,2,3,4,5]

def solution(array):
    first  = array[0]

    while len(array) > 1 and array[0] > array[-1]:
        mid = len(array) // 2
        if array[mid] > first :
            array = array[mid+1:]
        elif array[mid] < first and len(array) > 2:
            array = array[:mid+1]
        else:
            array = [array[mid]]
    return array[0]

result = solution(array)

print result


