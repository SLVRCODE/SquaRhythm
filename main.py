import pygame

# for now
WIN_WIDTH   :int = 800
WIN_HEIGHT  :int = 600

WIN_TITLE   :str = "Squarhythm"
WIN_FPS     :int = 60

class SceneID:
    mainMenu    :int = 0
    settings    :int = 1
    gameplay    :int = 2

class Keybindings:
    stopRunning     :int = pygame.K_ESCAPE

class Game:
    def __init__(self):
        self.winSize    :tuple = (WIN_WIDTH, WIN_HEIGHT)
        pygame.init()
        
        self.window = pygame.display.set_mode(self.winSize)
        pygame.display.set_caption(WIN_TITLE)

        self.FPS        :int = WIN_FPS
        self.pyClock = pygame.time.Clock()

        self.running    :bool = False
        self.mouseHovering:bool = False

        self.sceneID    :SceneID
        self.swapScene(SceneID.mainMenu)

    def startMainLoop(self):
        self.running = True

        while self.running:
            self.pyClock.tick(self.FPS)

            self.drawUserInterface()
            self.processInputs()
        
        pygame.quit()

    def processInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYUP:
                if event.key == Keybindings.stopRunning:
                    self.running = False
                    return

    def drawUserInterface(self):
        pass # make a list of objects then draw them

    def swapScene(self, sceneID: SceneID):
        self.sceneID = sceneID

if __name__ == "__main__":
    game = Game()
    game.startMainLoop()

    exit(0)
