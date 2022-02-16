import csv
import numpy as np

file=open("Size of TV,_Average time spent watching TV in a week (hours).csv")
data=csv.reader(file)
file_data=list(data)

file_data.pop(0)

sizeList=[]
timeSpentList=[]

for i in range(len(file_data)):
    size=file_data[i][0]
    time=file_data[i][1]

    sizeList.append(float(size))
    timeSpentList.append(float(time))
coeffiect=np.corrcoef(sizeList, timeSpentList)
print(coeffiect[0,1])    