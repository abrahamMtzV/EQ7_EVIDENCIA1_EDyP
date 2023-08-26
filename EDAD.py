"""
CODIFICA UN PROGRAMA QUE LE SOLICITE AL USUARIO SU FECHA DE NACIMIENTO,
EL PROGRAMA DEBERÁ RESPONDER CON LA EDAD DE ESA PERSONA QUE CUMPLIRÁ
O CUMPLIÓ EN ESTE AÑO
"""

import datetime
_fecha_nac = input("Escribe tu fecha de nacimiento en formato (dd/mm/aaaa)\n-> ")
fecha_Nac = datetime.datetime.strptime(_fecha_nac, "%d/%m/%Y").date()

fecha_actual = datetime.datetime.today()
print(f"\nGrupo: 32")
print(f"\nFecha de nacimiento-> {fecha_Nac}")
print(f"Fecha del dia de hoy-> {fecha_actual}\n")

edad = fecha_actual.year - fecha_Nac.year

print(f"En este año {fecha_actual.year} cumples {edad} años")




