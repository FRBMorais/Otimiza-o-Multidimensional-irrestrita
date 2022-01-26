import numpy as np
from bisseccao_1D import Bisseccao


class MaximaDescida:
    def __init__(self,
                 x_vtr,
                 analise,
                 iteracoes_limite,
                 tol=10e-8,
                 h=10e-4):

        self.x_vtr = x_vtr
        self.x_vetor_1 = []
        self.analise = analise
        self.iteracoes_limite = iteracoes_limite
        self.r_vetor_aleatorios = []
        self.x_vetor_otimo = x_vtr
        self.tol = tol
        self.n_iteracoes = 1
        self.h = h
        self.alfax = None
        self.alfay = None
        self.Si = []

    def derivada_parcial_x(self, x):
        derivada1 = (self.f_xi([x[0] + self.h, x[1]]) - self.f_xi([x[0] - self.h, x[1]])) / (2 * self.h)
        # Derívada numérica - Diferenças finitas
        return derivada1

    def derivada_parcial_y(self, x):
        derivada1 = (self.f_xi([x[0], x[1] + self.h]) - self.f_xi([x[0], x[1] - self.h])) / (2 * self.h)
        # Derívada numérica - Diferenças finitas
        return derivada1

    def f_xi(self, x_vetor):
        """
        :param x_vetor: Variável X multidimensional que está sendo minimizada
        :return: Retorna o valor da função em x_vetor
        """
        if self.analise == 1:  # Sphere function
            return x_vetor[0] ** 2 + x_vetor[1] ** 2
        elif self.analise == 0:
            return x_vetor[0] - x_vetor[1] \
                   + 2 * x_vetor[0] ** 2 \
                   + 2 * x_vetor[0] * x_vetor[1] \
                   + x_vetor[1] ** 2
        elif self.analise == 2:  # Beale Function
            return (1.5 - x_vetor[0] + x_vetor[0] * x_vetor[1]) ** 2 + \
                   (2.25 - x_vetor[0] + x_vetor[0] * x_vetor[1] ** 2) ** 2 + \
                   (2.625 - x_vetor[0] + x_vetor[0] * x_vetor[1] ** 3) ** 2
        elif self.analise == 3:  # Three-Ramp-Camel
            return 2 * x_vetor[0] ** 2 - 1.05 * x_vetor[0] ** 4 + \
                   x_vetor[0] ** 6 / 6 + x_vetor[0] * x_vetor[1] + x_vetor[1] ** 2
        elif self.analise == 4:  # Rastrigin
            a = 10
            n = 2
            return a * n + (x_vetor[0] ** 2 - a * np.cos(2 * np.pi * x_vetor[0]) +
                             (x_vetor[1] ** 2 - a * np.cos(2 * np.pi * x_vetor[1])))
        elif self.analise == 5:  # Ackley
            return -20 * np.exp(-0.2 *
                                (0.5 * (x_vetor[0] ** 2 + x_vetor[1] ** 2)) ** (1 / 2)) \
                   - np.exp(0.5 * (np.cos(2 * np.pi * x_vetor[0]) + np.cos(2 * np.pi * x_vetor[1]))) \
                   + np.e + 20
        elif self.analise == 6:  # Levi number 13
            return np.sin(3 * np.pi * x_vetor[0]) ** 2 \
                   + (x_vetor[0] - 1) ** 2 * (1 + np.sin(3 * np.pi * x_vetor[1]) ** 2) \
                   + (x_vetor[1] - 1) ** 2 * (1 + np.sin(2 * np.pi * x_vetor[1]) ** 2)
        elif self.analise == 7:  # Eason
            return -np.cos(x_vetor[0]) * np.cos(x_vetor[1]) * np.exp(-((x_vetor[0] - np.pi) ** 2
                                                                       + (x_vetor[1] - np.pi) ** 2))
        elif self.analise == 8:  # Sxhaffer number 2
            return 0.5 + (np.sin(x_vetor[0] ** 2 - x_vetor[1] ** 2) ** 2 - 0.5) \
                   / (1 + 0.001 * (x_vetor[0] ** 2 + x_vetor[1] ** 2)) ** 2
        elif self.analise == 9:  # Default problem
            k1 = 2
            k2 = 2.5
            k3 = 1.5
            ff = 50
            return 0.5 * k2 * x_vetor[0] ** 2 \
                   + 0.5 * k3 * (x_vetor[1] - x_vetor[0]) ** 2 \
                   + 0.5 * k1 * x_vetor[1] ** 2 - ff * x_vetor[1]

    def estrutura_metodo(self):
        tolerancia = 1
        while tolerancia > self.tol and self.n_iteracoes < self.iteracoes_limite:
            """
            1. Start with an arbitrary initial point X1. Set the iteration number as i = 1;  ok
            2. Find the search direction Si as; Equation from book;  ok
            3. Determine the optimal step lenght (lambd i asterix) in the direction Si
            and set xi+1 = xi +  (lambd i asterix) * Si
            For this, we minimize f_xi(X1 + lambd1*S1)
            and find lambd1
            """
            # Definindo a direção
            self.Si.append(-self.derivada_parcial_x(self.x_vtr))
            self.Si.append(-self.derivada_parcial_y(self.x_vtr))

            bi = Bisseccao(-10, 10, 0.001, self.x_vtr, self.Si, self.analise)
            bi.metodo()
            lambdd_ideal = bi.c

            x_vtr_novo = [self.x_vtr[i] + lambdd_ideal * self.Si[i] for i in range(len(self.x_vtr))]

            tolerancia = abs((self.f_xi(x_vtr_novo) - self.f_xi(self.x_vtr)) / self.f_xi(self.x_vtr))

            self.x_vtr = x_vtr_novo.copy()
            self.Si.clear()
            print(f'X{self.n_iteracoes}:  {self.x_vtr}\n'
                  f'Lambda ideal {self.n_iteracoes}:  {lambdd_ideal}')
            self.n_iteracoes += 1


