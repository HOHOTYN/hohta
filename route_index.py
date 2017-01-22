#!/usr/bin/env python3

from bottle import get

@get('/')
def index_page():
  return 'Здесь будет Сашин крутой сайт hohta.ru!'

@get('/test/')
def index_page():
  return 'ТЕСТ 1'
