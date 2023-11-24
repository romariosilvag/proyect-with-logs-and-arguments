
from parametros import CargarParametros
from peticion import *
from logs import *
from argumentos import *


def main():
    severidad = CargarArgumentos.cargarSeveridadLogs()
    Logs.cargarLogs(severidad,"main_log")
    logging.info(f"Severidad configurada: {severidad}")
    logging.info('Inicio del proceso.')
    logging.warning('Algo anda mal !!!')
    jsonResultado = Peticion.ejecutarPeticion(CargarParametros.parametros())
    logging.warning(f'Respuesta de peticion: {jsonResultado}')
    logging.error(f"Error encontrado!!!")
    logging.critical(f"Error CRITICO encontrado!!!")
    logging.info('Fin del proceso.')

if __name__ == '__main__':
    main()
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RomarioSilvaG
"""