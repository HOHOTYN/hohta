#!/usr/bin/env python3

import bottle
from bottle import error as error_page
import route_index

app = application = bottle.app()

@error_page(404)
def error404(error): # pylint: disable=unused-argument
    return 'Нет такой страницы'

@error_page(500)
def error500(error):
    return 'Ошибка сервера: {}'.format(error)

if __name__ == '__main__':
    bottle.run(app=app, host='0.0.0.0', port=8080, debug=True, reloader=True)
