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
