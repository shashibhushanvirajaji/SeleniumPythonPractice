import xlrd

workbook = xlrd.open_workbook('C:\\Users\\svirajaj\\PycharmProjects\\nopCommerceApp\\testdata\\testdata.xlsx')
sheet = workbook.sheet_by_name('login')
print(sheet.cell_value(1, 0) )
