print('**************NOTAs*********************∖n')
nombre = input ("Ingrese su nombre: ")
nota = float(input("ingrese su nota: "))

if nota < 0:
    mensaje = "Su nota no puede ser menor que 0"
elif nota <2 :
    mensaje =  "Su nota es menor de 2.0. Usted esta reprobado ಥ_ಥ"
elif nota <3:
    mensaje =  "Su nota esta entre 3.0/3.9. Aprobo, pero puedes mejorar ^_^"
elif nota <4:
    mensaje =  "Su nota esta entre 4.0/4.5. Aprobo. sobresaliente (*/ω＼*)"
elif nota <4.6:
    mensaje = "Su nota esta entre 4.0/4.5. Aprobo. sobresaliente (*/ω＼*)"
elif nota <=5:
    mensaje = "Su nota esta entre 4.0/4.5. Aprobo. sobresaliente (*/ω＼*)"
else:
    mensaje =  "Su nota esta entre 4.0/4.5. Aprobo. sobresaliente (*/ω＼*)"
    

print (nombre, "HAS ACABO EL MODULO CON: ",mensaje)