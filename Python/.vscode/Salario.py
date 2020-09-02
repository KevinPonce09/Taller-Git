
nombre = input ("Ingrese su nombre: ")
Salario = float(input("ingrese el total de su salario: "))
Hextra = float(input("Ingrese el total de horas extras que hizo: "))
Hdomi = float(input("Ingrese el total de horas dominicales que hizo: "))

VlrDía = Salario/30
VlrHora = Salario/240
VlrExt = VlrHora*1.35
VlrDom = VlrHora*1.75
VlrExtTo = VlrExt * Hextra
VlrDomTo = VlrDom * Hdomi

SalarioTotal = Salario + VlrExtTo + VlrDomTo 


print("Su nombre es: ",nombre,"con un salario base de: ",Salario,
"por consiguiente con un valor por día de: ",VlrDía,
"por consiguiente con un valor por hora de: ",VlrHora,
"hizo ",Hextra,"horas extra y por cada hora se le pagara: ",VlrExt,
"y en total por las horas extras se le dara: ",VlrExtTo,
"hizo",Hdomi,"Horad dominicales y por cada hora se le pagara: ",VlrDom,
"y en total por las horas dominicales se le dara: ",VlrDomTo,
"Siendo asi el total que se le pagara este mes es: ", SalarioTotal)

if SalarioTotal<1000000:
    mensaje = nombre,"Solicita un aumento, papu"
elif SalarioTotal<2000000:
    retencion = 1 * SalarioTotal/100
    SalarioTotal = retencion-SalarioTotal
    mensaje = nombre,"Su salario es de: " ,SalarioTotal,"y lo que nos llevamos por la cara de gratis es de: ",retencion
elif SalarioTotal <=3000000:
    retencion = 3 * SalarioTotal/100
    SalarioTotal = retencion-SalarioTotal
    mensaje = nombre,"Su salario es de: " ,SalarioTotal,"y lo que nos llevamos por la cara de gratis es de: ",retencion
else:
    retencion = 4 * SalarioTotal/100
    SalarioTotal = retencion-SalarioTotal
    mensaje = nombre,"Su salario es de: " ,SalarioTotal,"y lo que nos llevamos por la cara de gratis es de: ",retencion

print(mensaje) 

