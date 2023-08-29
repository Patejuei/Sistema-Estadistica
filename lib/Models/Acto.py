import datetime
from lib.Models.connection import Conexion
class Acto(Conexion):
    def __init__(self, ccia, acto, cgral, date, address, list, cvol, vols, carros):
        super().__init__()
        self.company_cor = ccia
        self.act_type = acto
        self.general_cor = self.Filter_Int(cgral)
        self.date = self.Filter_Date(date)
        self.address = self.Filter_Address(address)
        self.list = list
        self.qty_vols = cvol
        self.vols = vols
        self.carros = self.list_to_string(carros)


    @staticmethod
    def list_to_string(lista):
        string = ""
        for i in range(len(lista)):
            if i > 0:
                string += ','
            string += lista[i]
        return string

    @staticmethod
    def Filter_Address(address):
        address = address.upper()
        address = address.replace("/", "ESQ.")

        return address

    @staticmethod
    def Filter_Int(num):
        if num == "":
            return 0
        else:
            return int(num)

    def get_Vols(self):
        lista = []
        for vol in self.vols:
            lista.append((self.company_cor, vol))
        return tuple(lista)

    #TODO(DONE): Implementar los métodos relacionados con los actos que se encuentran en Conexion
    def addLista(self):
        query = "INSERT INTO actos VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (self.company_cor, self.act_type, self.general_cor, self.date, self.address, self.list, self.qty_vols, self.carros))
        self.cursor.executemany("INSERT INTO asistencia (corr_cia_acto, reg_gral_voluntario) VALUES ( %s, %s)", self.get_Vols())
        self.connection.commit()
        self.connection.close()

    def editLista(self):
        act_data = (self.act_type, self.general_cor, self.date, self.address, self.list, self.qty_vols, self.carros, self.company_cor)
        self.cursor.execute(
            'UPDATE actos SET acto=%s, corr_gral=%s, fecha=%s , direccion=%s, lista=%s, c_vols=%s, unidad=%s WHERE corr_cia = %s', act_data)
        self.cursor.execute(f'DELETE FROM asistencia WHERE corr_cia_acto = "{act_data[-1]}"')
        self.cursor.executemany('INSERT INTO asistencia VALUES (default, %s, %s)', self.get_Vols())
        self.connection.commit()
        self.connection.close()
