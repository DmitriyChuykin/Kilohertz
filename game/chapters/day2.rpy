label day2:
    #Фон: Комната Максима и Айрата Рустемовича.
    scene dormitory_max_room
    "Я потянулся, просыпаясь, и тут же завернулся обратно в одеяло. Было так тепло и хорошо, что не хотелось даже открывать глаза."
    "Погодите…"
    "А который час?"
    "Я вскочил на кровати и схватил телефон, чтобы посмотреть время."
    "Вот чёрт! Первая пара уже в самом разгаре!"
    "Я наскоро умылся, оделся и бросился на остановку - настолько быстро, насколько позволяла моя нога."
    #Фон: Университет (коридор).
    scene university_hallway
    "Вторая пара начиналась как раз в тот момент, когда я стоял около расписания. А ведь мне предстояло ещё найти аудиторию!"
    "Коридор был тих, только из-за дверей слышались голоса преподавателей, сливающиеся в едва заметный гул."
    "Я не один искал аудиторию, ещё одна девушка ходила туда-сюда, пытаясь разобраться, куда идти."
    show alia
    "Она была одета по-деловому - рубашка, юбка, свитер, но при этом не выглядела строго: её одежда была нежных, пастельных тонов."
    "Девушка казалась хрупкой, как заколка-бабочка в её светлых волосах."
    "Я решил подойти к ней."
    max "Привет. Ты, случаем, не первокурсница?"
    q "Да…"
    max "Я тоже. Ищешь аудиторию?"
    q "Ага. Скажи, ты не знаешь, где у прикладной информатики пара?"
    max "Знаю. 2-202. Мне тоже туда надо."
    q "Тогда пойдём скорее, пара уже начинается."
    #Фон: Большая аудитория.
    scene university_room
    show alia
    "Немного поблуждав по коридорам, мы нашли наконец нужную аудиторию."
    "Преподаватель на секунду отвлёкся от лекции, когда мы вошли, и строго посмотрел на нас, так что мы шёпотом извинились и прошмыгнули на задние парты."
    "Девушка наклонилась ко мне."
    q "Ужасно неловко вот так опаздывать в первый же день…"
    max "Да ладно. Столько пар ещё будет - ничего страшного, если на одну опоздали. Тебя как зовут?"
    q "Алия."
    max "Красивое имя. Я Максим."
    alia "Приятно познакомиться, Максим."
    "Девушка робко улыбнулась, и я не смог не ответить ей тем же."
    "После этого Алия полностью сосредоточилась на лекции и аккуратным, ровным почерком записывала каждое слово преподавателя."
    "Ближе к концу занятия преподавателю понадобилась доска."
    alia "Ой…"
    max "Что-то случилось?"
    alia "Я забыла очки дома. Совсем не вижу, что он пишет…"
    max "Ничего, я тебе помогу."
    "Я быстро переносил всё, что преподаватель чертил мелом на доске, себе в тетрадь. Алия продолжила записи, время от времени шёпотом благодаря меня."
    "На переменке между парами я бездумно глядел в доску и покачивал ногой. Алия рылась в сумке. Какой-то листок выпал у неё из рук и плавно опустился в проход между партами."
    "Я потянулся за ним. На бумаге расположилось бесчисленное скопище разных рисуночков: какие-то домики, люди, ровные геометрические узоры."
    "Алия густо покраснела."
    alia "Отдай, пожалуйста."
    max "Так ты рисуешь?"
    "Я протянул ей листок. Она быстро схватила его и убрала под тетрадь."
    max "У тебя здорово получается. Ты ходила в художку?"
    alia "Нет…"
    max "Так ты самоучка? Это ещё круче!"
    alia "Ты так думаешь?"
    "Я прижал руку к сердцу и с притворной серьёзностью кивнул."
    max "Честное пионерское. Можно ещё раз посмотреть?"
    "Помедлив, Алия достала листок. Пока я рассматривал её рисунки, девушка тихо заговорила."
    alia "Извини, я, наверное, была слишком резкой… Дома не любят, когда я рисую, вот мне и не нравится, когда кто-то смотрит на мои работы."
    max "Серьёзно? Так нельзя, у тебя же талант. Кстати, а можешь нарисовать меня?"
    "Лицо Алии просветлело."
    alia "Конечно!"
    "Она взялась уже было за карандаш и чистый листок, но переменка закончилась, и нам пришлось вернуться к занятию."

    #Сцена 2
    #Фон: Университет (коридор).
    scene university_hallway
    "На выходе из аудитории Вероника со смехом хлопнула меня по плечу."
    show vera at left
    show stas at right
    vera "Эй, прогульщик! Пошли в столовую!"
    max "Да, конечно. Только подожди чуть-чуть…"
    stas "Ищешь кого-то?"
    "Я окинул взглядом аудиторию, но Алии не увидел. Видимо, она уже ушла."
    max "Да нет, уже никого."
    #Фон: Столовая.
    scene university_cafe
    "Мы с Вероникой и Стасом оказались не единственными студентами, пожелавшими утолить голод в обеденный перерыв - что было ожидаемо."
    "Свободных мест за столиками почти не было."
    "Пока я высматривал, где можно сесть, Вероника уже положила еду на поднос. И как она только всё успевает?..."
    "Стас тоже набрал еды и сел на первое попавшееся место."
    stas "Извини, сегодня я не с вами."
    "Я торопливо взял свой обед и чашку с компотом. Пробираться через толкучку, удерживать поднос и опираться на трость одновременно оказалось нелегко."
    "Кто-то бросил рюкзак прямо между столиков, и я зацепился тростью за его лямку. Поднос в другой руке опасно качнулся."
    "Едва я восстановил равновесие, как чашка с компотом упала прямо на парня передо мной."
    show eugine
    q "Какого чёрта?"
    max "Блин…"
    "Парень обернулся. Он выглядел так, будто только что вышел с какого-нибудь важного совещания в крупной компании: строгие костюм и рубашка, дорогие часы на руке, аккуратный галстук."
    "Взгляд у него был презрительный, будто он не ест со всеми в одной столовой, а случайно здесь оказался. Если бы он не выглядел как мой ровесник, парня можно было бы принять за важную шишку."
    "Его образ, конечно, портило тёмное пятно, расплывающееся по пиджаку."
    q "Ты хоть представляешь, сколько стоит этот пиджак?"
    max "Думаешь, я в него специально целился? Тут сумка  прямо посреди прохода, это сильно мешает ходить."
    q "Мешает, ага... Ходить аккуратней надо."
    q "Отнесёшь пиджак в химчистку, а завтра перед парами я его заберу."
    "Он снял пиджак и бросил его мне."
    "Я оторопел."
    max "С чего ты взял, что я стану этим заниматься?"
    q "Какие-то проблемы?"
    "Из-за спины наглого незнакомца выступил ещё один, бугай гоповатого вида."
    "Я постарался сдержать злость."
    "Лезть в драку сейчас было бы глупо. Мне казалось, что бугай за этим нарциссом способен покалечить даже инвалида. Пускай и не на публике, а где-нибудь за углом."
    max "Тебе будет проще сходить в туалет, чтобы отмыть пятно."
    q "Вот еще! Я не собираюсь марать руки."
    max "Похоже, в этот раз придётся."
    max "И вообще, нахрена такие дорогие тряпки носить в вузе? Обычная одежда для тебя выглядит недостаточно хорошо?"
    "Незнакомец раздражённо вздохнул и посмотрел на меня, как на несмышлёного маленького ребёнка."
    q "Не твоего ума дело. Не будь ты калекой, разговор бы был другим."
    "Незнакомец хмыкнул, потом принял недовольный вид и ушел."
    hide eugine
    max "Придурок."
    "Впереди засмеялась сидевшая за столиком Вероника."
    vera "Лузер!"
    "Я покраснел. Обязательно, что ли, кричать на всю столовую? Вокруг послышались смешки."
    "К моему облегчению, весело было не всем. Я отвернулся от Вероники и увидел серьёзное лицо Алии. Она, кажется, только заметила меня и теперь взмахнула рукой, приглашая сесть рядом."
    menu:
        "Сесть с Вероникой":
            show vera
            "Веронику просто слегка заносит временами. Вряд ли она хотела меня обидеть."
            "Я сел рядом с подругой."
            max "Что смешного?"
            vera "Ну и лицо у тебя было! Видел бы ты себя!"
            "Она захихикала."
            max "Весело тебе. А мне теперь где-то стирать дорогущий пиджак. Что это вообще за парень?"
            vera "Это Евгений. Он тоже первокурсник, как мы."
            max "Уже собрала все сплетни?"
            "Она наклонилась ко мне и продолжила говорить тише, но всё так же оживлённо."
            vera "Говорят, его родители - супербогаты! Вот он нос и задирает, ему же всё с рук сходит."
            max "Неприятный тип."
            vera "Зато какой у него был взгляд, когда ты компот разлил!"
            "Вероника едва сдерживала смех. Я запоздало задумался: а кого она назвала лузером? Меня или его?"
        "Сесть с Алиёй":
            show alia
            "Нет уж! Настроение и так подпорчено, лучше сяду с той, кто надо мной не смеётся."
            max "Не занято?"
            alia "Что ты, нет! Садись, пожалуйста."
            "Алия сочувственно улыбнулась, когда я опустился на соседний стул."
            alia "Не везёт тебе сегодня."
            max "Что это вообще за парень?"
            alia "Даже не знаю… Но ты не обращай на него внимания. Такие люди считают, что могут делать всё, что вздумается."
            max "Пошёл он…"
            "Я запнулся и бросил взгляд на Алию."
            max "…куда подальше."
            alia "Да. Спасибо тебе большое…"
            alia "Ты очень выручил меня на лекциях. Надеюсь, я тебя не слишком отвлекла."
            max "Я был только рад помочь."
    #Сцена 3
    #Затемнение.
    scene d with Dissolve(1)
    "Остаток лекций прошёл мимо меня. Я то и дело поглядывал на дурацкий пиджак и злился. Наконец, учебный день закончился…"
    "Сегодня он оказался долгим и не слишком приятным. Ещё и в химчистку пришлось идти."
    "Я хотел проветриться, отдохнуть. Поэтому я не сразу пошёл на остановку."
    "Вместо этого я слонялся по улицам около универа, и вскоре заметил вывеску: «Milk cafe»."
    #Фон: Бар (вечер).
    scene bar1
    "Местечко было что надо: желтый свет светильников был приглушён, и пространство покрывал уютный полумрак."
    "Я пробрался к барной стойке и сел на стул около неё, отложил в сторону трость, а затем с наслаждением потянулся."
    "Пора расслабиться!"
    "Я взглянул на меню."
    max "Нет, пиво я больше пить не буду…"
    "Пока я разглядывал привычный перечень напитков, который можно было найти в любом кафе, подошёл бармен."
    barmen "Добрый вечер. Не желаете заказать наш кумыс?"
    "Я понятия не имел, что это вообще такое, но почему бы не попробовать что-то новое?"
    max "Да, пожалуйста."
    "За спиной раздался топот. Как раз когда я повернулся к источнику шума, к стойке подлетел взъерошенный парень."
    show misha
    q "Панки хой!"
    "Он перегнулся через стойку и дружески хлопнул по плечу бармена. Они перекинулись парой фраз, и парень плюхнулся на стул рядом со мной."
    q "Мне вон того, тёмного."
    "Первое, что бросалось в глаза при взгляде на незнакомца, - его косуха, покрытая десятками металлических шипов и пёстрыми нашивками."
    max "Отличная куртка."
    q "А? Да! Сам сделал. Шипы и прочую фигню."
    "Он протянул мне руку."
    q "Миша. Атеист, анархист и не верю в бога."
    max "Максим. Студент, э-э… на басе играю."
    "Мы пожали руки. Бармен подал напитки. Миша выпил весь стакан разом, а я с интересом разглядывал свой кумыс. Это был молочный напиток, вроде и сладкий, но в тоже время с кислинкой."
    misha "Эт чё, кумыс?"
    max "Ага. Решил попробовать что-то новое."
    misha "Одобряю. Ты не местный, что ли?"
    "Я кивнул."
    misha "Тоже в общаге живёшь?"
    max "Да. А ты?"
    misha "И я. Значит, ты басист?"
    "Я кивнул."
    misha "А я барабанщик."
    max "В группе играешь?"
    misha "Не-а. Иногда в переходе сижу, но не с барабанами."
    "Бармен наполнил стакан Миши. Тот качнул головой в знак благодарности."
    misha "Во, как раз на заработанное там пью. Как пришло - так и ушло."
    max "Звучит не очень весело."
    "Миша осушил ещё стакан."
    misha "Не-не, ты не понимаешь. Я просто живу так, чтобы всегда было в кайф: и работаю в кайф, и учусь в кайф, и отдыхаю в кайф."
    misha "Сам-то будешь что-то кроме кумыса?"
    max "Нет. Когда я пил в прошлый раз - упал со сцены. Теперь таскаюсь с этим."
    "Я показал на трость."
    misha "Ё-моё. Ну, что тут сказать… Зато концерт запоминающийся вышел."
    max "Это уж точно."
    "Миша обернулся к бармену."
    misha "Налей-ка мне ещё. Так и что, Максим, ты такой грустный из-за ноги?"
    max "Ну, к ней я привык…"
    "Я колебался мгновение или два, а потом всё-таки вывалил этому человеку, с которым был знаком всего минут пять, сегодняшнюю историю с пиджаком и всё, что я думаю о Евгении."
    "Миша отложил в сторону успевший опустеть стакан."
    misha "Знаешь, ты прав. Пшёл он туда…"
    "Миша показал неприличный жест и чуть не рухнул со стула, но в последний момент удержал-таки равновесие."
    misha "…со своим пиджаком."
    scene d with Dissolve(1)
    #Сцена 4
    #Фон: Бар (вечер).
    "Следующие полчаса мы провели, обсуждая учёбу и универ. Наконец Миша опёрся локтём о стойку и зевнул."
    scene bar1
    show misha
    misha "Что-то меня рубит. А ещё к девушке зайти надо… Пройдёмся?"
    "Я слез со стула. Почему бы и не прогуляться? Всё равно уже пора в общагу."
    "Сквозь негромкую музыку кафе я услышал тихое пение, точно такое же, как в автобусе."
    scene street_night
    show eva
    "Я удивлённо оглянулся. У дверей бара я увидел девушку и пригляделся: да, та самая, из автобуса. Она выходила, и, если я хотел её догнать, мне стоило поспешить."
    menu:
        "Пойти за незнакомкой":
            "Не думаю, что Миша расстроится, если я не пойду с ним."
            "Я был уверен, что эта девушка, с которой я случайно столкнулся уже второй раз, занимается пением профессионально. Такой шанс не следует упускать!"
            "Я взял трость и бросился за девушкой наружу."
            "На ней были наушники, и мои попытки окликнуть её провалились: ответом был лишь громкий рок, отчётливо различимый на тихой ночной улице, и тихий голос."
            "К несчастью, она шла намного быстрее меня, лёгким и стремительным шагом, так что мне никак не удавалось поравняться с ней."
            "Девушка ушла с улицы во двор. Мы некоторое время петляли по нему, пока она не завернула за очередной угол."
            "Я последовал за ней."
            "Тёмные дома нависали надо мной и замыкались в сплошную стену. Не было видно ни единого прохода, куда бы могла уйти незнакомка, разве что она зашла в одну из дверей."
            "Я разочарованно вздохнул. Было бы глупо стучаться туда-сюда в попытках найти девушку, и я развернулся, чтобы уйти в общежитие."
        "Помочь Мише дойти до общежития":
            scene bar1
            show misha
            "В Мише я неожиданно нашёл неплохого собеседника. А девушку я совсем не знаю, подумаешь, пересёкся разок-другой."
            "Так что, как там говорила Вероника? Надо заводить друзей? Так и поступлю."
            "Я расплатился с барменом (Мише он просто махнул рукой - мол, потом отдашь) и мы вышли."
            scene street_night
            show misha
            misha "Сократим здесь."
            "Он показал рукой на арку здания, ведущую во двор."
            max "Уверен?"
            misha "Ага."
            "Мы побрели между домами, и вдруг Миша остановился, уставившись на тёмные окна одного из зданий."
            misha "Ты знаешь такого писателя - Довлатова?"
            "Я, слабо знавший литературу, но где-то слышавший эту фамилию, неуверенно кивнул."
            misha "Хороший был чувак. «Чемодан» просто в кайф читать."
            max "Как-то ты внезапно его вспомнил."
            misha "А-а, ты ж не местный, не знаешь…"
            "Он театрально обвёл рукой дом, перед которым мы стояли."
            misha "Он тут родился. Правда, пробыл здесь недолго. Потом жил в Питере, потом в США. Но всё-таки…"
            misha "Ну, мне пора."
            max "Здорово поболтали. Предлагаю как-нибудь сыграть вместе."
            misha "Предложение принято. Бывай!"
            "Мы попрощались. Миша дёрнул подъездную дверь и махнул мне рукой."
    #Затемнение.
    scene d with Dissolve(1)
    jump day3