from ex44_gameEscapeModule import *

class Engine(object):
    def __init__(self, firstScene):
        self.current_scene = firstScene
    def play(self):
        while not isinstance(self.current_scene, End):
            print("\n-------")
            self.current_scene = self.current_scene.enter()

if __name__ == '__main__':
    initScene = CentralCorridor()
    a_game = Engine(initScene)
    a_game.play()
