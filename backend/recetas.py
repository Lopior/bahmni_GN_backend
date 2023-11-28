from flask import jsonify
import mysql.connector
import config
#import time

def obtenerRecetas():
    conn = mysql.connector.connect(
        host=config.host,
        database=config.bd,
        user=config.username,
        password=config.password
    )

    #cur = conn.cursor()
    #cur.execute("SELECT * FROM Recetas_Electronicas")
    #ahora = time.strftime("%c") 
    #results = cur.fetchall()
    recetas = []
    content = {}
    #for result in results:
    #    content = {'id': result[0], 'paciente': result[2], 'fecha': result[3], 'estado': result[5]}
    #    recetas.append(content)
    #    content = {}


    #cur.close()
    #conn.close()
    return jsonify(recetas)