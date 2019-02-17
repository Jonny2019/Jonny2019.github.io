'''
Justus Bendel, 25.08.2018
Elementarteilchen
'''
import time
import os
import sys
import pygame
from pygame.locals import *

class Elementarteilchen(object):
    def __init__(self):
        pygame.init()
        self.fermionen = {"Quarks" :
                          {"up" : ["2,3MeV", "2/3", "1/2"],     #Masse, Ladung, Spin
                           "down" : ["4,8MeV", "-1/3", "1/2"],
                           "charm" : ["1,275GeV", "2/3", "1/2"],
                           "strange": ["95MeV", "-1/3", "1/2"],
                           "top" : ["173,07GeV", "2/3", "1/2"],
                           "bottom" : ["4,18GeV", "-1/3", "1/2"]},
                          "Leptonen" :
                          {"Elektron-Neutrino" : ["<2eV", "0", "1/2"],
                           "Elektron" : ["0,511MeV", "-1", "1/2"],
                           "Myon-Neutrino" : ["<0,19MeV", "0", "1/2"],
                           "Myon" : ["105,7MeV", "-1", "1/2"],
                           "Tau-Neutrino" : ["<18,2MeV", "0", "1/2"],
                           "Tau" : ["1,777GeV", "-1", "1/2"]}}
        self.bosonen = {"Eichbosonen" :
                        {"Photon" : ["0", "0", "1"],
                         "Gluon" : ["0", "0", "1"],
                         "Z Boson" : ["91,2GeV", "0", "1"],
                         "W Boson(+/-)" : ["80,4GeV", "+/-1", "1"]},
                        "Higgs Bosonen" :
                        {"Higgs Boson":["125,09GeV", "0", "0"]}}
        self.colors = {"R" : (200, 50, 50),
                       "G" : (200, 200,0),
                       "Bl" : (50, 50, 200),
                       "Gr" : (50, 200, 50),
                       "W" : (255, 255, 255),
                       "B" : (0, 0, 0)}
        self.greek = {"My" : "u'\u03BC'",
                      "Tau" : "u'\u03C4'",
                      "Gamma" : "u'\u03B3'",
                      "Ny" : "u'\u03BD'"}
        self.UE = u'Ü'
        self.Fg = pygame.font.SysFont('Arial', 100, bold=True)
        self.Fk = pygame.font.SysFont('Arial', 40)
        self.Fsk = pygame.font.SysFont('Arial', 30)
    def show(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)
        GUI = pygame.display.set_mode((1600, 900), RESIZABLE, 32)
        pygame.display.set_caption('Elementarteilchen ' + self.UE + 'bersicht')
        GUI.fill(self.colors["W"])
        
        for x in range(300, 900, 200):
            pygame.draw.rect(GUI, (self.colors["R"]), (x, 50, 200, 182.5))
            pygame.draw.rect(GUI, (self.colors["B"]), (x, 50, 200, 182.5), 3)
        for x in range(300, 900, 200):
            pygame.draw.rect(GUI, (self.colors["R"]), (x, 232.5, 200, 182.5))
            pygame.draw.rect(GUI, (self.colors["B"]), (x, 232.5, 200, 182.5), 3)
        for x in range(300, 900, 200):
            pygame.draw.rect(GUI, (self.colors["G"]), (x, 415, 200, 182.5))
            pygame.draw.rect(GUI, (self.colors["B"]), (x, 415, 200, 182.5), 3)
        for x in range(300, 900, 200):
            pygame.draw.rect(GUI, (self.colors["G"]), (x, 597.5, 200, 182.5))
            pygame.draw.rect(GUI, (self.colors["B"]), (x, 597.5, 200, 182.5), 3)
        for y in range(50, 597, 182):
            pygame.draw.rect(GUI, (self.colors["Bl"]), (900, y, 200, 182.5))
            pygame.draw.rect(GUI, (self.colors["B"]), (900, y, 200, 182.5), 3)
        pygame.draw.rect(GUI, (self.colors["Gr"]), (1100, 50, 200, 182.5))
        pygame.draw.rect(GUI, (self.colors["B"]), (1100, 50, 200, 182.5), 3)


        #fermionen
        #quarks

        #up
        sym = self.Fg.render('u', 1, (self.colors['B']))
        nam = self.Fk.render('up', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "up", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "up", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "up", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (370, 80))
        GUI.blit(nam, (380, 170))
        GUI.blit(mas, (305, 55))
        GUI.blit(lad, (305, 95))
        GUI.blit(spi, (305, 130))

        #down
        sym = self.Fg.render('d', 1, (self.colors['B']))
        nam = self.Fk.render('down', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "down", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "down", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "down", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (370, 262.5))
        GUI.blit(nam, (360, 352.5))
        GUI.blit(mas, (305, 237.5))
        GUI.blit(lad, (305, 277.5))
        GUI.blit(spi, (305, 312.5))

        #charm
        sym = self.Fg.render('c', 1, (self.colors['B']))
        nam = self.Fk.render('charm', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "charm", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "charm", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "charm", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (570, 80))
        GUI.blit(nam, (555, 170))
        GUI.blit(mas, (505, 55))
        GUI.blit(lad, (505, 95))
        GUI.blit(spi, (505, 130))

        #strange
        sym = self.Fg.render('s', 1, (self.colors['B']))
        nam = self.Fk.render('strange', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "strange", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "strange", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "strange", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (570, 262.5))
        GUI.blit(nam, (550, 352.5))
        GUI.blit(mas, (505, 237.5))
        GUI.blit(lad, (505, 277.5))
        GUI.blit(spi, (505, 312.5))

        #top
        sym = self.Fg.render('t', 1, (self.colors['B']))
        nam = self.Fk.render('top', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "top", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "top", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "top", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (770, 80))
        GUI.blit(nam, (770, 170))
        GUI.blit(mas, (705, 55))
        GUI.blit(lad, (705, 95))
        GUI.blit(spi, (705, 130))

        #bottom
        sym = self.Fg.render('b', 1, (self.colors['B']))
        nam = self.Fk.render('bottom', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "bottom", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "bottom", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Quarks", "bottom", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (770, 262.5))
        GUI.blit(nam, (755, 352.5))
        GUI.blit(mas, (705, 237.5))
        GUI.blit(lad, (705, 277.5))
        GUI.blit(spi, (705, 312.5))

        #Leptonen

        #Elektron-Neutrino
        sym = self.Fg.render(eval(self.greek["Ny"]), 1, (self.colors['B']))
        szs = self.Fsk.render('e', 1, (self.colors['B']))
        nam = self.Fsk.render('Elektron-Neutrino', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron-Neutrino", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron-Neutrino", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron-Neutrino", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (370, 445))
        GUI.blit(szs, (420, 500))
        GUI.blit(nam, (305, 535))
        GUI.blit(mas, (305, 420))
        GUI.blit(lad, (305, 460))
        GUI.blit(spi, (305, 495))

        #Myon-Neutrino
        sym = self.Fg.render(eval(self.greek["Ny"]), 1, (self.colors['B']))
        szs = self.Fsk.render(eval(self.greek["My"]), 1, (self.colors['B']))
        nam = self.Fsk.render('Myon-Neutrino', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon-Neutrino", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon-Neutrino", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon-Neutrino", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (570, 445))
        GUI.blit(szs, (620, 500))
        GUI.blit(nam, (520, 535))
        GUI.blit(mas, (505, 420))
        GUI.blit(lad, (505, 460))
        GUI.blit(spi, (505, 495))

        #Tau-Neutrino
        sym = self.Fg.render(eval(self.greek["Ny"]), 1, (self.colors['B']))
        szs = self.Fsk.render(eval(self.greek["Tau"]), 1, (self.colors['B']))
        nam = self.Fsk.render('Tau-Neutrino', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau-Neutrino", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau-Neutrino", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau-Neutrino", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (770, 445))
        GUI.blit(szs, (820, 500))
        GUI.blit(nam, (730, 535))
        GUI.blit(mas, (705, 420))
        GUI.blit(lad, (705, 460))
        GUI.blit(spi, (705, 495))

        #Elektron
        sym = self.Fg.render('e', 1, (self.colors['B']))
        nam = self.Fk.render('Elektron', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Elektron", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (370, 627.5))
        GUI.blit(nam, (340, 717.5))
        GUI.blit(mas, (305, 602.5))
        GUI.blit(lad, (305, 642.5))
        GUI.blit(spi, (305, 677.5))

        #Myon
        sym = self.Fg.render(eval(self.greek["My"]), 1, (self.colors['B']))
        nam = self.Fk.render('Myon', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Myon", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (570, 607.5))
        GUI.blit(nam, (560, 717.5))
        GUI.blit(mas, (505, 602.5))
        GUI.blit(lad, (505, 642.5))
        GUI.blit(spi, (505, 677.5))

        #Tau
        sym = self.Fg.render(eval(self.greek["Tau"]), 1, (self.colors['B']))
        nam = self.Fk.render('Tau', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "fermionen","Leptonen", "Tau", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (770, 627.5))
        GUI.blit(nam, (770, 717.5))
        GUI.blit(mas, (705, 602.5))
        GUI.blit(lad, (705, 642.5))
        GUI.blit(spi, (705, 677.5))


        #Bosonen
        #Eichbosonen

        #Photon
        sym = self.Fg.render(eval(self.greek["Gamma"]), 1, (self.colors['B']))
        nam = self.Fk.render('Photon', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Photon", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Photon", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Photon", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (970, 60))
        GUI.blit(nam, (950, 170))
        GUI.blit(mas, (905, 55))
        GUI.blit(lad, (905, 95))
        GUI.blit(spi, (905, 130))

        #Gluon
        sym = self.Fg.render('g', 1, (self.colors['B']))
        nam = self.Fk.render('Gluon', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Gluon", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Gluon", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Gluon", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (970, 242.5))
        GUI.blit(nam, (955, 352.5))
        GUI.blit(mas, (905, 237.5))
        GUI.blit(lad, (905, 277.5))
        GUI.blit(spi, (905, 312.5))

        #Z Boson
        sym = self.Fg.render('Z', 1, (self.colors['B']))
        szs = self.Fsk.render('0', 1, (self.colors['B']))
        nam = self.Fk.render('Z Boson', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Z Boson", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Z Boson", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "Z Boson", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (970, 445))
        GUI.blit(szs, (1040, 450)) 
        GUI.blit(nam, (955, 535))
        GUI.blit(mas, (905, 420))
        GUI.blit(lad, (905, 460))
        GUI.blit(spi, (905, 495))

        #W Boson
        sym = self.Fg.render('W', 1, (self.colors['B']))
        szs = self.Fsk.render('+/-', 1, (self.colors['B']))
        nam = self.Fk.render('W Boson', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "W Boson(+/-)", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "W Boson(+/-)", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Eichbosonen", "W Boson(+/-)", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (960, 627.5))
        GUI.blit(szs, (1060, 632.5)) 
        GUI.blit(nam, (945, 717.5))
        GUI.blit(mas, (905, 602.5))
        GUI.blit(lad, (905, 642.5))
        GUI.blit(spi, (905, 677.5))


        #Higgs Bosonen


        #Higgs Boson
        sym = self.Fg.render('H', 1, (self.colors['B']))
        nam = self.Fk.render('Higgs Boson', 1, (self.colors['B']))
        mas = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Higgs Bosonen", "Higgs Boson", "mass")), 1, (self.colors['B']))
        lad = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Higgs Bosonen", "Higgs Boson", "charge")), 1, (self.colors['B']))
        spi = self.Fk.render(eval(Elementarteilchen.value(self, "bosonen","Higgs Bosonen", "Higgs Boson", "spin")), 1, (self.colors['B']))
        GUI.blit(sym, (1170, 80))
        GUI.blit(nam, (1105, 170))
        GUI.blit(mas, (1105, 55))
        GUI.blit(lad, (1105, 95))
        GUI.blit(spi, (1105, 130))




        #Legende / Beschriftungen
        
        M = self.Fk.render('Masse', 1, (self.colors['B']))
        L = self.Fk.render('Ladung', 1, (self.colors['B']))
        S = self.Fk.render('Spin', 1, (self.colors['B']))
        GUI.blit(M, (150, 50))
        GUI.blit(L, (150, 90))
        GUI.blit(S, (150, 130))

        Q = self.Fk.render('Quarks', 1, (self.colors['R']))
        GUI.blit(Q, (150, 375))
        L = self.Fk.render('Leptonen', 1, (self.colors['G']))
        GUI.blit(L, (150, 735))
        E = self.Fk.render('Eichbosonen', 1, (self.colors['Bl']))
        GUI.blit(E, (1110, 735))
        H = self.Fk.render('Higgs Bosonen', 1, (self.colors['Gr']))
        GUI.blit(H, (1310, 180))

        F = self.Fk.render('Fermionen', 1, (self.colors['B']))
        GUI.blit(F, (300, 10))
        B = self.Fk.render('Bosonen', 1, (self.colors['B']))
        GUI.blit(B, (900, 10))
        
            
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:           #50, 200, 182.5
                pos = pygame.mouse.get_pos()
                px = pos[0]
                py = pos[1]
                if px > 300 and px < 500 and py > 50 and py < 232.5:
                    Elementarteilchen.up(self)
            time.sleep(0.05)
            
    def up(self):
        GUI = pygame.display.set_mode((1600, 900), RESIZABLE, 32)
        pygame.display.set_caption('Quarks - up')
        GUI.fill(self.colors['W'])

        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def value(self, groop1, groop2, particle, particle_value):
        a = "((self."+groop1+"['"+groop2+"'])['"+particle+"'])["
        if particle_value == "mass":
            b = '0]'
        elif particle_value == "charge":
            b = '1]'
        elif particle_value == "spin":
            b = '2]'
        c =  a+b
        return(c)

ET = Elementarteilchen()
ET.show()
