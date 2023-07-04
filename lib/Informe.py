import os
import pdfkit
import pandas as pd

from lib.connection import Conexion

#TODO: Implementar los métodos de Conexión relacionados con la generación de informes

class Informe(Conexion):
    def __init__(self):
        super().__init__()
