import pygame

from code.EndScreen import EndScreen
from code.Level import Level
from code.Menu import Menu
from code.Const import MENU_REPLAY, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                end_screen = EndScreen(self.window, level_return == 'win')
                end_result = end_screen.run(level_return)
                if end_result == MENU_REPLAY[0]:
                    continue
                elif end_result == MENU_REPLAY[1]:
                    pygame.quit()
                    quit()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
