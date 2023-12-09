label day1:
    #Сцена 1
    #Фон: Комната Максима и Айрата Рустемовича.
    scene dormitory_max_room with Dissolve(1)
    "Луч солнца заставил меня поморщиться и открыть глаза."
    "Со сна я не сразу вспомнил, где нахожусь, и несколько секунд просто рассматривал потолок."
    "Повалявшись ещё немного, я наконец сполз с кровати."
    "Айрата Рустемовича в комнате не было."
    #Фон: Коридор общежития.
    scene dormitory_hallway
    "Наскоро умывшись и одевшись, я взял рюкзак и вышел в коридор."
    max "Пожалуй, стоит зайти за Стасом."
    "Дверь в его комнату, в сущности, не отличалась ничем от всех прочих в коридоре, разве что парой приметных царапин на дереве."
    play sound door
    "Я постучал."
    "Никто не отозвался."
    play sound door_1
    "Я постучал ещё и даже дёрнул ручку, но ответа не получил. Видимо, Стас уже ушёл."
    "Я пожал плечами и двинулся к выходу."
    #Фон: Остановка у общежития (утро).
    scene dormitory_bus_stop
    "Общежитие располагалось далековато от университета, так что мне пришлось ехать на автобусе."
    "Тепло лета всё ещё не ушло, и я с наслаждением подставил лицо солнцу. Вскоре подошёл мой автобус."
    scene bus
    play music bus
    "За окном мелькали дома и машины, и я зевал, рассматривая их убаюкивающую карусель."
    "Неожиданно я заметил, как кто-то напевал песню, очень тихо и едва слышно."
    "Я встряхнул головой, прогоняя сонливость, и в отражении в стекле я увидел силуэт красивой девушки в кожанке."
    "Я обернулся."
    show eva
    "Она сидела у окна напротив. Её тёмное каре заканчивалось чуть ниже ушей и не скрывало татуировку на шее: череп с розой в зубах."
    stop music
    play sound bus_1
    "Автобус резко остановился на светофоре."
    "Мелочь, которую я до того держал в руке, рассыпалась, и я кинулся собирать её с пола."
    max "Ну вот, теперь по всему автобусу за ней ползать…"
    "Подобрав монеты, я вновь сел на своё место и потёр заболевшее от резких движений колено."
    "Украдкой я бросил взгляд на место, где сидела та девушка."
    "Никого."
    "Я расстроенно вздохнул. Впрочем… мы одного возраста. Возможно, я ещё встречу её в университете?"
    #Фон: Большая толпа у университета (утро).
    scene university_crowd
    play music first_september
    "На площади перед университетом, где проходила линейка, было так много народу, что яблоку негде упасть."
    "Из стареньких, ещё заставших Советский Союз, динамиков слышалась бодренькая песня, но в текст я не вслушивался."
    "Глазами я пытался найти в толпе Стаса, но взгляд натыкался только на незнакомые спины других первокурсников."
    "Музыка прервалась, гомон стих, и раздался голос кого-то из преподавателей или вроде того - я стоял в конце, и толком не видел говорящего."
    "Да и слушать очередную скучную речь про то, какие мы молодцы и сделали правильный выбор, поступив именно сюда, было неинтересно."
    "Я бросил попытки найти Стаса и теперь боролся с зевотой."
    "Некоторое время спустя нас разделили по факультетам и отправили внутрь."
    stop music
    #Фон: Большая аудитория.
    scene university_room
    show stas
    play music crowd
    "Ещё проходя по коридору, я заметил широкую спину Стаса, и, оказавшись в большой аудитории, я подсел к нему."
    "Здесь нам пришлось слушать примерно тоже, что уже было сказано на улице, только другими словами."
    "Непохоже, чтобы люди вокруг меня испытывали интерес к происходящему."
    "Первое время аудитория застыла в нерешительности, но постепенно все расслабились."
    "Кто-то знакомился, кто-то говорил про образовательную новинку - ЕГЭ, кто-то делился слухами про преподов. Всё обсуждалось шёпотом, конечно."
    "Я наклонился к Стасу."
    max "Я думал, мы вместе пойдём на линейку."
    "Стас с трудом сдержал зевок."
    stas "Я тоже. Я попытался постучаться в твою комнату, но ты, походу, дрых слишком крепко."
    max "Я одного не понимаю: ты как умудрился раньше меня встать?"
    "Стас махнул рукой."
    stas "А-а, я и не планировал. Мой сосед вскочил в самую рань, и я тоже проснулся."
    stas "Кстати, как у тебя дела с соседом? Слышал, он аспирант."
    "Я на мгновение задумался, а потом повертел ладонью в воздухе - мол, более-менее."
    stop music
    #Сцена 2
    #Фон: Университет (день).
    scene university_outside
    show stas at left
    "Когда с официальными мероприятиями было покончено, мы вышли из университета. Делать там всё равно было больше нечего."
    "Я задержался у самолёта, украшавшего площадь перед зданием главного корпуса."
    play music vera_1
    q "Макс!!! Стас!!!"
    "Какой-то знакомый голос… Вероника?"
    "К нам со всех ног неслась невысокая девушка в футболке с сердечком. Я без труда вспомнил её круглое личико - это определённо Вероника, наша бывшая одноклассница."
    show vera at right
    vera "Макс! Стас!"
    max "Вероника, привет."
    stas "Привет!"
    "Я махнул девушке рукой. Стас растерянно, но радостно  улыбнулся."
    vera "До вас не докричишься. Привет!"
    stas "Не ожидали тебя здесь увидеть."
    max "Какими судьбами?"
    "Вероника откинула волосы, заплетённые в две небрежные косички, за спину и слегка надулась."
    vera "Что за глупый вопрос? Я тут учусь!"
    "Она засмеялась. Мы улыбнулись."
    max "Ничего глупого. Я б не удивился, если бы ты мимо охраны проскочила. Помнишь, что ты в шестом классе весной устроила?"
    stas "И зимой в седьмом."
    "Мы со Стасом переглянулись."
    vera "Вам по лбу дать?"
    "Девушка нахмурилась ещё сильнее. Я вскинул руки, притворно защищаясь."
    max "Э, полегче! Мне и с ногой проблем хватает."
    vera "Ой! А что с твоей ногой?"
    "Дурной настрой Вероники мигом пропал. Она всё ещё хмурилась, но голос звучал обеспокоенно."
    max "Упал неудачно."
    vera "Бедняжка! Что случилось?"
    stas "Около проводов прыгал."
    "Я закатил глаза."
    max "Да просто Паша кабель-менеджментом заниматься не умеет… "
    vera "Ладно, пойдём в «Рокстикс», будем учить тебя нормально праздновать."
    max "Ну уж нет. Вредная еда мне сейчас точно ни к чему."
    vera "Какой ты правильный! В честь дня знаний можно себя чем-то побаловать."
    stas "Ну, не знаю, как Максим, а вот я от бургера точно не откажусь."
    "Вероника радостно кивнула."
    vera "Значит, два против одного. Пошли!"
    "Она схватила меня за руку и потащила к выходу с территории университета. Я едва успел переставлять трость."
    max "Да подожди ты…"
    vera "Прости! Давай пойдём помедленнее."
    #Фон: Рокстикс (внутри).
    scene rocksticks
    show stas at left
    show vera at right
    "Вскоре мы уже сидели за столиком с картошкой, бургерами и колой."
    "Вероника быстро разобралась со своей картошкой, и теперь будто бы невзначай брала её то у меня с подноса, то у Стаса."
    "Я делал вид, что не замечаю, а Стас ворчал, но беззлобно: мне кажется, он больше нас всех радовался этой неожиданной встрече."
    stas "Эх, скучал я по всему этому. После того, как ты переехала, в нашей компашке чего-то стало не хватать."
    max "Похитителя картошки?"
    "Вероника ахнула с видом оскорблённой невинности."
    vera "Как грубо! Я, вообще-то, человек искусства."
    "Она принялась сооружать на своём подносе башенку из бумажек и коробочек."
    max "Ладно, так и быть. Как бы там ни было, Стас прав."
    max "Всё-таки совсем не ожидал, что мы поступим в один универ."
    vera "Я разве не говорила? Я давно хотела поехать учиться в другой город."
    max "Да. И всё-таки - какое совпадение… А на каком ты факультете?"
    vera "Факультет информатики и робототехники. Прикладная информатика."
    stas "О, так мы в одной группе."
    vera "Жалко, что мы на линейке не встретились."
    max "Я слишком хотел спать, чтобы суметь найти кого-то в такой толпе… Всё-таки вставать в восемь утра - настоящая пытка."
    vera "Ну ты что! Сегодня же первый день в универе. Надо общаться, заводить дружбу с другими!"
    "Вероника важно взмахнула палочкой картошки."
    max "Да мне пока и Стаса хватает. И ты ещё, оказывается, тоже с нами учишься."
    stas "Слушай, имей совесть, оставь мне хоть немного картошки."
    "Вероника бессовестно взяла ещё палочку картошки."
    vera "Ну и как иначе мне набирать силы для тренировок?"
    max "Тренировки? Это ещё что за новый вид занятий в музыкалке?"
    vera "Это в спорткомплексе. Я теперь на баскетбол хожу! Видишь, какая я всесторонне развитая личность?"
    stas "Как ты всё успеваешь?"
    vera "Ну… На самом деле, музыку пока пришлось отложить. И театральный кружок тоже."
    vera "А сами вы чем хотите заниматься?"
    stas "Ну… я пока не определился."
    vera "А ты, Макс? У тебя вроде группа была?"
    "Я криво улыбнулся."
    max "Было дело, хотя не думаю, что нас можно было назвать группой."
    vera "О-о. Вижу, вы расстались на плохой ноте."
    max "Неприятно, конечно, но жизнь продолжается. Думаю вот группу свою создать."
    vera "Здорово! Позови меня, когда начнёшь собирать ребят, хорошо?"
    "Я кивнул и взял стаканчик с колой."
    "Стас потянулся и довольно вздохнул. Мы как раз закончили с едой, а Вероника - с постройкой башенки."
    max "Ну что, человек искусства, пойдём?"
    "Вероника показала большой палец вверх, и мы пошли на выход из «Рокстикса»."
    stop music
    #Фон: Остановка у университета (вечер).
    scene university_bus_stop_night
    show stas at left
    show vera at right
    "Вскоре мы стояли на остановке. Мне стало прохладно, и я поглубже натянул капюшон куртки. Стас тоже нахохлился. Вероника же сосредоточенно прыгала, разгоняя кровь."
    vera "Жалко, что ты ногу повредил! Я бы тебя на баскетбол затащила! Или ещё куда-нибудь!"
    "Она говорила немного запыхавшись. Я хотел было ответить ей, но вдруг Вероника прекратила скакать туда-сюда."
    vera "О! Мой автобус!"
    "Я присмотрелся к номеру и остановкам, указанным на табличке автобуса."
    max "Так он же не до общежития, совсем в другую сторону едет."
    vera "А я и не в общаге живу."
    stas "Квартиру снимаешь?"
    vera "Ага! Семь остановок отсюда! Ну всё, пока!"
    "Она махнула нам на прощанье и запрыгнула в автобус. Мы со Стасом остались ждать свой."
    #Сцена 3
    #Фон: Комната Максима и Айрата Рустемовича.
    scene dormitory_max_room
    "Когда я вернулся в комнату, Айрат Рустемович работал, как и прошлым вечером."
    "Мне хотелось больше узнать о нём. Всё-таки мы теперь соседи по комнате."
    show ar
    max "Айрат Рустемович, как прошёл ваш день?"
    ar "Нормально."
    "Повисла пауза. Я решил было, что больше Айрат Рустемович уже ничего не скажет, но тут он отложил в сторону книгу и кашлянул."
    ar "А твой?"
    max "Ну… я был на линейке."
    ar "Рад за тебя."
    max "Я видел вашу фотографию. Вы правда играли в рок-группе?"
    ar "Было дело."
    "Он покосился на гитару. Только сейчас я заметил, что она покрыта тонким слоем пыли."
    max "А ваши друзья? Они ещё играют?"
    ar "Нет."
    max "Понятно. А есть тут… ну, не знаю, рок-клуб или вроде того?"
    ar "Послушай, Максим…"
    "Он устало потёр переносицу."
    ar "Со всеми вопросами тебе лучше пойти в музыкальный кружок. Он в актовом зале, на третьем этаже."
    max "Спасибо."
    ar "Я играл там когда-то."
    "Айрат Рустемович вновь уткнулся в учебники."
    "Я посчитал правильным не отвлекать его больше, к тому же, что самое важное я выяснил: тут есть другие люди, которых интересует музыка."
    "Было поздно, и мне стоило лечь спать."
    #Фон: Затемнение.
    scene d with Dissolve(1)
    jump day2
