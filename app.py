from flask import Flask, jsonify, request
from flask_cors import CORS
#import mysql.connector
#import pymysql
#import config
#import time

from recetas import obtenerRecetas
from ges import obtenerGes
from ges import obtenerGesPorRun
from ges import cambiarEstadoGes
from ges import obtenerGesPorId
from ges import notificarGes
from ges import firmaPacienteGes
from ges import obtenerGesPorUuid
import json

app = Flask(__name__)
CORS(app)

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Recetas
# Get Data Routes
@app.route('/recetas', methods=['GET'])
def getRecetas(): 
    return obtenerRecetas()

# GES
# Get GES Routes
@app.route('/ges', methods=['GET'])
def getGes():
    patientidentifier = request.args.get('patientidentifier')
    uuid = request.args.get('uuid')
    
    if patientidentifier is not None and patientidentifier != '':
        return obtenerGesPorRun(patientidentifier)
    else:
        if uuid is not None and uuid != '':
            return obtenerGesPorUuid(uuid)
        else:
            return obtenerGes()


# obtener notificaciones ges por id
@app.route('/ges/<string:id_ges>', methods=['GET'])
def getGesById(id_ges):
     return obtenerGesPorId(id_ges)



# actualizar estado de GES por id
@app.route('/ges/<string:id_ges>/<string:estado>', methods=['PUT'])
def updateGes(id_ges, estado):
    return cambiarEstadoGes(id_ges, estado)


# Notificar GES Routes
@app.route('/ges', methods=['POST'])
def notifyGes():
    print("********** Back: request del frontend **********")
    print(request.json)
    return notificarGes(request.json)

# Notificar GES Routes
@app.route('/ges/firma', methods=['POST'])
def PatientSignGes():
    print("********** Back: request del frontend **********")
    print(request.json)
    return firmaPacienteGes(request.json)


# Run Server
if __name__ == '__main__':
    app.run(debug=True, port=4000)