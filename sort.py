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
    for i in range(0,2):
      self.top += app.kockica
      nacrtajClanove(brojevi,app)
   

  def idiGore(self, brojevi,app):
    for i in range(0,2):
      self.top -= app.kockica
      nacrtajClanove(brojevi,app)

    
  #pomeraj = za koliko treba da se pomeri
  def idiLevo(self, indeks, brojevi, app, pomeraj):
    for i in range(0, pomeraj):
      brojevi[indeks+pomeraj-i].left += 2*app.kockica   
      brojevi[indeks].left -= 2*app.kockica    
      nacrtajClanove(brojevi,app)


  def dodeli(self, b2):
    self.top = b2.top
    self.left = b2.left
    self.vrednost = b2.vrednost

    
def nacrtajClanove(brojevi, app):
  screen.fill(app.background_colour)
  for clan in brojevi:
    pygame.draw.rect(screen, (255, 255,0), pygame.Rect( clan.left, clan.top, app.kockica, app.kockica))
    number_image = app.number_font.render(str(clan.vrednost), False, (0, 0, 0))
    screen.blit( number_image, ( clan.left + app.kockica//2, clan.top + app.kockica//2 ) )
  pygame.display.update()
  pygame.time.delay(300)

 
def zameni(brojevi,app,pomeraj,indeks):
  brojevi[indeks].idiDole(brojevi, app)
  brojevi[indeks].idiLevo( indeks, brojevi, app, pomeraj)
  brojevi[indeks].idiGore(brojevi, app)


def b1Doleb2Gore(b1,b2, app):
  for i in range (2):
    b1.top += app.kockica
    b2.top -= app.kockica
    nacrtajClanove(brojevi, app)

def idiZameniPozicije(b1, b2, pomeraj, app):
  b1Doleb2Gore(b1,b2,app)
  for i in range(0, pomeraj):
      b2.left += 2*app.kockica
      b1.left -= 2*app.kockica 
      nacrtajClanove(brojevi, app)
  b1Doleb2Gore(b2,b1,app)


def definisiNiz(arr, app):
  brojevi = []
  for i in range(0, len(arr)-1):
    left = 40+i*2*app.kockica
    top = 100
    brojevi.append( Clan(left, top, arr[i]))
  return brojevi

def insertionSort(brojevi, app):
  key = Clan(0,0,0)
  for i in range(1, len(brojevi)):
  
          #jeste ocajno ali ako radi, radi
          key.dodeli(brojevi[i])
          j = i-1
          while j >= 0 and key.vrednost < brojevi[j].vrednost :
                  brojevi[j+1].dodeli(brojevi[j])
                  j -= 1
          brojevi[j+1].dodeli(key)
          pomeraj = i-j-1
          zameni(brojevi,app,i-j-1,j+1)


def bubbleSort(brojevi, app):
    t= Clan(0,0,0)
 
    # Traverse through all array elements
    for i in range(len(brojevi)):
 
        # Last i elements are already in place
        for j in range(0, len(brojevi)-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if brojevi[j].vrednost > brojevi[j+1].vrednost :
                t.dodeli(brojevi[j])
                brojevi[j].dodeli(brojevi[j+1])
                brojevi[j+1].dodeli(t)
                zameni(brojevi, app, 1, j)

def selectionSort(brojevi, app):
  t= Clan(0,0,0)
  for i in range(len(brojevi)):
        
      # Find the minimum element in remaining 
      # unsorted array
      min_idx = i
      for j in range(i+1, len(brojevi)):
          if brojevi[min_idx].vrednost > brojevi[j].vrednost:
              min_idx = j
                
      # Swap the found minimum element with 
      # the first element        
      t.dodeli(brojevi[i])
      brojevi[i].dodeli(brojevi[min_idx])
      brojevi[min_idx].dodeli(t)
      if (min_idx-i != 0): idiZameniPozicije(brojevi[i], brojevi[min_idx], min_idx-i, app)

def shellSort(brojevi, app):
    t = Clan(0,0,0)

    interval = len(brojevi) // 2
    while interval > 0:
        for i in range(interval, len(brojevi)):
            t.dodeli(brojevi[i])
            j = i
            while j >= interval and brojevi[j - interval].vrednost> t.vrednost:
                brojevi[j].dodeli(brojevi[j - interval])
                j -= interval

            brojevi[j].dodeli(t)
            if (i != j): idiZameniPozicije(brojevi[j], t, interval, app)
        interval //= 2

    

arr = [9,5,3,8,6,4,1,2,7,10]
app = App()
brojevi = definisiNiz(arr, app)
screen = pygame.display.set_mode((app.width, app.height))
pygame.display.set_caption('insertion')
screen.fill(app.background_colour)


nacrtajClanove(brojevi, app)
selectionSort(brojevi, app)
pygame.display.update() 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False