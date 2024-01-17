
import mysql.connector
import random
from tabulate import tabulate
import function_ticket_view
import time
#================================================SEARCH=================================================================
def search_train():
    #database
    my_db = mysql.connector.connect(host="localhost",user="root", passwd = 'A;sldkfj14321',
                                        database = "railway_res_system")
    my_cursor = my_db.cursor()

    #===========fancy============
    print("SEARCH AND BOOK".center(141))
    print('-'*141)

    #==================================dictionary=================================
    #the initial Stations
    Int_location_dic = {1:"HABIBGANJ", 2:"SECUNDERABAD", 3:"HOWRAH JUNCTION", 4:"PUNE JUNCTION", 5:"LOKMANYA TILAK TERMINUS",
                        6:"DEHRADUN", 7:"RANCHI JUNCTION", 8:"YESVANTPUR JUNCTION", 9:"LUCKNOW CHARBAGH NR", 10:"DARJEELING",
                        11:"THIRUVANANTHAPURAM CENTRAL", 12:"MUMBAI CENTRAL"}

    Int_location_list = [['NO','DEPARTURE STATION NAME'],[1,"HABIBGANJ"], [2,"SECUNDERABAD"], [3,"HOWRAH JUNCTION"], [4,"PUNE JUNCTION"],
                         [5,"LOKMANYA TILAK TERMINUS"], [6,"DEHRADUN"], [7,"RANCHI JUNCTION"], [8,"YESVANTPUR JUNCTION"],
                         [9,"LUCKNOW CHARBAGH NR"], [10,"DARJEELING"], [11, "THIRUVANANTHAPURAM CENTRAL"], [12, "MUMBAI CENTRAL"]]
    print()
    print("Available Stations:".center(6))
    print(tabulate(Int_location_list,headers="firstrow",tablefmt='grid'))
    Fin_location_dic = {}

    print()
    print( "NOTE: Enter the corresponding number to your station")

    #======================== initial location =======================
    int_input = int(input("From: "))
    initial_loc = Int_location_dic[int_input]
    my_cursor.execute("select train_no,train_name,int_loc,fin_loc from train_data where int_loc='{}'".format(initial_loc))
    initial_data = my_cursor.fetchall()
    print()

    #======================== final location display/ available trains =================
    print("Available Trains".center(141))
    print(tabulate(initial_data,headers=['Train No','Train Name','Initial Location','Final Location'],tablefmt='grid'))
    print()
    while True:
        proceed = input("Do you wish to proceed? (Y/N): ")
        if proceed in "Yy":
            print()
            print("Choose a train to learn more")
            train_choice = int(input("Enter Train No: "))
            break
        elif proceed in "Nn":
            print("Redirecting to Main Menu", end='')
            for i in range(3):
                print('.',end='')
                time.sleep(0.5)
            print("Done")
            return None
        else:
            print("Invalid Choice!")


    #============================train choice=======================
    my_cursor.execute("select * from train_data where train_no='{}'".format(train_choice))
    final_data = my_cursor.fetchall()
    train_info_data = []
    train_info_data.append(final_data[0][0:7])
    # final train display
    print()
    print("TRAIN INFO".center(141))
    print()
    print(tabulate(train_info_data, headers=['Train No', 'Train Name', 'Initial Location', 'Final Location', 'Running Days',
                                        'Departure Time', 'Arrival Time',  'Duration (hrs)'], tablefmt='pretty'))

    #=============booking call===============
    print("Do you want to continue booking process?")
    while True:
        booking_choice = input("Respond with Y/N: ")
        if booking_choice in 'Yy':
            book_train(train_choice)
            break
        elif booking_choice in 'Nn':
            print("Bookings halted")
            print("Redirecting to Main Menu",end='')
            for i in range(3):
                print('.',end='')
                time.sleep(0.5)
                print("Done")

#========================================================BOOKING================================================================
def book_train(train_no):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd='A;sldkfj14321',
                                    database="railway_res_system")
    my_cursor = my_db.cursor()
    # passenger

    my_cursor.execute("select * from train_data where train_no={}".format(train_no))
    train_day_data = my_cursor.fetchall()
    train_day = train_day_data[0][4]
    train_cost = train_day_data[0][7]
    day_list = {'Sunday': 'SUN', 'Monday': 'MON', 'Tuesday': 'TUE', 'Wednesday': 'WED', 'Thursday': 'THU',
                'Friday': 'FRI', 'Saturday': 'SAT'}



    # ===================input====================
    print()
    print('-' * 141)
    print()
    print('BOOKING'.center(141))
    print()
    print("Ticket Price: ")
    #==========================Class======================
    class_info_data = []
    class_info_data.append(train_day_data[0][8:])
    class_list = [['1', 'First Class AC', float(class_info_data[0][1])], ['2','Second Class AC',float(class_info_data[0][0])],
                  ['3','General Seat',class_info_data[0][2]], ['4','Sleeper Class',class_info_data[0][3]]]
    print(tabulate(class_list,headers=['NO','Class','Price (Rs)'],tablefmt='pretty'))

    while True:
        class_choice = int(input("Enter Class Choice: "))
        if class_choice==2:
            class_type = 'Second Class AC'
            class_string_one = 'B'
            cost = class_info_data[0][0]
            break
        elif class_choice==1:
            class_type = 'First Class AC'
            class_string_one = 'A'
            cost = class_info_data[0][1]
            break
        elif class_choice==3:
            class_type = 'General Seat'
            class_string_one = 'D'
            cost = class_info_data[0][2]
            break
        elif class_choice==4:
            class_type = 'Sleeper Class'
            class_string_one = 'C'
            cost = class_info_data[0][3]
            break
        else:
            print("Invalid Choice")
    print()
    total_tickets = int(input("How many tickets would you like to book?: "))
    print("Total Cost is Rs.", cost * total_tickets)
    booking_confirm = input("Would you like to proceed? (Y/N): ")
    if booking_confirm in "Yy":
        for i in range(total_tickets):
            while True:
                print()
                print('Please fill in the following:-')
                passenger_name = input("Name: ")
                passenger_sex = input("Sex: ").upper()
                passenger_age = int(input("Age: "))
                print()
                if passenger_age >= 60 or passenger_age <= 10:
                    print("You are eligible for a 10% discount!")
                    train_cost -= train_cost * 10 / 100
                print()
                print("The selected train is available on:", train_day)
                while True:
                    passenger_date = input("Travel Date (YYYY-MM-DD): ")
                    date_query = " select Dayname('" + passenger_date + "')"
                    my_cursor.execute(date_query)
                    date_data = my_cursor.fetchall()
                    date_check = date_data[0][0]
                    if day_list[date_check] in train_day:
                        passenger_day = day_list[date_check]
                        break
                    else:
                        print("TRAIN IS ONLY AVAILABLE ON THESE DAYS:", train_day)
                        continue

                    # ====================================== seat ===========================
                    #seat numbers
                seats = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
                         'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'B01', 'B02',
                         'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
                         'B16',
                         'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29',
                         'B30', "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14",
                         "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", 'D01', 'D02', 'D03', 'D04',
                         'D05', 'D06', 'D07', 'D08', 'D09', 'D10',  'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
                         'D19', 'D20', 'D21', 'D22', 'D23', 'D24']
                print()
                print("The available seats:")
                print("-----------------------")
                query = "select seat_no from passenger_data where train_no=" + str(
                    train_no) + " and ticket_date=" + "'" + passenger_date + "'"
                my_cursor.execute(query)
                seat_occu = []
                seat_data = my_cursor.fetchall()
                for i in seat_data:
                    for k in i:
                        seat_occu.append(k)
                loop = 0
                for i in seats:
                    if i not in seat_occu and i[0]==class_string_one:
                        loop += 1
                        if loop % 6 != 0:
                            print(i, end=' ')
                        else:
                            print(i)
                            print()

                print("\n-----------------------")
                print()
                passenger_seat = input("Enter the seat number: ")
                print()
                data2 = [[passenger_name, passenger_sex, passenger_age, passenger_date, str(train_no), passenger_seat]]
                print("Confirm below information:")
                print(tabulate(data2, headers=['Name', 'Sex', 'Age', 'Date of Travel', 'Train NO', 'Seat No'],
                               tablefmt='psql'))
                print()
                print("NOTE: Enter C to cancel booking process")
                data_confirm = input('''By entering Y you confirm that the above information is correct 
and that no further changes will be entertained. You also agree to the terms and conditions.(Y/N/C): ''')
                if data_confirm in 'Yy':
                    break
                elif data_confirm in 'Nn':
                    continue
                elif data_confirm in 'Cc':
                    print("Bookings Halted")
                    print("Redirecting to Main Menu", end='')
                    for i in range(3):
                        print('.', end='')
                        time.sleep(0.5)
                    print("Done")
                    return None
            print()
            print("Booking", end='')
            for i in range(3):
                print('.', end='')
                time.sleep(1)

            my_cursor.execute("select max(ticket_no) from passenger_data")
            pdata = my_cursor.fetchall()
            ptup = pdata[0]
            ticket_no = ptup[0]

            passenger_ticket = ticket_no + 1

            # ==========================PNR=======================================
            query = "select PNR from passenger_data where train_no=" + str(train_no)
            my_cursor.execute(query)
            PNR_occu = []
            PNR_data = my_cursor.fetchall()
            for i in PNR_data:
                for k in i:
                    PNR_occu.append(k)
            while True:
                rand_value1 = random.randrange(1000000000, 9999999999)  # 10 digits
                if str(rand_value1) not in PNR_occu:
                    passenger_pnr = rand_value1
                    break
                else:
                    continue

            data = (passenger_ticket, passenger_pnr, passenger_name, passenger_sex, passenger_age, passenger_seat,
                    passenger_date, train_no, cost)

            # =============================SQL=============================
            command = "Insert into passenger_data(ticket_no,PNR,passenger_name,sex,age,seat_no,ticket_date,train_no,ticket_cost) values(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s)"
            my_cursor.execute(command, data)
            my_db.commit()
            my_cursor.execute("select * from passenger_data where PNR={}".format(passenger_pnr))
            presult = my_cursor.fetchall()
            my_cursor.execute("select * from train_data where train_no={}".format(train_no))
            tresult = my_cursor.fetchall()
            print("Done")
            function_ticket_view.print_ticket(presult, tresult)

    menu_input = input("Press any key to go back to MAIN MENU: ")
    if menu_input != '':
        print("Redirecting to Main Menu", end='')
        for i in range(3):
            print('.', end='')
            time.sleep(0.5)
        print("Done")
