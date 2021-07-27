# Чат-боты для Telegram и Вконтакте(Общение с группой), с использованием DialogFlow

Скрипт состоит из нескольких частей: бот для общения в Telegram, бот для общения
в группе во Вконтакте. Боты используют сервис [Dialogflow](https://cloud.google.com/dialogflow/docs/)
от Google, который отвечает на запросы с использованием обучаемой нейросети. В проект 
входит дополнительный telegram-бот для получения сообщений об ошибках. В проект входит
отдельный скрипт для загрузки новых вопросов и ответов.

![vk-bot](vk-bot.gif)|![tg-bot](tg-bot.gif)
---------------------|---------------------

[Пример чат-бота telegram](https://t.me/Sheru_support_bot).

## Как установить

### Скачать 

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/support-bot/archive/master.zip) этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

#### Получение токенов, ключей, привязка Dialogflow

1. Создать двух ботов для Telegram, получить их токены у [Отца Ботов](https://telegram.me/BotFather).
   Один для общения, другой для сбора логов.
2. Получить свой chat_id у  телеграм-бота [userinfobot](https://telegram.me/userinfobot).
3. Создайте группу в Vk, она будет доступна во вкладке [управление](https://vk.com/groups?tab=admin). 
   В настройках группы включите отправку сообщений, создайте ключ доступа.
<a href="https://ibb.co/J278JbK"><img src="https://i.ibb.co/wCW8mbR/8.png" alt="8" border="0"></a>
4. Создайте проект на Google cloud, следуя [документации](https://cloud.google.com/dialogflow/es/docs/quick/setup).
   Вы получите уникальный Project id:  
   <a href="https://ibb.co/FqS75YZ"><img src="https://i.ibb.co/Z1nTBg4/photo-2021-07-27-15-19-41.jpg" alt="photo-2021-07-27-15-19-41" border="0"></a>
5. Следуя [документации](https://cloud.google.com/dialogflow/es/docs/quick/setup),
   после выполнения пункта "Create a service account and download the private key 
   file", ключевой json-файл загрузится на ваш компьютер. Переименуйте в 
   google-credentialsa.json и положите в данный репозиторий.
6. На сайте [DialogFlow](https://dialogflow.cloud.google.com/#/getStarted) создайте 
   агента, привязав к нему идентификатор проекта из шага 4(Project id). Выберите
   русский язык для корректной работы агента. [Инструкция](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
   Вы увидите меню агента:  
   <a href="https://ibb.co/4P9JjJR"><img src="https://i.ibb.co/syktFt9/agent.png" alt="agent" border="0"></a>

#### Переменные окружения

Создайте в корне репозитория файл `.env` и добавьте в него следующие строки:

```sh
TG_DIALOG_BOT=Токен_телеграм_бота
TG_SERVICE_BOT=Токен_бота_логов
TG_CHAT_ID=Чайт_ID_бота_логов
VK_GROUP_TOKEN=Токен_группы_вк
GOOGLE_APPLICATION_CREDENTIALS=Полный_путь_к_файлу_google-credentialsa.json
PROJECT_ID=Ваш_Project_ID
```

Пример пути к файлу google-credentialsa.json:  
`C:/Users/Ваш_пользователь/Downloads/Support bot/google-credentials.json`

### Запуск локально

Telegram-бот:
```sh
python tg_bot.py
```

Vk-бот:
```sh
python vk_bot.py
```

### Деплой и запуск на Heroku

1. Зарегистрируйтесь на Heroku и создайте приложение (app):  
   
<a href="https://ibb.co/r5mDQ2Z"><img src="https://i.ibb.co/447hFRj/Screenshot-from-2019-04-10-17-43-30.png" alt="Screenshot-from-2019-04-10-17-43-30" border="0"></a><br />  

2. Опубликуйте код репозитория на свой GitHub.  
3. Привяжите свой аккаунт на GitHub к Heroku:  

<a href="https://ibb.co/Hqy7yvP"><img src="https://i.ibb.co/zZgsgc2/123.png" alt="123" border="0"></a>

4. Задеплойте проект на Heroku:  

<a href="https://ibb.co/kgpN9tF"><img src="https://i.ibb.co/1f3Fdkx/5353.jpg" alt="5353" border="0"></a>  

5. В разделе Resources включите ботов vk и telegram:  

<a href="https://ibb.co/n3VbdLj"><img src="https://i.ibb.co/bHyPwKX/666.png" alt="666" border="0"></a>  

6. Перейдите в раздел Settings и в пункте Config Vars укажите из вашего файла .env
   TG_DIALOG_BOT, TG_SERVICE_BOT, TG_CHAT_ID, VK_GROUP_TOKEN, PROJECT_ID:  

<a href="https://ibb.co/5x70h7H"><img src="https://i.ibb.co/FqPr4PT/8.png" alt="8" border="0"></a>  

7. В тот же Config Vars необходимо прописать ваш ключ google-credentialsa.json.
   Сделать это нужно следующим образом:
   1. Создайте ключ Config Vars GOOGLE_CREDENTIALS и вставьте содержимое JSON-файла 
      учетных данных учетной записи службы как есть.
   2. Создайте ключ в Config Vars GOOGLE_APPLICATION_CREDENTIALS и установите 
      значение как google-credentials.json.
      
<a href="https://ibb.co/4Nd361J"><img src="https://i.ibb.co/C02DkPW/3gxMn.png" alt="3gxMn" border="0"></a>

8. В разделе Buildpacks добавьте билд и вставьте в него строку
   `https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack`.
   Если билд heroku/python отсутствует, добавьте его. Конечный результат:  
   
<a href="https://ibb.co/9HGWfSL"><img src="https://i.ibb.co/zVNZLDY/photo-2021-07-27-15-19-41.jpg" alt="photo-2021-07-27-15-19-41" border="0"></a>

Примечание: добавление билдпака в шаге 8 необходимо для создания файла google-credentials.json
и корректной работы скрипта.

9. Задеплоить повторно(пункт 4).  

Вы увидите сообщение о запуске в чате бота-логгера:  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/jWbcXx0/agent.png" alt="agent" border="0"></a>

#### Обучение новым агента dialogflow новым фразам

Для обучения новым фразам в корне репозиторий создайте файл `questions.json` и добавьте
в него свои вопросы и ответы. Пример файла:

```sh
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту прийдёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}
```

Затем запустите скрипт обучения:

```sh
python agent_training.py
```

#### Работа с ботом из командной строки

Установить консольный [CLI client](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Быстрый старт CLI:

Примечание: для Windows можно открыть командную строку cmd и работать в ней.

Подключение к Heroku:
```sh
heroku login
```
Посмотреть список своих приложений:
```sh
heroku apps
```
Посмотреть логи:
```sh
heroku logs --app=имя_приложения
```
Статус бота:
```sh
heroku ps -a имя_приложения
```
Добавить билдпак(пример):
```sh
heroku buildpacks:set https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack -a Имя-Приложения
```

[Руководство по Heroku CLI](https://devcenter.heroku.com/articles/using-the-cli)

### Цель проекта

Код написан в учебных целях, это часть курса по созданию [чат-ботов](https://dvmn.org/modules/chat-bots/)
на сайте веб-разработчиков [Девман](https://dvmn.org/api/docs/).
