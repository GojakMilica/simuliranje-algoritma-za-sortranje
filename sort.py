import pygame
pygame.font.init()
class App:
  def __init__(self):
    self.background_colour = (255,255,255)
    self.kockica = 50
    (self.width, self.height) = (20*self.kockica, 10*self.kockica)
    self.number_font = pygame.font.SysFont( 'Comic Sans MS', 16 )

class Clan:
  def __init__(self, left, top, vrednost):
    self.top = top
    self.left = left
    self.vrednost = vrednost

  def idiDole(self, brojevi,app):
    for i in range(0,3):
      self.top += app.kockica
      nacrtajClanove(brojevi,app)
   

  def idiGore(self, brojevi,app):
    for i in range(0,3):
      self.top -= app.kockica
      nacrtajClanove(brojevi,app)

    
  #pomeraj = za koliko treba da se pomeri
  def idiLevo(self, indeks, brojevi, app, pomeraj):
    for i in range(0, pomeraj):
      brojevi[indeks-1-i].left += 2*app.kockica   
      brojevi[indeks].left -= 2*app.kockica    
      nacrtajClanove(brojevi,app)

    
def nacrtajClanove(brojevi, app):
  screen.fill(app.background_colour)
  for clan in brojevi:
    pygame.draw.rect(screen, (255, 255,0), pygame.Rect( clan.left, clan.top, app.kockica, app.kockica))
    number_image = app.number_font.render(str(clan.vrednost), False, (0, 0, 0))
    screen.blit( number_image, ( clan.left + app.kockica//2, clan.top + app.kockica//2 ) )
  pygame.display.update()
  pygame.time.delay(500)

 
def zameni(brojevi,app,pomeraj,indeks):
  brojevi[indeks].idiDole(brojevi, app)
  brojevi[indeks].idiLevo( indeks, brojevi, app, pomeraj)
  brojevi[indeks].idiGore(brojevi, app)

def dodeli(b1, b2):
  b1.top = b2.top
  b1.left = b2.left
  b1.vrednost = b2.vrednost


arr = [9,5,3,8,6,4,1,2,7,10]
app = App()
brojevi = []
screen = pygame.display.set_mode((app.width, app.height))
pygame.display.set_caption('insertion')
screen.fill(app.background_colour)
for i in range(0, len(arr)-1):
  left = 30+i*2*app.kockica
  top = 30
  brojevi.append( Clan(left, top, arr[i]))

nacrtajClanove(brojevi, app)
brojevi[5].idiDole(brojevi, app)
brojevi[5].idiLevo( 5, brojevi, app, 2)
brojevi[5].idiGore(brojevi, app)

'''for i in range(1, len(brojevi)):
 
        key = brojevi[i].vrednost
        j = i-1
        while j >= 0 and key < brojevi[j].vrednost :
                dodeli(brojevi[j+1],brojevi[j])
                j -= 1
        brojevi[j+1]
        brojevi[j + 1].vrednost = key'''
pygame.display.update() 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False