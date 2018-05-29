from flask import Flask

app = Flask(__name__) #Flask necesita como primer parametro el nombre del modulo.

@app.route('/')
def hello_world():
    return 'Hola, mundo.'

if __name__ == '__main__':
    app.run()
