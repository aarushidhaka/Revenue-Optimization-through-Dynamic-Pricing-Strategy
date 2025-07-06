"""
Created on Thu Mar  6 12:47:37 2025

@author: aritro
"""
import numpy as np
import pandas as pd
from pyomo.environ import *

# Load the dataset
file_name = 'BuildMax_Data.xlsx' 

# Load data from each sheet, skipping the first 3 rows
df_excavators = pd.read_excel(file_name, sheet_name='Excavators', skiprows=3, index_col=0)
df_cranes = pd.read_excel(file_name, sheet_name='Cranes', skiprows=3, index_col=0)
df_bulldozers = pd.read_excel(file_name, sheet_name='Bulldozers', skiprows=3, index_col=0)

# Function to extract demand and price for each equipment type
def extract_data(df):
    demand = df.iloc[:, :4].to_numpy()  # First 4 columns: demand
    price = df.iloc[:, 4:8].to_numpy()  # Next 4 columns: price
    return demand, price

# Extract demand and price for each equipment type
demand_excavators, price_excavators = extract_data(df_excavators)
demand_cranes, price_cranes = extract_data(df_cranes)
demand_bulldozers, price_bulldozers = extract_data(df_bulldozers)

# Combine data into dictionaries for easier access
demand = {
    "Excavators": demand_excavators,
    "Cranes": demand_cranes,
    "Bulldozers": demand_bulldozers
}

price = {
    "Excavators": price_excavators,
    "Cranes": price_cranes,
    "Bulldozers": price_bulldozers
}

# Define model parameters
equipment_types = ["Excavators", "Cranes", "Bulldozers"]
durations = [1, 4, 8, 16]  # Rental durations in weeks
num_weeks = len(demand["Excavators"])  # Number of weeks in dataset

# Initial inventory levels
initial_inventory = {
    "Excavators": 760,
    "Cranes": 830,
    "Bulldozers": 900
}

# Create Pyomo model
model = ConcreteModel()

# Define decision variable X[i, j, o]: Rentals for equipment i, in week j, for duration o
model.X = Var(range(len(equipment_types)), range(num_weeks), range(len(durations)), domain=NonNegativeIntegers)

# Define inventory variable Inv[i, j]: Inventory at week j for equipment i
model.Inv = Var(range(len(equipment_types)), range(num_weeks), domain=NonNegativeIntegers)


# Objective Function: Maximize Revenue
def revenue_rule(model):
    return sum(
        durations[o] * 7 * price[equipment_types[i]][j, o] * model.X[i, j, o]  
        for i in range(len(equipment_types))
        for j in range(num_weeks)
        for o in range(len(durations))
    )

model.obj = Objective(rule=revenue_rule, sense=maximize)

# Inventory Balance Constraint (Returns = Rentals from previous weeks)
def inventory_rule(model, i, j):
    if j == 0:
        return model.Inv[i, j] == initial_inventory[equipment_types[i]]  # Week 0: Start with initial inventory
    else:
        returns_total = sum(model.X[i, j-durations[o], o] for o in range(len(durations)) if j - durations[o] >= 0)
        return model.Inv[i, j] == model.Inv[i, j-1] - sum(model.X[i, j-1, o] for o in range(len(durations))) + returns_total

model.inventory_constraint = Constraint(range(len(equipment_types)), range(num_weeks), rule=inventory_rule)

# Demand Constraint
def demand_rule(model, i, j, o):
    return model.X[i, j, o] <= demand[equipment_types[i]][j, o]

model.demand_constraint = Constraint(range(len(equipment_types)), range(num_weeks), range(len(durations)), rule=demand_rule)

# Capacity Constraint
def capacity_rule(model, i, j):
    return sum(model.X[i, j, o] for o in range(len(durations))) <= model.Inv[i, j]

model.capacity_constraint = Constraint(range(len(equipment_types)), range(num_weeks), rule=capacity_rule)

# Solve the model
solver = SolverFactory('glpk')
results = solver.solve(model)

# Dictionary to store revenue by equipment type
revenue_by_equipment = {equipment: 0 for equipment in equipment_types}

# Compute revenue for each equipment type
for i in range(len(equipment_types)):
    for j in range(num_weeks):
        for o in range(len(durations)):
            revenue = durations[o] * 7 * price[equipment_types[i]][j, o] * value(model.X[i, j, o])
            revenue_by_equipment[equipment_types[i]] += revenue

# Check if solution is optimal
if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
    total_revenue = f"£{model.obj():,.2f}"
    print(f'Total revenue: {total_revenue}')
else:
    print('No optimal solution found.')
    
    
    
# Print revenue per equipment type
for equipment, revenue in revenue_by_equipment.items():
    print(f"Revenue from {equipment}: £{revenue:,.2f}")
    
    
# ------------------------------------------------------
# Check for Inventoy Violations
# ------------------------------------------------------    
    
# Additional inventory tracking and rental summary
weeks = range(num_weeks)
rental_data = []

equipment_names = equipment_types

for j in range(len(equipment_types)):
    for t in weeks:
        total_rentals = sum(value(model.X[j, t, i]) for i in range(len(durations)))
        available_inventory = initial_inventory[equipment_types[j]] if t == 0 else value(model.Inv[j, t])
        exceeds_inventory = total_rentals > available_inventory
        rental_data.append([
            equipment_names[j], t, total_rentals, available_inventory, " Exceeds Inventory" if exceeds_inventory else "Normal"
        ])
        
# Convert to DataFrame
df_rental_summary = pd.DataFrame(rental_data, columns=["Equipment", "Week", "Total Rentals", "Available Inventory", "Inventory Status"])


# Print first 10 rows of summary
print(df_rental_summary.head(10))




