define m = Character('Максим', color="#4682B4") #SteelBlue
define v = Character('Вероника', color="#FF69B4") #HotPink
define e = Character('Ева', color="#191970") #MidnightBlue
define s = Character('Светлана', color="#F5DEB3") #Wheat (Бежевый)

define fan = Character('Фанатка', color="#999999")
define fan1 = Character('Толпа', color="#999999")
define pasha = Character('Паша', color="#999999")
define nurse = Character('Медсестра', color="#999999")
define st = Character('Стас', color="#999999")
define ar = Character('Айрат Рустемович', color="999999")
define q = Character('???', color="#999999")

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

screen osmotr:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.1
        ypos 0.28
        idle "images/eye.png"
        action [Call("check1")]
        hover "images/eye.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.28
        idle "images/eye.png"
        action [Call("check2")]
        hover "images/eye.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "images/eye.png"
        action [Call("check3")]
        hover "images/eye.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.28
        idle "images/eye.png"
        action [Call("check4")]
        hover "images/eye.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.9
        ypos 0.28
        idle "images/eye.png"
        action [Call("check5")]
        hover "images/eye.png"

label check1:
    m "Это… Les Paul  от Gibson?! Шик!"
    $ o1 = 1
    return

label check2:
    m "Ламповая. Это ламповая голова! Что тут за переключатели? Ревёрб, делау, волум..."
    $ o2 = 1
    return

label check3:
    m "Похоже, мой сосед - любитель старины. Или сам - старина."
    $ o3 = 1
    return

label check4:
    m "Разве в общагу можно приносить животных?.."
    $ o4 = 1
    return

label check5:
    m "Ого, он тоже играл в группе? Но, судя по снимку,  с тех пор прошло много лет."
    $ o5 = 1
    return
