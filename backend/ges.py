from flask import jsonify
#import pymysql
import mysql.connector
import config
from flask import request
import json
from correo import enviarCorreoElectronicoGes
from datetime import datetime
import uuid


def obtenerGes():
    conn = mysql.connector.connect(
        host=config.host,
        database=config.bd_notificacion,
        user=config.username,
        password=config.password
    )

    cur = conn.cursor()
    cur.execute("SELECT ng.id, ng.rut_paciente, ng.nombre_paciente, ng.fechahora_registro, ng.diagnostico_ges, ng.estado FROM notificacion_ges ng;")

    results = cur.fetchall()
    ges = []
    content = {}
    for (id,rut_paciente,nombre_paciente,fecha_registro,diagnostico_ges,estado) in results:
        content = {'id': id, 'rut_paciente': rut_paciente, 'paciente': nombre_paciente, 'fecha': fecha_registro, 'problema_ges': diagnostico_ges, 'estado': estado}
        ges.append(content)
        content = {}


    cur.close()
    conn.close()
    return jsonify(ges)

#obtener GES por run
def obtenerGesPorRun(run_paciente):
    conn = mysql.connector.connect(
        host=config.host,
        database=config.bd_notificacion,
        user=config.username,
        password=config.password
    )

    cur = conn.cursor()
    cur.execute("SELECT ng.id, ng.rut_paciente, ng.nombre_paciente, ng.fechahora_registro, ng.diagnostico_ges, ng.estado FROM notificacion_ges ng WHERE ng.rut_paciente = %s;", (run_paciente,))

    results = cur.fetchall()
    ges = []
    content = {}
    for (id,rut_paciente,nombre_paciente,fecha_registro,diagnostico_ges,estado) in results:
        content = {'id': id, 'rut_paciente': rut_paciente, 'paciente': nombre_paciente, 'fecha': fecha_registro, 'problema_ges': diagnostico_ges, 'estado': estado}
        ges.append(content)
        content = {}


    cur.close()
    conn.close()
    return jsonify(ges)


#obtener GES por uuid
def obtenerGesPorUuid(uuid):
    conn = mysql.connector.connect(
        host=config.host,
        database=config.bd_notificacion,
        user=config.username,
        password=config.password
    )

    cur = conn.cursor()
    cur.execute("SELECT ng.id, ng.nombre_establecimiento, ng.direccion_establecimiento, ng.ciudad_establecimiento, ng.nombre_notificador, ng.rut_notificador, ng.rut_paciente, ng.nombre_paciente, ng.aseguradora_paciente, ng.direccion_paciente, ng.comuna_paciente, ng.region_paciente, ng.telefono_fijo_paciente, ng.celular_paciente, ng.email_paciente, ng.diagnostico_ges, ng.tipo, ng.fechahora_notificacion, ng.nombre_representante, ng.rut_representante, ng.telefono_representante, ng.email_representante, ng.estado, ng.firma_notificador, ng.firma_paciente FROM notificacion_ges ng WHERE ng.uuid = %s;", (uuid,))

    results = cur.fetchall()
    #ges = []
    content = {}
    for (id, nombre_establecimiento, direccion_establecimiento, ciudad_establecimiento, nombre_notificador, rut_notificador, rut_paciente, nombre_paciente, aseguradora_paciente, direccion_paciente, comuna_paciente, region_paciente, telefono_fijo_paciente, celular_paciente, email_paciente, diagnostico_ges, tipo, fechahora_notificacion, nombre_representante, rut_representante, telefono_representante, email_representante, estado, firma_notificador, firma_paciente) in results:
        fechahora_notificacion = fechahora_notificacion.strftime("%d/%m/%Y %H:%M")
        content = {'id': id, 'nombre_establecimiento': nombre_establecimiento, 'direccion_establecimiento': direccion_establecimiento, 'ciudad_establecimiento': ciudad_establecimiento,'nombre_notificador': nombre_notificador, 'rut_notificador': rut_notificador, 'rut_paciente': rut_paciente, 'nombre_paciente': nombre_paciente, 'aseguradora_paciente': aseguradora_paciente, 'direccion_paciente': direccion_paciente, 'comuna_paciente': comuna_paciente, 'region_paciente': region_paciente, 'telefono_fijo_paciente': telefono_fijo_paciente, 'celular_paciente': celular_paciente, 'email_paciente': email_paciente, 'diagnostico_ges': diagnostico_ges, 'tipo': tipo, 'fechahora_notificacion': fechahora_notificacion, 'nombre_representante': nombre_representante, 'rut_representante': rut_representante, 'telefono_representante': telefono_representante, 'email_representante': email_representante, 'estado': estado, 'firma_notificador': firma_notificador, 'firma_paciente': firma_paciente}
    

    cur.close()
    conn.close()
    return jsonify(content)

#obtener GES por id

def obtenerGesPorId(id_ges):
    conn = mysql.connector.connect(
        host=config.host,
        database=config.bd_notificacion,
        user=config.username,
        password=config.password
    )

    cur = conn.cursor()
    cur.execute("SELECT ng.id, ng.nombre_establecimiento, ng.direccion_establecimiento, ng.ciudad_establecimiento, ng.nombre_notificador, ng.rut_notificador, ng.rut_paciente, ng.nombre_paciente, ng.aseguradora_paciente, ng.direccion_paciente, ng.comuna_paciente, ng.region_paciente, ng.telefono_fijo_paciente, ng.celular_paciente, ng.email_paciente, ng.diagnostico_ges, ng.tipo, ng.fechahora_notificacion, ng.nombre_representante, ng.rut_representante, ng.telefono_representante, ng.email_representante, ng.estado, ng.firma_notificador, ng.firma_paciente, ng.uuid FROM notificacion_ges ng WHERE ng.id = %s;", (id_ges,))

    results = cur.fetchall()
    content = {}
    for (id, nombre_establecimiento, direccion_establecimiento, ciudad_establecimiento, nombre_notificador, rut_notificador, rut_paciente, nombre_paciente, aseguradora_paciente, direccion_paciente, comuna_paciente, region_paciente, telefono_fijo_paciente, celular_paciente, email_paciente, diagnostico_ges, tipo, fechahora_notificacion, nombre_representante, rut_representante, telefono_representante, email_representante, estado, firma_notificador, firma_paciente, uuid) in results:
        if fechahora_notificacion is not None and fechahora_notificacion != "":
            fechahora_notificacion = fechahora_notificacion.strftime("%d/%m/%Y %H:%M")
        else:
            fechahora_notificacion = None
        content = {'id': id, 'nombre_establecimiento': nombre_establecimiento, 'direccion_establecimiento': direccion_establecimiento, 'ciudad_establecimiento': ciudad_establecimiento, 'nombre_notificador': nombre_notificador, 'rut_notificador': rut_notificador, 'rut_paciente': rut_paciente, 'nombre_paciente': nombre_paciente, 'aseguradora_paciente': aseguradora_paciente, 'direccion_paciente': direccion_paciente, 'comuna_paciente': comuna_paciente, 'region_paciente': region_paciente, 'telefono_fijo_paciente': telefono_fijo_paciente, 'celular_paciente': celular_paciente, 'email_paciente': email_paciente, 'diagnostico_ges': diagnostico_ges, 'tipo': tipo, 'fechahora_notificacion': fechahora_notificacion, 'nombre_representante': nombre_representante, 'rut_representante': rut_representante, 'telefono_representante': telefono_representante, 'email_representante': email_representante, 'estado': estado, 'firma_notificador': firma_notificador, 'firma_paciente': firma_paciente, 'uuid': uuid}

    cur.close()
    conn.close()
    return jsonify(content)



#cambio de estado de GES por id
def cambiarEstadoGes(id_ges, estado, practitioner_user):
    
    practitioner_user = practitioner_user.strip()  # Remove leading and trailing spaces
    
    try:
        conn = mysql.connector.connect(
            host=config.host,
            database=config.bd_notificacion,
            user=config.username,
            password=config.password
        )
        

        #calcular fecha y hora actual
        bd_openmrs = config.bd_openmrs
        current_datetime = datetime.now()
        cur = conn.cursor()
        cur.execute("UPDATE notificacion_ges SET estado = %s, fechahora_actualizacion = %s, usuario_actualizacion = (SELECT t.person_id FROM "+bd_openmrs+".users t WHERE username = %s) WHERE id = %s;", (estado, current_datetime, practitioner_user, id_ges))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'cod': 'ok','message': 'Estado cambiado'})
    
    except Exception as e:
        print("Error al cambiar estado GES:", str(e))
        return jsonify({'cod': 'error', 'message': 'error al notificar GES'+str(e)})

#Notificar GES

# Notificar GES, actualiza datos y confirma la notificacion en la BD

def notificarGes(request):
    
    try:
        data = json.loads(request)
        print("********** Back: request del frontend en objeto python **********")
        print(data)

        conn = mysql.connector.connect(
            host=config.host,
            database=config.bd_notificacion,
            user=config.username,
            password=config.password
        )

        
        cur = conn.cursor()
        current_datetime = datetime.now()
        uuid_v4 = str(uuid.uuid4())
        cur.execute("UPDATE notificacion_ges SET notificador_id = %s, nombre_notificador = %s, rut_notificador = %s, email_paciente = %s, tipo = %s, fechahora_notificacion = %s, nombre_representante = %s, rut_representante = %s, telefono_representante = %s, email_representante = %s, estado = %s , fechahora_actualizacion = %s, usuario_actualizacion = %s, uuid = %s WHERE id = %s;", (data['notificador_id'], data['nombre_notificador'], data['rut_notificador'], data['email_paciente'],  data['tipo'], current_datetime, data['nombre_representante'], data['rut_representante'], data['telefono_representante'], data['email_representante'], 'N', current_datetime, data['notificador_id'], uuid_v4 , data['id']))
        conn.commit()
        cur.close()
        conn.close()
        
        enviarCorreoElectronicoGes(data['email_paciente'], "http://http://127.0.0.1:5000/notificaciongespaciente/"+uuid_v4)


        return jsonify({'cod': 'ok', 'message': 'GES notificado correctamente'})

    except Exception as e:
        print("Error al notificar GES:", str(e))
        return jsonify({'cod': 'error', 'message': 'error al notificar GES'+str(e)})

        
    

def firmaPacienteGes(request):
    
    try:
        data = json.loads(request)
        print("********** Back: request del frontend en objeto python **********")
        print(data)

        conn = mysql.connector.connect(
            host=config.host,
            database=config.bd_notificacion,
            user=config.username,
            password=config.password
        )

        cur = conn.cursor()
        current_datetime = datetime.now()
        cur.execute("UPDATE notificacion_ges SET firma_paciente = %s, fechahora_firma_paciente = %s, fechahora_actualizacion = %s, estado = %s WHERE id = %s;", (data['firma_paciente'], current_datetime, current_datetime, 'F',  data['id']))
        conn.commit()
        cur.close()
        conn.close()
        
        #enviarCorreoElectronicoGes(data['email_paciente'], "http://localhost:5000/notificaciongespaciente/123")


        return jsonify({'cod': 'ok', 'message': 'GES firmado correctamente'})

    except Exception as e:
        print("Error al notificar GES:", str(e))
        return jsonify({'cod': 'error', 'message': 'error al notificar GES'+str(e)})
        

#obtener person_id y person_name del practioner con el id desde la bd
def obtenerPractitioner(practitioner_id):
    try:
        print(practitioner_id)
        practitioner_id = practitioner_id.strip()  # Remove leading and trailing spaces
        practitioner_id = practitioner_id.replace('"', '')  # Remove double quotes
        
        conn = mysql.connector.connect(
            host=config.host,
            database=config.bd_openmrs,
            user=config.username,
            password=config.password
        )

        cur = conn.cursor()
        cur.execute("SELECT p.person_id, p.given_name, p.family_name FROM users t INNER JOIN person_name p ON t.person_id = p.person_id WHERE t.username = %s;", (practitioner_id,))

        results = cur.fetchall()
        content = {}
        for (person_id, given_name, family_name) in results:
            content = {'person_id': person_id, 'given_name': given_name, 'family_name': family_name}

        cur.close()
        conn.close()
        print(content)
        return jsonify(content)
    except Exception as e:
        print("Error al obtener datos del profesional:", str(e))
        return jsonify({'cod': 'error', 'message': 'error al obtener datos del profesional'+str(e)})
    




