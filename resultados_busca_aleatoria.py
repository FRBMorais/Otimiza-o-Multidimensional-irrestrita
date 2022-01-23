from classe_buscaaleatoria import BuscaAleatoria

"""
Método de ordem 0 --> BUSCA ALEATÓRIA -- ok --> BEM SUCEDIDO
"""
# # Sphere Function -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [3, 3], [-3, -3], 100_000, 1)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (0, 0)
f(x, y)mín == 2.6930e-05 ---------- (0.00297, -0.00425)
"""
#
# # Beale Function -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([2, 1], [5, 3], [-4, -3], 100_000, 2)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (3, 0.5)
f(x, y)mín == 0.000496 ---------- (2.9472, 0.4876)
"""
#
# # Three Ramp Camel -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [5, 5], [-4, -4], 100_000, 3)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (0, 0)
f(x, y)mín == 0.00042 ---------- (0.01550, -0.0099)
"""
#
# Rastrigin -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [5, 5], [-4, -4], 100_000, 4)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (0, 0)
f(x, y)mín == 0.00068 ---------- (-0.001321, -0.00130)
"""
#
# # Ackley -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [5, 5], [-5, -5], 100_000, 5)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (0, 0)
f(x, y)mín == 0.01456 ---------- (0.0029, 0.0039)
"""
#
# # Levi number 13 -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([3, 3], [5, 5], [-5, -5], 100_000, 6)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (1, 1)
f(x, y)mín == 0.00154 ---------- (1.00336, 1.0227)
"""
#
# # Eason -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [5, 5], [-5, -5], 100_000, 7)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == -1 ---------- (pi, pi)
f(x, y)mín == -0.9995 ---------- (3.1495, 3.1258)
"""
#
# # Sxhaffer number 2 -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([1, 1], [5, 5], [-4, -4], 100_000, 8)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == 0 ---------- (0, 0)
f(x, y)mín == 6.75017e-08 ---------- (0.0077, 0.00228)
"""
#
# # Problema Default -- ok --> BEM SUCEDIDO
# teste = BuscaAleatoria([6, 15], [9, 18], [2, 14], 100_000, 9)
# teste.estrutura_metodo()
# print(teste.x_vetor_otimo, teste.f_xi(teste.x_vetor_otimo))
"""
f(x, y)mín == -425.5319 ---------- (6.3830, 17.02013)
f(x, y)mín == -425.5318 ---------- (6.3758, 17.01633)
"""


