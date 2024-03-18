from pymongo import MongoClient
from datetime import datetime
from threading import Thread
from time import sleep
import random

client = MongoClient("mongodb://localhost:27017")
if client:
    print("Connected to MongoDB successfully!")
    db = client["bancoiot"]
    sensores = db.sensores
else:
    print("Failed to connect to MongoDB!")


def inserir_documento_sensor(sensor):
    sensores.insert_one({
        'nomeSensor': sensor,
        'valorSensor':0,
        'unidadeMedida':'C°',
        'sensorAlarmado':False
    })

def atulizar_temperatura_documento_sensor(sensor, temperatura):
    if(temperatura > 38):
        return True
    else:
        sensor_estado = False
        sensores.update_one({'nomeSensor': sensor}, {'$set':{'valorSensor': temperatura}})

    print(f"Sucesso: {sensor}: {temperatura} C°, Alarmado:{sensor_estado}")
    return sensor_estado


def realizar_leitura_sensor(sensor, intervalo):
    while True:
        temperatura = random.randint(30, 40)
        
        if(temperatura > 38):
            print(f"Atenção! Temperatura muito alta! Verificar {sensor}!")
            break
        else:
            atulizar_temperatura_documento_sensor(sensor, temperatura)
            sleep(intervalo)


inserir_documento_sensor("Sensor 1")
inserir_documento_sensor("Sensor 2")
inserir_documento_sensor("Sensor 3")

a = Thread(target=realizar_leitura_sensor, args=("Sensor 1", 1))
b = Thread(target=realizar_leitura_sensor, args=("Sensor 2", 1))
c = Thread(target=realizar_leitura_sensor, args=("Sensor 3", 1))

a.start()
b.start()
c.start()