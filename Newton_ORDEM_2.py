"""
Os M´etodos de Segunda Ordem s˜ao estrat´egias que fazem uso de informações do vetor
gradiente e da matriz Hessiana da fun¸c˜ao objetivo para a determinação da direção de busca
em problemas de otimização.
"""
import numpy as np
from bisseccao_1D import Bisseccao


class NewtonSegundaOrdem:
    def __init__(self,
                 x_vtr,
                 analise,
                 iteracoes_limite,
                 h=10e-4,
                 tol=10e-8):
        self.analise = analise
        self.x_vtr = x_vtr
        self.iteracoes_limite = iteracoes_limite
        self.h = h
        self.tol = tol
        self.segundo = []
        self.n_iteracoes = 1

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

    def derivada_x_1(self, x, y):
        derivada1 = (self.f_xi([x + self.h, y]) - self.f_xi([x - self.h, y])) / (2 * self.h)
        return derivada1

    def derivada_y_1(self, x, y):
        derivada1 = (self.f_xi([x, y + self.h]) - self.f_xi([x, y - self.h])) / (2 * self.h)
        return derivada1

    def derivada_x_2(self, x, y):
        derivada2 = (self.f_xi([x + self.h, y]) - 2 * self.f_xi([x, y]) + self.f_xi([x - self.h, y])) / (self.h ** 2)
        return derivada2

    def derivada_y_2(self, x, y):
        derivada2 = (self.f_xi([x, y + self.h]) - 2 * self.f_xi([x, y]) + self.f_xi([x, y - self.h])) / (self.h ** 2)
        return derivada2

    def derivada_xy(self, x, y):
        parcela1 = self.f_xi([x - self.h, y - self.h])
        parcela2 = self.f_xi([x - self.h, y + self.h])
        parcela3 = self.f_xi([x + self.h, y - self.h])
        parcela4 = self.f_xi([x + self.h, y + self.h])
        derivada = (1 / (4 * self.h ** 2)) * (parcela1 - parcela2 - parcela3 + parcela4)
        return derivada

    def h_i(self, x,  y):
        hessiana = np.array([[self.derivada_x_2(x, y), self.derivada_xy(x, y)],
                             [self.derivada_xy(x, y), self.derivada_y_2(x, y)]])
        inversa = np.linalg.inv(hessiana)
        return inversa

    def gradiente_fx_i(self, x, y):
        gradiente = np.array([[self.derivada_x_1(x, y)], [self.derivada_y_1(x, y)]])
        return gradiente

    def segundo_termo(self, x, y):
        return np.dot(self.h_i(x, y), self.gradiente_fx_i(x, y))

    def metodo(self):
        tolerancia = 1
        while tolerancia > self.tol and self.n_iteracoes < self.iteracoes_limite:
            # Definindo a direção
            # print(self.segundo_termo(self.x_vtr[0], self.x_vtr[1]))
            self.segundo.append(self.segundo_termo(self.x_vtr[0], self.x_vtr[1])[0, 0])
            self.segundo.append(self.segundo_termo(self.x_vtr[0], self.x_vtr[1])[1, 0])

            bi = Bisseccao(-10, 10, 0.001, self.x_vtr, self.segundo, self.analise)
            bi.metodo()
            lambdd_ideal = bi.c

            x_vtr_novo = [self.x_vtr[i] + lambdd_ideal * self.segundo[i] for i in range(len(self.x_vtr))]

            tolerancia = abs((self.f_xi(x_vtr_novo) - self.f_xi(self.x_vtr)) / self.f_xi(self.x_vtr))

            self.x_vtr = x_vtr_novo.copy()
            self.segundo.clear()
            print(f'X{self.n_iteracoes}:  {self.x_vtr}\n'
                  f'Lambda ideal {self.n_iteracoes}:  {lambdd_ideal}')
            self.n_iteracoes += 1
