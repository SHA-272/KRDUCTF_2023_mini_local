# Rndint oneluv

## Описание 

Как бы это странно не звучало, но Евпатий сегодня не в настроении...
После того как компания урезала ему зарплату он решил поломать весь код
Придя в себя он начал восстанавливать, но напрочь забыл ключ, хотяб шифр остался и на том спасибо... хотя это ему никак не поможет, так как без ключа он не сможет даже к себе на рабочее место зайти...
Помогите ему справиться с данной задачей

## Публикация

Дать файлы из папки ./public/

## Решение

Декодировать hex строку шифротекста, через b64decode и перебором ключа random.randint(0, 255) перебрать все возможные ключи, и через функцию расшифровать данный нам шифртекст

## Ответ

krdu{6c306c5f406c6d3073745f4033735f7233744072643364}