from lib.Models.connection import Conexion
import datetime

class Voluntario(Conexion):
    def __init__(self, rGeneral, rCia, nombre, apellidoP, apellidoM, crut, eMail, fIngreso, Sub_Estado):
        super().__init__()
        self.rGeneral = rGeneral
        self.rCia = rCia
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.eMail = eMail
        self.fIngreso = self.Filter_Date(fIngreso)
        self.Sub_Estado = Sub_Estado
        self.rut, self.dv = self.FilterRut(crut)

    @staticmethod
    def FilterRut(rut):
        try:
            rut = rut.split('-')
            dv = rut[1]
            rut = int(rut[0])
            return rut, dv
        except Exception as e:
            return 0, '0'

    def addVols(self):
        _values = (self.rGeneral, self.nombre, self.apellidoP, self.apellidoM, self.eMail, self.rut, self.dv, self.rCia, self.fIngreso, self.Sub_Estado)
        self.cursor.execute('INSERT INTO bomberos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', _values)
        self.connection.commit()

    def editVol(self):
        _values = (self.rGeneral, self.nombre, self.apellidoP, self.apellidoM, self.eMail, self.rut, self.dv, self.rCia, self.fIngreso, self.Sub_Estado, self.rGeneral)
        _query = 'UPDATE bomberos SET reg_gral = %s,nombre = %s, apellidoP = %s, apellidoM = %s, email = %s, rut = %s, dv = %s, reg_cia = %s, f_ingreso = %s, sub_estado = %s WHERE reg_gral = %s'
        self.cursor.execute(_query, _values)
        self.connection.commit()

    #TODO: Implementar el calculo e ingreso de las suspenciones