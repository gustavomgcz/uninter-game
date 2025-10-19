import random
import pygame

from code.Boss import Boss
from code.Const import EVENT_ENEMY, EVENT_TIMEOUT, HUD_PLAYER_HEALTH, OPTIONS_TEXT_COLOR, WIN_HEIGHT, MENU_OPTION, WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator

from pygame import Surface, Rect
from pygame.font import Font

from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 60000  # 60s
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, random.randint(1000, 3500))
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        boss_spawned = False
        while True:
            clock.tick(60)

            players_alive = [ent for ent in self.entity_list if isinstance(
                ent, Player) and ent.health > 0]
            if not players_alive:
                return 'lose'

            boss_alive = [boss for boss in self.entity_list if isinstance(
                boss, Boss) and boss.health > 0]

            if boss_spawned and not boss_alive:
                return 'win'

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy, Boss)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(
                        16, f'Player1 - Health: {ent.health} | Score: {ent.score}', HUD_PLAYER_HEALTH, (10, 10))
                if ent.name == 'Player2':
                    self.level_text(
                        16, f'Player2 - Health: {ent.health} | Score: {ent.score}', HUD_PLAYER_HEALTH, (10, 30))
                if ent.name == 'Boss':
                    self.level_text(
                        16, f'Boss Health: {ent.health}', HUD_PLAYER_HEALTH, (WIN_WIDTH - 110, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout <= 0 and not boss_spawned:
                        boss_spawned = True
                        self.entity_list.append(
                            EntityFactory.get_entity('Boss'))

            self.level_text(
                14, self.name, OPTIONS_TEXT_COLOR, (WIN_WIDTH / 2, 5))
            if self.timeout > 0:
                self.level_text(
                    14, f'Boss arriving in: {self.timeout / 1000:.1f}s', OPTIONS_TEXT_COLOR, (WIN_WIDTH / 2 - 35, 20))
            self.level_text(
                14, f'fps: {clock.get_fps():.0f}', OPTIONS_TEXT_COLOR, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
