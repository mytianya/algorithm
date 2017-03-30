"""
最大非空子数组问题：分治法
@version: 1.0
@author: zyw
@file: MaxinumSubArray.py
@time: 17-3-29 下午2:50
"""
num_in=input("please input a array,split with blank space\n");
testArray=[int(n) for n in num_in.split()];
def maxSubArray(array,low,high):
    if low==high:
        temp=[];
        temp.append(array[low])
        return temp;
    mid=int((low+high)/2);
    leftArray=maxSubArray(array,low,mid);
    rightArray=maxSubArray(array,mid+1,high);
    midArray=maxMidSubArray(array,low,mid,high);
    if(compute(leftArray)>compute(rightArray) and compute(leftArray)>compute(midArray)):
        return leftArray;
    elif(compute(rightArray)>compute(leftArray) and compute(rightArray)>compute(midArray)):
        return rightArray;
    else:
        return midArray;
def maxMidSubArray(array,low,mid,high):
    print(low,mid,high);
    l_flag=array[mid];
    sum=0;
    maxleft=mid;
    maxright=mid;
    for i in reversed(range(low,mid+1)):
        print("i:", i);
        sum+=array[i];
        if(sum>=l_flag):
            l_flag=sum;
            maxleft=i;
    r_flag=array[mid];
    sum=0;
    for j in range(mid,high+1):
        sum+=array[j];
        if(sum>=r_flag):
            r_flag=sum;
            maxright=j;
    if maxleft==maxright:
        temp=[];
        temp.append(array[maxleft]);
        return temp;
    return array[maxleft:maxright+1];
def compute(array):
    sum=0;
    for k in range(len(array)):
        sum+=array[k];
    return sum;
print(maxSubArray(testArray,0,len(testArray)-1));

