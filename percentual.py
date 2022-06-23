
sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953

lista = [sp, rj, mg, es, outros]
total_faturamento = sum([x for x in lista])


def calcula_percentual(cidade):
    percentual = (cidade * total_faturamento) / 100
    return percentual


porcentagem_sp = calcula_percentual(sp)
porcentagem_rj = calcula_percentual(rj)
porcentagem_mg = calcula_percentual(mg)
porcentagem_es = calcula_percentual(es)
porcentagem_outros = calcula_percentual(outros)
