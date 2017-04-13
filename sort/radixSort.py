"""
基数排序:以计数排序为基础,时间复杂度为O(n)
@version: 1.0
@author: zyw
@file: radixSort.py
@time: 17-4-13 上午11:11
"""
num_in=input("please input a array,split with blank space\n");
sortArray=[int(n) for n in num_in.split()];
def getDistance(array):
    max=array[0];
    for elem in array:
        if elem>max:
            max=elem;
    distance=1;
    while max>=10:
        max/=10;
        distance+=1;
    return distance;
def radixSort(array):
    distance=getDistance(array);
    temp=[[0 for n in range(10)] for n in range(10)];
    count=[0 for n in range(10)];
    n=1;
    t=1;
    while n<=distance:
        for elem in array:
            digit=(elem//t)%10;
            temp[digit][count[digit]]=elem;
            count[digit]+=1;
        k=0;
        #重新排列输入数组
        for i,c in enumerate(count):
            index=0;
            while index<c:
                array[k]=temp[i][index];
                k+=1;
                index+=1;
            count[i]=0;
        n=n+1;
        t=t*10;
    return array;
print("after radixSort:",radixSort(sortArray));



