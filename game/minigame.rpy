label exit_custom:
    $ renpy.full_restart()

init python:
    config.screen_width=1920
    config.screen_height=1080
    import json
    import time
    import pygame
    K1 = pygame.K_z
    K2 = pygame.K_x
    K3 = pygame.K_DOWN
    K4 = pygame.K_RIGHT

    def pos():
        return time.time() - t - timing
        return renpy.music.get_pos()

    def timing_update():
        store.timing = pause_delta()

    def pause_delta():
        return time.time() - t - renpy.music.get_pos()

    def miss():
        store.misses += 1
        store.combo = 0
        store.hp -= 10
        if hp <= 0:
            exit_from_minigame("lost")

    def hit():
        store.hits += 1
        store.combo += 1
        if (combo > max_combo):
            store.max_combo = combo
        store.hp += 1
        if hp > 100:
            store.hp = 100

    def exit_from_minigame(reason = "win"):
        data = json_load()
        renpy.scene()
        renpy.show(data["all tracks"][track]["background"])
        store.minigame_type = "None"
        renpy.hide_screen("show_vars")
        renpy.hide_screen("say_m")
        renpy.music.stop()
        if (reason == "win"):
            if (data["all tracks"][track]["best percent"] < percent):
                data["all tracks"][track]["best percent"] = percent
            data["all tracks"][track]["custom enable"] = 1
            data["all tracks"][track]["current_game"] = store.percent
            json_save(data)
            renpy.show_screen("MinigameResult", str(store.hits), str(store.max_combo), str(store.percent))
        else:
            data["all tracks"][track]["current_game"] = 0
            json_save(data)
            renpy.show_screen("MinigameResult", str(store.hits), str(store.max_combo), "No")
        store.my_pause = True
        #renpy.jump(store.exit)

    def chunk_update():
        if not store.my_pause:
            with renpy.open_file(filename) as file:
                last = objects_index_start + chunk + 50
                if (last > store.fsize):
                    last = store.fsize
                for notes in range(objects_index_start + chunk, last):
                    split = str(N[notes]).split("'")[1].split(",")
                    #test += str(int(int(split[0])/128)) + " " + split[2] + "\n"
                    sy = int(int(split[0])/128)
                    sx = int(split[2]) / 1000
                    if (sy == 0):
                        sprites1.append(RhythmD(sprite1, default_speed, sx, 1))
                    if (sy == 1):
                        sprites2.append(RhythmD(sprite2, default_speed, sx, 2))
                    if (sy == 2):
                        sprites3.append(RhythmD(sprite3, default_speed, sx, 3))
                    if (sy == 3):
                        sprites4.append(RhythmD(sprite4, default_speed, sx, 4))

    class RhythmD(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = leftX - 50 - note_size + ypos * distance_b_lines
            self.show.y = -100
            self.moving = False # No point in checking if it isn't.

        def update(self):
            if not store.my_pause:
                if self.delay < pos() + line / self.speed:
                    self.moving = True
                    dt = (pos() - self.delay)
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
        if not store.my_pause:
            if store.is_dialogs_exist:
                if (store.dialog_minigame_index < len(dialogs["events"])):
                    if (pos() >=dialogs["events"][store.dialog_minigame_index][0]):
                        renpy.show_screen("say_m", dialogs["events"][store.dialog_minigame_index][2], dialogs["events"][store.dialog_minigame_index][1])
                        store.dialog_minigame_index+=1
            if (len(sprites1) + len(sprites2) + len(sprites3) + len(sprites4) < 30):
                if (store.fsize > objects_index_start + chunk):
                    chunk_update()
                    store.chunk += 50
            if (pos() > playing_time):
                exit_from_minigame()
                renpy.restart_interaction()
            for sprite in sprites1[:]:
                sprite.update()
                if sprite.y > config.screen_height:
                    miss()
                    sprite.show.destroy()
                    sprites1.remove(sprite)
                    renpy.restart_interaction()
            for sprite in sprites2[:]:
                sprite.update()
                if sprite.y > config.screen_height:
                    miss()
                    sprite.show.destroy()
                    sprites2.remove(sprite)
                    renpy.restart_interaction()
            for sprite in sprites3[:]:
                sprite.update()
                if sprite.y > config.screen_height:
                    miss()
                    sprite.show.destroy()
                    sprites3.remove(sprite)
                    renpy.restart_interaction()
            for sprite in sprites4[:]:
                sprite.update()
                if sprite.y > config.screen_height:
                    miss()
                    sprite.show.destroy()
                    sprites4.remove(sprite)
                    renpy.restart_interaction()
            if (hits + misses != 0):
                store.percent = int(hits / (misses + hits) * 100)
            else:
                store.percent = 100
        return 0.01

    def sprites_event(ev, x, y, st):
        if not store.my_pause:
            if ev.type == pygame.KEYDOWN:
                if ev.key == K1:
                    is_hit = False
                    for sprite in sprites1[:]:
                        if sprite.moving:
                            if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                                hit()
                                is_hit = True
                                # We destroy the sprite, making it impossible to it twice :)
                                sprite.show.destroy()
                                sprites1.remove(sprite)
                                break
                    if not is_hit:
                        miss()
                    renpy.restart_interaction()
                if ev.key == K2:
                    is_hit = False
                    for sprite in sprites2[:]:
                        if sprite.moving:
                            if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                                hit()
                                is_hit = True
                                # We destroy the sprite, making it impossible to it twice :)
                                sprite.show.destroy()
                                sprites2.remove(sprite)
                                break
                    if not is_hit:
                        miss()
                    renpy.restart_interaction()
                if ev.key == K3:
                    is_hit = False
                    for sprite in sprites3[:]:
                        if sprite.moving:
                            if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                                hit()
                                is_hit = True
                                # We destroy the sprite, making it impossible to it twice :)
                                sprite.show.destroy()
                                sprites3.remove(sprite)
                                break
                    if not is_hit:
                        miss()
                    renpy.restart_interaction()
                if ev.key == K4:
                    is_hit = False
                    for sprite in sprites4[:]:
                        if sprite.moving:
                            if int(sprite.y) > line - dl and int(sprite.y) < line + dl:
                                hit()
                                is_hit = True
                                # We destroy the sprite, making it impossible to it twice :)
                                sprite.show.destroy()
                                sprites4.remove(sprite)
                                break
                    if not is_hit:
                        miss()
                    renpy.restart_interaction()

screen show_vars:
    #text "Misses: [misses], Hits: [hits]! \nCombo: [combo]" + ", Percent: [percent]%, T: " + str(pause_delta()) xalign 0.5
    text f'{hits:0{6}}':
        pos (leftX - 200, 0)
    text "[combo]":
        pos (leftX + int(distance_b_lines * 3 / 2) , 540)
    text "___________________":
        pos (leftX-40, line + dl -10)
    text "___________________":
        pos (leftX-40, line - dl +10)
    bar:
        value int(hp)
        range 100
        pos (leftX + int(distance_b_lines * 3.8), 580)
        xysize(15,500)
        bar_vertical True
    text "[test]":
        pos (500, 300)



label start_minigame():
    $ store.my_pause = False
    if not ( _game_menu_screen == "PauseMenu") :
        $ _game_menu_screen = "PauseMenu"
    scene d
    $ data = json_load()["all tracks"][track]
    $ renpy.show(data["background"])
    $ leftX = 350
    show note_bg1:
        xpos leftX - 50
    show fan_orig at right
    python:
        is_dialogs_exist = data["dialogs"]
        if is_dialogs_exist:
            dialogs = json_load("dialog_minigame")[store.track]
        store.dialog_minigame_index = 0
        store.timing = 0
        percent = 100
        note_size = 50
        distance_b_lines = 80
        flag = False
        playing_time = data["playing time"]
        line = 900
        dl = 100

        hits = 0
        misses = 0
        combo = 0
        max_combo = 0
        hp = 100

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
        test = ""
        for find in renpy.list_files():
            if (find.split("/")[-1] == data["file"]):
                filename = find
        # ОСУ конвертер
        data = file_load(filename)

        #renpy.jump(store.exit)

        renpy.show_screen("show_vars")
        renpy.show("_", what=manager, zorder=1)
    while True:
        $ result = ui.interact()
