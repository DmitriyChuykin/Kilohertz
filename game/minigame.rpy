init python:
    config.screen_width=1920
    config.screen_height=1080
    import time
    import pygame
    #import json
    K1 = pygame.K_z
    K2 = pygame.K_x
    K3 = pygame.K_DOWN
    K4 = pygame.K_RIGHT

    def chunk_update():
        with renpy.open_file(filename) as file:
            last = objects_index_start + chunk + 50
            if (last > fsize):
                last = fsize
            for notes in range(objects_index_start + chunk, last):
                split = str(N[notes]).split("'")[1].split(",")
                #test += str(int(int(split[0])/128)) + " " + split[2] + "\n"
                sy = int(int(split[0])/128)
                sx = int(split[2]) / 1000 + music_delay + music_countdown
                if (sy == 0):
                    sprites1.append(RhythmD(sprite1, default_speed + sx, sx, 1))
                if (sy == 1):
                    sprites2.append(RhythmD(sprite2, default_speed + sx, sx, 2))
                if (sy == 2):
                    sprites3.append(RhythmD(sprite3, default_speed + sx, sx, 3))
                if (sy == 3):
                    sprites4.append(RhythmD(sprite4, default_speed + sx, sx, 4))

    class RhythmD(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = leftX - 50 + ypos * 50
            self.show.y = -100
            self.moving = False # No point in checking if it isn't.

        def update(self):
            if store.t + self.delay < time.time() + line / self.speed:
                self.moving = True
                dt = (time.time() - store.t - self.delay)
                self.y = line + self.speed * dt
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):

            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    def sprites_update(st):
        if (len(sprites1) + len(sprites2) + len(sprites3) + len(sprites4) < 30):
            if (fsize > objects_index_start + chunk):
                chunk_update()
                store.chunk += 50
        if (time.time() - t - music_countdown > playing_time):
            renpy.jump("exit")
        for sprite in sprites1[:]:
            sprite.update()
            if sprite.y > config.screen_height:
                store.misses += 1
                store.combo = 0
                sprite.show.destroy()
                sprites1.remove(sprite)
                renpy.restart_interaction()
        for sprite in sprites2[:]:
            sprite.update()
            if sprite.y > config.screen_height:
                store.misses += 1
                store.combo = 0
                sprite.show.destroy()
                sprites2.remove(sprite)
                renpy.restart_interaction()
        for sprite in sprites3[:]:
            sprite.update()
            if sprite.y > config.screen_height:
                store.misses += 1
                store.combo = 0
                sprite.show.destroy()
                sprites3.remove(sprite)
                renpy.restart_interaction()
        for sprite in sprites4[:]:
            sprite.update()
            if sprite.y > config.screen_height:
                store.misses += 1
                store.combo = 0
                sprite.show.destroy()
                sprites4.remove(sprite)
                renpy.restart_interaction()
        return 0.01

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.KEYDOWN:
            if ev.key == K1:
                hit = False
                for sprite in sprites1[:]:
                    if sprite.moving:
                        if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                            store.hits += 1
                            store.combo += 1
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites1.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                renpy.restart_interaction()
            if ev.key == K2:
                hit = False
                for sprite in sprites2[:]:
                    if sprite.moving:
                        if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                            store.hits += 1
                            store.combo += 1
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites2.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                renpy.restart_interaction()
            if ev.key == K3:
                hit = False
                for sprite in sprites3[:]:
                    if sprite.moving:
                        if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                            store.hits += 1
                            store.combo += 1
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites3.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                renpy.restart_interaction()
            if ev.key == K4:
                hit = False
                for sprite in sprites4[:]:
                    if sprite.moving:
                        if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                            store.hits += 1
                            store.combo += 1
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites4.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                    store.combo = 0
                renpy.restart_interaction()

screen show_vars:
    text "Misses: [misses], Hits: [hits]! \nCombo: [combo], Chunk/Size [chunk]/ " + str(fsize-objects_index_start) + ":, T: " + str(int(time.time() - t - music_countdown)) xalign 0.5
    text "_":
        pos (leftX, line + dl -10)
    text "_":
        pos (leftX + 50, line + dl -10)
    text "_":
        pos (leftX + 100, line + dl -10)
    text "_":
        pos (leftX + 150, line + dl -10)
    text "_":
        pos (leftX, line - dl +10)
    text "_":
        pos (leftX + 50, line - dl +10)
    text "_":
        pos (leftX + 100, line - dl +10)
    text "_":
        pos (leftX + 150, line - dl +10)
    text "[test]":
        pos (500, 300)

label minigame:
    scene scene2 with Dissolve(2)
    python:
        flag = False
        playing_time = 120
        t = time.time()
        leftX = 500
        line = 900
        dl = 60
        hits = 0
        misses = 0
        combo = 0
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        sprite1 = "images/1.png"
        sprite2 = "images/2.png"
        sprite3 = "images/3.png"
        sprite4 = "images/4.png"
        sprites1 = []
        sprites2 = []
        sprites3 = []
        sprites4 = []
        default_speed = 400
        music_countdown = 3
        test = ""
        for find in renpy.list_files():
            if (find.split(".")[-1] == "osu"):
                filename = find
        # ОСУ конвертер
        with renpy.open_file(filename) as file:
            N = file.readlines()
            fsize = len(N)
            track = str(N[3]).split(":")[1].split("\\")[0].lstrip()
            #music_delay = int(str(N[51]).split("'")[1].split(",")[0])/1000
            music_delay = 0
            renpy.music.play(["<silence " + str(music_countdown) +">","OSU_Maps/" +track], "music")
            #test = str(N[234]).split("'")[1].split("\\")[0] == "[HitObjects]"
            objects_index_start = N.index(bytes('[HitObjects]\r\n', 'utf-8')) + 1
            #for notes in range(objects_index_start+1,fsize):
            chunk = 0
            if (fsize < objects_index_start + chunk):
                chunk = fsize - objects_index_start
            for notes in range(objects_index_start,objects_index_start+chunk):
                split = str(N[notes]).split("'")[1].split(",")
                #test += str(int(int(split[0])/128)) + " " + split[2] + "\n"
                sy = int(int(split[0])/128)
                sx = int(split[2]) / 1000 + music_delay + music_countdown
                if (sy == 0):
                    sprites1.append(RhythmD(sprite1, default_speed + sx, sx, 1))
                if (sy == 1):
                    sprites2.append(RhythmD(sprite2, default_speed + sx, sx, 2))
                if (sy == 2):
                    sprites3.append(RhythmD(sprite3, default_speed + sx, sx, 3))
                if (sy == 3):
                    sprites4.append(RhythmD(sprite4, default_speed + sx, sx, 4))
                #test += str(N[line]) + "\n"
        """
        with renpy.open_file('song1.txt') as json_file:
            data = json.load(json_file)
            for buff in data['sprites1']:
                sprites1.append(RhythmD(sprite1, default_speed, buff, 1))
            for buff in data['sprites2']:
                sprites2.append(RhythmD(sprite2, default_speed, buff, 2))
            for buff in data['sprites3']:
                sprites3.append(RhythmD(sprite3, default_speed, buff, 3))
            for buff in data['sprites4']:
                sprites4.append(RhythmD(sprite4, default_speed, buff, 4))
        """
        renpy.show_screen("show_vars")
        renpy.show("_", what=manager, zorder=1)
    while True:
        $ result = ui.interact()

label exit:
    stop music
    hide screen show_vars
    jump day0_1
