#alfabeto de referencia o canónico
_ALFABETO_ = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª'

#__________________________________________________MÁQUINA ENGIMA_CONFIGUARCIÓN_DEFECTO__________________________________________#


rotor_I = {
	"nombre": "ROTOR_I",

	"giro" : "E",

	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª'),

	"conexiones" : 
		{
			'r': 'O', 'º': '!', 'V': 'T', 'I': 'Y', '8': 'g', 'ª': 'W', 'd': 'ñ', '5': 'r', 't': '+', 'O': 'P', '¿': 'Ñ', '6': 'f',
			'>': 'G', 's': '&', 'y': '2', '<': 'K', 'J': ']', '2': 'u', 'C': '[', '!': 'n', 'Y': '5', 'i': 'L', 'z': 'B', '-': 'q',
			',': '¡', 'Ñ': '<', '1': 'J', '.': 'm', '?': '?', '¡': 's', 'm': 'E', 'T': 'M', 'K': '*', 'f': ';', 'ñ': 'o', 'v': 'h',
			'Q': 'y', 'F': 'z', '%': 'Z', ':': '=', 'R': '_', ']': '3', '+': 'X', 'q': 'I', 'X': 'V', 'k': ',', 'P': 'p', 'u': '8',
			'c': '.', 'S': 'e', 'h': 'l', '_': 'º', 'e': 'b', '[': '1', 'B': '%', 'Z': '-', 'D': '#', '3': 'a', '=': 'i', 'a': 'd',
			'*': ':', 'n': 'w', 'w': 't', 'b': '¿', 'H': 'F', '0': '@', 'l': 'U', '@': '9', '4': 'R', '&': 'H', 'A': 'C', '7': '>',
			'U': 'N', 'x': 'c', 'G': 'x', '9': '0', 'L': 'k', 'j': 'ª', ';': 'A', 'p': 'v', 'E': '6', 'N': '7', '#': '4', 'M': 'S',
			'W': 'Q', 'o': 'D', 'g': 'j'
		},

	"conexiones_sim" : None,

	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª')

}

rotor_II = {
	"nombre": "ROTOR_II",

	"giro" : "M",

	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª'),

	"conexiones" : 
		{
			'%': 'D', '*': 'p', 'G': '7', '¿': 'A', '.': '@', 'x': 'j', 'ñ': '*', 'B': 'ª', 'A': '<', 'w': 'N', 'N': 'i', '¡': '5',
			'@': '_', 'h': 'Y', 'P': 'a', 'n': 't', 'e': '¡', ',': 'C', 'a': 'V', '0': '8', 'u': 'G', 'Y': ';', 'o': 'k', '2': 'W', 
			'º': 'B', '6': 'l', 'F': 'n', 'Z': 'M', '<': '6', ':': 'd', '7': 'E', 'j': 'Z', 'g': '¿', 'L': '>', 'H': 'e', 'E': ',', 
			'v': 'O', '4': ']', 'T': 'F', ']': 'S', '8': 'u', 'y': '4', '=': 'I', '>': 'h', 'X': 'z', 'S': '.', 'r': 'o', '!': 'w',
			'K': '+', 'V': '-', 'R': 'T', '5': '%', '-': 'g', '3': 'º', '#': 'H', 'M': 'ñ', 'b': 'c', 'Ñ': '&', 'O': 's', 'J': '=',
			'm': '1', 'l': 'U', 'c': 'v', '[': 'r', '9': '#', 't': 'R', ';': '[', 'ª': 'q', '&': '?', 'k': 'J', 'p': 'Ñ', 'q': 'Q',
			'D': 'L', 'z': 'X', 'I': 'b', 's': 'x', 'i': 'P', 'U': 'f',	'd': 'm', 'W': ':', '_': '0', '1': 'K', '+': '3', 'f': '2',
			'Q': '!', 'C': '9', '?': 'y'
		},

	"conexiones_sim" : None,

	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª')
}

rotor_III = {
	"nombre" : "ROTOR_III",

	"giro" : "T",

 	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª'),

 	"conexiones" : 
 		{
 			'w': 'F', 'l': 'R', '9': 'V', 'T': 'y', 'z': ',', 'm': 'n', '<': '>', '5': 'ª', 'E': 'Q', ']': '+', 'Ñ': 'p', 'F': 'M',
 			'd': 'P', 'O': '*', 'u': 'J', '4': '<', 'X': '[', 'p': ';', '*': 'O', 'Y': '¿', '_': '?', 'P': 'd', '7': '5', 'y': 'k',
 			'J': 'W', 'x': '-', '-': 'h', 'G': 'X', 'q': '6', 'B': '!', 'r': '¡', 't': 'S', 'D': 'e', '1': '=', 'C': '_', 'k': '0',
 			'º': ']', 'ñ': 'Z', 'H': 'j', 'S': 'l', 'h': 'Y', 'v': ':', '0': 'A', '?': 't', '>': '7', '¡': 'c', ';': 'm', '%': 'D',
 			'o': '9', '&': 'T', 'L': 'u', '[': 'i', 'Q': 'o', 'I': 'v', 'U': 'q', '#': 'f', 'e': '#', 'n': '%', 'a': 'U', 'f': 's',
 			'6': 'H', 's': '.', 'V': 'ñ', 'R': 'G', 'A': 'C', '.': '4', '2': '2', 'i': 'E', 'W': 'º', 'K': 'a', 'b': 'x', 'g': '&',
 			'M': 'L', 'ª': 'B', 'j': 'w', '¿': 'I', '@': 'b', '!': 'Ñ', '8': 'z', 'Z': '8', ',': 'N', 'N': '@', '3': 'g', '=': 'K',
 			':': '3', '+': '1', 'c': 'r'
 		},

 	"conexiones_sim" : None,

 	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª')
 }


"""
El reflector proporciona la simetria al sistema, es un elemento único de Enigma. 
"""
RFL ={
		'A': 'ª', 'B': 'º', 'C': '-', 'D': '=', 'E': '*', 'F': '+', 'G': ']', 'H': '[', 'I': '>', 'J': '<', 'K': ';', 'L': ':',
		'M': ',', 'N': '.', 'Ñ': '¡', 'O': '!', 'P': '?', 'Q': '¿', 'R': '%', 'S': '&', 'T': '#', 'U': '@', 'V': '_', 'W': '9',
		'X': '8', 'Y': '7', 'Z': '6', 'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0', 'g': 'z', 'h': 'y', 'i': 'x',
		'j': 'w', 'k': 'v', 'l': 'u', 'm': 't', 'n': 's', 'ñ': 'r', 'o': 'q', 'p': 'p', 'q': 'o', 'r': 'ñ', 's': 'n', 't': 'm',
		'u': 'l', 'v': 'k', 'w': 'j', 'x': 'i', 'y': 'h', 'z': 'g', '0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a',
		'6': 'Z', '7': 'Y', '8': 'X', '9': 'W', '_': 'V', '@': 'U', '#': 'T', '&': 'S', '%': 'R', '¿': 'Q', '?': 'P', '!': 'O',
		'¡': 'Ñ', '.': 'N', ',': 'M', ':': 'L', ';': 'K', '<': 'J', '>': 'I', '[': 'H', ']': 'G', '+': 'F', '*': 'E', '=': 'D',
		'-': 'C', 'º': 'B', 'ª': 'A'
	}

#			--------------------------------	
plugboard = {'A':'K', 'G':'X', 'W':'P', 'E':'Ñ', 'K':'A', 'X':'G', 'P':'W', 'Ñ':'E'}
#											      ----------------------------------	

#	A G W E  K X W P
#   K X W P  A G W E


#_______________________________________________________________________________________________________________________________#





def crear_conexiones_sim(rotor): 
	rotor['conexiones_sim'] = dict(list(zip(rotor['conexiones'].values(), rotor['conexiones'].keys())))

crear_conexiones_sim(rotor_I)
crear_conexiones_sim(rotor_II)
crear_conexiones_sim(rotor_III)

"""
Representa el conjunto de rotores que van a utilizarse, pueden cambiarse de orden y añadir todos los que se quieran.
"""
_ROTORES_ = [rotor_I, rotor_II, rotor_III]
 
"""
 l_in:  letra 
 plug: plugboard
"""
def check_plug(l_in, plug):
	if l_in in plug :
		return list(_ALFABETO_).index(plug[l_in])
	return list(_ALFABETO_).index(l_in)


def config_plug(cnx_i, cnx_o):
	global plugboard
	l_cnx_i = list(cnx_i) + list(cnx_o)
	l_cnx_o = list(cnx_o) + list(cnx_i)
	plugboard = dict(zip(l_cnx_i, l_cnx_o))

"""
Recibe un entero que sirve como indice para obtener la letra que se quiere reflectar (r),
Devuelve un entero que sirve como indice para identificar la letra reflectada con facilidad en el alfabeto canónico.
""" 
def reflectar(i):
	r = RFL[_ALFABETO_[i]]
	return list(_ALFABETO_).index(r)

"""
Característica básica de un rotor. Consiste en un desplazamiento simple hacia la derecha
Para un alfabeto canónico sería lo siguiente: 'ABCDEF.....XYZ' ---> 'ZABCDE.....wXY'

El anillo tambien gira en solidario con el rotor, las dos piezas estan conectadas y no giran de forma
independiente mientras la maquina está en funcionamiento
"""
def rotar(rotor): 
	rotor['alfabeto'] = list(rotor['alfabeto'][len(_ALFABETO_)-1]) + rotor['alfabeto'][0:len(_ALFABETO_)-1]
	rotor['anillo'] = list(rotor['anillo'][len(_ALFABETO_)-1]) + rotor['anillo'][0:len(_ALFABETO_)-1]# El anillo es solidario con rotor, 



"""
El anillo se gira (rota) al principio de la comunicación para sincronizar las maquinas a una configuracion 
inicial común. Esta configuración forma parte de la clave.
"""
def config_ring(letra, rotor): #configurar_anillo(rotor)
	while rotor['anillo'][0] != letra : 
		rotor['anillo'] = list(rotor['anillo'][len(_ALFABETO_)-1]) + rotor['anillo'][0:len(_ALFABETO_)-1]

"""s
Igual que el anillo.
"""


def config_rotor(letra_R, desp_A, rotor):
	while rotor['alfabeto'][0] != letra_R : 
		rotar(rotor)

	while desp_A != 0:
		rotor['anillo'] = list(rotor['anillo'][len(_ALFABETO_)-1]) + rotor['anillo'][0:len(_ALFABETO_)-1]
		desp_A=desp_A-1



#De momento no se usa, las conexiones las he definido a mano en el rotor
def crear_conexiones(): #crear_conexiones(rotor)
	return None

"""
La letra identificada en el alfabeto del rotor por la posicion 'index' se cifra a traves de
las permutaciones inducidas por las conexiones del rotor 'rotor' y el anillo de este.
El parámetro 'index' se obtiene por la derecha, dado por otro rotor o por la entrada,
en caso de que este rotor sea el primero.

Devuelve un entero que representa la posicion del resultado en el alfabeto del rotor.
Este valor se le pasará al siguiente rotor o al reflector.
"""
def cifrar_ida(index, rotor):
	in_rotor = rotor['alfabeto'][index]
	cnx = rotor['conexiones'][in_rotor] 
	index_ring = rotor['alfabeto'].index(cnx)
	return index_ring

"""
Es igual que 'cifrar_ida' pero en sentido opuesto, es decir la letra en vez de entrar por la derecha del rotor,
viene por la izquierda, dada por otro rotor o por el reflector, en caso de ser el último rotor.
"""
def cifrar_vuelta(index, rotor):
	in_rotor = rotor['alfabeto'][index]
	cnx = rotor['conexiones_sim'][in_rotor]
	index_cnx = rotor['alfabeto'].index(cnx)
	return index_cnx

def check_rotar(_ROTORES_):
	rotar(_ROTORES_[0]) 
	#print(f"{_ROTORES_[0]['nombre']}")
	#print("".join(_ROTORES_[0]['alfabeto']))

	if  _ROTORES_[0]['alfabeto'][0] == _ROTORES_[0]['giro']:
		rotar(_ROTORES_[1]) 
	#	print(f"{_ROTORES_[1]['nombre']}")

	if _ROTORES_[1]['alfabeto'][0] == _ROTORES_[1]['giro']:
		rotar(_ROTORES_[2]) 
	#	print(f">>>{_ROTORES_[2]['nombre']}")

"""
Función fundamental.
El cifrado de una letra 'l_in' se divide en 3 partes.

Primero recorre todos los rotores de izquierda a derecha (cifrar_ida), cada rotor induce un poderoso cifrado.
La letra resultante llega al reflector y se mapea a otra que sale del reflector, esto permite la simetría.
Por último recorre los rotores de nuevo al en orden inverso por un camino totalmente distinto.(cifrar_vuelta)

Se retorna el indice de la letra resultante en el alfabeto simétrico.

"""
def cifrar(l_in):
	global _ROTORES_
	l_in = check_plug(_ALFABETO_[l_in], plugboard)
	c_index = l_in

	check_rotar(_ROTORES_)

	for rotor in _ROTORES_ : 
			c_index = cifrar_ida(c_index, rotor)

	c_index = reflectar(c_index) 

	for rotor in reversed(_ROTORES_) : 
			c_index = cifrar_vuelta(c_index, rotor)

	c_index = check_plug(_ALFABETO_[c_index], plugboard)
	return c_index



		
def imprimir_rotor(rotor):
	print(rotor['nombre'])
	print(f"	-Alfabeto: {''.join(rotor['alfabeto'])}")
	print(f"	-Anilo:    {''.join(rotor['anillo'])}")

def print_rotor(rotor):
	print(rotor['nombre'])
	print(f"	Giro: {rotor['giro']}")
	print(f"	Posicion:   {rotor['alfabeto'][0]}-{rotor['anillo'].index('A')+1}")
	print(f"	Alfabeto:   {''.join((rotor['alfabeto']))}")
	print(f"	Anillo:     {(''.join(rotor['anillo']))}")
	print(f"	Conexiones: {(''.join(rotor['conexiones'].keys()))}")
	print(f"	            {(''.join(rotor['conexiones'].values()))}")
	print()


def print_reflector():
	print("REFLECTOR")
	print(f"	            {''.join(list(RFL.keys()))}")
	print(f"	            {''.join(list(RFL.values()))}")


def print_plugboard():
	print("PLUGBOARD")
	print(f"	            {''.join(list(plugboard.keys()))}")
	print(f"	            {''.join(list(plugboard.values()))}")
#==========================================================



def print_enigma():
	for rotor in _ROTORES_ :
			print_rotor(rotor)
			print()
	print_reflector()
	print()
	print_plugboard()
	print()


#print("	Configuración por defecto.----------------->1")
#print("	Configuración personalizada---------------->2")
#print("	Visualizar configuración------------------->3")
#print("	Salir-------------------------------------->4")

#opcion = input("Opcion: ")





config_rotor('l',50,rotor_I)
config_rotor('.',70,rotor_II)
config_rotor('@',100,rotor_III)
config_plug("&hª%_ta7:=Hm2>L6ñAr8*39,TZW!U¿yOpYK;zMJci1S", "<º5uCsXdD.bn0E?lvB4¡ÑGgqFoINje@k[-RfwQP#xV+")
print_enigma()

m = input("IN:  ")

try :
	c = [cifrar(list(_ALFABETO_).index(l)) for l in m]
except ValueError:
	print(f"Cáracter inválido , solo se admite {_ALFABETO_}")
else: 
	res = [_ALFABETO_[i] for i in c]
	print(f"OUT: {''.join(res)}")
#[imprimir_rotor(i) for i in _ROTORES_]

