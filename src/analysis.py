"""
Módulo de Análise Bibliométrica.
Responsável por processar os dados brutos e gerar visualizações para o portfólio.
Autor: Matheus Beiruth
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações Globais
sns.set(style="whitegrid")
DATA_PATH = os.path.join("..", "data", "dados_bibliometricos.csv")
ASSETS_DIR = os.path.join("..", "assets")


def carregar_dados(caminho):
    """Carrega o dataset e verifica sua integridade."""
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    return pd.read_csv(caminho)


def salvar_grafico(fig, nome_arquivo):
    """Salva a figura atual na pasta de assets."""
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
    path = os.path.join(ASSETS_DIR, nome_arquivo)
    fig.savefig(path, dpi=300, bbox_inches="tight")
    print(f"[OK] Gráfico salvo: {path}")


def plotar_evolucao_anual(df):
    """Gera gráfico de barras da evolução temporal."""
    # Filtra dados nulos (pois o CSV tem linhas extras para outras colunas)
    df_clean = df.dropna(subset=["Ano"])

    plt.figure(figsize=(10, 6))
    contagem = df_clean["Ano"].astype(int).value_counts().sort_index()

    ax = sns.barplot(x=contagem.index, y=contagem.values, palette="viridis")
    plt.title("Evolução Anual de Publicações (2015-2022)", fontsize=16, pad=20)
    plt.xlabel("Ano de Publicação", fontsize=12)
    plt.ylabel("Quantidade de Artigos", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Anotações
    for p in ax.patches:
        ax.annotate(
            f"{int(p.get_height())}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    salvar_grafico(plt.gcf(), "grafico_01_evolucao_anual.png")
    plt.close()


def plotar_tipos_estudo(df):
    """Gera gráfico horizontal dos tipos de estudo."""
    df_clean = df.dropna(subset=["Tipo_Estudo"])

    # Agrupamento simplificado para melhor visualização
    def categorizar(tipo):
        tipo = str(tipo).lower()
        if "caso" in tipo or "experiência" in tipo or "indústria" in tipo:
            return "Estudos de Caso / Relatórios"
        elif "rsl" in tipo or "revisão" in tipo or "survey" in tipo:
            return "Revisões de Literatura (RSL)"
        elif "experimento" in tipo or "empírico" in tipo:
            return "Experimentos / Empíricos"
        return "Outros (Propostas, Posição)"

    df_clean["Grupo"] = df_clean["Tipo_Estudo"].apply(categorizar)
    contagem = df_clean["Grupo"].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(y=contagem.index, x=contagem.values, palette="plasma", orient="h")

    plt.title("Distribuição por Metodologia de Pesquisa", fontsize=16, pad=20)
    plt.xlabel("Quantidade", fontsize=12)
    plt.ylabel("")

    salvar_grafico(plt.gcf(), "grafico_02_metodologia.png")
    plt.close()


def plotar_metricas(df):
    """Gera gráfico das principais métricas avaliadas."""
    df_clean = df.dropna(subset=["Categoria_Metrica"])
    contagem = df_clean["Categoria_Metrica"].value_counts()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=contagem.index, y=contagem.values, palette="magma")

    plt.title("Foco Temático: Principais Métricas Avaliadas", fontsize=16, pad=20)
    plt.xticks(rotation=15, ha="right")
    plt.ylabel("Frequência", fontsize=12)
    plt.xlabel("")

    salvar_grafico(plt.gcf(), "grafico_03_metricas.png")
    plt.close()


def plotar_geografia(df):
    """Gera gráfico da distribuição geográfica."""
    df_clean = df.dropna(subset=["Regiao"])
    contagem = df_clean["Regiao"].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(
        contagem.values,
        labels=contagem.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("pastel"),
    )

    plt.title("Distribuição Geográfica das Publicações", fontsize=16)

    salvar_grafico(plt.gcf(), "grafico_04_geografia.png")
    plt.close()


def main():
    print("--- Iniciando Análise Bibliométrica ---")
    try:
        df = carregar_dados(DATA_PATH)
        print(f"Dados carregados: {len(df)} registros brutos.")

        plotar_evolucao_anual(df)
        plotar_tipos_estudo(df)
        plotar_metricas(df)
        plotar_geografia(df)

        print("\nSucesso! Todos os gráficos foram gerados na pasta 'assets'.")
    except Exception as e:
        print(f"Erro crítico: {e}")


if __name__ == "__main__":
    main()
