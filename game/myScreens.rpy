screen Stickerbook():
    tag menu
    image "images/screens/screen_stickerbook.jpg"
    python:
        store.data_achivements = load("achivements")
        style.musicroom_musiclabel = Style(style.button_text)
        style.musicroom_musiclabel.color = "#FF0000"
        style.musicroom_musiclabel.hover_color = "#0000FF"
    textbutton _("Вернуться") action Return():
        text_style "musicroom_musiclabel"
    for images in data_achivements:
        if data_achivements[images]["unlocked"] == 1:
            image "images/achivements/"+data_achivements[images]["image"]:
                xalign data_achivements[images]["x"]
                yalign data_achivements[images]["y"]


label to_minigame(name = track_to_play):
    $ minigame(name, "exit_custom")
    $ renpy.full_restart()

screen CustomPlay():
    tag menu
    image "images/screens/screen_customplay.jpg"
    python:
        store.data = load()["all tracks"]
        store.track_to_play = ""
    vbox:
        for tracks in data:
            if (data[tracks]["custom enable"] == 1):
                textbutton tracks + ": " +str(data[tracks]["best percent"]) + "%".ljust(100) action [SetVariable("track_to_play", tracks), Start("to_minigame")]:
                    background "images/screens/button_bg_idle.png"
                    hover_background "images/screens/button_bg_hovered.png"
                null height 70
        xalign 0.2
        yalign 0.2
    textbutton _("Вернуться") action Return()

screen say_m(what, who = ""):
    image "images/screens/screen_window_small.png":
        xpos 0.45
        ypos 0.7
    text who:
        xpos 0.45
        ypos 0.7
    text what:
        xpos 0.45
        ypos 0.75


init python:
    def pause_show():
        store.pause = True
        renpy.music.set_pause(True)
        return
    def pause_hide():
        store.pause = False
        if minigame_type == "piano":
            timing_update()
        renpy.music.set_pause(False)
        return

screen PauseMenu():
    on "show" action Function(pause_show)
    on "hide" action Function(pause_hide)

    tag menu
    image "images/screens/screen_pause.png"
    vbox:
        imagebutton:
            idle "images/screens/button_continue_idle.png"
            hover "images/screens/button_continue_hovered.png"
            action Return()
        null height 20
        if store.minigame_type != "None":
            imagebutton:
                idle "images/screens/button_retry_idle.png"
                hover "images/screens/button_retry_hovered.png"
                action [Start("start_minigame")]
            null height 20
        imagebutton:
            idle "images/screens/button_main_menu_idle.png"
            hover "images/screens/button_main_menu_hovered.png"
            action MainMenu()
        xalign 0.45
        yalign 0.45

screen MinigameResult(score, combo, percent):
    vbox:
        text "Score: " + score
        text "Combo: " + combo
        text "Percent: " + percent + "%"
        xalign 0.45
        yalign 0.45
    textbutton "Restart":
        action [Hide(), Jump("start_minigame")]
        xalign 0.3
        yalign 0.9
    textbutton "Continue":
        action [Hide(), Jump(store.exit)]
        xalign 0.7
        yalign 0.9
