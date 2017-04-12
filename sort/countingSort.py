"""
计数排序:当输入的元素是n个0到k之间的整数时，它的运行时间是Θ(n + k)
@version: 1.0
@author: zyw
@file: countingSort.py
@time: 17-4-12 下午11:25
"""
num_in=input("please input a array,split with blank space\n");
sortArray=[int(n) for n in num_in.split()];
#find max elem
def findMax(array):
    max=array[0];
    for n in range(len(array)):
        if max<array[n]:
            max=array[n];
    return max;
def countingSort(array):
    max=findMax(array);
    countArray=[0 for n in range(max+1)];#计数数组
    sortArray=[0 for n in range(len(array))];#排序结果
    for n in range(len(array)):
        countArray[array[n]]+=1;
    print("countArray:",countArray);
    for n in range(max+1):
        if n==0:
            pass
        else:
            countArray[n]=countArray[n]+countArray[n-1];
    print("overlying countArray",countArray);
    for n in reversed(range(len(array))):
        sortArray[countArray[array[n]]-1]=array[n];
        countArray[array[n]]-=1;
    return sortArray;
print("after countingSort:",countingSort(sortArray));