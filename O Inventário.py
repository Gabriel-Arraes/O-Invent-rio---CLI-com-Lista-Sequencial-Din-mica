import os 
def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

class Inventory:
    def __init__(self):
        self.maxCapacity = 6
        self.currentSize = 4
        self.List = ["Espada Flamejante", "Poção de Cura", "Manto de Invisibilidade", "Arco Élfico", None, None]
        
    def createNewMemorySequencial(self,capacity):
        return [None]* capacity
    
    def insertAt(self,data,position):
        if position < 0 or position > self.currentSize:
            return ("Posição inválida para inserir.")
        
        if self.currentSize == self.maxCapacity:
            print("A bolsa encheu !!, precisamos achar uma maior. (Realocando memória)")
            self.newCapacity = self.maxCapacity * 2
            self.newList = self.createNewMemorySequencial(self.newCapacity)
            
            for i in range (self.currentSize):
                self.newList[i] = self.List[i]
                
            self.List = self.newList
            self.maxCapacity = self.newCapacity
            
        for i in range(self.currentSize, position, -1):
            self.List[i] = self.List[i -1]
            
        self.List[position] = data
        self.currentSize = self.currentSize +1
        return self.List, self.currentSize, self.maxCapacity,"Item adicionado com Sucesso."

    def removeAt(self,position):
        if position < 0 or position >= self.currentSize:
            return ("Erro: posição invalida")
            
        for i in range(position, self.currentSize -1):
        
            self.List[i] = self.List[i + 1]
        self.currentSize = self.currentSize - 1                
        self.List[self.currentSize] = None
        return self.List, self.currentSize
            
            
bolsa = Inventory()


while True:
    cleaner()
    
    print("—————————————————————————————")
    print("        O INVENTÁRIO         ")
    print("—————————————————————————————")
    print(f"Carga:  {bolsa.currentSize}/{bolsa.maxCapacity} Slots Ocupados\n")
     
    for i in range(bolsa.maxCapacity -1):
        if i < bolsa.currentSize :
            print(f" [{i}] {bolsa.List[i]}")
        else:
            print(f" [{i}] • Vazio")
    print("\n————————————————————————————————")
    print("(1) Saquear | (2) Descartar | (3) Organizar | (0) Sair")
    
    action = input("Escolha uma ação: ")
    
    if action == '1':
        newItem = input("Qual item encontrou ? ")        
        bolsa.insertAt(newItem, bolsa.currentSize)
        print(newItem, "Está guardado na bolsa!")
        
    elif action == '2':
        try:
            positionTarget = int(input("Qual posição quer esvaziar ? "))
            positionTarget = bolsa.removeAt(positionTarget)
            print("Item foi descartado!")
        except ValueError:
            print("\n[Erro] Você precisa digitar um número inteiro.")
            
    elif action == '3':
        try:
            positionOld =int(input("Qual a posição atual do item que quer mover ? "))
            item = bolsa.List[positionOld]
            positionNew = int(input(f"Para qual posição quer mover '{item}'? " ))
            bolsa.removeAt(positionOld)
            bolsa.insertAt(item, positionNew)
            print("Item organizado com sucesso !")
        except ValueError:
            print("\n[Erro] Você precisa digitar um número inteiro.")
            
    elif action == '0':
        print("Fechando inventário....")
        break
    else:
        print("\n Ação desconhecida. Escolha uma opção válida!")

        
    input("Pressione Enter para continuar ....")           
        
        