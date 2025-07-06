import tkinter as tk
from tkinter import messagebox
import json
from matplotlib import pyplot as plt

# Carrega os dilemas do arquivo
with open('dilemas.json', encoding='utf-8') as f:
    dilemas = json.load(f)

# Variáveis globais
indice = 0
pontuacao = {"Utilitarista": 0, "Deontologico": 0, "Relacional": 0}


def mostrar_resultado():
    total = sum(pontuacao.values())
    if total == 0:
        messagebox.showinfo("Resultado Final", "Nenhuma escolha foi feita.")
        return

    descricao_perfis = {
        "Utilitarista": "Utilitarista – acredita que o fim justifica os meios.",
        "Deontologico": "Deontológico – acredita que princípios importam mais que resultados.",
        "Relacional": "Relacional – prioriza vínculos e emoções.",
    }

    resultado = "🧠 Resultado do seu perfil ético:\n\n"
    for etica, valor in pontuacao.items():
        percentual = int((valor / total) * 100)
        resultado += f"- {descricao_perfis[etica]} ({percentual}%)\n"

    # Exibir a descrição com porcentagens
    messagebox.showinfo("Resultado Final", resultado)

    # Exibir gráfico de pizza
    plt.pie(pontuacao.values(), labels=pontuacao.keys(), autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Seu Perfil Ético')
    plt.show()


# Avança para o próximo dilema
def proximo_dilema(pontos):
    global indice
    for etica, valor in pontos.items():
        pontuacao[etica] += valor

    indice += 1
    if indice < len(dilemas):
        mostrar_dilema(indice)
    else:
        mostrar_resultado()
        frame_principal.destroy()


# Exibe um dilema com botões de escolha
def mostrar_dilema(i):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    dilema = dilemas[i]

    titulo = tk.Label(frame_principal, text=dilema['titulo'], font=('Helvetica', 16, 'bold'), wraplength=500, pady=10)
    titulo.pack()

    descricao = tk.Label(frame_principal, text=dilema['descricao'], font=('Helvetica', 12), wraplength=500)
    descricao.pack()

    for opcao in dilema['opcoes']:
        btn = tk.Button(
            frame_principal,
            text=opcao['texto'],
            font=('Helvetica', 11),
            wraplength=450,
            padx=10,
            pady=8,
            bg='#ddddff',
            activebackground='#ccccee',
            relief='raised',
            command=lambda pontos=opcao['pontuacao']: proximo_dilema(pontos)
        )
        btn.pack(pady=6, fill='x')


# Janela principal
janela = tk.Tk()
janela.title("🧠 Simulador de Dilemas Éticos")
janela.geometry("600x500")
janela.resizable(False, False)

frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(expand=True)

mostrar_dilema(indice)

janela.mainloop()


# Função para analisar os resultados
def analisar_resultados(pontuacoes):
    total = sum(pontuacoes.values())
    if total == 0:
        return "Nenhuma escolha feita."

    relatorio = "\nResultado do seu perfil ético:\n"
    for chave, valor in pontuacoes.items():
        percentual = (valor / total) * 100
        if chave == "Utilitarista":
            descricao = "Utilitarista – acredita que o fim justifica os meios."
        elif chave == "Deontológico":
            descricao = "Deontológico – acredita que princípios importam mais que resultados."
        elif chave == "Imparcial":
            descricao = "Imparcial – preza pela justiça acima das relações pessoais."
        elif chave == "Relacional":
            descricao = "Relacional – prioriza vínculos e emoções."
        else:
            descricao = "Outro."

        relatorio += f"- {descricao} ({percentual:.1f}%)\n"

    return relatorio
