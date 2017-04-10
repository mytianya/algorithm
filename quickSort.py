"""
快速排序,分治法,平均时间复杂度为O(nlogn),最坏为有序或无序O(n^2)
@version: 1.0
@author: zyw
@file: quickSort.py
@time: 17-4-10 下午5:19
"""
num_in=input("please input a array,split with blank space\n");
sortArray=[int(n) for n in num_in.split(" ")];
def quickSort(array,q,p):
    if q>=p:
        return;
    else:
        r=swap(array,q,p);
        quickSort(array,q,r-1);
        quickSort(array,r+1,p);
def swap(array,q,p):
    i=q;
    j=q+1;
    pivot=array[q];
    while j<=p:
        if array[j]<pivot:
            temp=array[i+1];
            array[i+1]=array[j];
            array[j]=temp;
            i=i+1;
        j=j+1;
    array[q]=array[i];
    array[i]=pivot;
    print(i);
    return i;
quickSort(sortArray,0,len(sortArray)-1);
print("排序后结果:",sortArray);
