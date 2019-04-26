import re
import io

#------------------------------#
# Esta version es una prueba para poder crear un fichero de configuracion para la maquina, que debe
# ser leido a traves de expresiones regulares. Pero presenta varios problemas de diseño (22 Sept 2018)

# - ¿El alfabeto interno de los rotores, debe ser igual para todos o no?->En ese caso hay codigo rebundante
# - La misma pregunta para el anillo, en este caso adicionalmente deberia de indicarse el desplazamiento del mismo
# - Las conexiones internas estan exentas de problemas, deben de leerse una por una, pues cada rotor presenta diferente conexionado	

# - ¿Deberia hacerse una comprobracion de la integridad/coherencia de los parametros introducidos?
#------------------------------#


#alfabeto de referencia o canónico
_ALFABETO_ = None


rotor_I = {
	"nombre": None,

	"giro" : None,

	"alfabeto" : list(_ALFABETO_),

	"conexiones" : None,

	"conexiones_sim" : None,

	"anillo" : list(_ALFABETO_)
}

rotor_II = {
	"nombre": None,

	"giro" : None,

	"alfabeto" : list(_ALFABETO_),

	"conexiones" : None,

	"conexiones_sim" : None,

	"anillo" : list(_ALFABETO_)
}

rotor_III = {
	"nombre": None,

	"giro" : None,

	"alfabeto" : list(_ALFABETO_),

	"conexiones" : None,

	"conexiones_sim" : None,

	"anillo" : list(_ALFABETO_)
}


"""
El reflector proporciona la simetria al sistema, es un elemento único de Enigma. 
"""
RFL = None

#			--------------------------------	
plugboard = None
#											      ----------------------------------	

#	A G W E  K X W P
#   K X W P  A G W E


#_______________________________________________________________________________________________________________________________#




f = open("config.txt", "r")
texto = f.read()


p_ini = re.compile("CONFIGURACION_ENIGMA=(.*)\n\nALFABETO=(.*)")
p_rotores = re.compile("ROTOR_<.>\n\tNOMBRE=(.*)\n\tGIRO=(.*)\n\tALFABETO=(.*)\n\tCONEXIONES:\n\t\t\tIN=(.*)\n\t\t\tOUT=(.*)\n\tANILLO=(.*)")
p_fin = re.compile("REFLECTOR:\n\t\t\tIN=(.*)\n\t\t\tOUT=(.*)\n\nPLUGBOARD:\n\t\t\tIN=(.*)\n\t\t\tOUT=(.*)\n\nORDEN=(.*)")

m_ini = p_ini.match(texto)
m_rotores = p_rotores.findall(texto)
m_fin = p_fin.search(texto)
#(texto)

if m_ini : 
	print(m_ini[1])
	print(m_ini[2])

	print()

if m_rotores :
	for rotor_i in m_rotores :
		print(rotor_i[0])
		print(rotor_i[1])
		print(rotor_i[2])
		print(rotor_i[3])
		print(rotor_i[4])
		print(rotor_i[5])

		print()

if m_fin : 
	print(m_fin[1])
	print(m_fin[2])
	print(m_fin[3])
	print(m_fin[4])
	print(m_fin[5])

	print()