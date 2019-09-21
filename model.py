from random import randint #randint bliver hentet fra pakken random, som bruges senere for at fine et tilfældigt tal ud fra givne tal.

# Kode til min bil, hej Martin :)

class Car(object): #Her er min Car klasse, her bliver modellen opdateret
    def __init__(self): #Den her del af koden kører så snart at klassen bliver kørt. "__init__" vil være det samme alle de fire gange det bliver brugt, så jeg vil kun forklare hvis der sker noget nyt.
        self.theEngine = Engine() # Jeg definerer theEngine til at være Engine klassen

    def updateModel(self,dt): #Denne funktion sørger for at opdaterer modellen i delta tid, som er en matematisk præcis tidsbegreb.
        self.theEngine.updateModel(dt)

class Wheel(object): #Her er min Wheel klasse, som sørger for at hjulene på bussen drejer rundt rundt rundt, rundt rundt rundt.
    def __init__(self):
        self.orientation = randint(0,360) #Jeg definerer "orientation" til at være et tilfældigt tal mellem 0 og 360, fordi der er 360 grader i en cirkel.

    def rotate(self, revolutions): #Denne funktion rotererer hjulene, som er afhængig af "revolutions" og orientation.
        self.orientation=(self.orientation+(revolutions*360)) % 360 #revolutions bliver defineret når funktionen og klassen bliver kaldt.

class Engine(object): #Her er min Engine klasse, der sørger for at motoren fungerer sammen.
        def __init__(self):
            self.throttlePosition=0
            self.theGearbox=Gearbox() #theGearbox er afhængig af Gearbox klassen, så den definerer jeg til at være det
            self.currentRpm=0 #Fart på bilen
            self.consumptionConstant=0.0025 #Hvor meget benzin der bliver suget
            self.maxRpm=100 #Maksimum fart
            self.theTank=Tank() #theTank bliver defineres som klassen Tank, da tanken er tank

        def updateModel(self, dt): #Opdaterer modellen med de forskellige hastigheder
            if self.theTank.contents > 0: #Hvis tanken ikke er tom, så sker denne del
                self.currentRpm=self.throttlePosition*self.maxRpm #sætter hastighed
                self.theTank.remove(self.currentRpm*self.consumptionConstant) #mængden af benzin der bliver fjernet, efter hastighed og benzin consumption
                self.theGearbox.rotate(self.currentRpm*(dt/60)) #skal roterer hjul efter hastighed, så de drejer hurtigerer
            else: #Hvis tanken er tom, så sker denne del
                self.currentRpm=0 #Sætter hastighed til 0

class Gearbox(object): #Her er min gearbox klasse, som sørger for at gearboxen fungerer
    def __init__(self):
        self.gears = [0,0.8,1,1.4,2.2,3.8] #Laver en liste til hver gear konstant
        self.currentGear = 0 #Når klassen køres, så skal den starte i nulte gear
        self.clutchEngaged = False #Automatisk er clutchen slået fra
        self.wheels = {'frontLeft':Wheel(), 'frontRight':Wheel(), 'rearLeft':Wheel(), 'rearRight':Wheel()} #Laver hvert hjul til en instans af hjul klassen

    def shiftUp(self): #I denne funktion bliver gearet sat op
        if self.currentGear == (len(self.gears)-1) or self.clutchEngaged == True:
            pass #Så længe at den er på det højeste gear, eller at clutchen er slået til, så sker der ikke noget
        else:
            self.currentGear = self.currentGear +1 #Ellers ligger den en til gearet

    def shiftDown(self): #I denne funktion bliver gearet slået ned
        if self.currentGear > 0 or self.clutchEngaged == True: #Så længe at gearet ikke er på nul, eller clutchen er slået til, så sker der ikke noget
            pass
        else:
            self.currentGear = self.currentGear -1 #ELlers trækker den en fra gearet

    def rotate(self, revolutions): #Denne del rotererer alle hjulene hvis clutchen er slået til
        if self.clutchEngaged == True:
            for wheel in self.wheels:
                self.wheels[wheel].rotate(revolutions*self.gears[self.currentGear])

class Tank(object): #I denne klasse definerer jeg tanken
    def __init__(self):
        self.capacity=100 #Sætter max gas til at være 100
        self.contents=100 #Sætter start gas til at være 100

    def remove(self, amount): #Hvor meget der skal fjernes fra tanken
        if self.contents > amount: #Fjerner så længe at der er det den vil trække fra ikke er mere end der er benzin
            self.contents -= amount
        else: #Ellers så er mængden nul, hvis det er den ikke kan tage noget fra
            self.contents = 0

    def refuel(self): #Refuel knappen funktionen, jeg er træt
        self.contents = self.capacity #sætter benzin til max benzin hej godnat
