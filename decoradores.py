# -*- coding: utf-8 -*-

def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('la contraseña es incorrecta')
    return wrapper

@protected
def protected_func():
    print('tu contraseña es correcta')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)
