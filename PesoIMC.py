Peso = float(input("Digite o seu peso em quilos: "))
altura = float(input("Digite sua altura em metros:  "))
imc  = Peso/(altura*altura)

print("Seu índice de Massa corporal é: ", str(imc))

if imc<18.5:
    print("Abaixo do Peso")
    
elif imc>18.6 and imc <24.9:
    print("Peso Ideal (Boa campeão)")
    
elif imc>25.0 and imc <29.9:
    print("Levemente acima do Peso")
    
elif imc>30.0 and imc <34.9:
    print("Obesidade Grau 1")
    
elif imc>35.0 and imc <39.9:
    print("Obesidade Severa grau 2")
    
if imc>40:
    print("Obesidade mórbida GRAU 3")