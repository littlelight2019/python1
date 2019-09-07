# from sys import exit
from random import randint

class Engine(object):
    def __init__(self, firstScene):
        self.current_scene = firstScene
    def play(self):
        while True:
            print("\n-------")
            self.current_scene = self.current_scene.enter()

class Scene(object):
    pass

class Death(Scene):
    def enter(self):
        print("No luck; game ends")
        print("too bad")
        next = input("Try again? Hit any key to continue; 0 to end: >")
        if next != "0":
            global attempt
            attempt += 1
            print("Attempt NO. %d" % attempt)
            return CentralCorridor()
        else:
            print("Good bye; see you next time!")
            return End()


class CentralCorridor(Scene):
    def enter(self):
        print("Welcome to the CentralCorridor...[chance is 1/3]")
        luck = randint(0,2)
        if luck != 0:
            return Death()
        else:
            print("Congratulations! You get to enter LaserWeaponArmory")
            return LaserWeaponArmory()

class LaserWeaponArmory(Scene):
    def enter(self):
        print("Welcome to the Laser Weapon Armory...try to get the code for the bomb...[chance is 1/10]")
        getCode = False
        codes = []
        for chance in range(0,10):
            luck = "%d%d" % (randint(0,9), randint(0,9))
            if luck == "77":
                getCode = True
                break
            codes.append(luck)
        if getCode:
            print("You got the right code for the bomb! Go to The Bridge")
            return TheBridge()
        else:
            print("Sorry your code %s does not work" % str(codes))
            return Death()

class TheBridge(Scene):
    def enter(self):
        print("Welcome to the bridge...try to carry and place the bomb...[chance is 1/2]")
        luck = randint(0,1)
        if luck != 0:
            return Death()
        else:
            print("Congratulations! you placed the bomb and now go to Escape Pod")
            return EscapePod()

class EscapePod(Scene):
    def enter(self):
        print("Welcome to the EscapePod...try to enter the right pod...[chance is 1/5]")
        luck = randint(0,4)
        if luck != 0:
            return Death()
        else:
            print("Congratulations! you escaped and win the game")
            return End()

class End(Scene):
    def enter(self):
        exit(0)

if __name__ == '__main__':
    initScene = CentralCorridor()
    global attempt
    attempt = 1
    print("Attempt NO. %d" % attempt)
    a_game = Engine(initScene)
    a_game.play()
