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

Se escribe el mensaje que se quiere cifrar:

```{bash}
IN:  HOLAXESTOXESXUNAXPRUEBA
OUT: NAGNMNGWEEXLXYUHOÑHUMZV
```


Y se comprueba que si se introduce la salida se obtiene la entrada original, la simetría surge efecto y el mensaje se ha descrifado.
```{bash}
IN:  NAGNMNGWEEXLXYUHOÑHUMZV
OUT: HOLAXESTOXESXUNAXPRUEBA
```

Se puede ver que los rotores cumplen la función de enmascarar los simbolos:
```{bash}
IN:  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
OUT: OOWNSOTNRDIÑBVQHUUOLDSVMPVZSLAHNZZSMZYUZSWÑMYZGÑIDFZHNTDVL

Y la símetria vuelve a hacer efecto para descifrar el mensaje:
```{bash}
IN:  OOWNSOTNRDIÑBVQHUUOLDSVMPVZSLAHNZZSMZYUZSWÑMYZGÑIDFZHNTDVL
OUT: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```



También esta disponible una versión modificada, con un alfabeto extendido: `enigma_mod.py`

```{bash}
ROTOR_I
	Giro: E
	Posicion:   l-13
	Alfabeto:   lmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºªABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijk
	Anillo:     :;<>[]+*=-ºªABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,
	Conexiones: rºVI8ªd5tO¿6>sy<J2C!Yiz-,Ñ1.?¡mTKfñvQF%:R]+qXkPucSh_e[BZD3=a*nwbH0l@4&A7UxG9Lj;pEN#MWog
	            O!TYgWñr+PÑfG&2K]u[n5LBq¡<Jm?sEM*;ohyzZ=_3XIV,p8.elºb1%-#aid:wt¿F@U9RHC>Ncx0kªAv674SQDj


ROTOR_II
	Giro: M
	Posicion:   .-85
	Alfabeto:   .,:;<>[]+*=-ºªABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡
	Anillo:     DEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºªABC
	Conexiones: %*G¿.xñBAwN¡@hPne,a0uYo2º6FZ<:7jgLHEv4T]8y=>XSr!KVR5-3#MbÑOJmlc[9t;ª&kpqDzIsiUdW_1+fQC?
	            Dp7A@j*ª<Ni5_Yat¡CV8G;kWBlnM6dEZ¿>e,O]FSu4Ihz.ow+-T%gºHñc&s=1Uvr#R[q?JÑQLXbxPfm:0K32!9y


ROTOR_III
	Giro: T
	Posicion:   @-36
	Alfabeto:   @#&%¿?!¡.,:;<>[]+*=-ºªABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_
	Anillo:     yz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºªABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwx
	Conexiones: wl9Tzm<5E]ÑFdOu4Xp*Y_P7yJx-GqBrtD1CkºñHShv0?>¡;%o&L[QIU#enaf6sVRA.2iWKbgMªj¿@!8Z,N3=:+c
	            FRVy,n>ªQ+pMP*J<[;O¿?d5kW-hX6!¡Se=_0]ZjlY:At7cmD9Tuiovqf#%UsH.ñGC42Eºax&LBwIbÑz8N@gK31r


REFLECTOR
	            ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789_@#&%¿?!¡.,:;<>[]+*=-ºª
	            ªº-=*+][><;:,.¡!?¿%&#@_9876543210zyxwvutsrqpoñnmlkjihgfedcbaZYXWVUTSRQPOÑNMLKJIHGFEDCBA

PLUGBOARD
	            &hª%_ta7:=Hm2>L6ñAr8*39,TZW!U¿yOpYK;zMJci1S<º5uCsXdD.bn0E?lvB4¡ÑGgqFoINje@k[-RfwQP#xV+
	            <º5uCsXdD.bn0E?lvB4¡ÑGgqFoINje@k[-RfwQP#xV+&hª%_ta7:=Hm2>L6ñAr8*39,TZW!U¿yOpYK;zMJci1S
```


Algunos ejemplos de su funcionamiento: 

```{bash}
IN:  HOLAXESTOXESXUNAXPRUEBA       
OUT: >pªx2,[¿b>nhI:ªw1v;seBO

IN:  >pªx2,[¿b>nhI:ªw1v;seBO
OUT: HOLAXESTOXESXUNAXPRUEBA
```

```{bash}
IN:  ABCDEFABCDEFABCDEFABCDEFABCDEF
OUT: WN=]I[7XLÑnO#Cº]9¿+mºw%m.epYoº

IN:  WN=]I[7XLÑnO#Cº]9¿+mºw%m.epYoº
OUT: ABCDEFABCDEFABCDEFABCDEFABCDEF
```

```{bash}
IN:  012345678901234567890123456789
OUT: %MXraoj0%?xHaH#sw7¿Xz-L@lh;KVJ

IN:  %MXraoj0%?xHaH#sw7¿Xz-L@lh;KVJ
OUT: 012345678901234567890123456789
```

