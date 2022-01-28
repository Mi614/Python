import requests
import xml.etree.ElementTree as ET
from decimal import *

getcontext().prec = 3

def currency_rates(user_val):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = response.content.decode('cp1251')
    root = ET.fromstring(data)
    user_input = user_val.upper()
    val_name = ''
    val_curse = 0
    data = root.attrib.get('Date').replace('.', '-')

    for valute in root.findall('Valute'):
        if valute.find('CharCode').text == user_input:
            val_name = valute.find('Name').text
            val_curse = round(float(valute.find('Value').text.replace(',', '.')), 2)
            return val_name, val_curse, data
    return None


run = currency_rates(input())
print(run)
