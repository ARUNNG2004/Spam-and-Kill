import csv
import sys
a=0
csv.field_size_limit(sys.maxsize)
lista=[]
while a<=20000:
	with open ('loops.csv','r') as F:
		reader=csv.reader(F)
		for row in reader:
			lista.append(row)
	F.close()
	with open ('loops.csv','a') as F:
		writer=csv.writer(F)
		writer.writerow(lista)
	F.close()
	a+=1
