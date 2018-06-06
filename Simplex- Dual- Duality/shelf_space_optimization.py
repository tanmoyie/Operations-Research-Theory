
# coding: utf-8

# In[2]:


#import all relevant libraries

import pandas as pd

import numpy as np

import math

from math import isnan

from pulp import *

from collections import Counter

#from more_itertools import unique_everseen

 

sales=pd.read_csv("sales_lift.csv",header=None) #input file

lift=sales.iloc[2:,1:]

lift=np.array(lift)

lift = lift.astype(np.int) # read the lifts from csv

brands=sales.iloc[0:1,:]

brands=np.array(brands)

brands=np.delete(brands,0)

brands=brands.tolist()  # read the brands from csv

ff=Counter(brands)

all_brands=ff.items()

# the racks and the shelfs available

rack_shelf=[[1,1,2,3],[2,4,5,6],[3,7,8,9,10]]

 

#define the optimization function

prob=LpProblem("SO",LpMaximize)

 

#define decision variables

dec_var=LpVariable.matrix("dec_var",(range(len(lift)),range(len(lift[0]))),0,1,LpBinary)

 

#Compute the sum product of decision variables and lifts

prodt_matrix=[dec_var[i][j]*lift[i][j] for i in range(len(lift))

for j in range(len(lift[0]))]

 

#total lift which has to be maximized sum(prodt_matrix)

 

#define the objective function

prob+=lpSum(prodt_matrix)

 

order=list(unique_everseen(brands))

order_map = {}

for pos, item in enumerate(order):

    order_map[item] = pos

#brands in order as in input file

brands_lift=sorted(all_brands, key=lambda x: order_map[x[0]])

 

#DEFINE CONSTRAINTS

#1) Each shelf can have only one product i.e. sum (each row)<=1

for i in range(len(lift)):

    prob+=lpSum(dec_var[i])<=1

 

# 2) Each product can be displayed only on a limited number of shelves i.e. Column constraints

#Constraints are given as

col_con=[1,0,0,2,2,3,1,1]

dec_var=np.array(dec_var)

col_data=[]

for j in range(len(brands)):

    col_data.append(list(zip(*dec_var)[j]))

    prob+=lpSum(col_data[j])<=col_con[j]

#write the problem

prob.writeLP("SO.lp")

#solve the problem

prob.solve()

print("The maximum Total lift obtained is:",value(prob.objective)) # print the output

#print the decision variable output matrix

Matrix=[[0 for X in range(len(lift[0]))] for y in range(len(lift))]

for v in prob.variables():

    Matrix[int(v.name.split("_")[2])][int(v.name.split("_")[3])]=v.varValue

    matrix=np.int_(Matrix)

print ("The decision variable matrix is:")

print(matrix)

