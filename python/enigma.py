from tkinter import *
#alfabeto de referencia o canónico
_ALFABETO_ = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#__________________________________________________MÁQUINA ENGIMA_CONFIGUARCIÓN_DEFECTO__________________________________________#


rotor_I = {
	"nombre": "ROTOR_I",

	"giro" : "E",

	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'),

	"conexiones" : 
		{
			'A':'N','B':'U','C':'G','D':'V','E':'F','F':'X','G':'W','H':'M','I':'D','J':'L','K':'A','L':'Y','M':'T','N':'Z',
			'Ñ':'K','O':'C','P':'S','Q':'J','R':'E','S':'B','T':'O','U':'Ñ','V':'I','W':'P','X':'H','Y':'R','Z':'Q'
		},

	"conexiones_sim" : None,

	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

}

rotor_II = {
	"nombre": "ROTOR_II",

	"giro" : "M",

	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'),

	"conexiones" : 
		{
			'A':'O','B':'K','C':'R','D':'N','E':'U','F':'Y','G':'J','H':'W','I':'Z','J':'X','K':'M','L':'H','M':'F','N':'G',
			'Ñ':'D','O':'A','P':'E','Q':'C','R':'V','S':'I','T':'B','U':'S','V':'T','W':'Q','X':'L','Y':'P','Z':'Ñ'
		},

	"conexiones_sim" : None,

	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
}

rotor_III = {
	"nombre" : "ROTOR_III",

	"giro" : "T",

 	"alfabeto" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'),

 	"conexiones" : 
 		{
 			'A':'V','B':'M','C':'F','D':'Q','E':'O','F':'L','G':'C','H':'S','I':'Ñ','J':'T','K':'Z','L':'I','M':'D','N':'R',
 			'Ñ':'A','O':'B','P':'E','Q':'G','R':'H','S':'J','T':'K','U':'W','V':'N','W':'U','X':'P','Y':'X','Z':'Y'
 		},

 	"conexiones_sim" : None,

 	"anillo" : list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
 }


"""
El reflector proporciona la simetria al sistema, es un elemento único de Enigma. 
"""
RFL = { 
		'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'Ñ',
		'N':'N','Ñ':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'
}

#				  --------------------------------	
plugboard = 	{'A':'K', 'G':'X', 'W':'P', 'E':'Ñ', 'K':'A', 'X':'G', 'P':'W', 'Ñ':'E'}
#													  ----------------------------------	

#_______________________________________________________________________________________________________________________________#


def crear_conexiones_sim(rotor): 
	rotor['conexiones_sim'] = dict(list(zip(rotor['conexiones'].values(), rotor['conexiones'].keys())))

crear_conexiones_sim(rotor_I)
crear_conexiones_sim(rotor_II)
crear_conexiones_sim(rotor_III)

"""
Representa el conjunto de rotores que van a utilizarse, pueden cambiarse de orden y añadir todos los que se quieran.
"""
_ROTORES_ = [rotor_III, rotor_II, rotor_I]
 
"""
 l_in:  letra 
 plug: plugboard
"""
def check_plug(l_in, plug):
	if l_in in plug :
#		print(f"{l_in} se convierte en {plug[l_in]}")
		return list(_ALFABETO_).index(plug[l_in])
	return list(_ALFABETO_).index(l_in)

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

"""
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

	c_index = reflectar(c_index) #Obtiene letra conectada en bucle en el reflector

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
	print(f"	Posicion: {rotor['alfabeto'][0]}-{rotor['anillo'].index('A')+1}")
	print(f"	Alfabeto: {(rotor['alfabeto'])}")
	print(f"	Anillo:   {(rotor['anillo'])}")
	print(f"	Conexiones:")
	print(f"		  {list(rotor['conexiones'].keys())}")
	print(f"		  {list(rotor['conexiones'].values())}")

def print_reflector():
	print("REFLECTOR")
	print(f"		  {list(RFL.keys())}")
	print(f"		  {list(RFL.values())}")	

def print_plugboard():
	print("PLUGBOARD")
	print(f"		  {list(plugboard.keys())}")
	print(f"		  {list(plugboard.values())}")
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



config_rotor('O',3,rotor_I)
config_rotor('X',18, rotor_II)
config_rotor('V',8, rotor_III)
print_enigma()

m = input("IN:  ").upper()

try :
	c = [cifrar(list(_ALFABETO_).index(l)) for l in m]
except ValueError:
	print(f"Cáracter inválido , solo se admite {_ALFABETO_}")
else: 
	res = [_ALFABETO_[i] for i in c]
	print(f"OUT: {''.join(res)}")
#[imprimir_rotor(i) for i in _ROTORES_]

