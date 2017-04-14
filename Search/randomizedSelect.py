"""
随机查找算法：时间复杂度最好O(n),最坏O(n^2).
可以通过辅助函数,递归选择pivot,保证worst情况也是linear time,这里并没有实现.
之前quickSort选择pivot都是选择第一位,这里采用随机选择.
description:在一个没有重复元素的序列中,找到第K大的数.
@version: 1.0
@author: zyw
@file: randomizedSelect.py
@time: 17-4-14 下午4:01
"""
import random
num_in=input("please input a array,split with blank space\n");
num=input("please input k\n");
array=[int(n) for n in num_in.split()];
def randomizedSelect(array,k):
    position=randomPartition(array);
    if k==position:
        return array[k];
    elif k<position:
        return randomizedSelect(array[:position],k);
    else:
        return randomizedSelect(array[position+1:],k-position-1);
def randomPartition(array):
    if len(array)==1:
        return 0;
    #随机选择一个elem作为pivot,与数组第一个elem互换,后面分区与quickSort思路一样
    r=random.randint(0,len(array)-1);
    temp=array[0];array[0]=array[r];array[r]=temp;
    i=0;
    j=1;
    pivot = array[0];
    while j <= len(array)-1:
        if array[j] < pivot:
            temp = array[i + 1];
            array[i + 1] = array[j];
            array[j] = temp;
            i = i + 1;
        j = j + 1;
    array[0] = array[i];
    array[i] = pivot;
    return i;
if int(num)>len(array):
    print("输入第k小数字错误");
else:
    print(array,"第",num,"小的数为:",randomizedSelect(array,int(num)-1));