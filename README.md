# 📊 Data Visualization with Python
---

## About this project

This repository contains an example of how to create **interactive dashboards in Python** using **Streamlit** and **Plotly**.

The dashboard loads and filters car sales data by month, showing:

- 📅 Monthly billing per region (bar chart)
- 🏢 Company revenue shares (pie chart)
- ⚙️ Transmission type usage comparison (manual vs automatic)
- 💰 Evolution of the average price by region (line chart)
- 🚗 Top 5 best-selling vehicles (brand + model)

### 🚀 How it works

1. The app is built with **Streamlit**, a Python framework for building dashboards and data apps.
2. Data is read from a CSV file and transformed using **pandas**.
3. Visualizations are created with **Plotly Express** for interactivity and responsiveness.
4. The layout uses `st.columns()` to simulate a grid with multiple charts side by side.
5. User input is handled via a sidebar, allowing month selection.

### ▶️ How to run

Make sure you have Python installed. Then:

```bash
pip install streamlit pandas plotly
streamlit run index.py
```

---

## Sobre o projeto

Este repositório apresenta um exemplo de como criar **dashboards interativos em Python** utilizando **Streamlit** e **Plotly**.

O dashboard carrega e filtra dados de vendas de carros por mês, exibindo:

- 📅 Faturamento mensal por região (gráfico de barras)
- 🏢 Participação no faturamento por companhia (gráfico de pizza)
- ⚙️ Comparação do uso de câmbio manual vs automático (gráfico de barras)
- 💰 Evolução do preço médio por região (gráfico de linha)
- 🚗 Top 5 veículos mais vendidos (marca + modelo)

### 🚀 Como funciona

1. O app é feito com **Streamlit**, uma ferramenta Python para criar dashboards e aplicações de dados.
2. Os dados são lidos de um arquivo CSV e tratados com **pandas**.
3. Os gráficos são gerados com **Plotly Express**, garantindo interatividade.
4. O layout utiliza `st.columns()` para organizar os gráficos lado a lado.
5. A seleção do mês é feita via sidebar para filtrar os dados.

### ▶️ Como executar

Certifique-se de ter o Python instalado. Depois:

```bash
pip install streamlit pandas plotly
streamlit run index.py
```

---

📁 **Data source**: `./Data/Car Sales.xlsx - car_data.csv`  