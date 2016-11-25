from usuario import usuario 

user = usuario()
print(type(user))

print("Nombre de usario antes de peticion")
print(user.nombre)

respuesta = user.obteninfo()

print("respuesta")
print(type(respuesta))

respuesta2 = user.publicarComentario(message = "Hola Mundo")

print("respuesta2")
print(type(respuesta2))


borrador = user.allComentarios()