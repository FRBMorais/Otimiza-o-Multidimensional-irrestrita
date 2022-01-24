import numpy as np


class Bisseccao:
    """ Otimiza uma função utilizando o método da bissecção
    parâmetros de entrada
    intervalo a ser otmizado (a, b)
    --> mínimo a
    --> máximo b
    analise --> se refere a função a ser analisada
    --> delta: Passo necessário no método da bissecção
    --> tol = tolerância da otimização, por padrão 10e-8
    self.iterações --> quantidade de iterações que o programa demorou para convergir
    self.caminho --> histórico de onde a otimização buscou
    self.residuo --> modulo do último resultado encontrado menos o anterior a ele,
    parâmetro para avaliar a convergência do programa
    """
    def __init__(self,
                 a,
                 b,
                 delta,
                 x_vetor,
                 derivada,
                 analise,
                 tol=10e-8):
        self.a = a
        self.b = b
        self.c = None
        self.delta = delta
        self.x_vetor = x_vetor
        self.derivada = derivada
        self.analise = analise
        self.tol = tol
        self.ya = None
        self.yb = None
        self.yc = None
        self.iteracoes = 0
        self.caminho = []
        self.valor = []
        self.residuo = []

    def funcao(self, valor):
        """
        :param valor: Um valor aí
        :return:
        """

        x_vetor = [self.x_vetor[0] + valor * self.derivada[0],
                   self.x_vetor[1] + valor * self.derivada[1]]

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

    def metodo(self):
        self.ya = self.funcao(self.a)
        self.yb = self.funcao(self.b)
        self.c = 0.5 * (self.a + self.b)
        self.yc = self.funcao(self.c)
        while abs(self.a - self. b) > self.tol:
            self.caminho.append(self.c)
            self.valor.append(self.yc)
            self.iteracoes += 1
            self.residuo.append(abs(self.yb - self.ya))
            if self.funcao(self.c + self.delta) > self.funcao(self.c - self.delta):
                self.b = self.c
                self.yb = self.yc
                self.c = 0.5 * (self.a + self.b)
                self.yc = self.funcao(self.c)
            elif self.funcao(self.c + self.delta) < self.funcao(self.c - self.delta):
                self.a = self.c
                self.ya = self.yc
                self.c = 0.5 * (self.a + self.b)
                self.yc = self.funcao(self.c)
            elif self.funcao(self.c + self.delta) == self.funcao(self.c - self.delta):
                break
            else:
                print("Entre com um novo intervalo [a, b]")
        self.yc = self.funcao(self.c)

        if -10e-8 < self.yc < 10e-8:
            self.yc = 0

        if -10e-8 < self.c < 10e-8:
            self.c = 0
