
print("--- Calculadora de Consumo Elétrico ---")

# 1. Coletando os dados do usuário
nome_aparelho = input("Digite o nome do aparelho: ")
# Usamos float() para permitir números com vírgula (decimais)
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# 2. Calculando o consumo mensal em kWh usando a fórmula fornecida
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Dica: Adicionando o cálculo de custo estimado (R$ 0,75 por kWh)
tarifa_kwh = 0.75
custo_estimado = consumo_mensal * tarifa_kwh

# 3. Mostrando o resultado formatado na tela
print("\n--- Resultado ---")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} por mês")