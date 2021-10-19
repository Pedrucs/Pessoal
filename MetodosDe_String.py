#Aqui veremos os métodos que podem ser usados para a variável string

nome = "pedro henrique muniz araujo"

print(len(nome)) #len = length, vai retornar o tamanho da nossa string, incluindo espaços vazios
print(nome.find()) #find = vai procurar a caractere digitada
print(nome.capitalize()) #capitalize = Deixa o primeiro caractere da sua string em maiúsculo
print(nome.upper()) # upper = deixa toda sua string em maiúsculo
print(nome.lower()) # lower = deixa toda sua string em minúsculo
print(nome.isdigit()) # isdigit = vai retornar se é verdadeiro ou falso se a string for um dígito, por exemplo 123
print(nome.isalpha()) # isalpha = vai retornar se a sua string contém apenas letras do alfabeto
print(nome.count()) # count = conta quantas caracteres contém na sua string
print(nome.replace("", "")) # replace = substitui um caractere da string

#bonus = retornar a string várias vezes
print(nome*3)
