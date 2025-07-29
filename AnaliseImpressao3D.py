import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt

# ------------------------------
# Base de dados de modelos 3D
# ------------------------------
modelos = [
    {"nome": "Suporte de celular", "qtd_filamento": 45, "tempo": 2, "cor": "Preto", "preco_kg": 120},
    {"nome": "Vasinho decorativo", "qtd_filamento": 80, "tempo": 4, "cor": "Branco", "preco_kg": 125},
    {"nome": "Miniatura de dragão", "qtd_filamento": 35, "tempo": 3, "cor": "Dourado", "preco_kg": 150},
    {"nome": "Organizador de cabos", "qtd_filamento": 50, "tempo": 3.5, "cor": "Cinza", "preco_kg": 110},
    {"nome": "Porta-lápis", "qtd_filamento": 70, "tempo": 3.5, "cor": "Verde", "preco_kg": 137},
    {"nome": "Suporte para fone", "qtd_filamento": 110, "tempo": 5.5, "cor": "Laranja", "preco_kg": 135},
    {"nome": "Mini vaso autoirrigável", "qtd_filamento": 120, "tempo": 6, "cor": "Verde musgo", "preco_kg": 120},
    {"nome": "Quebra-cabeça 3D", "qtd_filamento": 20, "tempo": 1.5, "cor": "Multicolorido", "preco_kg": 180},
    {"nome": "Estatueta decorativa", "qtd_filamento": 150, "tempo": 7, "cor": "Bronze", "preco_kg": 135},
    {"nome": "Caixa organizadora pequena", "qtd_filamento": 90, "tempo": 4, "cor": "Branco gelo", "preco_kg": 127},
    {"nome": "Suporte de parede para escovas", "qtd_filamento": 25, "tempo": 1.2, "cor": "Cinza claro", "preco_kg": 123},
    {"nome": "Gatilho adaptador para spray", "qtd_filamento": 38, "tempo": 2.5, "cor": "Preto fosco", "preco_kg": 120},
    {"nome": "Mini suporte para notebook", "qtd_filamento": 100, "tempo": 5, "cor": "Verde oliva", "preco_kg": 135},
    {"nome": "Dispenser para álcool gel", "qtd_filamento": 130, "tempo": 6.5, "cor": "Transparente", "preco_kg": 120},
    {"nome": "Torre de aprendizado infantil", "qtd_filamento": 180, "tempo": 9, "cor": "Madeira natural", "preco_kg": 180},
    {"nome": "Conjunto de ganchos multifuncionais", "qtd_filamento": 60, "tempo": 3, "cor": "Amarelo", "preco_kg": 132},
    {"nome": "Suporte de tomada rotativo", "qtd_filamento": 45, "tempo": 2.8, "cor": "Preto", "preco_kg": 120}
]

# ------------------------------
# Função de fitness
# ------------------------------
def fitness(individuo):
    custo_filamento = 0
    tempo_total = 0
    for i in individuo:
        modelo = modelos[i]
        preco_por_grama = modelo["preco_kg"] / 1000
        custo_filamento += modelo["qtd_filamento"] * preco_por_grama
        tempo_total += modelo["tempo"]

    custo_total = custo_filamento + (tempo_total * 2)
    custo_min = 15
    custo_max = 500
    pontuacao = 100 - ((custo_total - custo_min) / (custo_max - custo_min)) * 99
    return max(1, min(100, pontuacao))

# ------------------------------
# Operadores Genéticos
# ------------------------------
def gerar_populacao(tamanho):
    return [random.sample(range(len(modelos)), 3) for _ in range(tamanho)]

def selecao(populacao):
    return max(populacao, key=fitness)

def cruzamento(pai, mae):
    ponto = random.randint(1, 2)
    filho = pai[:ponto] + [gene for gene in mae if gene not in pai[:ponto]]
    return filho[:3]

def mutacao(individuo):
    if random.random() < 0.2:
        novo = random.randint(0, len(modelos) - 1)
        if novo not in individuo:
            individuo[random.randint(0, 2)] = novo
    return individuo

# ------------------------------
# Interface Gráfica
# ------------------------------
class InterfaceGenetica:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo Genético - Impressão 3D")
        self.geracoes = 1000
        self.populacao = gerar_populacao(10)
        self.pontuacoes_por_geracao = []

        self.label_titulo = ttk.Label(root, text="Evolução Genética de Modelos 3D", font=("Arial", 14))
        self.label_titulo.pack(pady=10)

        self.resultado_box = tk.Text(root, height=30, width=65)
        self.resultado_box.pack(padx=10, pady=10)

        self.botao_iniciar = ttk.Button(root, text="Executar", command=self.executar_algoritmo)
        self.botao_iniciar.pack()

        self.botao_comparar = ttk.Button(root, text="Comparar com Aleatório", command=self.comparar_com_metodo_convencional)
        self.botao_comparar.pack(pady=5)

    def executar_algoritmo(self):
        self.resultado_box.delete("1.0", tk.END)
        consecutivas = 0
        melhor_anterior = None
        self.pontuacoes_por_geracao.clear()

        for gen in range(self.geracoes):
            nova_geracao = []
            for _ in range(len(self.populacao)):
                pai = selecao(self.populacao)
                mae = selecao(self.populacao)
                filho = cruzamento(pai, mae)
                filho = mutacao(filho)
                nova_geracao.append(filho)
            self.populacao = nova_geracao

            melhor = selecao(self.populacao)
            if melhor_anterior and sorted(melhor) == sorted(melhor_anterior):
                consecutivas += 1
            else:
                consecutivas = 1
                melhor_anterior = melhor

            pontuacao = fitness(melhor)
            self.pontuacoes_por_geracao.append(pontuacao)

            self.resultado_box.delete("1.0", tk.END)
            self.resultado_box.insert(tk.END, f"Geração {gen+1}:")
            for i in melhor:
                modelo = modelos[i]
                self.resultado_box.insert(tk.END, f" - {modelo['nome']} ({modelo['cor']})\n")
            self.resultado_box.insert(tk.END, f"Pontuação: {pontuacao:.2f}/100\n")
            self.root.update()
            time.sleep(0.5)

            if consecutivas == 10:
                self.resultado_box.insert(tk.END, "\n🚨 Convergência detectada!\n")
                break

    def comparar_com_metodo_convencional(self):
        self.resultado_box.delete("1.0", tk.END)
        self.resultado_box.insert(tk.END, "🔍 Comparando com método convencional (aleatório)...\n\n")

        def gerar_combinacoes_aleatorias(qtd=100):
            return [random.sample(range(len(modelos)), 3) for _ in range(qtd)]

        combinacoes = gerar_combinacoes_aleatorias()
        avaliados = [(ind, fitness(ind)) for ind in combinacoes]
        avaliados.sort(key=lambda x: -x[1])
        melhor_fitness_convencional = avaliados[0][1]

        for idx, (individuo, pontuacao) in enumerate(avaliados[:3], 1):
            custo_total = 0
            filamento_total = 0
            self.resultado_box.insert(tk.END, f"⭐ Conjunto #{idx} (Fitness: {pontuacao:.2f}/100)\n")
            for i in individuo:
                modelo = modelos[i]
                preco_por_grama = modelo["preco_kg"] / 1000
                custo = modelo["qtd_filamento"] * preco_por_grama
                custo_total += custo
                filamento_total += modelo["qtd_filamento"]

                self.resultado_box.insert(
                    tk.END,
                    f" - {modelo['nome']} ({modelo['cor']}) | {modelo['qtd_filamento']}g | {modelo['tempo']}h | R$ {custo:.2f}\n"
                )

            preco_medio = (custo_total / filamento_total) * 1000 if filamento_total > 0 else 0
            self.resultado_box.insert(tk.END, f" Custo total: R$ {custo_total:.2f}\n")
            self.resultado_box.insert(tk.END, f" Preço médio por kg: R$ {preco_medio:.2f}/kg\n")
            self.resultado_box.insert(tk.END, "-" * 50 + "\n")

        self.plotar_comparativo(melhor_fitness_convencional)

    def plotar_comparativo(self, melhor_convencional):
        if not self.pontuacoes_por_geracao:
            return

        geracoes = list(range(1, len(self.pontuacoes_por_geracao) + 1))
        plt.figure(figsize=(8, 5))
        plt.plot(geracoes, self.pontuacoes_por_geracao, marker='o', label='Algoritmo Genético')
        plt.hlines(y=melhor_convencional, xmin=1, xmax=len(geracoes), colors='r', linestyles='--', label='Melhor Aleatório (100)')
        plt.title("Comparativo: Algoritmo Genético vs Aleatório")
        plt.xlabel("Geração")
        plt.ylabel("Fitness")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# ------------------------------
# Execução principal
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGenetica(root)
    root.mainloop()
