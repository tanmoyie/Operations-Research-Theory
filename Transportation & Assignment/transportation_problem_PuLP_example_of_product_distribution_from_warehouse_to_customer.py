# -*- coding: utf-8 -*-
"""
The Product Distribution Problem for the PuLP Modeller

Original Authors: Antony Phillips, Dr Stuart Mitchell  2007
Adopted by: Tanmoy Das, 2018
Source code: https://github.com/openstack/deb-python-pulp/edit/master/examples/BeerDistributionProblem_resolve.py
https://www.coin-or.org/PuLP/CaseStudies/a_transportation_problem.html
https://github.com/tanmoyie/Operations-Research/tree/master/Transportation

"""

# Import PuLP modeler functions
from pulp import *

# Creates a list of all the supply nodes
Warehouses = ["A", "B"]

# Creates a dictionary for the number of units of supply for each supply node
supply = {"A": 2050,
          "B": 8010}

# Creates a list of all demand nodes
CustomerPoint = ["1", "2", "3", "4", "5"]

# Creates a dictionary for the number of units of demand for each demand node
demand = {"1":1000,
          "2":1800,
          "3":4000,
          "4":500,
          "5":1350,}

# Creates a list of costs of each transportation path
costs = [   #CustomerPoint 1 2 3 4 5
         [2,4,5,2,1],#A   Warehouses
         [3,1,3,2,3] #B
         ]

# The cost data is made into a dictionary
costs = makeDict([Warehouses,CustomerPoint],costs,0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Product Distribution Problem",LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(w,b) for w in Warehouses for b in CustomerPoint]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route",(Warehouses,CustomerPoint),0,None,LpInteger)


prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

# The supply maximum constraints are added to prob for each supply node (warehouse)
for w in Warehouses:
    prob += lpSum([vars[w][b] for b in CustomerPoint])<=supply[w], "Sum_of_Products_out_of_Warehouse_%s"%w

# The demand minimum constraints are added to prob for each demand node (customer)
# These constraints are stored for resolve later
customer_demand_constraint = {}
for b in CustomerPoint:
    constraint = lpSum([vars[w][b] for w in Warehouses])>=demand[b]
    prob += constraint, "Sum_of_Products_into_customer_%s"%b
    customer_demand_constraint[b] = constraint

# The problem data is written to an .lp file
prob.writeLP("ProductDistributionProblem.lp")

for demand in range(500, 601, 10):
    # reoptimise the problem by increasing demand at customer '1'
    # note the constant is stored as the LHS constant not the RHS of the constraint
    customer_demand_constraint['1'].constant = - demand

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print("Status:", LpStatus[prob.status])

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # The optimised objective function value is printed to the screen
    print("Total Cost of Transportation = ", value(prob.objective),"\n")
