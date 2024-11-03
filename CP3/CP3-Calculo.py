import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

impostos_renda = int(input('Deseja adicionar ou tirar impostos na venda do produto? Digite o valor da porcentagem dos impostos (positivo ou negativo): '))
impostos_Custo = int(input('Deseja adicionar ou tirar impostos no preço da produção? Digite o valor da porcentagem dos impostos (positivo ou negativo): '))


#Criando Funções Custo, rceita e Lucro
def Custo(x):
    return (200 + 5 * x ** 2 + 10 * x) * (1 + impostos_Custo / 100)


def Receita(x):
    return (40 * x) * (1 + impostos_renda / 100)


def Lucro(x):
    return Receita(x) - Custo(x)

# Encontrar o ponto ótimo de produção
resultado = minimize_scalar(lambda x: -Lucro(x), bounds=(0, 10), method='bounded')
x_otimo = resultado.x
lucro_otimo = -resultado.fun

# Valores de x para simulação
x_valor = np.linspace(0, 10, 500)
valor_custo = Custo(x_valor)
valor_receita = Receita(x_valor)
valor_lucro = Lucro(x_valor)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(x_valor, valor_custo, label='Custo', color='blue')
plt.plot(x_valor, valor_receita, label='Receita', color='green')
plt.plot(x_valor, valor_lucro, label='Lucro', color='red')

# Exibindo o ponto ótimo
plt.scatter(x_otimo, lucro_otimo, color='red', zorder=5)
plt.text(x_otimo, lucro_otimo, f'  Ponto Ótimo ({x_otimo:.2f}, {lucro_otimo:.2f})')

plt.title('Custo, Receita e Lucro em Função da Produção')
plt.xlabel('Unidades Produzidas (x)')
plt.ylabel('Valor')
plt.axhline(0, color='black', lw=0.8, ls='--')
plt.axvline(0, color='black', lw=0.8, ls='--')
plt.legend()
plt.grid()
plt.show()