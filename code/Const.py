# Window size
import pygame


WIN_WIDTH = 720
WIN_HEIGHT = 405

# Menu Text
TITLE_TEXT_COLOR = (255, 128, 0)
OPTIONS_TEXT_COLOR = (255, 255, 255)
OPTIONS_ACTIVE_TEXT_COLOR = (255, 215, 0)
HUD_PLAYER_HEALTH = (255, 0, 0)

# Menu Options
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'EXIT')

MENU_REPLAY = ('PLAY AGAIN',
               'EXIT')

CONTROLS = ('Player 1 Movement:',
            '- Up, Down, Left, Right',
            'Player 1 Shoot:',
            '- Hold Right CTRL',
            'Player 2 Movement:',
            '- W, S, A, D',
            'Player 2 Shoot:',
            '- Hold Left CTRL',)

# Entities
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 4,
    'Player2': 4,
    'Enemy1': 3,
    'Enemy2': 2,
    'Player1Shoot': 5,
    'Player2Shoot': 5,
    'Enemy1Shoot': 4,
    'Enemy2Shoot': 3,
    'Boss': 0,
    'BossShoot': 6,
}

ENTITY_HEALTH = {
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'Level1Bg3': 9999,
    'Level1Bg4': 9999,
    'Level1Bg5': 9999,
    'Level1Bg6': 9999,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shoot': 1,
    'Player2Shoot': 1,
    'Enemy1Shoot': 1,
    'Enemy2Shoot': 1,
    'Boss': 10,
    'BossShoot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shoot': 25,
    'Player2Shoot': 25,
    'Enemy1Shoot': 10,
    'Enemy2Shoot': 15,
    'Boss': 1,
    'BossShoot': 50,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 150,
    'Player1Shoot': 0,
    'Player2Shoot': 0,
    'Enemy1Shoot': 0,
    'Enemy2Shoot': 0,
    'Boss': 0,
    'BossShoot': 1000,
}

ENTITY_SHOOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 75,
    'Enemy2': 115,
    'Boss': 45,
}

# Events
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

# Controls
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}
