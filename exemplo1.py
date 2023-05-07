### Trabalho programação linear
### Aluna: Jéssica Barbosa de Souza Costa
### Exemplo 1

"""
O objetivo desse código é achar a melhor combinação possível de x , y e z, de forma que maximize a função objetivo
mas atenda as restrições de valores

"""

from ortools.linear_solver import pywraplp


# Chama o solver utilizado, no caso o GLOP pois é PL simples.
solver = pywraplp.Solver.CreateSolver('GLOP')
if not solver:
    print("Solver não encontrado")

# Cria as variáveis  the variables x and y, entre os limites de valores escolhidos - No caso entre 0 e infinito
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')
z = solver.NumVar(0, solver.infinity(), 'z')

print('Número de variáveis =', solver.NumVariables())

# restrições 1: x + 2y + z  <= 53
solver.Add(x + y + z <= 100.0)

# restrições 2: 3y - x + z >= 0.
solver.Add(3 * y - x + z >= 0.0)

# restrições 3: 2x - z + 2*y  > 2.
solver.Add(2 * x - z + 2*y >= 2.0)

print(' Número de restrições =', solver.NumConstraints())

# Criar função objetivo: 3x - 7y + 4z.
solver.Maximize(3*x - 7*y + 4*z)

status = solver.Solve()

print('Solution:')
print('Status = ', status == pywraplp.Solver.OPTIMAL)
print('Objective value =', solver.Objective().Value())
print('x =', x.solution_value())
print('y =', y.solution_value())
print('z =', z.solution_value())


