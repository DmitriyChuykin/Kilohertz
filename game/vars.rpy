define max = Character('Максим', color="#4682B4") #SteelBlue
define vera = Character('Вероника', color="#FF69B4") #HotPink
define eva = Character('Ева', color="#191970") #MidnightBlue
define alia = Character('Алия', color="#F5DEB3") #Wheat (Бежевый)
define misha = Character('Миша', color="#F5DEB3")
define eugene = Character('Евгений', color="#F5DEB3")
define stas = Character('Стас', color="#999999")
define ar = Character('Айрат Рустемович', color="999999")

define fan = Character('Фанатка', color="#999999")
define fan1 = Character('Толпа', color="#999999")
define pasha = Character('Паша', color="#999999")
define nurse = Character('Медсестра', color="#999999")
define q = Character('???', color="#999999")
define barmen = Character('Бармен', color="#999999")

define audio.fall = "audio/fall.mp3"
define audio.mainMusic = "audio/main music.mp3"
define audio.marker = "audio/marker.mp3"
define audio.medicalMonitor = "audio/medical monitor.mp3"
define audio.rockConcert = "audio/rock concert 1.mp3"
define audio.schoolRuler = "audio/school ruler.mp3"
define audio.train = "audio/train.mp3"
define audio.upsettingFans = "audio/upsetting fans.mp3"
define audio.waitingFans = "audio/waiting fans.mp3"
define audio.cough = "audio/сough.mp3"

init python:
    import json

    def file_load(filename):
        with renpy.open_file(filename) as file:
            store.N = file.readlines()
            store.fsize = len(N)
            for find in renpy.list_files():
                if (find.split("/")[-1] == str(N[3]).split(":")[1].split("\\")[0].lstrip()):
                    store.musicfile = find
            #music_delay = int(str(N[51]).split("'")[1].split(",")[0])/1000
            music_delay = 0
            renpy.music.play(musicfile, "music")
            store.t = time.time()
            store.minigame_type = "piano"
            i = 0
            while (not (str(N[i]).split("'")[1].split("\\")[0]  == "[HitObjects]")):
                i+=1
            store.objects_index_start = i + 1
            #test = "|" + str(N[157]) + "|" + str(bytes('[HitObjects]\r\n', 'utf-8')) + "|"
            #test = N.index(bytes('[HitObjects]\r\n', 'utf-8')) + 1
            store.chunk = 0
            if (fsize < objects_index_start + chunk):
                store.chunk = fsize - objects_index_start
            file.close()
            for notes in range(objects_index_start,objects_index_start+chunk):
                split = str(N[notes]).split("'")[1].split(",")
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
            return 1

    def json_load(file = "musics"):
        with open(config.gamedir + "/database/" + file + ".json", encoding='utf-8') as json_file:
            return json.load(json_file)
            json_file.close()

    def json_save(data, file = "musics"):
        with open(config.gamedir + "/database/" + file + ".json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, separators=(',', ': '), ensure_ascii=False)
            json_file.close()

    def minigame(track, exit):
        renpy.config.skipping = None
        data = json_load()
        store.track = track
        store.exit = exit
        json_save(data)
        renpy.call("start_minigame")

    def get_achive(name):
        data = json_load("achivements")
        if data[name]["unlocked"] != 1:
            data[name]["unlocked"] = 1
            renpy.notify(name)
        json_save(data, "achivements")
screen osmotr:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.05
        ypos 0.833
        idle "images/Icons/transparent/icon les paul.png"
        action [Call("check1")]
        hover "images/Icons/fill/icon les paul.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3125
        ypos 0.833
        idle "images/Icons/transparent/icon combo amplifier.png"
        action [Call("check2")]
        hover "images/Icons/fill/icon combo amplifier.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.224
        ypos 0.648
        idle "images/Icons/transparent/icon vinyl disc.png"
        action [Call("check3")]
        hover "images/Icons/fill/icon vinyl disc.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.469
        ypos 0.532
        idle "images/Icons/transparent/icon cat.png"
        action [Call("check4")]
        hover "images/Icons/fill/icon cat.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.1562
        ypos 0.463
        idle "images/Icons/transparent/icon photo.png"
        action [Call("check5")]
        hover "images/Icons/fill/icon photo.png"


label check1:
    max "Это… Les Paul  от Gibson?! Шик!"
    $ o1 = 1
    jump osmotr1

label check2:
    max "Ламповая. Это ламповая голова! Что тут за переключатели? Ревёрб, делау, волум..."
    $ o2 = 1
    jump osmotr1

label check3:
    max "Похоже, мой сосед - любитель старины. Или сам - старина."
    $ o3 = 1
    jump osmotr1

label check4:
    max "Разве в общагу можно приносить животных?.."
    $ o4 = 1
    jump osmotr1

label check5:
    max "Ого, он тоже играл в группе? Но, судя по снимку,  с тех пор прошло много лет."
    $ o5 = 1
    jump osmotr1
