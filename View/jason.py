import xlrd
from collections import OrderedDict
import json

wb = xlrd.open_workbook("dict1.xls")
sh = wb.sheet_by_index(0)

data_list = []


for rownum in range(1, sh.nrows):
     data = OrderedDict()
     row_values = sh.row_values(rownum)
     data['Name'] = row_values[0]
     data['Description'] = row_values[1]
     print(type(data))
     data_list.append(data)
print(data_list)
with open("h.json", "w", encoding="utf-8") as writeJsonfile:
      json.dump(data_list, writeJsonfile, indent=4,default=str)
