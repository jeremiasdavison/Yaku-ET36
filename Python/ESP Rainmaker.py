import requests
import json
import accounts     #Libreria con las cuentas de acceso
import pymongo
from pymongo import MongoClient
from time import gmtime, strftime
import time as t
import datetime


def main():
    data = accounts.data
    response = requests.post(url='https://api.rainmaker.espressif.com/v1/login', data=json.dumps(data)) #Devuelve los tokens
    response = json.loads(response.content) # Carga el contenido de los tokens

    headers={"Authorization": response['accesstoken']}
    #nodesList = requests.get(url='https://api.rainmaker.espressif.com/v1/user/nodes', headers=headers)
    #nodeList = json.loads(nodesList.content)
    
    nodoUno = json.loads((requests.get(url="https://api.rainmaker.espressif.com/v1/user/nodes/params?node_id=USANptj2EUMgXBjNZnwqhE", headers=headers).content))
    #nodoUno_device = nodoUno['Temperature Sensor']['Name']
    #nodoUno_val = nodoUno['Temperature Sensor']['Temperature']
    #nodoUno_params = nodoUno['Temperature Sensor'].keys()
    nodoUno = nodoUno['Temperature Sensor']
    ct = datetime.datetime.now()
    # ts store timestamp of current time
    ts = ct.timestamp()
    
    nodoUno['Date'] = ts # strftime("%d %b %Y, %H:%M")   Agrega al dic el tiempo
    return nodoUno
 
def data_base():
    mongoUser = accounts.mongoUser
    client = pymongo.MongoClient(mongoUser)
    db = client.Yaku

    coleccion = db['Nodo 1']
    print(main())
    coleccion.insert([main()])

if __name__ == '__main__':
    while True:
        data_base()
        t.sleep(60)