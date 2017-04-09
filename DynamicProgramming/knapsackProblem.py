"""
动态规划求解0-1背包过程
bag[i,j]=max{bag[i-1][j],bag[i-1][j-w[i]]+v[i]}//前i个物品放到容量为j的背包中
@version: 1.0
@author: zyw
@file: knapsackProblem.py
@time: 17-4-9 下午8:34
"""
value_in=input("please input value array,split with blank space\n");
weight_in=input("please input weight array,split with blank space\n");
maxweight=input("please input max weight\n");
v=[int(n) for n in value_in.split(" ")];
w=[int(n) for n in weight_in.split(" ")];
bag=[[0 for n in range((int)(maxweight)+1)] for n in range(len(v)+1)];
for i in range(1,len(v)+1):
    for j in range(1,(int)(maxweight)+1):
        if j>=w[i-1]:
            print(i,",",j);
            bag[i][j]=max(bag[i-1][j],bag[i-1][j-w[i-1]]+v[i-1]);
        else:
            bag[i][j]=bag[i-1][j];
print(bag);


