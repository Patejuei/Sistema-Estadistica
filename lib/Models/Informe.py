from lib.Models.connection import Conexion
from PySide6.QtWidgets import QFileDialog, QWidget
import pandas as pd


# TODO: Implementar los métodos de Conexión relacionados con la generación de informes

class Informe(Conexion):
    def __init__(self, Widget, DateStart=None, DateEnd=None, month=None, year=None):
        super().__init__()
        meses = {
            "Enero": "January",
            "Febrero": "February",
            "Marzo": "March",
            "Abril": "April",
            "Mayo": "May",
            "Junio": "June",
            "Julio": "July",
            "Agosto": "August",
            "Septiembre": "September",
            "Octubre": "October",
            "Noviembre": "November",
            "Diciembre": "December"
        }
        file_filter = 'Todos los Archivos;; Archivo Excel (*.xlsx *.xls);; Archivo PDF (*.pdf)'
        self.saveDirectory, self.saveFilter = QFileDialog.getSaveFileName(
            parent=Widget,
            caption='Guardar el Reporte',
            filter=file_filter,
            selectedFilter='Archivo Excel (*.xlsx *.xls)'
        )
        self.dateStart = self.Filter_Date(DateStart)
        self.dateEnd = self.Filter_Date(DateEnd)
        self.month = meses[month] if month is not None else self.month = None
        self.year = year

    def resMensual(self, month, year):
        _DateDefiner = (self.month, self.year)
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        for row in lista:
            _ExtractCondition = (self.month, self.year, row[0])
            self.cursor.execute(
                'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s and reg_gral_voluntario = %s',
                _ExtractCondition
            ) # Extracción de cantidad de listas que tiene el Voluntario
            lista[lista.index(row)].append(self.cursor.fetchone()[0]) # Ingreso de listas a la Lista generada
            self.cursor.execute(
                'SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND NOT (acto in ("C. ADM.","J. OFF", "CONS. DISC"))',
                _DateDefiner
            ) # Extracción de total de listas
            lista[lista.index(row)].append(row[4] / self.cursor.fetchone()[0]) # Obtención de porcentaje
            self.cursor.execute(
                'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s and reg_gral_voluntario = %s AND a.lista = "OB"',
                _ExtractCondition
            ) # Extracción de Listas Obligatorias
            lista[lista.index(row)].append(self.cursor.fetchone()[0]) # Ingreso de listas obligatorias
            self.cursor.execute(
                'SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND lista = "OB"',
                _DateDefiner
            ) # Extracción de total de listas obligatorias
            lista[lista.index(row)].append(row[6] / self.cursor.fetchone()[0]) # Cálculo de porcentaje de Listas Obligatorias

        self.cursor.execute('SELECT * FROM actos WHERE MONTH(fecha) = %s ORDER BY fecha DESC, corr_cia DESC',
                            _DateDefiner
        )
        actos = self.cursor.fetchall()

        # Define the queries and their labels in a dictionary
        queries = {
            'Incendios Estructurales': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto = 'INCENDIO'",
            'Incendios Forestales': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto = 'I. FOREST.'",
            'Llamados de Comandancia': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9'",
            'Claves 10-0': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto LIKE '10-0-%'",
            'Rescates': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto LIKE '10-4-%'",
            'Salvamentos': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto LIKE '10-3-%' AND NOT acto = '10-3-9'",
            'Materiales Peligrosos (10-5, 10-6)': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto LIKE '10-5-%' OR acto LIKE '10-6-%')",
            'Apoyos a Otros Cuerpos (10-12, 0-11)': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto = '10-12'",
            'Otros Servicios': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto LIKE '10-9-%' OR acto = '10-3-9')",
            'Sesiones': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto = 'SS.OO.' OR acto = 'SS.EE')",
            'Academias': "SELECT count(corr_cia) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto = 'ACADEMIA'",
            'Promedio Asistencia Despachos': "SELECT avg(c_vols) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto LIKE '10-%' OR acto = 'INCENDIO' or acto = 'I. FOREST.')",
            'Promedio Asistencia Academias': "SELECT avg(c_vols) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND acto = 'ACADEMIA'",
            'Promedio Asistencia Sesiones': "SELECT avg(c_vols) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto = 'SS.OO.' OR acto = 'SS.EE')",
            'Promedio Asistencia Citaciones CBPA': "SELECT avg(c_vols) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND (acto = 'DESFILE CB' OR acto = 'ROMERIA CB' or acto = 'SS. EE. CB')",
            'Promedio Asistencia General': "SELECT avg(c_vols) FROM actos WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s AND NOT (acto in ('C. ADM.','J. OFF', 'CONS. DISC'))",
        }

        # Create a dictionary to store the results
        _Statistics = {}

        # Execute the queries and update the _Statistics dictionary
        for label, query in queries.items():
            self.cursor.execute(query, _DateDefiner)
            _Statistics[label] = self.cursor.fetchone()[0]



    def resEspecifico(self):
        lista = []
        _DateDifference = (self.dateStart, self.dateEnd)
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        for row in lista:
            _ExtractCondition = (self.dateStart, self.dateEnd, row[0])
            self.cursor.execute(
                'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE fecha BETWEEN %s AND %s and reg_gral_voluntario = %s',
                _ExtractCondition
            ) # Extracción de cantidad de listas que tiene el Voluntario
            lista[lista.index(row)].append(self.cursor.fetchone()[0]) # Ingreso de listas a la Lista generada
            self.cursor.execute(
                'SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND NOT (acto in ("C. ADM.","J. OFF", "CONS. DISC"))',
                _DateDifference
            ) # Extracción de total de listas
            lista[lista.index(row)].append(row[4] / self.cursor.fetchone()[0]) # Obtención de porcentaje
            self.cursor.execute(
                'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE fecha BETWEEN %s AND %s and reg_gral_voluntario = %s AND a.lista = "OB"',
                _ExtractCondition
            ) # Extracción de Listas Obligatorias
            lista[lista.index(row)].append(self.cursor.fetchone()[0]) # Ingreso de listas obligatorias
            self.cursor.execute(
                'SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND lista = "OB"',
                _DateDifference
            ) # Extracción de total de listas obligatorias
            lista[lista.index(row)].append(row[6] / self.cursor.fetchone()[0]) # Cálculo de porcentaje de Listas Obligatorias

        self.cursor.execute('SELECT * FROM actos WHERE fecha BETWEEN %s AND %s ORDER BY fecha DESC, corr_cia DESC',
                            _DateDifference
        )
        actos = self.cursor.fetchall()

        # Define the queries and their labels in a dictionary
        queries = {
            'Incendios Estructurales': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto = 'INCENDIO'",
            'Incendios Forestales': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto = 'I. FOREST.'",
            'Llamados de Comandancia': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9'",
            'Claves 10-0': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto LIKE '10-0-%'",
            'Rescates': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto LIKE '10-4-%'",
            'Salvamentos': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto LIKE '10-3-%' AND NOT acto = '10-3-9'",
            'Materiales Peligrosos (10-5, 10-6)': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto LIKE '10-5-%' OR acto LIKE '10-6-%')",
            'Apoyos a Otros Cuerpos (10-12, 0-11)': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto = '10-12'",
            'Otros Servicios': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto LIKE '10-9-%' OR acto = '10-3-9')",
            'Sesiones': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto = 'SS.OO.' OR acto = 'SS.EE')",
            'Academias': "SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN %s AND %s AND acto = 'ACADEMIA'",
            'Promedio Asistencia Despachos': "SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto LIKE '10-%' OR acto = 'INCENDIO' or acto = 'I. FOREST.')",
            'Promedio Asistencia Academias': "SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN %s AND %s AND acto = 'ACADEMIA'",
            'Promedio Asistencia Sesiones': "SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto = 'SS.OO.' OR acto = 'SS.EE')",
            'Promedio Asistencia Citaciones CBPA': "SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN %s AND %s AND (acto = 'DESFILE CB' OR acto = 'ROMERIA CB' or acto = 'SS. EE. CB')",
            'Promedio Asistencia General': "SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN %s AND %s AND NOT (acto in ('C. ADM.','J. OFF', 'CONS. DISC'))",
        }

        # Create a dictionary to store the results
        _Statistics = {}

        # Execute the queries and update the _Statistics dictionary
        for label, query in queries.items():
            self.cursor.execute(query, _DateDifference)
            _Statistics[label] = self.cursor.fetchone()[0]


    def info90(self):
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        self.cursor.execute('SELECT reg_gral_voluntario ,count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE a.fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY) GROUP BY reg_gral_voluntario')
        for row in self.cursor.fetchall():
            for i in lista:
                if i[0] == row[0]:
                    lista.remove(i)
                    break
        self.cursor.execute(f'SELECT * FROM actos WHERE fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY)')
        actos = self.cursor.fetchall()
        return lista, actos



