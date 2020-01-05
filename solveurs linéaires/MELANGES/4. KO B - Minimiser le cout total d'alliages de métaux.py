"""
 Mining and metals

We make steel with raw materials, we want to reduce the cost of producing this steel
to make more money, but still respecting the minimum characteristics of quality steel

"""

# Minimize the cost of metal alloys.
# Characteristics of the steel to be made

"""Element      %Minimum  %Max   %Real (it is a var)
   Carbon       2         3      2.26
   Copper       0.4       0.6    0.60
   Manganese    1.2       1.65   1.20

"""

# Characteristics, stocks and purchase price of alloys
"""
Alloy          C%   Cu%   Mn%     Stocks kg Price € / kg
Iron alloy     2.50 0.00  1.30    4000      1.20
Iron alloy     3.00 0.00  0.80    3000      1.50
Iron alloy     0.00 0.30  0.00    6000      0.90
Copper alloy   0.00 90.00 0.00    5000      1.30
Copper alloy   0.00 96.00 4.00    2000      1.45
Aluminum alloy 0.00 0.40  1.20    3000      1.20
Aluminum alloy 0.00 0.60  0.00    2500      1.00
"""

# Import the PuLP lib
from pulp import *

# Create the problem variable
prob = LpProblem ("MinimiserLpAlliage", LpMinimize)

# Problem Data
input_mats = ["iron_1", "iron_2", "iron_3",
              "cu_1", "cu_2",
              "al_1", "al_2"]

input_costs = {"iron_1": 1.20, "iron_2": 1.50, "iron_3": 0.90,
               "cu_1":   1.30, "cu_2": 1.45,
               "al_1":   1.20, "al_2":   1.00}

#                               C%   Cu%   Mn%
input_composition = {"iron_1": [2.5, 0.0,  1.3],
                     "iron_2": [3.0, 0.0,  0.8],
                     "iron_3": [0.0, 0.3,  0.0],
                     "cu_1":   [0.0, 90.0, 0.0],
                     "cu_2":   [0.0, 96.0, 4.0],
                     "al_1":   [0.0, 0.4,  1.2],
                     "al_2":   [0.0, 0.6,  0.0]}

input_stock = {"iron_1": 4000, "iron_2": 3000, "iron_3": 6000,
               "cu_1": 5000, "cu_2":  2000,
               "al_1": 3000, "al_2": 2500}

request_quantity = 5000

# Problem variables - amount in kg of each input
x = LpVariable.dicts("input_mat", input_mats, 0)

# The objective function is to minimize the total cost of the alloys in EUROS for a given quantity in KGS
prob += lpSum([input_costs[i]*x[i] for i in input_mats]), "AlliageCost"

# Quantity constraint in KGS.
prob += lpSum([x[i] for i in input_mats]) == request_quantity, "RequestedQuantity"

# MIN/MAX constraint of carbon in resultant steel
prob += lpSum([x[i]*input_composition[i][0] for i in input_mats]) >= (2.0/100.0)*request_quantity, "MinCarbon"
prob += lpSum([x[i]*input_composition[i][0] for i in input_mats]) <= (3.0/100.0)*request_quantity, "MaxCarbon"

# MIN/MAX constraints of copper in resultant steel
prob += lpSum([x[i]*input_composition[i][1] for i in input_mats]) >= (0.4/100.0)*request_quantity, "MinCu"
prob += lpSum([x[i]*input_composition[i][1] for i in input_mats]) <= (0.6/100.0)*request_quantity, "MaxCu"

# MIN/MAX constraints of manganese in resultant steel
prob += lpSum([x[i]*input_composition[i][2] for i in input_mats]) >= (1.2/100.0)*request_quantity, "MinMn"
prob += lpSum([x[i]*input_composition[i][2] for i in input_mats]) <= (1.65/100.0)*request_quantity, "MaxMn"


# MAX constraints of available stock
for i in input_mats:
    x[i] <= input_stock[i], ("MaxStock_" + i)


# The problem data is written to an .lp file
prob.writeLP ( "SteelModel.lp")

# We use the solver
prob.solve()

# The status of the solution
print ("Status:", LpStatus [prob.status])

# Dislay the optimums of each var
for v in prob.variables ():
    print (v.name, "=", v.varValue)

# Display mat'l compositions
Carbon_value = 100*(sum([x[i].varValue*input_composition[i][0] for i in input_mats])/request_quantity)
Cu_value = 100*(sum([x[i].varValue*input_composition[i][1] for i in input_mats])/request_quantity)
Mn_value = 100*(sum([x[i].varValue*input_composition[i][2] for i in input_mats])/request_quantity)

print ("Carbon content: " + str(Carbon_value))
print ("Copper content: " + str(Cu_value))
print ("Manganese content: " + str(Mn_value))

# The result of the objective function is here
print ("Total", value (prob.objective))