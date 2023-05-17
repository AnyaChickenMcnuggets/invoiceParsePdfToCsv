import csv
import os
from PyPDF2 import PdfReader

fieldnames = ['Компания', 'Владелец счета', 'Дата счета', 'Дата погашения', 'Номер счета', 'Сумма']
table = ['John Smith', 'Accounting', 'November']

files = os.listdir('input_data')

with open('result.csv', mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for file in files:
        reader = PdfReader(f'input_data/{file}')
        data = reader.pages[0].extract_text()
        dataArray = data.split("\n")
        pdfTable = {'Компания': dataArray[2], 'Владелец счета': dataArray[5],
                    'Дата счета': dataArray[6], 'Дата погашения': dataArray[7],
                    'Номер счета': dataArray[8], 'Сумма': dataArray[9][:-2]}
        writer.writerow(pdfTable)
print(pdfTable)
