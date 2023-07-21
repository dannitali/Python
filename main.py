from flask import Flask, render_template

#crear un objeto flask 
app =  Flask(__name__)

#con el objeto app definimos una ruta 
@app.route('/hola')

def index():
    return 'Hola mundo :)'

@app.route('/paises')

def continentes():

    
    continentes = [
        {
            "Nombre"  :"América",
            "Paises"  : [
                { "Nombre" : "Colombia",
                  "Capital": "Bogotá",
                  "Moneda" : "Peso",
                  "Poblacion" : 52
                },
                { "Nombre" : "Peru",
                  "Capital": "Lima",
                  "Moneda" : "Sol",
                  "Poblacion" : 33
                }
                
            ]
        },
        {
            "Nombre"  :"Europa",
            "Paises"  : [
                { "Nombre" : "España",
                  "Capital": "Madrid",
                  "Moneda" : "Euro",
                  "Poblacion" : 47
                },
                { "Nombre" : "Alemania",
                  "Capital": "Berlin",
                  "Moneda" : "Euro",
                  "Poblacion" : 83
                }
                
            ]
        },
        {
             "Nombre"  :"ASIA",
             "Paises"  : [
                 { "Nombre" : "Japon",
                  "Capital": "Tokio",
                  "Moneda" : "Yen Japones",
                   "Poblacion" : 125
                },
                { "Nombre" : "China",
                  "Capital": "Pekin",
                  "Moneda" : "Yuan Chino",
                   "Poblacion" : 1.412 
                }
                
            ]
        }
        
    
    ]
    
    ''''variables de conteo para cada continente'''
    longitud_america = len(continentes[0]["Paises"])
    longitud_europa = len(continentes[1]["Paises"])
    longitud_asia = len(continentes[2]["Paises"])
    print(longitud_america)
    print(longitud_europa)
    print(longitud_asia)
    user = 'Danna y Brigitho'
    return render_template('paises_listas.html',
                           user = user,
                           continentes = continentes,
                           america=longitud_america,
                           asia=longitud_asia,
                           europa=longitud_europa)   

