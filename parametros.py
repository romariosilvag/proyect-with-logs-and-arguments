import configparser
import logging

class CargarParametros:

    def parametros(amb = 0):
        """Cargar parametros para API

        amb = 0 : ambiente productivo (Por defecto)
        amb = 1 : ambiente laboratorio

        Returns:
            dict: retorna diccionario con los parametros del ambiente seleccionado
        """
        logging.warning(f'Cargando parametros, ambiente {amb}.')
        config = configparser.ConfigParser()
        config.read('config.ini')

        tenant = config['tenant']
        params = config['params']
        headers = config['headers']
        tocken = config['tocken']
        maestro = config['maestro']

        if amb == 0:
            tenantAmb = tenant['pdn']
            tockenAmb = tocken['pdn'] 
        else:
            tenantAmb = tenant['lab']
            tockenAmb = tocken['lab'] 

        queryParams = params['queryParams']
        accept = headers['accept']
        metodo = params['metodo']
        archivoMaestro = maestro['archivo']
        hojaGeneral = maestro['hojaGeneral']
        hojaDominio = maestro['hojaDominio']
        hojaDomyApp = maestro['hojaDomyApp']

        parametros = { 'metodo': metodo,'tenantAmb': tenantAmb, 'queryParams': queryParams,'accept': accept,'tockenAmb': tockenAmb, 'archivoMaestro': archivoMaestro, 'hojaGeneral': hojaGeneral, 'hojaDominio': hojaDominio, 'hojaDomyApp': hojaDomyApp}
        logging.debug(f'Cargando parametros, parametros: {parametros}')

        return parametros

        
#parametros = cargarParametros.parametros()
#print(parametros["tenantAmb"])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RomarioSilvaG
"""