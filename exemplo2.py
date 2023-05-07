### Trabalho programação linear
### Aluna: Jéssica Barbosa de Souza Costa
### Exemplo 2


"""
O objetivo desse código é achar a melhor combinação possível, de forma que reduza o resíduo (epsilon)
para os componentes abaixo fabricarem os grupos descritos a seguir

"""

from ortools.linear_solver import pywraplp

# Data

max_quantities = [
    ["N_Total", 1944],
    ["P2O5", 1166.4],
    ["K2O", 1822.5],
    ["CaO", 1458],
    ["MgO", 486],
    ["Fe", 9.7],
    ["B", 2.4],
    ["Zn", 15.9],
    ["Cu", 10.3],
    ["Mn", 44],
    ["Mo", 8.3],
    ["Cl", 15.3],
    ["S", 9.0],
    ["Na2O", 87.0],
    ["SiO2", 22.0]
]

chemical_set = [
    ["A", 0, 0, 51, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["B", 11, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["C", 6.1, 14.9, 38.4, 0, 3, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    ["D", 148, 70, 24.5, 0, 15, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    ["E", 16.0, 15.8, 16.1, 0, 10, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    ["F", 0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
    ["G", 0, 0, 0, 0, 0, 1.1, 0, 0, 0.3, 0, 0, 0, 0, 0, 0],
    ["H", 0, 0, 0, 0, 0, 0, 0, 4.3, 0, 0.6, 0, 0, 0, 0, 0],
    ["I", 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.1, 0.5, 0, 0, 0, 0],
    ["J", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.1, 0, 0],
    ["K", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.2, 0.5, 0],
    ["L", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.0, 3]
]

ALL_PRODUCTS = range(0, len(max_quantities))

ALL_SETS = range(0, len(chemical_set))

# Modelo

max_set = [
    min(max_quantities[q][1] / chemical_set[s][q + 1] for q in ALL_PRODUCTS
        if chemical_set[s][q + 1] != 0.0) for s in ALL_SETS
]

solver = pywraplp.Solver("chemical_set_lp",
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

set_vars = [solver.NumVar(0, max_set[s], f"set_{s}") for s in ALL_SETS]

epsilon = solver.NumVar(0, 1000, "epsilon")

for p in ALL_PRODUCTS:
    solver.Add(
        sum(chemical_set[s][p + 1] * set_vars[s]
            for s in ALL_SETS) <= max_quantities[p][1])
    solver.Add(
        sum(chemical_set[s][p + 1] * set_vars[s]
            for s in ALL_SETS) >= max_quantities[p][1] - epsilon)

solver.Minimize(epsilon)

print(f"Número de variáveis = {solver.NumVariables()}")
print(f"Número de restrições = {solver.NumConstraints()}")

status = solver.Solve()

# O problema tem uma solucao otima ?
print('Status = ', status == pywraplp.Solver.OPTIMAL)

# Qual o valor da função objetivo ?
print(f"Função objetivo = {solver.Objective().Value()}")

for s in ALL_SETS:
    print(f"  {chemical_set[s][0]} = {set_vars[s].solution_value()}", end=" ")
    print()

# Extra: print para analisar o o valor usado de cada material
for p in ALL_PRODUCTS:
    name = max_quantities[p][0]
    max_quantity = max_quantities[p][1]
    quantity = sum(set_vars[s].solution_value() * chemical_set[s][p + 1]
                   for s in ALL_SETS)
    print(f"{name}: {quantity} usada de  {max_quantity}")