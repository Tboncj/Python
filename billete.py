import os

typeUser = {'A':'ADULTO', 'E':'ESTUDIANTE', 'M':'MAYOR'}
to_place = {'P':'PUNTA', 'B':'BAJO', 'V':'VALLE'}
act_credit = 0


def menu():
	print('Sistema de tickets')
	print('')
	for x in typeUser:
		print('\t',x,'-',typeUser[x])
		pass
	print ()
	pass
def setSaldo():
	return input("Digite el monto actual del boleto: ")
	pass
def setCharge(ma):
	nwm = cfloat( input('Ingrese el monto: ') )
	nwm = nwm + ma
	return nwm
	pass
def getOption():
	return input("Seleccione un tipo de usuario: ")
	pass
def clear():
	os.system ("cls")
	os.system ("clear")
	
	if os.name == "posix":
	   os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
	   os.system ("cls")
	pass

menu()
opc = getOption()

while not opc in typeUser:
	clear()
	menu() 
	opc = getOption()
	pass

act_credit = setSaldo()
print('Saldo Actual: ' ,act_credit)



print( "BY")
