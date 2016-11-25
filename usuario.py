import requests
import json



class usuario:
	nombre = ""
	def __init__(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBAI6mbRzPYQLG2Sp1nSvVlyBe41TR404Cfkb0PJwpERQbVZBPOZB6nPiaARotBTGfQUnUiFpQgG8KUe6L4jRWFE234VgBLdU3h9FKBpdAmaOozeZAJ3Om9E7ZCZAJZAZBggUC8a7UtHC3ING3SmEtGUOtk5vcg1RdwZDZD"

	def obteninfo(self):
		parametros = {"access_token": self.token}
		resultado = requests.get(self.url, params=parametros).json()
		print(resultado)
		self.nombre = resultado["name"]	
		return resultado

	def publicarComentario(self, message):
		self.url = "https://graph.facebook.com/v2.8/feed"
		parametros = {"message": message, "access_token": self.token}
		resultado = requests.post(self.url, params=parametros).json()
		print(resultado)
		return(resultado)

	def allComentarios(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		parametros = {"fields": "posts,birthday", "access_token": self.token}
		resultado = requests.get(self.url, params=parametros).json()
		print(resultado)
		return(resultado)




	'''def borrarComentarios(self, borrador):
		self.url = "https://graph.facebook.com/v2.8/posts"	
		parametros = '''