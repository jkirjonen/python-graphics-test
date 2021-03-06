from graphics import *
import random


# Pallo objekti
class Ball:

    def __init__(self,startx,starty):
        self.c = Circle(Point(startx,starty), random.randint(3,12))
        #self.c = Circle(Point(startx,starty), 10)
        self.c.setFill(color_rgb(0,random.randint(30,235),0))
        self.c.setOutline(color_rgb(0,0,0))
        self.c.setWidth(1)
        self.xdirection = random.randint(0,1)
        self.ydirection = random.randint(0,1)
        self.infected = False
      

def main():
    # Määritellään ikkuna
    windowX = 2800
    windowY = 1400
    win = GraphWin("My Balls", windowX, windowY,autoflush=False)
    win.setBackground(color_rgb(9,31,0))
    lob = []
    locs = []
    dx = 0
    dy = 0

    # määritellään pallojenlukumäärä ja luodaan pallot ja laitetaan ne listaan lob
    for i in range(60):
        x = random.randint(0,windowX)
        y = random.randint(0,windowY)
        lob.append(Ball(x,y))

    #kaksi testi palloja nurkista
    #lob.append(Ball(0,0))
    #lob.append(Ball(1000,1000))

    #piirretään pallot ikkunaan
    for items in lob:
        items.c.draw(win)

    # asetetaan sairastunut pallo ja sille väri
    lob[0].infected = True
    lob[0].c.setFill(color_rgb(220,0,0))    

    # main looppi
    while(True):

        # käydään pallo listaa läpi
        for ball in lob:
            # haetaan pallon keskikohta p muuttujaan
            p = ball.c.getCenter()
    
            # Määrittellän pallojen suunta jotta pysyvät ikkunan sisällä
            # eli jos pallon keskikohdan koordinaatit menevät yli
            # ikkunan leveyden miinus pallon halkaisija jaettuna kahdella niin suunta muuttuu
            if(p.getX() > (windowX - (ball.c.getRadius() / 2))):    
                ball.xdirection = 0
            if(p.getX() < (0 + (ball.c.getRadius() / 2))):
                ball.xdirection = 1 

            # ja sama pysty suuntaan
            if(p.getY() > (windowY - (ball.c.getRadius() / 2))):    
                ball.ydirection = 0
            if(p.getY() < (0 + (ball.c.getRadius() / 2))):
                ball.ydirection = 1

            # pallojen törmäys. Tarkistaa jokaisen pallon listalta että osuvatko koordinaatit samaan itsensä kanssa. Vastaan
            # tulevan pallon keskikohtaan lisätään palloon halkaisijan verran pikseleitä, jos nämä pikselit osuvat itse pallon 
            # keskikohdan pikseliin niin silloin tapahtuu törmäys ja väri muutetaan ja pallon suunta arvotaan.
            # TODO: tee paremmin 
            for l in lob:
                xr = range(int(l.c.getCenter().getX() - l.c.getRadius()), int(l.c.getCenter().getX() + l.c.getRadius()))
                yr = range(int(l.c.getCenter().getY() - l.c.getRadius()), int(l.c.getCenter().getY() + l.c.getRadius()))
                if( p.getX() in xr and p.getY() in yr and lob.index(ball) != lob.index(l) and l.infected == True):
                    ball.c.setFill(color_rgb(220,0,0))
                    ball.infected = True
                    ball.xdirection = random.randint(0,1)
                    ball.ydirection = random.randint(0,1)
                    l.xdirection = random.randint(0,1)
                    l.ydirection = random.randint(0,1)
                    print("infected")

            # Määritellään pallon nopeus pallon halkaisijan mukaan = siirretään palloa 
            # halkasijan verran eteenpäin 
            if(ball.xdirection == 1):
                dx = (ball.c.getRadius())
            else:
                dx = -(ball.c.getRadius())

            if(ball.ydirection == 1):
                dy = (ball.c.getRadius())
            else:
                dy = -(ball.c.getRadius())  

            ball.c.move(dx,dy)      
 
        # tää tulee grafiikka kirjastosta ja mahdollistaa ettei tarvita pausetusta loopissa
        update(60)
        
    # TODO: vaatii jotain ku eivät toimi
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()