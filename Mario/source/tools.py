# 编写者：akira
# 时间：2022/7/4 21:25
# 工具和游戏主控

import pygame
import random
import os


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        # print(name,ext)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():  # 判断图片是否是透明底格式，抠完图专用的
                img = img.convert_alpha()  # convert_alpha()方法会使用透明的方法绘制前景对象
                # print(img,type(img))
            else:
                img = img.convert()
                # print(img, type(img))
            graphics[name] = img
    return graphics


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_sound(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')):

    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pygame.mixer.Sound(os.path.join(directory, fx))
    return effects


def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))  # 创建一个和方框一样大的一个图层
    # pygame.Surface.blit() 将一个图像（Surface 对象）绘制到另一个图像上  第一个参数为图片，第二个为坐标，第三个为
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)  # 将该颜色设置为透明
    image = pygame.transform.scale(
        image, (int(width*scale), int(height*scale)))
    return image


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def start(self, persistant, current_time):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass
