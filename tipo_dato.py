 
def tipo_de_dato(dato,tipo=''):
    _tipo="desconocido"

    if isinstance (dato, str):
      _tipo = "str"
        
    if isinstance (dato, int): 
      _tipo = "int"

    if isinstance (dato, float): 
      _tipo = "float"

    if isinstance (dato, bool): 
      _tipo = "bool"

    msg= "\t {0}\t es del tipo\t {1}".format(dato,_tipo)
    return msg

# res = tipo_de_dato( 23 )
# print(res)
print("")
print( tipo_de_dato( 23 ) )
print( tipo_de_dato( 23.23 ) )
print( tipo_de_dato( False ) )
print( tipo_de_dato( 'Hola' ) )