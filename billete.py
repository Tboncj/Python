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
	nwm = float( input('\nIngrese el monto: ') )
	nwm = nwm + float(ma)
	return nwm
	pass
def getOption():
	return input("Seleccione un tipo de usuario: ")
	pass
def getAskforCharge():
	ask =  input('\nDesea abonar a su saldo (S/N)? ')

	while not ask in ['S','N','n','s']:
		ask =  input('Desea abonar a su saldo (S/N)? ')
		pass

	return ask

	pass
def getDestiny():
	print('')
	 
	print('')
	for x in to_place:
		print('\t',x,'-',to_place[x])
		pass
	print ()
	dst = input('\nIndique el destino: ')
	while not dst in to_place:
		dst = input('Indique el destino: ')
	pass
	return dst
	pass
def getTableOptions():
  	#  				   Punta(P) 	Valle(V) 	Bajo(B) 
	# Adulto 		(A) 	740 		660 	610 
	# Estudiante    (E) 	210 		210 	210 
	# Adulto Mayor  (M) 	210 		210 	210

	table = {
				'AP':740, 'AV':660, 'AB':610,
				'EP':210, 'EV':210, 'EB':210,
				'MP':210, 'MV':210, 'MB':210
			}

	mopt = opc + selec_dest 

	return table[ mopt ]

	pass
def clear():
	os.system ("cls")
	os.system ("clear")
	
	if os.name == "posix":
	   os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
	   os.system ("cls")
	pass
def getResume(act):
	act_credit =act
	clear()

	print('\n\n------------------------------')
	print('\n\nSaldo Actual \t:' ,act_credit)
	print('Tipo de Usuario :',typeUser[opc])
	print('Destino \t:', to_place[selec_dest] )
	print('Costo   \t:', cost)
	if float(act_credit)>float(cost):
		saldo_final = float(act_credit)-float(cost)
		print("\nSaldo Final \t: ", saldo_final )
		pass

	print('\n\n------------------------------')
	if float(act_credit) < float(cost):
		validatemontos(act_credit)
		pass
	pass
def validatemontos(act_credit):
	
	gask = getAskforCharge()
	if  gask.upper()=="S":
		act_credit = setCharge(act_credit)
		getResume(act_credit)
	else:
		print('\nTu saldo ha sido retenido')
		print('saldo Final : 0.0')
		
	pass




#prueba de escritorio
clear()

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
cost = getTableOptions()

getResume(act_credit)

# validatemontos(act_credit,cost)

print( "")

