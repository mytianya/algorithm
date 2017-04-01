"""
动态规划求解最长递增子序列
@version: 1.0
@author: zyw
@file: LongestIncreasingSubSequence.py
@time: 17-4-1 下午9:20
"""
num_in=input("please input a array split by blank\n");
sequence=[int(n)  for n in num_in.split(" ")];
def dpLIS(sequence):
    length=len(sequence);
    l=[1 for n in range(length)];
    i,j=0,0;
    maxlength=1;
    for i in range(length):
        for j in range(i):
            if sequence[j]<=sequence[i] and l[i]<l[j]+1:
                l[i]=l[j]+1;
                if(l[i]>maxlength):
                    maxlength=l[i];
    return maxlength;
print("longest inscreasing subsequence's length:",dpLIS(sequence));
