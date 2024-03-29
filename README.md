# Прикинь будущую зарплату
Проект позволит вам узнать статистику по вакансиям программиста с различных сайтов.
### Как установить
Python 3 должен уже быть установлен. Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
### Как настроить окружение
Для доступа к API SuperJob вам необходимо [зарегистрировать](https://api.superjob.ru/register) свое приложение. После регистрации вы получите `Secret key` своего приложения, который необходимо присвоить переменной `SUPERJOB_APP_ID` в файле `.env`.
```
SUPERJOB_APP_ID=v3.h.4225001.5f33d302f6bcae9d13cdd5a2c48a4c7dbf5b2f09.57ec80a7e04344a41f0ed7a900cd2396aa46c30a
```
### Как пользоваться скриптом
Для запуска скрипта воспользуйтесь примером запуска из консоли. 

В проекте подключено два сайта с вакансиями, но вы можете добавить ещё. Для этого, создайте файл с расширением *.py*, в котором вам необходимо написать код для извлечения данных по вакансиям с этого сайта. 
Для примера возьмите уже готовые файлы, и замените параметры согласно API сайта, с которым вы работаете. 

После написания кода, в *main.py* добавьте переменную с полученными данными в *table_entries* (не забудьте импортировать свой скрипт).
### Пример запуска из консоли
```
$ python main.py
```
### Цель проекта
Код написан в образовательных целях на онлайн курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)