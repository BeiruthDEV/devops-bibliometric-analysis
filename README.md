# Análise Bibliométrica: Engenharia de Software Contínua & Experimental

<p align="center">
  <img src="assets/logo-vassouras.png" alt="Universidade de Vassouras" width="250"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Data%20Analysis-Pandas%20%7C%20Seaborn-orange.svg" alt="Data Science">
  <img src="https://img.shields.io/badge/Status-Concluído-green.svg" alt="Status">
</p>

---

## 🎯 Visão Geral

Este projeto consiste em uma análise técnica e bibliométrica sobre a interseção entre práticas modernas de **DevOps (Engenharia de Software Contínua)** e métodos de validação científica **(Engenharia de Software Experimental)**.

Através da análise de **17 artigos-chave publicados entre 2015 e 2022**, o projeto busca responder: *Como a indústria está validando empiricamente a aceleração dos ciclos de desenvolvimento?*

O repositório contém:
1. **Análise Teórica:** Síntese dos conceitos de CI/CD, Experimentos Controlados e DevSecOps.
2. **Pipeline de Dados:** Scripts em Python para processamento dos metadados dos artigos.
3. **Visualização de Dados:** Gráficos gerados automaticamente que revelam tendências da indústria.

---

## 📊 Insights dos Dados

Os gráficos abaixo foram gerados programaticamente pelo script `src/analysis.py` a partir do dataset consolidado.

### 1. Aceleração da Produção Científica
Nota-se um aumento consistente no interesse pelo tema, correlacionado com a adoção massiva de Kubernetes e microsserviços na indústria a partir de 2018.

![Evolução Anual](assets/grafico_01_evolucao_anual.png)

### 2. Metodologias Predominantes
A análise revelou que a área ainda é dominada por **Estudos de Caso**. Isso indica que a Engenharia de Software Contínua ainda é fortemente dependente do contexto específico de cada empresa, dificultando a criação de "leis gerais" (validade externa), mas fornecendo insights práticos valiosos.

![Metodologias](assets/grafico_02_metodologia.png)

### 3. O que está sendo medido?
As empresas não buscam apenas "velocidade". Os dados mostram que **Qualidade e Desempenho** são tão vitais quanto a produtividade, refutando a ideia de que DevOps sacrifica qualidade por rapidez.

![Métricas](assets/grafico_03_metricas.png)

---

## 📚 Fundamentação Teórica

A análise dos artigos permitiu identificar três pilares na relação entre Indústria e Academia:

1. **O Paradigma da Engenharia Contínua (ESC)**
   - Práticas de *Continuous Integration* (CI) e *Continuous Delivery* (CD) transformaram o desenvolvimento em um fluxo constante de valor.
   - **Desafio encontrado:** Resistência cultural e complexidade na gestão de configurações.

2. **O Papel da Engenharia Experimental (ESE)**
   - Uso de métodos rigorosos (experimentos controlados, surveys) para validar se uma nova ferramenta (ex: Docker) realmente traz ganho de performance.
   - **Laboratórios Vivos:** Ambientes de DevOps instrumentados servem como fonte rica de dados para análise em tempo real.

3. **Lacunas de Pesquisa**
   - Falta de estudos longitudinais (longo prazo).
   - Necessidade de maior foco em **DevSecOps** e fatores humanos na automação.

---

## 🛠️ Estrutura do Projeto

```bash
/
├── assets/                # Gráficos gerados e imagens
├── data/                  # Dataset bibliométrico (CSV)
├── papers/                # Artigos originais analisados (PDF)
├── src/                   # Código fonte de análise
│   └── analysis.py        # Script de processamento e visualização
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação principal
```

## 🚀 Como Executar
Para reproduzir as análises e gerar os gráficos em sua máquina:

Clone o repositório:

```bash

git clone [https://github.com/beiruthdev/p1-engenharia-de-software-cont-nua-e-experimental.git](https://github.com/beiruthdev/p1-engenharia-de-software-cont-nua-e-experimental.git)
cd p1-engenharia-de-software-cont-nua-e-experimental
```

Instale as dependências:

```bash

pip install -r requirements.txt
```

Execute o script de análise:
```bash


cd src
python analysis.py
```
Os arquivos PNG serão atualizados na pasta assets.

👨‍🎓 Autor
Matheus Beiruth Engenharia de Software @ Universidade de Vassouras

Este projeto foi desenvolvido como parte da avaliação da disciplina de Engenharia de Software Contínua e Experimental.
