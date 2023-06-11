import datetime
class Acto:
    def __init__(self, ccia, acto, cgral, date, address, list, cvol, vols):
        self.company_cor = ccia
        self.act_type = acto
        self.general_cor = self.Filter_Int(cgral)
        self.date = self.Filter_Date(date)
        self.address = self.Filter_Adrress(address)
        self.list = list
        self.qty_vols = cvol
        self.vols = vols

    def get_data(self):
        return (self.company_cor, self.act_type, self.general_cor, self.date, self.address, self.list, self.qty_vols)

    def Filter_Adrress(self, address):
        address = address.upper()
        address.replace("ESQ", "/")

        return address

    def Filter_Date(self, date):
        day, month, year = date.split("-")
        date = datetime.date(int(year), int(month), int(day))
        return date

    def Filter_Int(self, num):
        if num == "":
            return 0
        else:
            return int(num)

    def get_Vols(self):
        lista = []
        for vol in self.vols:
            lista.append((self.company_cor, vol))
        return tuple(lista)