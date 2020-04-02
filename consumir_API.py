import requests, xlsxwriter

"""
	Dado el API de random user, obtener cien usuarios diferentes y almacenarlos en un archivo .xls (Una hoja de excel).

	El archivo debe poseer una sola hoja con 4 columnas (Genero, nombre completo, email y edad)
	Los usuarios deben estar ordenados por edad de forma descendente.
	El archivo debe tener por nombre usuarios.xls.
"""

def clearData(users):
	rows =[]
	i=0	
	# print('')
	for user in users:
		gender =  user['gender']
		full_name= user['name']['title']+' '+ user['name']['first']
		email = user['email']
		age_u = user['dob']['age']
		
		rows.append([ gender , full_name,email ,age_u ])
		i+=1
	 
		# print(gender+'\t'+ full_name+ ' \t'+ email  )
		pass
	createFile(rows)

	pass
def createFile(obj):
	row=0
	col=0
	
	workbook = xlsxwriter.Workbook('usuarios.xlsx')
	worksheet = workbook.add_worksheet()
	
	cell_format = workbook.add_format({'bold': True })
	worksheet.write(row, 0, 'genero',cell_format)
	worksheet.write(row, 1, 'nombre completo',cell_format)
	worksheet.write(row, 2, 'email',cell_format)
	worksheet.write(row, 3, 'edad',cell_format)

	for n in (obj):
		row+=1
		worksheet.write(row, col, n[0])
		worksheet.write(row, col+1, n[1])
		worksheet.write(row, col+2, n[2])
		worksheet.write(row, col+3, n[3])
		pass

	workbook.close()
	pass

if __name__=='__main__':
	url = 'https://randomuser.me/api/'
	payload = { "results": 20}
	
	response = requests.get(url,params=payload)
	
	if response.status_code==200:
		obj= response.json()
		data = obj.get('results', [])
		clearData(data)
		pass