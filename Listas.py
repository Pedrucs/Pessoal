Comida = ["Pizza", "Hamburger", "Strogonoff", "Hot Dog"] #Define uma lista, com seus índices e posições

print(Comida) #Mostra a matriz

Comida.insert("índice","Item") #Insere um item na lista
Comida.remove("Item")#Remove um item da lista
Comida.append("item")#Adiciona um item ao final da lista
Comida.pop("Item")#Remove o ultimo item da lista
Comida.sort()#Vai organizar a lista em ordem alfabética


for x in Comida:
    print(x)