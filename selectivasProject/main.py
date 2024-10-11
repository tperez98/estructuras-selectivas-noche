# Esstructura Simple
a=33
b=200
if b > a:
    print(b, "es mayor que ",a)

# Estructura Doble
if a > b:
    print(a, "es mayor que ",b)
else:
    print(a, "no es mayor que ", b )

# condicion Multiple

a=200
b=207

if a > b:
    print(a, "es mayor que ",b)
elif a < b:
    print(a, "es menor que ", b)
else:
    print(a, "es igual que ", b)

#Condiciones enlazadas
X =28

if X > 10:
    print("Por encima de diez, ")
    if X > 20:
        print("y tambien por encima de 20! ")
    else:
        print("pero no por encima de 20. ")

# parametros END y SEP unifica las lineas
print("estudiar los sabados", end=' ')
print("es genial ")

print("Daniela","Luis","Carlos","Camila")#agrega un espaco por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#agrega una coma

print("Daniela","Luis","Carlos","Camila",sep="_", end="_Curso_Python")#implementacion end y sep
