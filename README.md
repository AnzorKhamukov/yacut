# Проект YaCut - сервис для укорачивания ссылок.
# Описание:
 Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
 Ключевые возможности сервиса:
 генерация коротких ссылок и связь их с исходными длинными ссылками,
 переадресация на исходный адрес при обращении к коротким ссылкам.
 Сервис состоит из пользовательского интерфейса и REST API.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone github.com/AnzorKhamukov/yacut/
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл с переменными окружения .env 
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
Выполнить миграции :
```
flask db init
```
```
flask db migrate
```
Запустить сервис на веб-сервере разработки Flask:
```
flask run
```
