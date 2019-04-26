# enigmaM4

Para ejecutar la versión normal, simplemente :
```{bash}
python enigma.py
```

```{bash}
ROTOR_III
	Giro: T
	Posicion: V-14
	Alfabeto: ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
	Anillo:   ['Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
	Conexiones:
		  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		  ['V', 'M', 'F', 'Q', 'O', 'L', 'C', 'S', 'Ñ', 'T', 'Z', 'I', 'D', 'R', 'A', 'B', 'E', 'G', 'H', 'J', 'K', 'W', 'N', 'U', 'P', 'X', 'Y']

ROTOR_II
	Giro: M
	Posicion: X-22
	Alfabeto: ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
	Anillo:   ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F']
	Conexiones:
		  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		  ['O', 'K', 'R', 'N', 'U', 'Y', 'J', 'W', 'Z', 'X', 'M', 'H', 'F', 'G', 'D', 'A', 'E', 'C', 'V', 'I', 'B', 'S', 'T', 'Q', 'L', 'P', 'Ñ']

ROTOR_I
	Giro: E
	Posicion: O-16
	Alfabeto: ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ']
	Anillo:   ['M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
	Conexiones:
		  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		  ['N', 'U', 'G', 'V', 'F', 'X', 'W', 'M', 'D', 'L', 'A', 'Y', 'T', 'Z', 'K', 'C', 'S', 'J', 'E', 'B', 'O', 'Ñ', 'I', 'P', 'H', 'R', 'Q']

REFLECTOR
		  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		  ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'Ñ', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

PLUGBOARD
		  ['A', 'G', 'W', 'E', 'K', 'X', 'P', 'Ñ']
		  ['K', 'X', 'P', 'Ñ', 'A', 'G', 'W', 'E']
```

Se escribe el mensaje que quiere cifrar:

```{bash}
IN:  HOLAXESTOXESXUNAXPRUEBA
OUT: NAGNMNGWEEXLXYUHOÑHUMZV
```


Y se comprueba que si se introduce la salida se obtiene la entrada original, la simetría surge efecto.
```{bash}
IN:  NAGNMNGWEEXLXYUHOÑHUMZV
OUT: HOLAXESTOXESXUNAXPRUEBA
```

