import mysql.connector
from tabulate import tabulate
import function_ticket_view
import time
def ticket_info( ):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="A;sldkfj14321",
                             database="railway_res_system")
    mycursor=mydb.cursor()
    print()
    print("\t\t\t\t\t\t\tTicket Information")
    print()
    while True:
        try:
            PNR = int(input("Enter the PNR number: "))
            mycursor.execute("select * from passenger_data where PNR={}".format(PNR))
            presult = mycursor.fetchall()
            global train_no
            train_no = presult[0][7]
            break
        except:
            print("Invalid PNR")
    mycursor.execute("select * from train_data where train_no={}".format(train_no))
    tresult = mycursor.fetchall()
    print("Collecting Info.", end='')
    for i in range(3):
        print('.', end='')
        time.sleep(0.25)
    print("Info Collected")
    print("Generating Ticket.", end='')
    for i in range(3):
        print('.', end='')
        time.sleep(0.5)
    print("Ticket Generated. Look for Pop-Up Window")
    function_ticket_view.print_ticket(presult, tresult)
    '''print()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTrain Info")
    print(tabulate(result, headers=['Train NO', 'Train Name', 'Initial Location', 'Final Location', 'Departure Time', 'Estimated Arrival Time'],
                 tablefmt="fancy_grid"))'''
    exitchoice = input("Input any letter to continue: ")
    if exitchoice != '':
        print()
    
