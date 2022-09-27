from math import floor, ceil
from ExeEstSeq import questao2, questao3, questao4, questao5, questao6, questao7, questao8

# 1. Faça um Programa que mostre uma mensagem na tela.
print('--- Bem vindo a lista de atividades sequesciais ---')

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]."""
questao2()

# 3. Faça um Programa que peça dois números e imprima a soma.
questao3()

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
questao4()

# 5. Faça um Programa que converta metros para centímetros.
questao5()

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
questao6()

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
questao7()

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
questao8()

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
print('__Conversor de temperatura, Fahrenheit → Celsius.__')

tempF = int(input('Insira a temperatura em Fahrenheit: '))
convertidoC = (tempF - 32) / 1.8

print(f'A temperatura em {tempF}°F, representa aproximadamente {convertidoC:.0f}°C')

# 10. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1.1 o produto do dobro do primeiro com metade do segundo .
# 1.2 a soma do triplo do primeiro com o terceiro.
# 1.3 o terceiro elevado ao cubo.

print('-- Calculos diversos --')
numint1 = int(input('Digite um número: '))
numint2 = int(input('Digite outro número: '))
numfloat1 = float(input('Digite outro número: '))

calc1 = int((numint1 * 2) + (numint2 / 2))
calc2 = int((numint1 * 3) + numfloat1)
calc3 = numfloat1 ** 3

print(f'1.1 {calc1}\n1.2 {calc2}\n1.3 {calc3}')

# 11. + 12. Tendo como dado de entrada a altura e peso da pessoa, construa um algoritmo que calcule seu peso ideal para homens e mulheres:
altura = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso? '))
sexo = input('Qual o seu sexo? [M]asculino ou [F]eminino? ').upper()
resultado_imc = peso / altura**2

if resultado_imc <= 20 and sexo == 'M' or resultado_imc < 19 and sexo == 'F':
    print(f'Seu IMC está abaixo do normal, com {resultado_imc}')
elif resultado_imc <= 24.9 and sexo == 'M' or resultado_imc < 23.9 and sexo == 'F':
    print(f'Seu IMC está normal, com {resultado_imc}')
elif resultado_imc <= 29.9 and sexo == 'M' or resultado_imc < 28.9 and sexo == 'F':
    print(f'Seu IMC está Obsidade leve, com {resultado_imc}')
elif resultado_imc <= 39.9 and sexo == 'M' or resultado_imc < 38.9 and sexo == 'F':
    print(f'Seu IMC está Obsidade moderada, com {resultado_imc}')
elif resultado_imc <= 42.9 and sexo == 'M' or resultado_imc >= 39 and sexo == 'F':
    print(f'Seu IMC está Obsidade mórbida, com {resultado_imc}')
else:
    print('Por favor, procure um médico.')


# 13. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peixe = float(input('Qual o peso do peixe? '))

if peixe > 50:
    excesso_de_peso = peixe - 50
    multa = excesso_de_peso * 4
    print(f'A multa por peso excedido é de R${multa:.2f}')
else:
    print('O peso do peixe está dentro do regulamento do estado.')

# 14. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 1.1 salário bruto.
# 1.2 quanto pagou ao INSS.
# 1.3 quanto pagou ao sindicato.
# 1.4 o salário líquido.
# 1.5 calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto - IR_11%: - INSS_8% - Sindicato_5%: = Salário Liquido
print('--Calculo básico de salário--')

salario = int(input('O valor do salário? '))
horas_trabalhadas = int(input('Quantidade de horas trabalhadas no mês? '))
valor_hora = salario / horas_trabalhadas
salario_inss = salario - (salario * 0.11)
salario_ir = salario_inss - (salario_inss * 0.08)
salario_sindicato = salario_ir - (salario_ir * 0.05)
salario_liquido = salario_sindicato - (salario * 0.3)

print('----------------------------')
print(f'Valor do salário: {salario}')
print(f'Inss: {salario * 0.11}')
print(f'IR: {salario_inss * 0.08}')
print(f'Sindical: {salario_ir * 0.05:.2f}')
print(f'Pensão: {salario * 0.3}')
print(f'Salario liquido: {salario_liquido:.2f}')

# 15. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area_para_pintar = int(input('Quantos metros quadrados precisam ser pintados? '))
litro_tinta = int(area_para_pintar / 3)
print(f'Quantidade de litros a ser usada: {litro_tinta:.0f}L')

if area_para_pintar/3 <= 18:
    print(f'Será necessário 1 lata de tinta para os {area_para_pintar}m²')
elif area_para_pintar/3 > 18:
    print(f'Serão necessárias 2 latas de tinta para os {area_para_pintar}m²')
elif area_para_pintar/3 > 18*2:
    print(f'Será necessário 2 Lata de tinta para os {area_para_pintar}m²')

# 16. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00 ou em galões de 3,6 litros, que custam R\$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1.1 comprar apenas latas de 18 litros;
# 1.2 comprar apenas galões de 3,6 litros;
# 1.3 misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_a_pintar = int(input('Quantos metros quadrados precisam ser pintados? '))
lata = 18
galao = 3.6
valor_lata = 80
valor_galao = 25
litro_tinta = ceil(area_a_pintar / 6)
litro_tinta_galao = floor(3.6 * 6)
print(f'Quantidade de litros a ser usada: {litro_tinta:.0f}L')

if litro_tinta <= lata:
    print(
        f'Será necessário 1 lata de tinta para os {area_a_pintar}m² por R$ {valor_lata}')
elif litro_tinta <= lata*2:
    print(
        f'Serão necessárias 2 latas de tinta para os {area_a_pintar}m² por R$ {valor_lata*2}')
elif litro_tinta > lata*2:
    print(
        f'Será necessário 3 Lata de tinta para os {area_a_pintar}m² por R$ {valor_lata*3}')
else:
    print('Insira uma área válida')

if area_a_pintar <= litro_tinta_galao:
    print(f'Ou se preferir pode comprar 1 galão de 3,6L por R$ {valor_galao}')
elif area_a_pintar <= litro_tinta_galao*2:
    print(
        f'Ou se preferir pode comprar 2 galão de 3,6L por R$ {valor_galao*2}')
elif area_a_pintar <= litro_tinta_galao*3:
    print(
        f'Ou se preferir pode comprar 3 galão de 3,6L por R$ {valor_galao*3}')
elif area_a_pintar > litro_tinta_galao*3:
    print(
        f'De 63m² a 84m² 4 galões(R$ {valor_galao*4}), de 84m² a 105m² 5 galões(R$ {valor_galao*5}). Acima de 63m² é melhor uma Lata de 18L R$ {valor_lata}')

# 17. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = int(
    input('Qual o tamanho do arquivo que pretende baixar em Mbs? '))
velocidade = 100
tamanho_arquivo_velocidade = tamanho_arquivo / velocidade
mega_por_min = tamanho_arquivo_velocidade / 60  # Por minuto
mega_por_seg = tamanho_arquivo_velocidade % 60  # Excedente nos segundos


print(
    f'O arquivo a ser baixado tem {tamanho_arquivo}Mb, a velocidade da internet é de {velocidade}Mb/m, levará {mega_por_min:.0f} minuto(s) e {mega_por_seg} segundo(s)')
