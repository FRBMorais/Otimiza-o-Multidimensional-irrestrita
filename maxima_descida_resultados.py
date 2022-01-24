from maxima_descida_ORDEM_1 import MaximaDescida


# # Sphere Function
# teste = MaximaDescida([1, 1], 1)
# teste.estrutura_metodo()
# print(f'Valor do ponto ótimo {teste.x_vtr},\n '
#       f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')
#
# """
# f(x, y)mín == 0 ---------- (0, 0)
# """

# Beale
teste = MaximaDescida([0, 0], 2, 100)
teste.estrutura_metodo()
print(f'Valor do ponto ótimo {teste.x_vtr},\n '
      f'Valor da função no ponto ótimo {teste.f_xi(teste.x_vtr)}')

"""
f(x, y)mín == 0 ---------- (3, 0.5)
f(x, y)mín == 0.000496 ---------- (2.9472, 0.4876)
"""