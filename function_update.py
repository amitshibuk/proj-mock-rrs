import mysql.connector
from tabulate import tabulate
import time

#moyush UwU
def update_ticket_seat():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="UltaPult1298",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    # seats innit
    seats = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
             'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'B01', 'B02',
             'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
             'B16',
             'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29',
             'B30', "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14",
             "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", 'D01', 'D02', 'D03', 'D04',
             'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
             'D19', 'D20', 'D21', 'D22', 'D23', 'D24']
    print("The available seats: ")
    query = "select seat_no from passenger_data where train_no="+str(train_no)
    mycursor.execute(query)
    seat_occu=[]
    seat_data = mycursor.fetchall()
    for i in seat_data:
        for k in i:
            seat_occu.append(k)

    for i in seats:
        if i in seat_occu:
            continue
        elif i not in seat_occu:
            print(i, end=' ')
    print()
    while True:
        x = input("Enter the new seat number: ")
        print("Are you sure the above-mentioned information is correct?")
        yn = input("Y/N: ")
        if yn in "yY":
            # the actual upd8ing lmao
            command = "update passenger_data set seat_no='" + x + "' where PNR=" + str(PNR)
            mycursor.execute(command)
            mydb.commit()
            print("Updating Seat", end='')
            for i in range(3):
                print('.', end='')
                time.sleep(1)
            print()
            print("Seat number has been updated.")
            break
        elif yn in "nN":
            pass

#moyush UwU
def update_ticket_date():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="UltaPult1298",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    mycursor.execute("select * from train_data where train_no={}".format(train_no))
    train_day_data = mycursor.fetchall()
    train_day = train_day_data[0][4]
    day_list = {1:'SUN', 2:'MON', 3:'TUE', 4:'WED', 5:'THU', 6:'FRI', 7:'SAT'}

    #dates innit
    print()
    
    while True:
        while True:
            passenger_date = input("Enter new date of travel (YYYY-MM-DD): ")
            print("1:SUNDAY, 2:MONDAY, 3:TUESDAY, 4:WEDNESDAY, 5:THURSDAY, 6:FRIDAY, 7:SATURDAY")
            passenger_day_input = int(input("Day (Enter corresponding NO): "))
            if day_list[passenger_day_input] in train_day:
                passenger_day = day_list[passenger_day_input]
                break
            else:
                print("TRAIN IS ONLY AVAILABE ON THESE DAYS:",train_day)
                continue
        print("Are you sure the abovementioned information is correct?")
        yn = input("Y/N: ")
        if yn in "yY":
            command = "update passenger_data set ticket_date='" + passenger_date + "' where PNR=" + str(PNR)
            mycursor.execute(command)
            mydb.commit()
            print("Updating date of travel", end='')
            print()
            print("Date of travel has been updated.")
            break
        elif yn in "nN":
            pass
        break

#moyush UwU
def update_ticket():
    # database
    mydb = mysql.connector.connect(host="localhost", user="root", password="UltaPult1298",
                                   database="railway_res_system")
    mycursor = mydb.cursor()

    # fancy
    print('*' * 80)
    print(' ' * 30, "UPDATE TICKET")
    print('*' * 80)

    # user input
    global PNR
    PNR = int(input("Enter the PNR number: "))
    mycursor.execute("select * from passenger_data where PNR={}".format(PNR))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ticket NO', 'PNR NO', 'Name', 'Sex', 'Age', 'Seat NO', 'Date of Travel', 'Train NO'],
                 tablefmt='psql'))
    global train_no
    train_no = result[0][7]
    # decision submenu
    while True:
        print("Choose the option to update: ")
        choice_list = [['1.', 'Update Seats'], ['2.', 'Update Date of Travel'], ['3.', 'Main Menu']]
        print(tabulate(choice_list, tablefmt='rst'))
        choice = int(input("Enter choice: "))
        if choice == 1:
            update_ticket_seat()
        elif choice == 2:
            update_ticket_date()
        elif choice == 3:
            print("Going back to main menu...")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice.")
            break

update_ticket()
