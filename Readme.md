Описание проекта

Разработка системы управления уроками
Проект основан на курсе домашних заданий по LMS системе

Требования к ландшафту
Создана база на PostgreSQL
Заполнен файл переменных окружения .env на основе .env.sample
Установлены библиотеки на основе requirements.txt
Установлен Redis или его аналоги для OC Windows
Выполнена настройка Celery для отправки уведомлений

Проект адаптирован для запуска с помощью DOCKER
Необходимые настройки

Создать и заполнить файл переменных окружения .env.docker с учетом настроек в файле docker-compose.yml
Создать образы и контейнеры DOCKER с помощью команд
docker-compose build
docker-compose up
