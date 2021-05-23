import pygame
from numpy import random
import tkinter as tk
from tkinter import simpledialog
pygame.font.init()
class App:
  def __init__(self):
    self.background_colour = (255,255,255)
    self.kockica = 48
    (self.width, self.height) = (20*self.kockica, 10*self.kockica)
    self.number_font = pygame.font.SysFont( 'Comic Sans MS', 16 )

class Clan:
  def __init__(self, left, top, vrednost):
    self.top = top
    self.left = left
    self.vrednost = vrednost

  def idiDole(self, brojevi,app):
    for i in range(0,16*2):
      self.top += app.kockica  //16
      nacrtajClanove(brojevi,app)
   

  def idiGore(self, brojevi,app):
    for i in range(0,16*2):
      self.top -= app.kockica //16
      nacrtajClanove(brojevi,app)

    
  #pomeraj = za koliko treba da se pomeri
  def idiLevo(self, indeks, brojevi, app, pomeraj):
    for i in range(0, 16*pomeraj):
      brojevi[indeks+pomeraj-i//16].left += 2*app.kockica //16  
      brojevi[indeks].left -= 2*app.kockica //16
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
  pygame.time.delay(10)

 
def zameni(brojevi,app,pomeraj,indeks):
  brojevi[indeks].idiDole(brojevi, app)
  brojevi[indeks].idiLevo( indeks, brojevi, app, pomeraj)
  brojevi[indeks].idiGore(brojevi, app)


def b1Doleb2Gore(b1,b2, app, brojevi):
  for i in range (16*2):
    b1.top += app.kockica//16
    b2.top -= app.kockica//16
    nacrtajClanove(brojevi, app)

def idiZameniPozicije(b1, b2, pomeraj, app, brojevi):
  b1Doleb2Gore(b1,b2,app, brojevi)
  for i in range(0, 16*pomeraj):
      b2.left += 2*app.kockica //16
      b1.left -= 2*app.kockica //16
      nacrtajClanove(brojevi, app)
  b1Doleb2Gore(b2,b1,app, brojevi)


def definisiNiz(n, app):
  brojevi = []
  for i in range(0, n):
    left = 40+i*2*app.kockica
    top = 100
    brojevi.append( Clan(left, top, random.randint(100)))
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
          if (i-j-1 != 0): zameni(brojevi,app,i-j-1,j+1)


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
      if (min_idx-i != 0): idiZameniPozicije(brojevi[i], brojevi[min_idx], min_idx-i, app, brojevi)

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

def popups():
  ROOT = tk.Tk()

  ROOT.withdraw()
  USER_INP = simpledialog.askstring(title = "br clanova", prompt="Unesite broj clanova")
  n = int(USER_INP)

  USER_INP2 = simpledialog.askstring(title = "sort", prompt="Koji sort zelite?(insertion, selection, bubble)")
  x = str(USER_INP2)
  return n, x

def main(n, x, app):
    brojevi = definisiNiz(n, app)
    nacrtajClanove(brojevi, app)
    if (x is "insertion"): insertionSort(brojevi, app)
    elif (x is"selection"): selectionSort(brojevi, app)
    elif (x is "bubble"): bubbleSort(brojevi, app)



app = App()
n, x = popups()
screen = pygame.display.set_mode((app.width, app.height))
pygame.display.set_caption('simulacija sorta')
screen.fill(app.background_colour)
brojevi = definisiNiz(n, app)
nacrtajClanove(brojevi, app)
if (x == "insertion"): insertionSort(brojevi, app)
elif (x =="selection"): selectionSort(brojevi, app)
elif (x == "bubble"): bubbleSort(brojevi, app)


pygame.display.update() 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False