#Anny Carolina Andrade Dias - RM:98295
#Luana Cabezaolias - RM:99320

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))


#Separando e validando os digitos so numero1
digito1 = numero1 // 10

resto1 = numero1 % 10
digito2 = resto1 // 1

resultado1 = digito1 if digito1 != 7 else 0 
resultado2 = digito2 if digito2 != 7 else 0

soluçao1 = (resultado1 * 10) + resultado2


#Separando e validando os digitos so numero2
digito3 = numero2 // 10

resto2 = numero2 % 10
digito4 = resto2 // 1

resultado3 = digito3 if digito3 != 7 else 0 
resultado4 = digito4 if digito4 != 7 else 0

soluçao2 = (resultado3 * 10) + resultado4


#Somando e validando o resultado 
soma = soluçao1 + soluçao2

a = soma // 10 
resto = soma % 10
b = resto // 1

resultadoA = a if a != 7 else 0 
resultadoB = b if b != 7 else 0 

print(f"A soma de {numero1} e {numero2} é {resultadoA}{resultadoB}")









