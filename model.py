from random import randint

class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360)

class Engine(object):
        def __init__(self):
            self.self.throttlePosition=0
            self.self.theGearbox=Gearbox()
            self.currentRpm=0
            self.consumptionConstant=0.0025
            self.maxRpm=100
            self.theTank=Tank()

        def updateModel(self, dt):
            if self.theTank > 0:
                self.currentRpm=self.throttlePosition*self.maxRpm

class Gearbox(object):
    def __init__(self):
        self.gears = [0,0.8,1,1.4,2.2,3.8]
        self.currentGear = 0
        self.clutchEngaged = False
        self.wheels = ['frontLeft', 'frontRight', 'rearLeft', 'rearRight']

    def shiftUp(self):
        if self.currentGear < len(self.gears) or self.clutchEngaged = True:
            self.currentGear = self.currentGear +1

    def shiftDown(self):
        if self.currentGear > 0 or self.clutchEngaged = True:
            self.currentGear = self.currentGear -1

    #def rotate(self, revolutions):
    #    if self.clutchEngaged = True:
    #        rotate(Wheel())

class Tank(object):
    pass
