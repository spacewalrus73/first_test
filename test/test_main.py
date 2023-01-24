#!/usr/bin/env python3
from main import capitalize

if capitalize('hello') != 'Hello':
    raise Exception("Функция работает неверно!")
if capitalize('') != '':
    raise Exception("Функция работает неверно!")

print('Все тесты пройдены!')