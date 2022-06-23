import json

with open("dados.json") as dados:
    dados = json.load(dados)

vetor = []
for v in dados:
    vetor.append(v['valor'])

# Filtrando os finais de semana
filtrando_fim_de_semana = list(filter(lambda x: x > 0, vetor))

# Obtendo o menor valor faturado
menor_valor_faturado = min(filtrando_fim_de_semana)

# Obtendo o maior valor faturado
maior_valor_faturado = max(filtrando_fim_de_semana)


# Obtendo a média do faturamento
media_faturamento = sum(filtrando_fim_de_semana) / len(filtrando_fim_de_semana)

# Obtendo a quantidade de dias que o valor diario foi maior que a média
valor_diario_maior_que_media = len(list(
    filter(lambda x: x > media_faturamento, filtrando_fim_de_semana)))
