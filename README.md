# ligo-igo
Этот репозиторий содержит специфические скрипты и мануалы для специфических задач

Состав пакета:

khooylowbot.py

archivarius.py

capibarakoroed.py
    image1.jpg
    image2.jpg
    image3.jpg
    video.mp4

Инструкция по применению:

Перед началом работы полезно завести таблицу с названиями ботов, их токенами, данными api и отметить, каким скриптам они соответствуют и какие у них должны быть права. Также выясните SOURCE CHANNEL ID и TARGET CHANNEL ID, например, при помощи форварда сообщения с канала в адрес https://t.me/JsonDumpBot , проверьте их соответствие и добавьте их в таблицу. Помните, что токены ботов-админов, api id и api hash — крайне чувствительные данные, держите их в надежном месте.  


khooylowbot.py

Этот cкрипт на языке Python, который запускает бота в Telegram. Этот бот работает всегда. Для запуска бота вам нужно:

Получить токен для вашего бота в Telegram. Вы можете получить его, следуя инструкциям на официальном сайте Telegram: https://core.telegram.org/bots#6-botfather

Заменить "insert_token" в строке 10 на ваш токен.

Установить необходимые пакеты. Этот скрипт использует библиотеку telegram и re, которые вы можете установить, запустив команду в терминале:

pip3 install python-telegram-bot==13.7

Запустить скрипт. Скрипт можно запустить в вашей среде разработки или в терминале, перейдя в папку с файлом скрипта и запустив команду:

python3 khooylowbot.py

После запуска бот будет готов к работе и будет отвечать на сообщения в групповых чатах и личных сообщениях.

Для того чтобы добавить бота в группу и сделать его администратором, нужно:

Найти бота в Telegram, используя его имя пользователя или название.
Нажать на имя бота и открыть чат с ним.
Нажать на кнопку "Добавить в группу" и выбрать группу, в которую вы хотите добавить бота.
Открыть настройки группы и выбрать раздел "Администраторы".
Нажать на кнопку "Добавить администратора" и выбрать добавленного бота из списка контактов.
Убедиться, что у бота нет никаких прав, иначе отмените их.
После того, как вы добавите бота в группу и сделаете его администратором, он начнет работать и отвечать на сообщения в этой группе.


archivarius.py

Этот скрипт на языке Python используется для пересылки сообщений из одного канала в другой в Telegram. Он необходим, например, для архивации канала. Данный скрипт запускается один раз и работает, пока не скопирует весь канал. 

Чтобы запустить скрипт, сначала необходимо внести несколько изменений в код:

Замените "YOUR_API_TOKEN" на свой токен бота Telegram. Если у вас еще нет токена, то следует создать бота и получить его токен, следуя инструкциям на официальном сайте Telegram https://core.telegram.org/bots#6-botfather. Обратите внимание, что это должен быть другой бот. 

Замените "SOURCE_CHANNEL_ID" и "TARGET_CHANNEL_ID" на ID каналов, из которых и куда будут пересылаться сообщения.
Замените "START_MESSAGE_ID" на ID первого сообщения, которое нужно переслать.

После того, как вы внесете эти изменения, вы можете запустить скрипт. Для этого:

Откройте командную строку на своем компьютере.
Перейдите в папку, где находится файл со скриптом.
Убедитесь, что у вас установлен Python версии 3.x и все необходимые библиотеки (requests, telegram, python-telegram-bot).

Напишите команду 

python3 archivarius.py

чтобы запустить скрипт.

Сообщения будут пересылаться каждые 15 секунд до тех пор, пока вы не остановите скрипт вручную.
    
    
capibarakoroed.py

Данный скрипт предназначен для автоматического обновления медиа-файлов и подписи к сообщениям в заданном чате в Telegram. Для работы боту необходимо быть администратором с правами.

Для того, чтобы запустить этот скрипт, вам нужно:

Получить API ID и API HASH, создать бота и получить его токен.

Заменить YOUR_API_ID, YOUR_API_HASH, YOUR_BOT_TOKEN, YOUR_CHAT_ID на свои соответствующие значения.

Предварительно загрузить необходимые медиа-файлы (изображения и видео) в папку с данным скриптом.

Указать в переменной media_files список имен этих файлов.

Заменить caption_text на желаемую подпись к сообщениям.

Задать значения START_ID и END_ID - это идентификаторы сообщений в заданном чате, которые вы хотите обновить.

Сохранить изменения и запустить скрипт через командную строку.
    
 python3 capibarakoroed.py
    
Для получения API ID и API HASH для Telegram API вы должны выполнить следующие действия:

Перейдите на сайт Telegram API (https://my.telegram.org/auth) и авторизуйтесь.

После авторизации вы увидите страницу с заголовком "API Development Tools".

На этой странице вам нужно создать новое приложение, нажав на кнопку "Создать новое приложение" (Create Application).

В появившемся окне заполните поля "Название" (App title) и "Сайт" (App website). Заполнение остальных полей необязательно.

После заполнения формы нажмите на кнопку "Создать приложение" (Create application).

На следующей странице вы увидите ID приложения (API ID) и хеш приложения (API HASH). Сохраните их в надежном месте.

API ID и API HASH используются для аутентификации вашего приложения в Telegram API. Пожалуйста, не делитесь ими с другими людьми.

reposter.py




Порядок работы пакета:

archivarius запускается раньше всех и обрабатывает порядка 5000 постов в сутки. capibarakoroed на хорошем соединении обрабатывает посты вдвое быстрее, поэтому рассчитайте время запуска так, чтобы archivarius успевал копировать посты раньше, чем до них доберется capibara. Когда закончит archivarius, дайте закончить капибаре и после этого запускайте reposter.
khooylowbot работает независимо от всех может быть запущен и остановлен в любое время. 
Чтобы логи не сыпались в консоль, перед командами запуска поставьте nohup, например: nohup python3 script.py
Скрипты будут сыпать свои логи в файл nohup.out, он будет расти в размере. Можно выключить логгинг вообще в самих скриптах.

Если случился вылет или рестарт:
    archivarius - посмотрите номер последнего скопированного поста, поправьте стартовый номер в скрипте, после чего перезапустите;
    capibaracoroed - вручную перебором номера поста в ссылке найдите последний поправленный пост. Если вводить URL в поле search телеграма, он сразу будет показывать превью поста в результатах, по которому будет видно, поправлен пост, или нет. Меняйте номер поста в url и найдите последний поправленный. Выясните его номер и поправьте стартовый номер поста в скрипте, после чего перезапускайте;
    reposter - не нуждается в правке кода и начинает работать сразу после запуска;
    khooylowbot - та
