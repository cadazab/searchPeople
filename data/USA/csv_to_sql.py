import csv
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="duls3data", # your password
                     db="Shitpeople") # name of the data base

cur = db.cursor() 
arr = {}
st = {}

def strClean(x):
	for i in range(0,len(x)):
		st[i]=x[i].replace('-0-','NULL').replace("'","")
		
with open('SDN.CSV','rb') as file:
	readfile = csv.reader(file, delimiter=',')
	for row in readfile:
		
		strClean(row)

		cur.execute("INSERT INTO Name(id_name,name,type,program,title,remarks) VALUES("+st[0]+",'"+st[1]+"','"+st[2]+"','"+st[3]+"','"+st[4]+"','"+st[5]+"');")
		print row
		
with open('ADD.CSV','rb') as file:
	readfile = csv.reader(file, delimiter=',')
	for row in readfile:
		
		strClean(row)

		cur.execute("INSERT INTO Address(id_address,id_name,address,city,country,add_remarks) VALUES("+st[1]+",'"+st[0]+"','"+st[2]+"','"+st[3]+"','"+st[4]+"','"+st[5]+"');")
		print row
	
with open('ALT.CSV','rb') as file:
	readfile = csv.reader(file, delimiter=',')
	for row in readfile:
		
		strClean(row)

		cur.execute("INSERT INTO Aka(id_aka,id_name,aka_type,aka_name,aka_remarks) VALUES("+st[1]+",'"+st[0]+"','"+st[2]+"','"+st[3]+"','"+st[4]+"');")
		print row
	
db.commit()