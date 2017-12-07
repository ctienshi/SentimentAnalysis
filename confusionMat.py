from __future__ import division
from pandas_ml import ConfusionMatrix
import matplotlib.pyplot as plt
from openpyxl import load_workbook

wb=load_workbook("/home/ching/WORK/SentimentAnalysis/testData/dataset.xlsx")
ws = wb.active
actual = ws['A']
pred = ws['B']
act_arr = []
pred_arr = []

for i in range(len(actual)):
    act_arr.append(actual[i].value)
    pred_arr.append(pred[i].value)

confusion_matrix = ConfusionMatrix(act_arr, pred_arr)

print("Confusion matrix:\n%s" % confusion_matrix)
confusion_matrix.plot()
plt.show()

def perf_measure(y_actual, y_hat):
    cor = 0
    wro = 0

    for i in range(len(y_hat)):
        if y_actual[i]==y_hat[i]:
            cor += 1
        else:
            wro += 1
    a = cor/(cor+wro)
    return(a)

print ("\n")
a = perf_measure(act_arr,pred_arr)
print("The Accuracy is: "+str(a*100)+"%")