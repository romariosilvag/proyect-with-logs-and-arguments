import logging
from logging.handlers import RotatingFileHandler
import os

#from argumentos import *

class Logs:

    def cargarLogs(severidad,nombreArchivo):
        handler = RotatingFileHandler(Logs.directorioLogs(nombreArchivo), maxBytes=1024*1024*5, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        handler.setFormatter(formatter)
        severidad = logging.getLevelName(severidad)
        logging.basicConfig(level=severidad, handlers=[handler])

    def directorioLogs(nombreArchivo):

        try:
            logs = os.listdir(os.getcwd())
            if "logs" in logs:
                pass
            else:
                os.makedirs("logs")
        except:
            nombreLog = os.getcwd()+"\\"+nombreArchivo+".log"
        else:
            nombreLog = os.getcwd()+"\\logs\\"+nombreArchivo+".log"      
        finally:            
            pass
        return nombreLog



#test = Logs.cargarLogs(CargarArgumentos.cargarSeveridadLogs(),__file__)
#print(test)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RomarioSilvaG
"""