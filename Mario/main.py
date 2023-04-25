# 编写者：akira
# 时间：2022/7/4 20:39
# 游戏入口

import os
import sys
import pygame

from source import constants as C

from source import setup, tools
from source.statues import main_menu, level, load_screen


def main():
    # 定义1
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level(),
        'game_over': load_screen.GameOver(),
        'level2': level.Level2(),
        'load_level2': load_screen.Load_level2(),
        'level3': level.Level3(),
        'load_level3': load_screen.Load_level3(),
        'level4': level.Level4(),
        'load_level4': load_screen.Load_level4()

    }

    game_info = {
        'statue': 'main_menu',
        'score': 0,
        'top_score': 0,
        'coin': 0,
        'current_time': 0,
        'lives': 1,
        'player_state': 'small',
        'time': 300
    }

    initGame()
    current_state = state_dict['main_menu']
    current_state.start(game_info, 0.0, pygame.display.get_surface())
    current_time = 0.0

    while True:

        for event in pygame.event.get():  # 循环获取事件，监听事件状态
            if event.type == pygame.QUIT:   # 判断用户是否点了"X"关闭按钮,并执行if代码段
                pygame.quit()
                return

        if current_state.finished:  # 判断该状态是否结束
            current_statefinished = False
            current_state = state_dict[current_state.next]
            current_state.start(game_info, current_time,
                                pygame.display.get_surface())

        current_state.update(pygame.display.get_surface(), pygame.key.get_pressed(),
                             current_time)  # 当前状态为结束，调用该状态的更新方法

        pygame.display.update()
        pygame.time.Clock().tick(60)


def initGame():
    # 初始化pygame, 设置展示窗口
    pygame.init()

    pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))  # 屏幕
    pygame.display.set_caption('Mario')

    os.chdir(os.path.dirname(sys.argv[0]))  # 设置当前工作区，确保所有相对路径都基于项目主目录

    setup.GRAPHICS = tools.load_graphics(
        os.path.join("resources", "graphics"))
    setup.SOUND = tools.load_all_sound(os.path.join(
        "resources", "sound"))
    setup.MUSIC = tools.load_all_music(os.path.join(
        "resources", "music"))


if __name__ == '__main__':  # test
    main()
