import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
from random import randrange
import copy


def crash():
    global info
    global newcompt
    newcompt = 17
    info = 'est tombé.'


def rien():
    global info
    info = 'Tout va bien pour'


def sanction():
    global infosanc
    global infopenal
    infosanc = 'Avertissement pour'
    infopenal = 'Pénalité pour'


def depassement():
    global infodep
    infodep = 'ET !!! le dépassement de'


def jaune():
    global infodrap
    infodrap = 'Drapeau Jaune dans le virage'


def pluie():
    global pluieinfo
    pluieinfo = 'Et la pluie s\'abbat sur le circuit'


def multicrash():
    global multipcrash
    multipcrash = 'Chute énorme de plusieurs pilotes !!!'


def probmeca():
    global meca
    meca = "a un problème mécanique, il y a de la fumée qui sort de sa moto. Malheureussement il va devoir arrêter la course !!!"


# preparation
motoGp = [str('Bagnaia'), 'Rins', 'Marini', 'Bezzecchi', 'Mir', 'Quartararo', 'Miller', 'Martin', 'Gardner',
          'P.Espargaro', 'A.Espargaro', 'Marquez', 'Fernandez', 'Bastianini', 'Di Giantiannio', 'Zarco', 'Nakagami',
          'Dovizozio', 'B.Binder',
          'D.Binder', 'Olivera', 'Vinales', 'Morbidelli']

#---- Ecran D'accueil ----#
home = Tk()
home.title('Grille de départ')
home.iconbitmap('race.ico')
home.geometry("723x597")
home.attributes('-alpha',0.8)

bg = PhotoImage(master=home,file="img/banner.png")
label1 = Label(home, image=bg)
label1.place(x=-3, y=372)

title = Label(home,text='MOTOGP SIMULATOR\nCUSTOM')
title.config(font=('Verdana',36))
title.place(x=90,y=65)


creat = Label(home,text='Crée par Luca Vidiri')
creat.pack()
creat.config(font=('Verdana',18))
creat.place(x=230,y=245)

home.after(2500, lambda: home.destroy())
home.mainloop()

# ---- PERSONNALISATION ----#

Commentateur = input('Saissisez le nom du commentateur')
if Commentateur == '':
    Commentateur = 'Guido Meda'
Second_Commentateur = input('Saissisez le nom du deuxième comentateur')
if Second_Commentateur == '':
    Second_Commentateur = 'Valentino'
Course = input('Saissisez le nom du circuit')
if Course == '':
    Course = 'Mugello'
Pays = input('Saissisez dans quel pays, le circuit se situe')
if Pays == '':
    Pays = 'Italie'
chaine = input('Saissisez la chaine de diffusion')
if chaine == '':
    chaine = 'GP+'
tour = int(input('Saissisez le nombre de tours (max 5)'))
while tour == 0:
    tour = int(input('Saissisez le nombre de tours'))
virage = int(input('Saissisez le nombre de virages'))
while virage == 0:
    virage  = int(input('Saissisez le nombre de virages'))
    
#---- ECRAN QUALIF----#
qualif = Tk()
qualif.title('Grille de départ')
qualif.iconbitmap('race.ico')
qualif.geometry("1023x697")
qualif.attributes('-alpha',0.8)

bg = PhotoImage(master=qualif,file="bureau.png")
label1 = Label(qualif, image=bg)
label1.place(x=700, y=505)

bgcom = PhotoImage(master=qualif,file="commentateur.png")
label1 = Label(qualif, image=bgcom)
label1.place(x=700, y=465)

bgcom2 = PhotoImage(master=qualif,file="commentateur2.png")
label1 = Label(qualif, image=bgcom2)
label1.place(x=870, y=455)

interact1 = PhotoImage(master=qualif,file="buble.png")
label1 = Label(qualif, image=interact1)
label1.place(x=480, y=340)

textin1 = Label(qualif,text=f'Salut les abonnés de {chaine} \n nous nous retrouvons \n en {Pays} au circuit {Course} \n en compagnie de {Second_Commentateur}')
textin1.config(font=('Verdana',9))
textin1.place(x=512,y=378)


interact2 = PhotoImage(master=qualif,file="buble2.png")
label1 = Label(qualif, image=interact2)
label1.place(x=720, y=330)

textin2 = Label(qualif,text=f'Bonjour, {Commentateur} \n Et c\'est parti pour \nles qualifications')
textin2.config(font=('Verdana',9))
textin2.place(x=745,y=363)


grids = []  # grille
best = 99.999  # meilleur temps
lnghtgrd = len(grids)
alreadySelected = []
timer = 0
while lnghtgrd != len(motoGp):
    lnghtgrd = len(grids)
    choice = random.choice(motoGp)
    while choice in grids:
        choice = random.choice(motoGp)
    second = round(random.uniform(0, 99), 3)
    time = ['1', second]
    if alreadySelected.count(choice) == 0:
        grids.append([choice, time])
        alreadySelected.append(choice)
        if time[1] < best:
            best = time[1]
            bestime = Label(qualif,text=f'Meilleur temps pour {choice} avec le temps de : 1.{round(time[1],3)}')
            bestime.place(x=350,y=7)
            bestime.config(font=('Verdana',9),fg='red')


timer = 0
signal = ''
while timer != len(grids):
    nom = Label(qualif,text=f'Temps de {grids[timer][0]} : {grids[timer][1][0]}.{grids[timer][1][1]}')
    nom.grid(row=timer+1,column=3)
    nom.config(font=("Verdana", 10), padx=40,pady=5)
    timer+=1
qualif.after(2500, lambda: qualif.destroy())
qualif.mainloop()
# ---- PARTIE TRIAGE CHRONO ----#
temps = []
for i in range(len(grids)):
    temps.append(grids[i][1][1])
temps.sort()
qualif.mainloop()
# ---- POSITION GRID ----#
grid2 = []
p = 0
y = 0
while len(grid2) != len(grids):
    chrono = temps[y]
    chronog = grids[p][1][1]
    if chronog == chrono:
        grid2.append([grids[p][0], '1.', grids[p][1][1]])
        p = 0
        y = y + 1
    else:
        p = p + 1

# ---- LISTE PARAMETRE ---#
actions = ['rien', 'crash', 'depassement', 'sortie']
meteo = ['Dégagé', 'pluie', 'couvert', 'humide']
pneusoleil = ['H secs', 'S secs', 'M secs']
pneupluie = ['S pluie', 'M pluie']

# ---- AFFICHAGE GRID ----#
grids = grid2.copy()

endqualif = Tk()
endqualif.title('Fin des qualifications')
endqualif.iconbitmap('race.ico')
endqualif.geometry("1023x697")
endqualif.attributes('-alpha',0.8)
desk = PhotoImage(master=endqualif,file="bureau.png")
label1 = Label(endqualif, image=desk)
label1.place(x=700, y=505)

bgcoment = PhotoImage(master=endqualif,file="commentateur.png")
label1 = Label(endqualif, image=bgcoment)
label1.place(x=700, y=465)

bgcoment2 = PhotoImage(master=endqualif,file="commentateur2.png")
label1 = Label(endqualif, image=bgcoment2)
label1.place(x=870, y=455)

interactend1 = PhotoImage(master=endqualif,file="buble.png")
label1 = Label(endqualif, image=interactend1)
label1.place(x=480, y=340)

textinend1 = Label(endqualif,text=f'C\'est la fin, des qualifications')
textinend1.config(font=('Verdana',9))
textinend1.place(x=512,y=388)


interactend2 = PhotoImage(master=endqualif,file="buble2.png")
label1 = Label(endqualif, image=interactend2)
label1.place(x=720, y=330)

textinend2 = Label(endqualif,text=f'Voici la grille de départ')
textinend2.config(font=('Verdana',10))
textinend2.place(x=738,y=374)

g = 1
while g != 24:
    nomg = Label(endqualif,text=f'{g}, e, {grids[g-1][0]}, {grids[g-1][1]} {grids[g-1][2]}')
    nomg.grid(row=g+1,column=3)
    nomg.config(font=("Verdana", 10), padx=40,pady=5)
    grids[g-1].append(g)
    g = g + 1
endqualif.after(2500, lambda: endqualif.destroy())
endqualif.mainloop()
# ---- STATUS RIDER ----#
status = "IN RACE"
r = 0
while r != 23:
    grids[r].append(status)
    r = r + 1

# ---- PARTIE VERTE ----#
green = 0
gr = 0
while gr != 23:
    grids[gr].append(green)
    gr = gr + 1
    
# ---- METEO ----#
weather = random.choice(meteo)
p = 0
while p != 23:
    if weather == 'pluie':
        grids[p].append(random.choice(pneupluie))
        grids[p].append(random.choice(pneupluie))
    else:
        grids[p].append(random.choice(pneusoleil))
        grids[p].append(random.choice(pneusoleil))
    p = p + 1

# ---- NATIONALITE ----#
nat = 0
pilote_name = ''
while nat != 23:
    pilote_name = grids[nat][0]
    if pilote_name == 'Bagnaia' or pilote_name == 'Marini'  or pilote_name == 'Bastianini' or pilote_name == 'Morbidelli' or pilote_name == 'Bezzecchi' or pilote_name == 'Dovizozio' or pilote_name == 'Di Giantiannio':
        grids[nat].append('ITA')
    elif pilote_name == 'Rins' or pilote_name == 'P.Espargaro' or pilote_name == 'Martin' or pilote_name == 'Marquez' or pilote_name == 'A.Espargaro' or pilote_name == 'Vinales' or pilote_name == 'Mir' or pilote_name == 'Fernandez':
        grids[nat].append('ESP')
    elif pilote_name == 'Zarco' or pilote_name == 'Quartararo':
        grids[nat].append('FRA')
    elif pilote_name == 'B.Binder' or pilote_name == 'D.Binder':
        grids[nat].append('ZA')
    elif pilote_name == 'Gardner' or pilote_name == 'Miller':
        grids[nat].append('AUS')
    elif pilote_name == 'Olivera':
        grids[nat].append('POR')
    elif pilote_name == 'Nakagami':
        grids[nat].append('JAP')
    nat+=1

#---- IMAGE PILOTE----#
img = 0
name_pilote = ""
while img != 23:
    name_pilote = grids[img][0]
    grids[img].append('img/'+name_pilote.lower()+'.PNG')
    grids[img].append('img/'+name_pilote.lower() + 'num.png')
    grids[img].append('img/giant/'+name_pilote.lower() + 'giant.png')
    img+=1


# ---- COURSE ----#
race = Tk()
race.title('Fin des qualifications')
race.iconbitmap('race.ico')
race.geometry("1023x697")
race.attributes('-alpha',0.8)
desk = PhotoImage(master=race,file="bureau.png")
label1 = Label(race, image=desk)
label1.place(x=700, y=505)

bgcomentrace = PhotoImage(master=race,file="commentateur.png")
label1 = Label(race, image=bgcomentrace)
label1.place(x=700, y=465)

bgcomentrace2 = PhotoImage(master=race,file="commentateur2.png")
label1 = Label(race, image=bgcomentrace2)
label1.place(x=870, y=455)

interactrace1 = PhotoImage(master=race,file="buble.png")
label1 = Label(race, image=interactrace1)
label1.place(x=480, y=340)

textirace1 = Label(race,text=f'3 2 1 \n BOOOOOOM!!!')
textirace1.config(font=('Verdana',9))
textirace1.place(x=512,y=388)


interactrace2 = PhotoImage(master=race,file="buble2.png")
label1 = Label(race, image=interactrace2)
label1.place(x=720, y=330)

textirace2 = Label(race,text=f'ET C\'est parti')
textirace2.config(font=('Verdana',16))
textirace2.place(x=742,y=376)

pl = 1
while pl != 24:
    nomgr = Label(race,text=f'{pl}, e, {grids[pl-1][0]}, {grids[pl-1][1]} {grids[pl-1][2]}')
    nomgr.grid(row=pl+1,column=3)
    nomgr.config(font=("Verdana", 10), padx=40,pady=5)
    pl = pl + 1
race.after(2500, lambda: race.destroy())
race.mainloop()
touract = int(1)
virageact = int(0)
effectue = []
out = []
vert = 0
compt = 0
while touract != tour:
    while compt != len(grids):
        for _ in range(1):
            pilote = grids[compt][0]
            if effectue.count(pilote) == 0:
                actions = ['crash', 'depassement', 'sortie', 'rien', 'bugmeca']
                tirageA = random.choices(actions, weights=(1, 3, 10, 40, 1), k=1)
                if tirageA == ['crash']:
                    crash()
                    jaune()
                    print(infodrap, virageact)
                    # Add image file
                    fencrsh = Tk()
                    fencrsh.title('Grille de départ')
                    fencrsh.iconbitmap('race.ico')
                    fencrsh.geometry("123x97")
                    fencrsh.config(bg='#1C2833')
                    # Add image file
                    head = PhotoImage(file=grids[compt][9])

                    label1 = Label(fencrsh, image=head)
                    label1.place(x=-12, y=7)
                    label1.config(bg='#1C2833')

                    num = PhotoImage(file=grids[compt][10])
                    label2 = Label(fencrsh, image=num)
                    label2.place(x=58, y=9)
                    label2.config(bg='#1C2833')

                    crsh = Label(fencrsh, text='CRASH')
                    crsh.config(font=('Arial', 12), bg='#C80502', width="13")
                    crsh.config(fg="white")
                    crsh.grid(row=0, column=0, pady=74)

                    can1 = Canvas(fencrsh, width=50, height=0, )
                    can1.grid(row=2, column=1, rowspan=5, padx=0,
                              pady=35)  # première ligne, troisième colones, s'étaler sur 3 lignes,espace largueur et hauteur
                    fencrsh.after(2500, lambda: fencrsh.destroy())
                    fencrsh.mainloop()
                    print(grids[compt][0], info, 'il abbandonne')
                    w = grids[compt][3]
                    r = grids[compt][3] - 1
                    t = w
                    grids[r][4] = 'OUT'
                    while t != len(grids):
                        if grids[t][3] > w:
                            grids[t][3] = grids[t][3] - 1
                            print(grids[t][0], 'est désormais', grids[t][3], 'e')
                        t = t + 1
                    out.append([grids[r][0],grids[r][8]])
                    del grids[r]
                    r = 0
                    grids.sort(key=lambda x: x[3])
                    if compt == len(grids):
                        continue
                    compt += 1
                    print('\n')
                if tirageA == ['depassement'] and grids[compt][3] > 1:
                    depassement()
                    place = compt - 1
                    grids[compt][3] = grids[compt][3] - 1
                    grids[place][3] = grids[place][3] + 1
                    grids.sort(key=lambda x: x[3])
                    print('Tour', touract, ', Virage', virageact, ' : ', infodep, grids[place][0], 'sur',
                          grids[compt][0], '.',
                          grids[place][0],
                          'est desormais', grids[place][3], 'e et', grids[compt][0], grids[compt][3], 'e \n')
                    updown = Tk()
                    updown.title('Grille de départ')
                    updown.iconbitmap('race.ico')
                    updown.geometry("283x117")
                    head = PhotoImage(file=grids[compt][9])

                    label1 = Label(updown, image=head)
                    label1.place(x=-2, y=7)

                    up = PhotoImage(file='img/green.png')
                    label2 = Label(updown, image=up)
                    label2.place(x=77, y=16)

                    if grids[compt][3] < len(grids)+1:
                        a = -1
                    else:
                        a = 1
                    head2 = PhotoImage(file=grids[compt+a][9])
                    label1 = Label(updown, image=head2)
                    label1.place(x=136, y=7)

                    down = PhotoImage(file='img/red.png')
                    label2 = Label(updown, image=down)
                    label2.place(x=215, y=25)

                    depasse= Label(updown, text='DEPASSEMENT')
                    depasse.config(font=('Arial', 12), bg='#C80502', width="31")
                    depasse.config(fg="white")
                    depasse.grid(row=0, column=0, pady=93)

                    updown.after(2500, lambda: updown.destroy())
                    updown.mainloop()
                    effectue.append(grids[compt][0])
                    if compt == len(grids) or compt+1>len(grids):
                        continue
                    compt = compt + 1
                if tirageA == ['sortie']:
                    sanction()
                    grids[compt][5] = grids[compt][5] + 1
                    print('Nombre de fois sortie dans le vert pour ', grids[compt][0], ':', grids[compt][5], '\n')
                    effectue.append(grids[compt][0])
                    if grids[compt][5] == 3:
                        print(infosanc, grids[compt][0])
                    if grids[compt][5] >= 5 and grids[compt][3] < 15:
                        grids[compt][3] = grids[compt][3] + 5
                        print(infopenal, grids[compt][0], 'Il est maintenant ', grids[compt][3], ' eme \n')
                    if compt == len(grids):
                        continue
                    compt+=1
                if tirageA == ['bugmeca']:
                    probmeca()
                    o = 0
                    auhasard = randrange(0, len(grids))
                    print(grids[auhasard][0], meca, '\n')
                    w = grids[auhasard][3]
                    while o != len(grids):
                        if grids[o][3] > w:
                            grids[o][3] = grids[o][3] - 1
                        o += 1
                    out.append([grids[auhasard][0],grids[auhasard][8]])
                    del grids[auhasard]
                    grids.sort(key=lambda x: x[3])
                    if compt == len(grids):
                        continue
                    compt += 1
                if tirageA == ['rien']:
                    rien()
                    print('Tour', touract, ', Virage', virageact, ' : ', info, grids[compt][0], 'il est en', grids[compt][3],
                          'eme position \n')
                    effectue.append(grids[compt][0])
                    if compt == len(grids):
                        continue
                    compt += 1
                else:
                    continue
                    compt += 1
    virageact+=1
    compt = 0
    effectue = []
    if virageact == virage:
        virageact = 1
        fen = Tk()
        fen.title('Grille de départ')
        fen.iconbitmap('race.ico')
        fen.geometry("700x515")
        # Add image file
        bg = PhotoImage(file="race.png")

        label1 = Label(fen, image=bg)
        label1.place(x=200, y=-10)

        can1 = Canvas(fen, width=300, height=0, bg='#490103')

        nbtv = Label(fen, text=f"Classement du Tour {touract}, Virage {virageact}")
        nbtv.grid(row=1, column=7)
        nbtv.config(font=("Verdana", 20))

        g = 0
        while g != len(grids):
            test = Label(fen, text=grids[g][3])
            test.grid(row=g, column=0)
            test.config(font=("Verdana", 10))
            g += 1

        gs = 0
        while gs != len(grids):
            nom = Label(fen, text=grids[gs][0])
            nom.grid(row=gs, column=1)
            nom.config(font=("Verdana", 10))
            gs += 1

        nbout = 0
        while nbout != len(out):
            outitle = Label(fen, text='OUT')
            outitle.grid(row=gs + nbout, column=0)
            nbout += 1

        ch = 0
        while ch != len(out):
            crashed = Label(fen, text=out[ch][0])
            crashed.grid(row=gs + ch, column=1)
            crashed.config(font=("Verdana", 10))
            ch += 1

        can1.grid(row=2, column=7, rowspan=3, padx=100,
                  pady=5)  # première ligne, troisième colones, s'étaler sur 3 lignes,espace largueur et hauteur
        fen.after(2500, lambda: fen.destroy())
        fen.mainloop()
        touract+=1

if touract == tour:
    print(Second_Commentateur, "c'est la fin de course. Voici les 3 premiers de la course : ")
    l = 0
    while l != 3:    
        print(grids[l][3], 'e', grids[l][0], grids[l][8])
        l = l + 1
    print('\n')
    print('\n')
    print('ET voici l\'hymne',grids[0][8], 'pour la victoire de',grids[0][0])
    print('\n')
    print('Voici les résultats complet de la course : ')
    h = 0
    outpiste = 0
    while h != len(grids):
        print(grids[h][3], 'e', grids[h][0], grids[h][8])
        h+=1
    while outpiste != len(out):
        print('OUT', out[outpiste][0], out[outpiste][1])
        outpiste+=1
    print('\n Et voici le podium')
    podium = Tk()
    podium.title('Podium de la course')
    podium.iconbitmap('race.ico')
    podium.geometry("1100x615")

    podium.columnconfigure(0, weight=1)
    podium.columnconfigure(1, weight=3)

    head = PhotoImage(file=grids[0][11])
    label1 = Label(podium, image=head)
    label1.place(relx=0.5,rely=0.4,anchor=CENTER)


    frst = PhotoImage(file='img/podium.png')
    label1 = Label(podium, image=frst)
    label1.place(y=520,relx=0.5,anchor=CENTER)

    win  = Label(podium, text='WIN')
    win.pack(side='top')
    win.config(font=('Verdana',36))

    champ = PhotoImage(file='img/win.png')
    label1 = Label(podium, image=champ)
    label1.place(relx=0.58,rely=0.2,anchor=CENTER)

    nations = PhotoImage(file='img/'+grids[0][8]+'.png')
    label1 = Label(podium, image=nations)
    label1.place(y=220, relx=0.8, anchor=CENTER)


    places = Label(podium, text='1er')
    places.config(font=('Verdana',70),fg='gold')
    places.place(relx=0.3,rely=0.4,anchor=CENTER)


    podium.after(2000, lambda: podium.destroy())
    podium.mainloop()

    two = Tk()
    two.title('Podium de la course')
    two.iconbitmap('race.ico')
    two.geometry("1100x615")

    two.columnconfigure(0, weight=1)
    two.columnconfigure(1, weight=3)

    head = PhotoImage(file=grids[1][11])
    label1 = Label(two, image=head)
    label1.place(relx=0.5, rely=0.4, anchor=CENTER)

    deux = PhotoImage(file='img/podium2.png')
    label1 = Label(two, image=deux)
    label1.place(y=520, relx=0.5, anchor=CENTER)


    natio = PhotoImage(file='img/'+grids[1][8]+'.png')
    label1 = Label(two, image=natio)
    label1.place(y=220, relx=0.8, anchor=CENTER)

    win = Label(two, text='2eme')
    win.pack(side='top')
    win.config(font=('Verdana', 36))

    champ = PhotoImage(file='img/win.png')
    label1 = Label(two, image=champ)
    label1.place(relx=0.58, rely=0.2, anchor=CENTER)

    places = Label(two, text='2e')
    places.config(font=('Verdana', 70), fg='silver')
    places.place(relx=0.3, rely=0.5, anchor=CENTER)
    two.after(2000, lambda: two.destroy())
    two.mainloop()

    three = Tk()
    three.title('Podium de la course')
    three.iconbitmap('race.ico')
    three.geometry("1100x615")

    three.columnconfigure(0, weight=1)
    three.columnconfigure(1, weight=3)

    head = PhotoImage(file=grids[2][11])
    label1 = Label(three, image=head)
    label1.place(relx=0.5, rely=0.4, anchor=CENTER)

    trois = PhotoImage(file='img/podium3.png')
    label1 = Label(three, image=trois)
    label1.place(y=520, relx=0.5, anchor=CENTER)

    win = Label(three, text='3eme')
    win.pack(side='top')
    win.config(font=('Verdana', 36))

    champ = PhotoImage(file='img/win.png')
    label1 = Label(three, image=champ)
    label1.place(relx=0.58, rely=0.2, anchor=CENTER)

    nations3 = PhotoImage(file='img/'+grids[2][8]+'.png')
    label1 = Label(three, image=nations3)
    label1.place(y=220, relx=0.8, anchor=CENTER)

    places = Label(three, text='3e')
    places.config(font=('Verdana', 70), fg='#a07155')
    places.place(relx=0.3, rely=0.4, anchor=CENTER)
    three.after(2000, lambda: three.destroy())
    three.mainloop()