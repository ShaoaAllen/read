import xlrd
book = xlrd.open_workbook(r'C:\Users\86180\Desktop\test.xlsx')
sheet = book.sheet_by_index(0)
cols = sheet.ncols
rows = sheet.nrows
dic = {}
# 嵌套循环迭代每个单元格
for i in range(rows):
    for j in range(cols):
        cell_value = sheet.cell_value(i, j)
        # 因每个单元格中冒号包含半角和全角，所以用判断把半角全角冒号都存进元组
        if ':'in str(cell_value):
            cell_tuple = str(cell_value).partition(':')
            dic[cell_tuple[0]] = cell_tuple[2]
        elif '：'in str(cell_value):
            cell_tuple = str(cell_value).partition('：')
            dic[cell_tuple[0]] = cell_tuple[2]
# print(dic)
for key, value in dic.items():
    print('{}:{}'.format(key, value))




