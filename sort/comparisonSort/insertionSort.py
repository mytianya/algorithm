"""
@version: 1.0
@author: zyw
@file: insertionSort.py
@time: 17-3-24 上午12:26
"""
''''insertion sort ,worst time O(n^{2}),best time O(n)'''
num_in=input("please input a array,split with blank space\n");
sortArray=[int(n) for n in num_in.split()];
print("before sort",sortArray);
def insertionSort(array):
    if len(array)<=1:
        return array;
    else:
        for j in range(1,len(array)):
            i=j-1;
            key=array[j];
            while i>=0 and array[i]>key:
                array[i+1]=array[i];
                i=i-1;
            array[i+1]=key;
        return array;
print("after insertionSort:",insertionSort(sortArray));
