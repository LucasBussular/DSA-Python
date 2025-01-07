# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

operacao = int(input('Selecione o número da operação desejada: \n'
                     '1 - Soma \n'
                     '2 - Subtração \n' 
                     '3 - Divisão \n' 
                     '4 - Multiplicação \n' 
                     'Digite o número da operação desejada: '))

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if operacao == 1:
    resultado = numero_1 + numero_2
    print('O resultado é: ', resultado)
elif operacao == 2:
    resultado = numero_1 - numero_2
    print('O resultado é: ', resultado)
elif operacao == 3:
    resultado = numero_1 / numero_2
    print('O resultado é: ', resultado)
else:
    resultado = numero_1 * numero_2
    print('O resultado é: ', resultado)