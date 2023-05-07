### Trabalho 3  programação linear
### Aluna: Jéssica Barbosa de Souza Costa
### Caso extra 1

"""
O objetivo desse código é achar a melhor combinação possível de x , y  de forma que maximize a função objetivo
mas atenda as restrições de valores

"""

from ortools.linear_solver import pywraplp

# Chama o solver utilizado, no caso o GLOP pois é PL simples.
solver = pywraplp.Solver.CreateSolver('SAT')
if not solver:
    print("Solver não encontrado")

# Cria as variáveis  x and y, entre os limites de valores escolhidos - No caso entre 0 e a capacidade máxima
# sulfato de aluminio
x = solver.NumVar(0, 20, 'x')
# acido sulfurico
y = solver.NumVar(0, 51.5, 'x')

print('Número de variáveis =', solver.NumVariables())

# restrições 1:
solver.Add(0.45 * x + 2.15 * y <= 24)

# restrições 2:
solver.Add(0.2 * x + 2.15 * y <= 24)

# restrições 3:
solver.Add(0.1 * x + 2.15 * y <= 24)

print(' Número de restrições =', solver.NumConstraints())

# Criar função objetivo:
solver.Maximize(3760.66*x + 4604.58*y)

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("Solução viável encontrada")
else:
    print("Nenhuma solução viável encontrada")

print('Solução:')
print('Valor da Função Objetivo =', solver.Objective().Value())
print('x =', x.solution_value())
print('y =', y.solution_value())