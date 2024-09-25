numero = input("Digite um número para a tabuada: ")
for i in range(1,11): #Em (z,y), y sempre será y-1. Nesse caso, 11-1=10
    print(numero + " x " + str(i) + " = " + str(i*int(numero)))