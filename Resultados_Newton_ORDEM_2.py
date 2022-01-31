from Newton_ORDEM_2 import NewtonSegundaOrdem


# # Sphere Function -- OK -- BEM SUCEDIDO
# teste = NewtonSegundaOrdem([1, 1], 1, 10_000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (0, 0)
"""


# # Beale -- ok --> BEM SUCEDIDIDO
# teste = NewtonSegundaOrdem([3, 3], 2, 100000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (3, 0.5)
"""
# # tree Ramp Camel -- ok --> BEM SUCEDIDO
# teste = NewtonSegundaOrdem([0.5, 0.5], 3, 100000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (0, 0)
"""
# # Rastrigin
# teste = NewtonSegundaOrdem([-0.1, 0.2], 4, 10)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (0, 0)
"""
# # Ackley
# teste = NewtonSegundaOrdem([-3, 3], 5, 10_000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (0, 0)
"""
# # Levi number 13
# teste = NewtonSegundaOrdem([2, -1], 6, 10_000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (1, 1)
"""
# # Eason -- ok -- BEM SUCEDIDO
# teste = NewtonSegundaOrdem([2, 2], 7, 10_000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == -1 ---------- (pi, pi)
"""
# # Sxhaffer number 2 -- OK --> BEM SUCEDIDO
# teste = NewtonSegundaOrdem([2, 2], 8, 10_000)
# teste.metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')
#
"""
f(x, y)mín == 0 ---------- (1, 1)
"""
# Problema Default -- ok --> BEM SUCEDIDO
# teste = NewtonSegundaOrdem([2, 10], 9, 10_000)
# teste.metodo()
# print(teste.x_vtr, teste.f_xi(teste.x_vtr))
"""
f(x, y)mín == -425.5319 ---------- (6.3830, 17.02013)
"""
