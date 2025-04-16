def salario(salario, comissao, inss):
    tcomissao = salario + (comissao*salario)
    tinss = salario - (salario*inss)
    total = tcomissao - tinss

    return round (total, 2) 
    