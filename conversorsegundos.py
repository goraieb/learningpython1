segundos_total = int(input("Digite a quantidade de segundo s a ser convertida: "))

dias = segundos_total // 86400

fracao_dias = segundos_total % 86400

horas = fracao_dias // 3600

fracao_minutos = fracao_dias % 3600

minutos = fracao_minutos // 60

segundos = fracao_minutos % 60

print(dias,"dias,",horas,"horas," ,minutos,"minutos e", segundos,"segundos.")
