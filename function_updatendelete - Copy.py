import mysql.connector
from tabulate import tabulate
import random
import time
#Manage Ticket Choice
def module_choice():
    while True:
        #print("="*141)
        print("TICKET MANAGEMENT".center(141))
        print('-'*141)
        print()
        print('''                                                        =  ========================= 
                                                        1. Update Ticket Info
                                                        2. Cancel Tickets
                                                        3. Main Menu
                                                        =  =========================
        ''')

        print()
        choice = int(input("Enter your Choice: "))
        if choice==1:
            update_ticket()
        elif choice==2:
            cancel_ticket()
        elif choice==3:
            print("Redirecting to Main Menu",end='')
            for i in range(3):
                print('.',end='')
                time.sleep(0.5)
            print("Done")
            break
        else:
            print("INVALID CHOICE")
#============Cancel Ticket============================
def cancel_ticket():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="A;sldkfj14321",
                                 database="railway_res_system")
    mycursor=mydb.cursor()
    print('='*141)
    print("TICKET CANCELLATION".center(141))
    print('-' *141)
    #PNR INPUT
    pnr_input=input("PNR Number: ")
    query2 = "select * from passenger_data where PNR="+pnr_input
    mycursor.execute(query2)
    ticket_info = mycursor.fetchall()
    print("Your Ticket:")
    print(tabulate(ticket_info, headers=['Ticket No', 'PNR', 'Name', 'Sex', 'Age', 'Seat No',
                                        'Ticket Date', 'Train No', 'Ticket Cost'], tablefmt='pretty'))
    choice = input('''Are you sure you want to cancel your ticket.
    This action cannot be undone (Y/N): ''')

    #query
    if choice in 'Yy':
        query = "delete from passenger_data where PNR=" + pnr_input
        mycursor.execute(query)
        mydb.commit()
        c=mycursor.rowcount
        if c>0:
            print("Cancelling Ticket", end='')
            for i in range(3):
                print('.', end='')
                time.sleep(1)
            print()
            print("Ticket has been cancelled succesfully")
        else:
            print("The PNR number you have entered is INVALID")
    else:
        pass

#Update Ticket Seat
def update_ticket_seat():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="A;sldkfj14321",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    #Seat Number
    seats = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
             'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'B01', 'B02',
             'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
             'B16',
             'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29',
             'B30', "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14",
             "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", 'D01', 'D02', 'D03', 'D04',
             'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
             'D19', 'D20', 'D21', 'D22', 'D23', 'D24']
    print()
    #train number display
    print("The available seats:")
    print("-----------------------")
    query = "select seat_no from passenger_data where train_no=" + str(train_no) +" and ticket_date="+"'"+str(passenger_date)+"'"
    mycursor.execute(query)
    seat_occu = []
    seat_data = mycursor.fetchall()
    for i in seat_data:
        for k in i:
            seat_occu.append(k)
            loop = 0
            for i in seats:
                if i not in seat_occu and i[0]==passenger_int_seat[0]:
                    loop+=1
                    if loop%6!=0:
                        print(i, end=' ')
                    else:
                        print(i)
                        print()
    print("\n-----------------------")

    print()
    while True:
        x = input("Enter the new seat number: ")
        yn = input("Are you sure the above mentioned information is correct? (Y/N): ")
        if yn in "yY":
            # the actual upd8ing lmao
            command = "update passenger_data set seat_no='" + x + "' where PNR=" + str(PNR)
            mycursor.execute(command)
            mydb.commit()
            print("Updating Seat", end='')
            for i in range(3):
                print('.', end='')
                time.sleep(1)
            print("Done")
            print()
            print("Seat number has been updated.")
            print()
            break
        elif yn in "nN":
            pass

#Update Ticket Date
def update_ticket_date():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="A;sldkfj14321",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    mycursor.execute("select * from train_data where train_no={}".format(train_no))
    train_day_data = mycursor.fetchall()
    train_day = train_day_data[0][4]
    day_list = {'Sunday': 'SUN', 'Monday': 'MON', 'Tuesday': 'TUE', 'Wednesday': 'WED', 'Thursday': 'THU',
                'Friday': 'FRI', 'Saturday': 'SAT'}

    # dates innit
    while True:
        print("The selected train is available on:", train_day)
        while True:
            passenger_date = input("Travel Date (YYYY-MM-DD): ")
            date_query = " select Dayname('" + passenger_date + "')"
            mycursor.execute(date_query)
            date_data = mycursor.fetchall()
            date_check = date_data[0][0]
            if day_list[date_check] in train_day:
                passenger_day = day_list[date_check]
                break
            else:
                print("TRAIN IS ONLY AVAILABLE ON THESE DAYS:", train_day)
                continue
            
        yn = input("Are you sure the above-mentioned information is correct? (Y/N): ")
        if yn in "yY":
            try:
                command = "update passenger_data set ticket_date='" + passenger_date + "' where PNR=" + str(PNR)
                mycursor.execute(command)
                mydb.commit()
                print("Updating Date.", end='')
                for i in range(3):
                    print('.', end='')
                    time.sleep(1)
                print()
                print("Seat number has been updated.")
                print()
                break
            except:
                print("INVALID DATE. Make Sure to Input Date in a Valid Format")

        elif yn in "nN":
            pass
        break

#Update Ticket Choice
def update_ticket():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="A;sldkfj14321",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    # fancy
    print('=' * 141)
    print("UPDATE TICKET".center(141))
    print('-' * 141)

    # user input


    global PNR
    while True:
        try:
            PNR = int(input("Enter the PNR number: "))
            mycursor.execute("select * from passenger_data where PNR={}".format(PNR))
            result = mycursor.fetchall()
            global train_no
            train_no = result[0][7]
            global passenger_date
            passenger_date = result[0][6]
            global passenger_int_seat
            passenger_int_seat = result[0][5]
            break
        except:
            print("Invalid PNR")
    print()
    print("TICKET INFO".center(141))
    print(tabulate(result, headers=['Ticket NO', 'PNR NO', 'Name', 'Sex', 'Age', 'Seat NO', 'Date of Travel', 'Train NO','Ticket Price'],
                 tablefmt='psql'))
    print()
    # decision submenu
    while True:
        print("Choose the option to update: ")
        print('''                                                        =  ========================= 
                                                        1. Update Seats
                                                        2. Update Date of Travel
                                                        3. Go Back
                                                        =  =========================
        ''')

        choice = int(input("Enter choice: "))
        if choice == 1:
            print()
            update_ticket_seat()
        elif choice == 2:
            print()
            update_ticket_date()
        elif choice == 3:
            print("Going back to menu...")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice.")
            break
