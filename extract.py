from Sentiment import calEmotionalLevel
from Sentiment import tes
from openpyxl import load_workbook
wb=load_workbook("/home/ching/Downloads/bizdev.xlsx")

ws = wb.active
first_column = ws['E']
col = ws['L']
test = str(first_column[4].value)

word = "You received this message because"

for i in range(70,90):
    a = str(first_column[i].value)
    a = a[:a.find(word)]
    #print (a)
    #print ('\n')

    x = calEmotionalLevel(a)
    p = tes(a)
    column_cell = 'L'
    cell = 'M'

    ws[column_cell+str(i+1)] = x
    ws[cell+str(i+1)] = p

    print(str(i+1)+" " +str(x)) + " " + str(p)
    print ("\n")


wb.save("/home/ching/Downloads/bizdev.xlsx")

