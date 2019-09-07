from ex44 import *

class Engine(object):
    def __init__(self, firstScene):
        self.current_scene = firstScene
    def play(self):
        while True:
            print("\n-------")
            self.current_scene = self.current_scene.enter()

if __name__ == '__main__':
    initScene = CentralCorridor()
    a_game = Engine(initScene)
    a_game.play()
