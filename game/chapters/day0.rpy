label day0:
    #Фон: Кулисы.
    scene scene1 with Dissolve(3)
    show fan with Dissolve(1)
    play music waitingFans
    max "Короче, после концерта я совершенно свободен."
    fan "Тогда я буду ждать тебя у выхода! "
    max "Договорились."
    fan "Я хотела попросить тебя ещё кое о чём…"
    fan "Дай, пожалуйста, свой автограф!"
    "Я улыбнулся девушке и сделал несколько росчерков на протянутом листе. Она радостно ахнула. "
    "На бумаге красовался мой автограф - небрежные завитки и нескромно раскинувшиеся линии, складывающиеся в имя “Максим”. "
    "Кто-то выкрикнул моё имя. "
    q "Максим! Хорош уже девчонок клеить! Двухминутная готовность."
    "Это был наш вокалист, Паша."
    max "Эй, да брось! Я просто общаюсь с фанатами."
    "Впрочем, он был прав. Сквозь гул в зале было слышно, как кто-то - то там, то здесь - выкрикивает наши имена. "
    "Сцена была готова - микрофоны выставлены, инструменты тоже на своих местах, как и группа. Только меня не хватало. "
    "Я опрокинул в себя остатки воды в пластиковом стаканчике, бросил его куда-то не глядя и поднялся по ступенькам."

    #Фон: Рок-сцена.
    scene scene2 with Dissolve(2)
    stop music
    play music rockConcert
    "Стоило мне взяться за бас-гитару, как вспыхнули софиты. Из-за яркого света я не мог видеть толпу, но зато отлично слышал её рёв, нараставший с каждой песней."
    "В голове шумело, не знаю, почему. Может быть, попросту потому, что я был на сцене. "
    "Сотни невидимых глаз устремили свой взгляд на нас, сотни невидимых глоток подбадривали нас криками и сотни голосов подпевали нашим песням. "
    jump minigame
    #jump day0_1
label day0_1:
    scene scene2
    play music waitingFans
    "Я шагнул вперёд. "
    "Перед глазами всё слегка шаталось."
    fan1 "Максим!"
    fan1 "Максим, я хочу от тебя детей!"
    fan1 "Максим! Максим! Максим!"
    max "Вы хотите, чтобы я прыгнул?"
    fan1 "Да!!!"
    max "Тогда - ловите! Раз, два, три!"
    "Я приготовился к прыжку, рванулся вперёд…"
    #Фон: Рок-сцена с Максимом в воздухе.
    scene scene3
    "…как вдруг что-то оказалось под моей ногой."
    "Шнур."
    "Но мой прыжок было уже не остановить. Неловко взмахнув руками, я полетел через край сцены совсем не туда, куда хотел."
    stop music
    play sound fall
    scene d
    "После этого я чувствовал только боль."
    "Весёлые вопли мигом сменились испуганными возгласами."
    "Сам я с трудом мог шевелить губами."

    #Сцена 2
    #Фон: Больничная палата.
    scene hospital1 with Dissolve(2)
    play music medicalMonitor
    "Открыв глаза, я не сразу понял, где нахожусь."
    "Обшарпанные стены, выкрашенные до середины в зелёный. Шесть кроватей, вместе с моей, и столько же тумб."
    "Через окно, не встречая преграды в виде штор или жалюзи, падал солнечный свет. Пахло лекарствами."
    "Больница."
    "Голова раскалывалась, не давая ни заснуть снова, ни встать и заняться делом."
    "Нога тоже болела - да уж, грохнулся я знатно. Наверное, перелом."
    "Я бессмысленно следил глазами за сеткой трещинок на краске, покрывавшей стены."
    "Тишину палаты нарушил звонок телефона."
    max "Ох… Моя голова…"
    "Это была моя новенькая Nokia. Я думал было сбросить вызов, но увидел на экранчике имя нашего вокалиста. Значит, трубку всё-таки стоит поднять."
    pasha "Наконец-то дозвонился! Ты хоть знаешь, какой бардак вчера устроил?!"
    max "И тебе привет. Какой бардак?"
    pasha "Совсем мозги отшибло? Ты весь концерт запорол! Пришлось возвращать билеты и выплачивать неустойку!"
    max "И как это я всё запорол?"
    pasha "Как обычно. Освежу твою память: ты решил сигануть в толпу."
    max "Это я помню. Только всё было бы хорошо, если бы шнур на сцене не оказался там, где его быть не должно."
    max "Ты же ответственен за… этот…"
    "Головная боль атаковала с новой силой."
    max "…кабель-менеджмент, вот. "
    pasha 'Если б ты был аккуратнее, ничего бы не случилось.'
    max "А ты зачем шнуры под ноги кидаешь?"
    pasha "Ну и раскладывал бы сам, вместо того, чтоб к девчонкам приставать!"
    pasha "Ни одна ведь в итоге тебя не навестит, я уверен."
    max "Ну и хрен с ними. В следующий раз к тебе буду приставать."
    pasha "Не будешь. И следующего раза не будет."
    "Во мне зародилось дурное предчувствие."
    pasha "Я не собачиться с тобой позвонил. Ты…"
    pasha "Ты больше не в группе. "
    max "Чего? "
    max "Вы что, уже нашли мне замену?"
    pasha "Какая разница? Ты всё равно в другой город уезжаешь учиться. Всё равно не смог бы с нами играть. "
    max "Ну и сволочи вы. Могли бы в лицо сказать, а не вот так, по телефону."
    pasha "Могли бы. Но тебе ж плевать на нас. Сколько раз просили: не пей перед концертом, помоги с подготовкой - тебе было всё равно. "
    pasha "Только на девчонок и тратишь время."
    max "Фанатов надо уважать."
    pasha "А нас ты уважаешь?"
    "Я не знал, что ответить."
    pasha "Ага. То-то и оно."
    "Паша устало вздохнул."
    pasha "В общем, выздоравливай. Даст бог, свидимся."
    "Раздались гудки."
    "Я был так зол, что забыл о боли."
    "Ну и пошли они."
    "Тоже мне друзья! Сам группу соберу. И концерт устрою."
    "Я закрыл глаза."
    "В палату зашла, цокая каблуками, медсестра."
    show nurse
    nurse "Лавров?"
    max "Есть такой."
    nurse "Ага, пришёл в себя. Нужно сдать анализы, так что я помогу вам дойти до процедурного кабинета."
    max "Благодарю, а то я тут ногу сломал - так некстати."
    "В глазах медсестры появилось сочувствие."
    nurse "Вы её не просто сломали."
    max "Как “не просто”? Что-то серьёзное?"
    "Я испуганно отдёрнул одеяло. Нога, к счастью, была на месте; впрочем, много радости мне это не добавило."
    "Медсестра: Доктор на обходе всё вам скажет."
    max "Скажите хоть что-нибудь!"
    nurse "Я не знаю в точности, но вам потребуется сложная операция. Без трости после выписки не обойдётесь."
    max "Боже мой, ну и попал я…"
    max "Не могли бы вы дать мне обезболивающее? Таблеточку там какую-нибудь."
    nurse "Таблеточку не могу дать, но я как раз должна сделать вам укол. Повернитесь."
    max "Это обезболивающее?"
    nurse "Это лекарство, которое вам необходимо получить."
    #Затемнение.
    scene d with Dissolve(1)
    max "Только вы сразу не колите, пожалуйста. Лучше на счёт три."
    nurse "Конечно-конечно."
    max "Раз…"
    max "Ай!"
    stop music

    #Сцена 3
    #Фон: Вагон.
    scene train with Dissolve(1)
    play music train
    max "Такая история."
    max "Вот так я и решил, что пойду в программисты. Зарплаты хорошие, работа сидячая. В самый раз."
    "Стас, мой друг, одноклассник, а теперь, похоже, и одногруппник, покатывался со смеху на соседней полке."
    show stas
    "Я поёрзал, тщетно пытаясь найти удобное положение. "
    max "Смешно тебе. А мне после всех этих уколов до сих пор сидеть не удобно."
    stas "Ладно-ладно. История смешная, ситуация страшная."
    stas "Только ты же музыкант. Если уж надо сидеть, сидел бы в оркестре каком-нибудь."
    max "Ага. Или в переходе, что вероятнее. Я же самоучка - консерватория мне не светит."
    stas "Да, переход вероятнее. Ну, пока не научишься."
    max "Ты у нас тоже не первый программист в стране."
    stas "Может, я и не очень опытен, но я хотя бы с PHP работал, да и JavaScript немного знаю. "
    stas "Я тебя бросать не собираюсь. Если понадобится совет - обращайся. Только знай, что за тебя я работу не сделаю, иначе обучение не даст плодов. "
    max "Спасибо. Как тебе идея заселиться вместе?"
    stas "Попробуем, авось получится."
    "Мы помолчали."
    "Стас вытянулся на полке и вскоре уже похрапывал."
    "Я же смотрел в окно. За стеклом мелькали столбы и деревья, а за ними, в свою очередь, тянулась вдоль полей дорога."
    "Мы ещё не успели добраться до Уфы, но пейзаж успел уже несколько раз смениться до совсем непривычного."
    "Старые знакомые (язык не поворачивается назвать их друзьями) остались позади, за многие десятки и даже сотни километров."
    "Да что уж там, вся жизнь теперь где-то далеко. Прежняя жизнь, то есть."
    "А впереди…"
    "Новый город, новые люди, новые дела."
    "Не изменюсь ли и я сам в конце этой дороги? Каким я стану?"
    stop music



    #Сцена 4
    #Затемнение.
    scene d with Dissolve(1)
    "Вскоре поезд достиг города, где нам со Стасом предстояло жить ближайшие несколько лет. "
    "Уфа раскинулась на холмах над рекой."
    "Покрытые стеклом современные высотки, строгие административные здания, деревянные домики выглядывали друг из-за друга или из-за деревьев на крутом берегу."
    "Мы пронеслись над водной гладью. Я заметил телевышку, поднимающуюся высоко над городским ландшафтом."
    "Ближе к берегу был какой-то памятник - доползти бы ещё до него с моей ногой."

    #Видеоролик.
    $ renpy.movie_cutscene("images/anim.ogv")
    #Фон: Общежитие снаружи.
    scene home1
    "Некоторое время спустя мы подъехали к общежитию."
    "Я расплатился с таксистом и повернулся к Стасу."
    max "Вроде это здесь. Ну что, дамы вперёд."
    stas "В таком случае, после вас."
    #Фон: Коридор общежития.
    scene dormitory_hallway
    play music crowd
    "В коридоре висел листок со списками заселяющихся. Кто-то из подходивших к нему радостно улыбался, кто-то - разочарованно пожимал плечами."
    #Арты: Список на заселение.
    scene home3
    "Мы со Стасом относились ко второму типу. "
    max "Может, попробуем попросить, чтоб заселили вместе?"
    stas "Попробуем."
    "Завидев меня со Стасом, комендантша строго зыркнула на нас из-под очков. "
    "Какой-то парень позади неё, видно, хорошо знакомый с нравом комендантши, округлил глаза и провёл ладонью у горла."
    "Мы дружно развернулись."
    stas "Не попробуем."
    "Делать нечего: мы разошлись по своим комнатам."
    stop music
    "Дверь в мою была открыта, однако никого внутри не было."
    #Фон: Комната Максима и Айрата Рустемовича.
    scene dormitory_max_room
    $ o1 = 0
    $ o2 = 0
    $ o3 = 0
    $ o4 = 0
    $ o5 = 0
    call screen osmotr

label osmotr1:
    if o1+o2+o3+o4+o5 == 5:
        hide screen osmotr
        jump day0_2
    call screen osmotr
    #Изучение комнаты, как в Зайчике.
    #Les Paul  от Gibson: Это… Les Paul  от Gibson?! Шик!
    #Ламповый комбик: Ламповая. Это ламповая голова! Что тут за переключатели? Ревёрб, делау, волум...
    #Виниловый проигрыватель с пластинками: Похоже, мой сосед - любитель старины. Или сам - старина.
    #Кот на подоконнике: Разве в общагу можно приносить животных?..
    #Фотография: Ого, он тоже играл в группе? Но, судя по снимку,  с тех пор прошло много лет.

label day0_2:
    show ar
    play sound cough
    "Пока я осматривался, кто-то подошёл к комнате и покашлял у двери. Я оглянулся."
    q "Прошу прощения, а вы, собственно, кто?"
    max "Я… это… заселился."
    "Мой сосед по комнате был старше меня - аспирант, наверное. Ого!"
    "Он был высоким, худым мужчиной и обладал приятным, располагающим к себе лицом. "
    "Одет он был просто, но опрятно: синяя водолазка и тёмные джинсы."
    q "Вот оно что… Я Айрат Рустемович."
    "Айрат Рустемович бросил взгляд на мой чехол с гитарой."
    ar "Вижу, ты музыкант?"
    max "Да, я играю на бас-гитаре. Звать Максимом."
    "Я протянул руку. Айрат Рустемович пожал её с неохотой."
    max "Вы - аспирант?"
    ar "Да. Не думал, что ко мне кого-то подселят. Похоже, в этом году и впрямь много поступающих. "
    ar "Ну что ж… не гнать же тебя на улицу. Особенно учитывая твою травму."
    "Он кивнул на мою ногу. Я стоял на ней нетвёрдо и больше опирался на трость - не знаю, сколько ещё придётся так проходить."
    ar "Как ты так повредился?"
    max "Да так… упал неудачно."
    "Я поспешил перевести тему."
    max "Тут столько дорогущих вещей… Как вы на всё это заработали?"
    "Айрат Рустемович легонько постучал по своей голове."
    ar "Мозгами, конечно. Учись хорошо - и без денег не останешься, поверь."
    "Да уж. Я ещё раз окинул взглядом комнату. Мой постер с Red Hot Chili Peppers на этом фоне выглядел в лучшем случае скромно. "
    "Может быть, если б я меньше пил перед концертами, тоже бы так комнату обставил."
    ar "Я ведь не ошибся? Ты только поступил?"
    max "Да. Так что… всё впереди. "
    "Айрат Рустемович как-то грустно усмехнулся, раскладывая принесённые книги на полке."
    ar "Это уж точно."
    max "А сколько вам?"
    ar "Двадцать семь."
    max "Вы только в “клуб 27” не попадите, ха-ха."
    ar "Прошу прощения?"
    max "Ну, как Курт Кобейн и Тупак Шакур."
    ar "Ах, понял. "
    ar "Но, вообще-то, Тупак Шакур погиб в возрасте двадцати пяти лет, так что он не может быть причисленным к “клубу 27”. "
    max "О…"
    "Я как-то подзабыл об этом."
    ar "Да и к тому же, вся эта история - во многом своего рода когнитивное искажение. "
    ar "Если взглянуть на смерти всех музыкантов в целом…"
    ar "…то окажется, что в двадцать семь умирают не чаще, чем в любом другом возрасте."
    ar "Просто Хендриксу, Моррисону и Джоплин не посчастливилось быть знаменитыми в музыке и умереть в одно время."
    ar "Кстати, стыдно не упомянуть их в первую очередь."
    "Айрат Рустемович строго на меня посмотрел."
    ar "В общем, людям нравится делать из совпадений нечто большее."
    ar "Но, если хочешь заниматься наукой, проверяй все факты."
    ar "Кстати… Я нечасто общаюсь с первокурсниками, но если выдаётся случай, я всем задаю один вопрос."
    ar "Ради чего ты поступил в университет?"
    menu:
        "Учёба":
            max "Хочу учиться."
            ar "Хм? Похвальное желание. Всецело одобряю."
        "Деньги":
            max "Хочу хорошо зарабатывать."
            ar "Что ж, по крайней мере, ты хочешь зарабатывать мозгами, а не кулаками."
        "Любовь":
            max "Хочу встретить девушку, с которой буду всегда."
            ar "Как романтично. Что ж, удачи в этом нелёгком деле - среди программистов-то."
        "Связи":
            max "Хочу завести полезные знакомства."
            ar "Видел я тут одного первокурсника… Думаю, вы с ним подружитесь."
        "Не знаю":
            max "Не знаю."
            ar "Не знаешь? Надо бы решить поскорее."
    ar "Ну, чего бы ты ни хотел, я надеюсь на одно: ты не станешь отвлекать меня от написания кандидатской."
    "Я кивнул."
    "Остаток вечера я решил посвятить разбору сумок. Я разложил все вещи, что привёз с собой, повесил над кроватью постер и облегчённо вздохнул.  "
    "Айрат Рустемович тем временем сидел над учебниками и что-то сосредоточенно выписывал."
    "Глаза слипались. Я зевнул и лёг спать."
    #Затемнение.
    scene d with Dissolve(1)
    jump day1
