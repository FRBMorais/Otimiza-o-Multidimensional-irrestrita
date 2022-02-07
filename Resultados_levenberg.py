from Levenberg import Levenberg


# Problema Default -- ok --> BEM SUCEDIDO
teste = Levenberg([2, 10], 9, 10_000)
teste.metodo()
print(teste.x_vtr, teste.f_xi(teste.x_vtr))
"""
f(x, y)mín == -425.5319 ---------- (6.3830, 17.02013)
"""