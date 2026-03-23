# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Consumo-Consciente-green?style=for-the-badge)

## 🎯 Objetivo do Sistema
O objetivo deste projeto é ajudar os usuários a estimarem quanto um aparelho gasta de energia elétrica por mês, com base em dados simples de uso. O sistema também fornece uma estimativa de custo em Reais.

## 💻 Linguagem Usada
* Python

## 🧮 Fórmula Utilizada para o Cálculo
Para calcular o consumo mensal em Quilowatt-hora (kWh), utilizamos a seguinte matemática:
`consumoMensal = (potencia * horasDia * 30) / 1000`

Para o custo em Reais, o consumo mensal é multiplicado por uma tarifa fixa (neste projeto, R$ 0,75).

## 🚀 Instruções para executar o programa
1. Certifique-se de ter o Python instalado em seu computador.
2. Abra o terminal ou prompt de comando.
3. Navegue até a pasta do projeto (`consumo-energia`).
4. Execute o seguinte comando:
   `python app.py`
5. Siga as instruções na tela e digite os dados do seu aparelho.
