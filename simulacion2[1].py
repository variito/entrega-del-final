import pygame
import random

class rectangulo():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = random.randrange(3,10)
		self.heigth = self.width
		self.movie_x = random.randrange(-3,5)
		self.movie_y = random.randrange(-3,5)
		self.color = (r1,r2,r3)
	def mover(self):
		self.x += self.movie_x
		self.y += self.movie_y
	def draw(self,pantalla):
		pygame.draw.rect(pantalla,self.color,[self.x,self.y,self.width,self.heigth])
FONDO = (0,0,0)
cantidad_de_particulas = 50
def crearParticulas (x,y):
	ParticulasLista = []
	for particula in range(cantidad_de_particulas):
		particula = rectangulo()
		particula.x = x
		particula.y = y
		ParticulasLista.append(particula)
	return ParticulasLista
pygame.init()
pantalla = pygame.display.set_mode([700,700])
pygame.display.set_caption("Simulacion de Particulas")
fps = 60
relog = pygame.time.Clock()

sub_lista = []

while True:
	r1 = random.randrange(0,255)
	r2 = random.randrange(0,255)
	r3 = random.randrange(0,255)
	for evento in pygame.event.get():
		if evento.type ==pygame.QUIT:
			break
		elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
			x,y = evento.pos
			lista = crearParticulas(x,y)
			sub_lista.append(lista)			
	pantalla.fill(FONDO)
	for lista in sub_lista:
		for particula in lista:
			particula.draw(pantalla)
			particula.mover()
	pygame.display.flip()
	relog.tick(fps)
pygame.quit()
