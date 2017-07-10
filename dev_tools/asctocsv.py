#copy this to the folder where the asc file is
#edit the name of the input asc file and output csv file
#open terminal in the folder and run this with python2.7
import csv
with open('input.asc') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	with open('output.csv','wb') as csvout:
		writefile=csv.writer(csvout,delimiter=";",lineterminator='\n')
		for row in readfile:
			writefile.writerow(row)
