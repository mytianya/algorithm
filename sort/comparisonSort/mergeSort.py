"""
@version: 1.0
@author: zyw
@file: mergeSort.py
@time: 17-3-24 上午12:48
"""
"""merge Sort"""
#coding=utf-8
"""递归合并，时间复杂度O(nlogn)"""
num_in=input("please input a array,split with blank space\n");
sortArray=[int(n) for n in num_in.split()];
print("before sort",sortArray);
def divide(array):
    if len(array)<=1:
        return array;
    else:
        mid=int(len(array)/2);
        leftArray=divide(array[:mid]);
        rightArray=divide(array[mid:]);
        return merge(leftArray,rightArray);
def merge(left,right):
    array=[];
    i,j=0,0;
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            array.append(left[i]);
            i=i+1;
        else:
            array.append(right[j]);
            j=j+1;
    array+=left[i:];
    array+=right[j:];
    return array;
print("after sort:",divide(sortArray));

