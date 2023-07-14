from flask import Flask

#crear un objeto flask 
app =  Flask(__name__)

#con el objeto app definimos una ruta 
@app.route('/')

def index():
    return 'Hola mundo :)'
