# Телеграм-бот для анализа PINFL

Этот проект представляет собой телеграм-бота, который анализирует введенный пользователем ПИНФЛ (Персональный идентификационный номер физического лица) и сообщает о его валидности, а также о дате рождения, коде региона и других параметрах.

## Зачем этот проект нужен?

ПИНФЛ (PINFL) - это уникальный идентификационный номер, используемый в ряде стран для идентификации граждан. Этот проект предназначен для обработки и анализа PINFL, чтобы убедиться в его корректности и предоставить информацию о дате рождения и других данных, содержащихся в этом номере.

## Как использовать?

1. Перейдите в деррикторию проекта

2. Скопируйте ``` .env.example ``` в ``` .env ```

3. Обновите все значения в ``` .env ```

4. ``` docker build -t pinfl_bot . ```

5. ``` docker run -d pinfl_bot ```

## Дополнительные функции

1. Бот предварительно проверяет введенный текст на наличие только цифр и длину не менее 14 символов. Если введенный текст не соответствует этим критериям, бот отправит сообщение с соответствующим предупреждением.

2. Если введенный PINFL короче 14 символов, недостающие символы будут заполнены нулями перед анализом.
