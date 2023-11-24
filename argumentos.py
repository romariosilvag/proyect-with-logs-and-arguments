import argparse

class CargarArgumentos:

    def cargarSeveridadLogs():
        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser(description='Niveles de severidad para libreria logging')
        parser.add_argument('-l', '--log', type=str, default="WARNING", choices=["DEBUG", "INFO", "WARNING", "ERROR","CRITICAL"], help='Nivel de severidad para libreria logging')
        args = parser.parse_args()
        return args.log   
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RomarioSilvaG
"""