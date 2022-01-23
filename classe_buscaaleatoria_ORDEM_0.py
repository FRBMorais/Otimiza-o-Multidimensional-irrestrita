import numpy as np
import random


class BuscaAleatoria:
    def __init__(self, x_vtr, xu_vetor, xl_vetor, n_iteracoes_limite, analise):
        self.x_vtr = x_vtr
        self.x_vetor_1 = []
        self.xu_vetor = xu_vetor
        self.xl_vetor = xl_vetor
        self.n_iteracoes_limite = n_iteracoes_limite
        self.analise = analise
        self.r_vetor_aleatorios = []
        self.x_vetor_otimo = x_vtr
        self.n_iteracoes = 0

    def aleatorios(self):
        """
        :return: Retorna o vetor de valores aleatórios entre 0 e 1
        """
        random.seed()
        self.r_vetor_aleatorios = [random.random(), random.random()]
        # print(self.r_vetor_aleatorios)

    def f_xi(self, x_vetor):
        """
        :param x_vetor: Variável X multidimensional que está sendo minimizada
        :return: Retorna o valor da função em x_vetor
        """
        if self.analise == 1:  # Sphere function
            return x_vetor[0] ** 2 + x_vetor[1] ** 2
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
        while self.n_iteracoes < self.n_iteracoes_limite:
            self.x_vetor_1.clear()
            for i in range(2):
                self.aleatorios()
                self.x_vetor_1.append(self.xl_vetor[i] + self.r_vetor_aleatorios[i] *
                                      (self.xu_vetor[i] - self.xl_vetor[i]))
            if self.f_xi(self.x_vetor_1) < self.f_xi(self.x_vetor_otimo):
                self.x_vetor_otimo = self.x_vetor_1.copy()
            self.n_iteracoes += 1
