# print ("") = Mostra uma mensagem na tela, mas somente dentro das aspas simples ou duplas
print("Olá mundo! Or if you preffer, Hello World!")

# variáveis = variável representa um valor, se definir algo como variável, ela se apresenta como tal

print(type('variável')) # função type mostra o tipo da variável

#string
#str = string: é uma série de caracteres
primeiro_nome = 'Pedro Henrique'
segundo_nome = 'Muniz Araujo'
nome_completo = primeiro_nome + segundo_nome

#print("Olá", nome_completo)

#int
#int = integer ou inteiro: valores numéricos inteiro
idade = 18 #valores numéricos não usam aspas, tudo que tiver dentro de aspas é considerado string
idade += 1
print("Sua idade é: "+str(idade)) #para juntar uma string com um outro tipo de dado, precisa fazer a concatenação com o +str
print(type(idade))

#float
#float = representa numeros decimais
altura = 1.78
print("Sua altura é: "+str(altura)+"m")
print(type(altura))


#boolean
#boolean = um dado verdadeiro ou falso

humano = True
print("Ser humano é: "+str(humano)) 
#print(type(humano))

#OS 4 TIPOS BÁSICOS DE DADOS 
#str = string: é uma série de caracteres
#int = integer ou inteiro: valores numéricos do tipo inteiro
#float = representa numeros decimais
#boolean (booleano) = um dado verdadeiro ou falso