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
def setAskforCharge():
	ask =  input('Desea abonar a su saldo (S/N)?')

	while not ask in ['S','N','n','s']:
		ask =  input('Desea abonar a su saldo (S/N)?')
		pass

	return ask

	pass
def getDestiny():
	print('')
	print('\tP - PUNTA')
	print('\tV - VALLE')
	print('\tB - BAJO')
	dst = input('\nIndique el destino: ')
	while not dst in to_place:
		dst = input('Indique el destino: ')
	pass
	return dst
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

selec_dest = getDestiny()
clear()
print('\n\n------------------------------')
print('\n\nSaldo Actual \t:' ,act_credit)
print('Tipo de Usuario :',typeUser[opc])
print('Destino \t:', to_place[selec_dest] )

print('\n\n------------------------------')


print( "")
