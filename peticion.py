import requests
from requests.exceptions import Timeout
import urllib3 
import json
import logging

class Peticion:
    
    def ejecutarPeticion(parametros):
        """Ejecutar peticion Http

        Args:
            parametros (dict): diccionario con los parametros del ambiente seleccionado

        Returns:
            list: retorna una lista con los valores a procesar
        """
        try:    
            logging.info('Ejecutando peticion ...')
            # Excepcion de warnings
            urllib3.disable_warnings()          
            # Request API
            response = requests.request(
                parametros["metodo"], 
                parametros["tenantAmb"]+parametros["queryParams"], 
                headers={ 'accept': parametros["accept"], 'Authorization': '{}'.format(parametros["tockenAmb"]) } , 
                verify=False, 
                timeout=20 # timeout configurado de 20 seg
                ) 

            #print(response.url) # Ver url api completa
        except Timeout:
            logging.critical(f'Timeout al consumir : {parametros["tenantAmb"]+parametros["queryParams"]}')        
        except Exception as e:
            logging.critical(f'Error al consumir : {parametros["tenantAmb"]+parametros["queryParams"]}')  
            logging.error(f'Detalle del error : {e}')
        else:
            if response.status_code == 200:
                logging.warning(f'Peticion finalizo correctamente, codigo de respuesta http {response.status_code}.')                
                # Transformar Json
                data = response.content
                data.decode("utf-8")
                response = json.loads(data)
            else:                
                logging.critical(f'Peticion NO finalizo correctamente, codigo de respuesta http {response.status_code}.')
                logging.error(f'Detalle del error : {response.content.decode("utf-8")}')
                response = ""
        
        #with open('data.json', 'w') as f: # Exportar json
        #    json.dump(response, f)

        return response
                
#parametros = cargarParametros.parametros()
#print(parametros)

#resultadoJson = peticion.ejecutarPeticion(parametros)
#print(resultadoJson)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RomarioSilvaG
"""