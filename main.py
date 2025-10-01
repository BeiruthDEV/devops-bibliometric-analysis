"""
Script para gerar gráficos de análise bibliográfica sobre Engenharia de Software Contínua e Experimental.

Este script utiliza os dados extraídos de um conjunto de 17 artigos acadêmicos para criar as seguintes visualizações:
1. Evolução anual de publicações.
2. Distribuição de artigos por tipo de estudo empírico.
3. Principais categorias de métricas avaliadas nos estudos.
4. Mapa comparativo de publicações por região geográfica.

Bibliotecas necessárias: pandas, matplotlib, seaborn.
Para instalar, use: pip install pandas matplotlib seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plotar_evolucao_anual():
    """
    Gera e exibe um gráfico de barras da evolução anual de publicações.
    """
    data_ano = {
        "Ano": [
            2015,
            2015,
            2016,
            2016,
            2016,
            2017,
            2017,
            2018,
            2018,
            2019,
            2019,
            2020,
            2020,
            2021,
            2021,
            2021,
            2022,
        ]
    }
    df_ano = pd.DataFrame(data_ano)
    contagem_ano = df_ano["Ano"].value_counts().sort_index()

    plt.figure(figsize=(12, 7))
    barplot = sns.barplot(
        x=contagem_ano.index, y=contagem_ano.values, palette="viridis"
    )

    plt.title("Gráfico 1: Evolução Anual de Publicações", fontsize=16)
    plt.xlabel("Ano de Publicação", fontsize=12)
    plt.ylabel("Quantidade de Artigos", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), ".0f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    plt.tight_layout()
    plt.show()


def plotar_distribuicao_tipo_estudo():
    """
    Gera e exibe um gráfico de barras da distribuição dos artigos por tipo de estudo.
    """
    study_types_data = {
        "Tipo de Estudo": [
            "Relatório de Experiência / Estudo de Caso",
            "Múltiplos Estudos de Caso",
            "Análise de Tendências",
            "Relatório de Experiência / Análise Crítica",
            "Múltiplos Estudos de Caso",
            "Proposta de Pesquisa",
            "Revisão Sistemática da Literatura (RSL)",
            "Artigo de Posição / Análise Crítica",
            "Estudo Empírico",
            "Estudo de Caso / Análise de Indústria",
            "Múltiplos Estudos de Caso",
            "RSL + Survey",
            "Família de Experimentos",
            "Estudo Empírico / Avaliação de Ferramenta",
            "Múltiplos Estudos de Caso",
            "Estudo Empírico",
            "Exercício de Ideação + Revisão de Literatura",
        ]
    }
    df_types = pd.DataFrame(study_types_data)

    def group_types(study_type):
        if (
            "Estudo de Caso" in study_type
            or "Relatório de Experiência" in study_type
            or "Análise de Tendências" in study_type
            or "Análise de Indústria" in study_type
        ):
            return "Estudo de Caso e Relatórios"
        if (
            "RSL" in study_type
            or "Revisão de Literatura" in study_type
            or "Survey" in study_type
        ):
            return "Revisão da Literatura"
        if "Estudo Empírico" in study_type:
            return "Estudo Empírico (Mineração/Análise)"
        if "Experimento" in study_type:
            return "Experimentos"
        return "Outros (Proposta, Posição, etc.)"

    df_types["Grupo"] = df_types["Tipo de Estudo"].apply(group_types)
    type_counts = df_types["Grupo"].value_counts()

    plt.figure(figsize=(12, 7))
    barplot = sns.barplot(x=type_counts.index, y=type_counts.values, palette="plasma")

    plt.title("Gráfico 2: Distribuição de Artigos por Tipo de Estudo", fontsize=16)
    plt.xlabel("Tipo de Estudo", fontsize=12)
    plt.ylabel("Quantidade de Artigos", fontsize=12)
    plt.xticks(rotation=15, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), ".0f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    plt.tight_layout()
    plt.show()


def plotar_metricas_avaliadas():
    """
    Gera e exibe um gráfico de barras das principais métricas avaliadas.
    """
    metrics_data = {
        "Métrica": [
            "Produtividade e Eficiência",
            "Produtividade e Eficiência",
            "Produtividade e Eficiência",
            "Qualidade e Desempenho",
            "Qualidade e Desempenho",
            "Manutenibilidade e Arquitetura",
            "Manutenibilidade e Arquitetura",
            "Manutenibilidade e Arquitetura",
            "Desafios e Práticas",
            "Desafios e Práticas",
            "Qualidade e Desempenho",
            "Qualidade e Desempenho",
            "Qualidade de Dados",
            "Produtividade e Eficiência",
            "Qualidade e Desempenho",
            "Manutenibilidade e Arquitetura",
            "Qualidade e Desempenho",
            "Percepção Humana e Adoção",
        ]
    }
    df_metrics = pd.DataFrame(metrics_data)
    metric_counts = df_metrics["Métrica"].value_counts()

    plt.figure(figsize=(12, 7))
    barplot = sns.barplot(
        x=metric_counts.index, y=metric_counts.values, palette="magma"
    )

    plt.title("Gráfico 3: Principais Categorias de Métricas Avaliadas", fontsize=16)
    plt.xlabel("Categoria da Métrica", fontsize=12)
    plt.ylabel("Frequência de Abordagem nos Artigos", fontsize=12)
    plt.xticks(rotation=15, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), ".0f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    plt.tight_layout()
    plt.show()


def plotar_mapa_comparativo_paises():
    """
    Gera e exibe um gráfico de barras comparando publicações por região.
    """
    countries = [
        "Europa",
        "Europa",
        "Europa",
        "Europa",
        "América do Norte",
        "Ásia",
        "Oceania",
        "América do Norte",
        "Europa",
        "Ásia",
        "Oceania",
        "Europa",
        "Europa",
        "América do Sul",
        "Europa",
        "Europa",
        "América do Norte",
        "Ásia",
        "Europa",
        "Europa",
        "América do Norte",
    ]
    df_countries = pd.DataFrame(countries, columns=["Região"])
    country_counts = df_countries["Região"].value_counts()

    plt.figure(figsize=(12, 7))
    barplot = sns.barplot(
        x=country_counts.index, y=country_counts.values, palette="coolwarm"
    )

    plt.title("Gráfico 4: Mapa Comparativo de Publicações por Região", fontsize=16)
    plt.xlabel("Continente / Região", fontsize=12)
    plt.ylabel("Quantidade de Artigos", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), ".0f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sns.set(style="whitegrid")

    print("Gerando Gráfico 1: Evolução Anual de Publicações...")
    plotar_evolucao_anual()

    print("\nGerando Gráfico 2: Distribuição de Artigos por Tipo de Estudo...")
    plotar_distribuicao_tipo_estudo()

    print("\nGerando Gráfico 3: Principais Categorias de Métricas Avaliadas...")
    plotar_metricas_avaliadas()

    print("\nGerando Gráfico 4: Mapa Comparativo de Publicações por Região...")
    plotar_mapa_comparativo_paises()

    print("\nTodos os gráficos foram gerados.")
