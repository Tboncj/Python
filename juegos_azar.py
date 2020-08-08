import os, time, random

class Juego(object):
    def __init__(self):
        self.balance = 0
    
    def validateopc(self):
        opc = input("\nSeleccione una opción: ")
        try:
            opc = int(opc)
            if opc > 0 and opc <= 4:
                return opc
            else:
                opc = self.validateopc()
        except ValueError:
            print("Error, opcion no disponible")
            self.imprimirmenu()
    
    def abonarSaldo(self):
        mount = input("Ingrese monto: ")
        try:
            mount = float(mount)
            self.balance += mount
            self.imprimirmenu()
        except ValueError:
            self.abonarSaldo()

    def takeMoney(self):
        os.system("cls")
        print("Saldo actual: ", self.balance)
        mount = input("\nMonto a retirar: ")
        try:
            cash = float(mount)
            if cash>self.balance:
                print("\nError: Saldo insuficiente")
                print("espere..")
                time.sleep(2)
                self.imprimirmenu()
            else:
                self.balance = self.balance-cash
                print("Saldo actual: ", self.balance)
                time.sleep(1)
                self.imprimirmenu()

        except ValueError:
            self.takeMoney()
    
    def consecutive(self, row):
        #devuelve tru si es consecutivo
        is_cons = False
        a = row[0]
        b = row[1]
        c = row[2]
        if a<b<c:
            is_cons = True
        return is_cons
            
    def getConsecutive(self, cols):
        lft = self.consecutive(cols)
        rgt = self.consecutive(cols[::-1])
        if lft:
            return lft
        else:
            return rgt
            
    def getpremio(self, jugada, tip):
        premios = {'X1':500, 'X3':1000, 'X5':5000, 'X7':7000}
        if jugada:
            premio = premios[tip]
            self.balance = self.balance+premio
            print("\nFelicidades has ganado")
            print("Tu premio: ",premio)
        else:
            print("\nLo siento perdiste")

    def getDiagonal(self,sdk):
        d1 = [sdk[0][0], sdk[1][1], sdk[2][2]]
        d2 = [sdk[0][2], sdk[1][1], sdk[2][0]]

        tnc = self.getConsecutive(d1)
        if tnc:
            return tnc

        tnc = self.getConsecutive(d2)
        if tnc:
            return tnc
        return False

    def getColumns(self, sdk):
        d1 = [sdk[0][0], sdk[1][0], sdk[2][0]]
        d2 = [sdk[0][1], sdk[1][1], sdk[2][1]]
        d3 = [sdk[0][2], sdk[1][2], sdk[2][2]]

        tnc = self.getConsecutive(d1)
        if tnc:
            return tnc

        tnc = self.getConsecutive(d2)
        if tnc:
            return tnc
        
        tnc = self.getConsecutive(d3)
        if tnc:
            return tnc
        return False

    def rulesGame(self,sdk, tip):        
        if tip=="X1":
            tnc = self.getConsecutive(sdk[1] )
        if tip == "X3":
            for i in sdk:
                tnc = self.getConsecutive(i)
                if tnc:
                    break
        if tip == "X5":
            for i in sdk:
                tnc = self.getConsecutive(i)
                if tnc:
                    break
            if tnc == False:
                tnc = self.getDiagonal(sdk)
        if tip=="X7":
            for i in sdk:
                tnc = self.getConsecutive(i)
                if tnc:
                    break
            tnc = False
            if tnc == False:
                tnc = self.getColumns(sdk)

            if tnc == False:
                tnc = self.getDiagonal(sdk)

        self.getpremio(tnc, tip)

    def juego(self, bet, tip ):
        os.system("cls")
        print("Tu apuesta por: ", bet)
        a = [[random.randrange(9) for i in range(3)] for j in range(3)]
        for i in a:
            print("\t",i)
        self.rulesGame( a, tip)
        time.sleep(8)
        self.imprimirmenu()
    
    def compareBalance(self, apos):
        if self.balance<apos:
            return False

        return True

    def apostar(self):
        os.system("cls")
        print("Seleccione el nivel de apuesta:")
        print("\n\t1.- X1\n\t2.- X3\n\t3.- X5\n\t4.- X7\n\t5.- Regresar")
        opc = int(input("\nElija una opción: "))
        
        apuestas=[0,100,300,500,700]
        premios =['X', 'X1', 'X3', 'X5', 'X7']
        
        next_opc = self.compareBalance(apuestas[opc])
        if next_opc==False:
            os.system("cls")
            print("\nError: no cuentas con saldo para apostar\nEspere...")
            time.sleep(3)
            self.imprimirmenu()
        #Actualizamos el saldo
        self.balance =  self.balance - apuestas[opc]

        if opc>0 & opc<=4:
            self.juego( apuestas[opc], premios[opc] )

        if opc ==5 :
            self.imprimirmenu()

    def imprimirmenu(self):
        os.system("cls")
        print("\n1.- Ingresar Dinero\n2.- Jugar\n3.- Retirar Dinero\n4.- Salir")
        opc = self.validateopc()
        if opc == 1:
            self.abonarSaldo()
        if opc == 2:
            self.apostar()
            
        if opc == 3:
            self.takeMoney()
        if opc == 4:
            os.system("cls")
            print("Adios")

Play = Juego()
Play.imprimirmenu()