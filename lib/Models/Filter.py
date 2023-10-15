import datetime as dt

def Filter_Date(date) -> dt.date:
    if type(date) is not dt.date:
        day, month, year = date.split("-")
        date = dt.date(int(year), int(month), int(day))
        return date
    else:
        return date
    
def list_to_string(lista) -> str:
    if type(lista) is list:
        return ','.join(lista)
    else:
        return lista

def Filter_Address(address):
    address = address.upper()
    address = address.replace("/", "ESQ.")
    return address

def Filter_Int(num : str) -> int:
    try:
        return int(num)
    except:
        return 0