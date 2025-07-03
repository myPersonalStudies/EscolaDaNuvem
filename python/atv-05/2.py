# Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.

from datetime import date;

def calcular_idade_em_dias(dia_nasc, mes_nasc, ano_nasc):

    data_nascimento = date(ano_nasc, mes_nasc, dia_nasc);
    data_hoje = date.today();
    idade_em_dias = (data_hoje - data_nascimento).days;

    return idade_em_dias;

dia = int(input('Que dia você nasceu? '));
mes = int(input('Que mês você nasceu? '));
ano = int(input('Que ano você nasceu? '));

print(calcular_idade_em_dias(dia, mes, ano), "dias");
