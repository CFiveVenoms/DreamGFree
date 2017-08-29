import xlwt
import xlrd
from xlutils.copy import copy

#首先打开表格
rb = xlrd.open_workbook('D:\\PycharmProjects\\etonhui_\\xls\\userLogin.xlsx')
wb = copy(rb)

s = wb.get_sheet(0)
s.write(3,4,'changed!')
wb.save("D:\\PycharmProjects\\etonhui_\\xls\\userLogin.xlsx")
