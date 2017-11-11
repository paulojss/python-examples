# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrao para perfis de usuario'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtida = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa) 

	def curtir(self):
		self.__curtida +=1

	def obter_curtidas(self):
		return self.__curtida
		

class Perfil_Vip(Perfil):
	'Classe padrao para perfis de usuarios vip'
	
	def __init__(self, nome, telefone, empresa, apelido):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)	
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip,self).obter_curtidas() * 10.0

