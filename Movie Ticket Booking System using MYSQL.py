# IMPORTING HEADER fILES
import mysql.connector as sc
import numpy as np


# DEFINITION OF Login() function
def Login():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	print("**********************")
	user = input("Enter USER ID:")
	pas = input("Enter PASSWORD:")
	if user == "Admin" and pas == "mgm":
		print("SUCCESSFULLY LOGGED !!!!")
		Homepage()
	else:
		print("INCORRECT CREDENTIALS")
		Login()


# DEFINITION OF Homepage() function
def Homepage():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	print("**********************")
	print("1. Registration Session")
	print("2. Ticket Booking")
	print("3. SEARCH")
	print("4. REPORT")
	op = int(input("Enter Your option:"))
	if op == 1:
		Registration()
	elif op == 2:
		TicketBooking()
	elif op == 3:
		Search()
	elif op == 4:
		Report()
	else:
		print("INVALID OPTION")


##DEfinition for Registration()
def Registration():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	print("1. ADD THEATER DETAILS")
	print("2. UPDATE THEATER DETAILS")
	print("3. REMOVE DETAILS OF THEATER")
	print("4. SEARCH")
	print("5. GO HOME")
	op = int(input("Enter your option"))
	if op == 1:
		AddTheater()
	elif op == 2:
		UpdateTheater()
	elif op == 3:
		RemoveTheater()
	elif op == 4:
		Search()
	elif op == 5:
		Homepage()
	else:
		print("Invalid option")


# Defintition for AddTheater() function
def AddTheater():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	Tid = int(input("Enter Theater Id:"))
	Tname = input("Enter name of the Theater:")
	Tfilim = input("Enter film name:")
	Tnofront = int(input("Enter number of Seats in front row:"))
	Tnomiddle = int(input("Enter number of Seats in middle row:"))
	Tnoback = int(input("Enter number of Seats in back row:"))
	Tnobalcony = int(input("Enter number of Seats in balcony:"))
	Tpricefront = int(input("Enter price of Seat in front row:"))
	Tpricemiddle = int(input("Enter price of Seat in middle row:"))
	Tpriceback = int(input("Enter price of Seat in back row:"))
	Tpricebalcony = int(input("Enter price of Seat in balcony:"))
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "insert into Theater values({},'{}','{}',{},{},{},{},{},{},{},{})".format(Tid, Tname, Tfilim, Tnofront,
	                                                                                  Tnomiddle, Tnoback, Tnobalcony,
	                                                                                  Tpricefront, Tpricemiddle,
	                                                                                  Tpriceback, Tpricebalcony)
	mycursor.execute(query)
	conn.commit()
	conn.close()
	print("SUCCESSFULLY ADD THEATER DEATILS")


# Defintition for UpdateTheater() function
def UpdateTheater():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	Tid = int(input("Enter Theater Id for updation:"))
	ufilim = input("Enter film name:")
	unofront = int(input("Enter number of Seats in front row:"))
	unomiddle = int(input("Enter number of Seats in middle row:"))
	unoback = int(input("Enter number of Seats in back row:"))
	unobalcony = int(input("Enter number of Seats in balcony:"))
	upricefront = int(input("Enter price of Seat in front row:"))
	upricemiddle = int(input("Enter price of Seat in middle row:"))
	upriceback = int(input("Enter price of Seat in back row:"))
	upricebalcony = int(input("Enter price of Seat in balcony:"))
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "update Theater set Tfilim='{}',Tfrontno={},Tmiddleno={},Tbackno={},Tbalconyno={},Tpricefront={},Tpricemiddle={},Tpriceback={},Tpricebalcony={} where Tid={}".format(
		ufilim, unofront, unomiddle, unoback, unobalcony, upricefront, upricemiddle, upriceback, upricebalcony, Tid)
	mycursor.execute(query)
	conn.commit()
	conn.close()
	print("SUCCESSFULLY UPDATE  THEATER DEATILS")


# DEfinition for RemoveTheater() function
def RemoveTheater():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	Tid = int(input("Enter Id of Theater we are removing :"))
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "delete from Theater where Tid={}".format(Tid)
	mycursor.execute(query)
	conn.commit()
	conn.close()
	print("SUCCESSFULLY REMOVE   THEATER DEATILS")


# DEfinition for Search() function
def Search():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	Tid = int(input("Enter Id of Theater we are searching :"))
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "select *  from Theater where Tid={}".format(Tid)
	mycursor.execute(query)
	myrecord = mycursor.fetchall()
	for x in myrecord:
		print(x)
	conn.close()


# DEfinition for  TicketBooking() section
def TicketBooking():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	print("1. Ticket Booking")
	print("2. Ticket Cancellation")
	print("3. Search Booking details")
	print("4. Go Home page")
	op = int(input("Enter your option"))
	if op == 1:
		Tbooking()
	elif op == 2:
		Tcancel()
	elif op == 3:
		SearchBooking()
	elif op == 4:
		Homepage()
	else:
		print("Invalid option")


# DEfinition for  TBooking() function
def Tbooking():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "select *  from Theater "
	mycursor.execute(query)
	myrecord = mycursor.fetchall()
	print("DEtails of Theaters ")
	for x in myrecord:
		print(x)
	conn.close()
	bid = int(input("Enter Booking id"))
	tid = int(input("Enter Theater id:"))
	typeticket = input("Enter type of ticket(Front/Middle/Back/Balcony)")
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query = "select *  from Theater where Tid={}".format(tid)
	mycursor.execute(query)
	myrecord = mycursor.fetchall()
	conn.close()
	fare = 0
	for x in myrecord:
		if typeticket == "Front":
			fare = x[7]
		elif typeticket == "Middle":
			fare = x[8]
		elif typeticket == "Back":
			fare = x[9]
		elif typeticket == "Balcony":
			fare = x[10]
	query1 = "insert into ticketbooking values({},{},'{}',{})".format(bid, tid, typeticket, fare)
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	mycursor.execute(query1)
	conn.commit()
	print("Successfully Booking done")
	conn.close()


# Definition for the function Tcancel()
def Tcancel():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	bidcan = int(input("Enter id of the ticket  to be cancelling:"))
	query1 = "select * from ticketbooking where bid={}".format(bidcan)
	mycursor.execute(query1)
	myrecord = mycursor.fetchall()
	typeticket = ""
	for x in myrecord:
		typeticket = x[2]
		tidcan = x[1]
		print(typeticket)
	query3 = "delete from ticketbooking where bid={}".format(bidcan)
	mycursor.execute(query3)
	query2 = ""
	if typeticket == "front":
		query2 = "update theater set Tfrontno=Tfrontno+1 where  tid={}".format(tidcan)
	elif typeticket == "middle":
		query2 = "update theater set Tmiddleno=Tmiddleno+1 where  tid={}".format(tidcan)
	elif typeticket == "back":
		query2 = "update theater set Tbackno=Tbackno+1 where  tid={}".format(tidcan)
	elif typeticket == "balcony":
		query2 = "update theater set Tbalconyno=Tbalconyno+1 where  tid={}".format(tidcan)
	mycursor.execute(query2)
	print("SUCCESSFULLY DONE THE CANCELLATION OF TICKET")
	conn.close()


# Definition for Search() function
def SearchBooking():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	bidcan = int(input("Enter id of the ticket booking to be searching: "))
	query1 = "select * from ticketbooking where bid={}".format(bidcan)
	mycursor.execute(query1)
	myrecord = mycursor.fetchall()
	print("Bookingid\tTheaterId\tTypeofseat\tprice\n")
	for x in myrecord:
		print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\n")
	conn.close()


# Definition for the function Report()
def Report():
	print("\n\n\n\n")
	print("*********************")
	print("WELCOME TO BOOK MY SHOW")
	print("1. Report Based on Types of seats")
	print("2. Report Based on Ticket price")
	print("3.GO HOME ")
	op = int(input("Enter your option:"))
	if op == 1:        conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
	mycursor = conn.cursor()
	query1 = "select typeofseat,count(*) from ticketbooking group by typeofseat"
	mycursor.execute(query1)
	myrecord = mycursor.fetchall()
	typeseat = []
	noseat = []
	conn.close()

elif op == 2: conn = sc.connect(host="localhost", user="root", password="mgm", database="ip12")
mycursor = conn.cursor()
query1 = "select typeofseat,sum(price) from ticketbooking group by typeofseat"
mycursor.execute(query1)
myrecord = mycursor.fetchall()
typeseat = []
noseat = []

conn.close()
## CALLING MAIN SECTION
Login()
