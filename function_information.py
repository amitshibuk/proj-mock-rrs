import mysql.connector
import time
from tabulate import *

my_db = mysql.connector.connect(host="localhost", user="root", passwd='A;sldkfj14321',
                                    database="railway_res_system")
my_cursor = my_db.cursor()

def info_module_choice():
    while True:
        print('='*141)
        print(' '*64, "INFORMATION")
        print('-'*141)
        print()
        #choice_list = [['1.', 'All Trains'], ['2.', 'Terms and Conditions'],['3.','Passenger Rules and Guidelines'],['4.','Main Menu']]
        #print(tabulate(choice_list, tablefmt='rst'))
        print('''                                                        =  ============================== 
                                                        1. All Trains
                                                        2. Terms and Conditions
                                                        3. Passenger Rules and Guidelines
                                                        4. Main Menu
                                                        =  ==============================
        ''')
        print()
        choice = int(input("Enter your Choice: "))
        if choice==1:
            train_details()
        elif choice==2:
            train_terms_n_conditions()
        elif choice==3:
            train_guidlines()
        elif choice==4:
            print("Redirecting to Main Menu",end='')
            for i in range(3):
                print('.',end='')
                time.sleep(0.5)
            print("Done")
            break
        else:
            print("INVALID CHOICE")

def train_details():
    my_cursor.execute("select * from train_data")
    result=my_cursor.fetchall()
    print(tabulate(result,headers=["train_no","train_name","int_loc","fin_loc","train_days","train_dep_time", "train_des_time",
                                   "train_hours","cost_ac_sec","cost_ac_fir","cost_ac_gen","cost_ac_slp"],tablefmt="pretty"))

def train_terms_n_conditions():
    print("====================")
    print("Terms and Conditions")
    print("--------------------")
    print("Last Updated in 2020")
    print("These are the Terms and Conditions to adhere to: ")
    print()
    print("E-Tickets:")
    print("----------")
    print()
    print('''The provision for specifying ID proof at the time of booking an e-ticket has been dispensed with. The accommodation booked
is not transferable and is valid only if one of the passenger booked on an e-ticket in a transaction presents any of the following
identity cards:
''')
    print('''1. Passport.
2. Voter photo identity card issued by Election Commission of India.
3. Driving Licence issued by RTO
4. Pan Card issued by Income Tax Department.
5. Photo Identity card having serial number issued by Central / State Government.
6. Student Identity Card with photograph issued by recognized School/College for their students.
7. Nationalized Bank Passbook with photographs.
8. Credit Cards issued by Banks with laminated photograph.
9. Printed Unique Identification card "Aadhaar" or downloaded Aadhaar (e-Aadhaar).
10. m-Aadhaar when shown through m-Aadhaar mobile app by the passenger on his/her mobile after entering the password is accepted
    as proof of identity for undertaking journey in any reserved class.
11. Photo identity cards having serial number issued by public sector Undertakings of State/Central Government, District
    Administrations, Municipal bodies and Panchayat Administrations.
12. Passenger showing the Aadhaar/Driving Licence from the “Issued Document” section by logging into his/her DigiLocker
    account considered as valid proof of identity. (Documents uploaded by the user i.e. the document in “Uploaded Document” section
    will not be considered as a valid proof of identity).''')
    print('''The ID proofs should be carried in original during train journey and same will be accepted as proof of identity failing
which the passengers will be treated as travelling without ticket and shall be dealt with as per extant Railway Rules.
''')
    print('''The user can take a printout of the Electronic Registration Slip (ERS) and perform the journey, duly carrying the
authorized Original Identity Card of any one of the passenger travelling in the PNR during train journey.
''')
    print('''E-Tickets (Reservations) can be cancelled only through Internet till Chart preparation of the train and it is not
allowed at face to face Railway Counters. If the user wishes to cancel his e-Ticket, he can do so till the time of chart preparation
for the train through the Internet. He can log on to www.irctc.co.in and go to Booked Tickets link and select the ticket to be
cancelled and can initiate the cancellation by selecting the passengers to be cancelled. Cancellation would be confirmed online and
the refund would be credited back to the account used for booking as for normal Internet tickets. If there is any partial
cancellation of ticket please ensure that the modified ticket (Electronic Reservation Slip) is printed separately.
''')
    print('''Electronic Reservation Slip (ERS)/Virtual Reservation Message (VRM)/ SMS sent by IRCTC along with any one of the prescribed
ID proofs in original and the indication of the passenger(s)' name(s) in the Reservation Chart will authorize the passenger(s)
to travel.
ERS/VRM/SMS sent by IRCTC along with one of the prescribed proofs of identity in original will also authorize the passenger to enter
the platform on the day of journey and he/she will not be required to purchase platform ticket. ERS/VRM/SMS sent by IRCTC along with
original id proof will be required to be produced on demand by Ticket Checking Staff on the platform. The ERS/VRM/SMS sent by IRCTC
along with the ID proof in original would be verified by TTE with the name and PNR on the chart. If the passenger fails to
produce/display ERS/VRM/SMS sent by IRCTC due to any eventuality (loss, discharged mobile/laptop, etc.) but has the prescribed
original proof of identity,penalty as applicable under Railway rules will be levied. The ticket checking staff on
train/at station will give EFT for the same.
''')
    print()
    print("Ticket Booking:")
    print("---------------")
    print()
    print('''Supply By Us: We agree to provide online ticket booking facilities to registered users who agree to the terms and condition
set forth in this document.
''')
    print("Standard of Service: We will supply the service to you with reasonable care and skill.")
    print()
    print('''Service Hours: Booking through Internet is allowed from 00:20 AM to 11:45 PM (Indian Standard Time) on all days including
Sundays. Service hours are liable to be changed without prior notice.
''')
    print("Opening day booking:(120th day in advance, excluding the date of journey) will be available only after 8 AM.")
    print()
    print('''Opening day means 120 days in advance of the date of journey (journey date not to be included) from train originating
station . Please note that in case of some intercity day trains, the ARP (Advance Reservation Period) is less than 60 days. For
Tatkal booking, opening day means one day in advance from date of departure of train from originating station. For e.g.-if train is
to depart from originating station on 2nd August, Tatkal Booking will Commence at 10.00 AM on 1st August.
''')
    print('''Issue of Tickets: You must be a registered user to use our site to book tickets and for any type of enquiries. No user
can register more than once on the site. All payments towards the cost of the tickets issued will be through one of the payment mode
provided on the payment page. Our site is VeriSign secured and your credit card details will travel on the Internet in a fully
encrypted (128 bit, browser independent encryption) form. To ensure security, your card details are NOT stored in our Website.
''')
    print('''Scope of Service: IRCTC makes no guarantee that any service will be uninterrupted, timely, secure or error-free.
''')
    print('''Rules Governing the Booking of Tickets through Internet: Normal Booking (Other than Tatkal Booking) is allowed for journey
by any train from the train starting station to any intermediate halting station or to the destination of the train or from one
halting station to another halting station on the train route subject to distance restriction prescribed for the concerned train.
Example: Suppose a train is running from New Delhi to Chennai with halting stations at Agra and Vijaywada, a passenger can book either
for New Delhi-Agra, New Delhi-Vijayawada, New Delhi-Chennai, Agra-Vijaywada, Agra-Chennai or Vijayawada-Chennai subject to distance
restrictions imposed by the Indian Railways. The facilities not available for tickets booked on Internet vis-à-vis tickets booked at
PRS counters are available in Para B above.
''')
    print('''All rules and regulations applicable for reservation of seats/berths and charging of fare for rail reservation on Indian
Railway's PRS will also apply to reservation through the Internet.
''')
    print('''Allotment of coach/berth/seats will be done as per existing allocation logic available in the PRS. We do not guarantee
allotment of seat/berth of your choice. Furthermore, it is not possible for us to advise you whether your choice of berth is being
allotted or not. In case a lady passenger alone or with children under 12 years, is willing to reserve berth/berths in ladies quota
wherever earmarked, she can give choice 'Ladies' in the field of quota. If berths are available in ladies quota the system will allot
accommodation in ladies cabin otherwise accommodation will be allotted in General quota, as available. In case of 1AC booking,
Coach/Seat No will be given at the time of charting.
''')
    print('''Confirmation of Booking: Your booking and reservation will be confirmed online, after you complete the transaction successfully.
Further, the system will issue you a unique Transaction ID for each booking. The choice of Payment Gateway lies with you. If any one
of the Payment Gateway is not functioning, please try the other one available. Booking of tickets is subject to realization of fare
and the service charges (including Service Tax) from concerned Bank through the Payment Gateway. You will be responsible for all
charges, fees, duties, taxes and assessments arising out of your use of this Website.
''')
    print('''If, for any reason, the reservation does not materialize, the entire amount debited from your card account will be
credited back to your card account. If you want to try for the same reservation again, it will be treated as a fresh booking.
''')
    print()
    print("Refund In Failed Transaction / Cancelled Tickets:")
    print("-------------------------------------------------")
    print()
    print('''Though IRCTC's payment reconciliation team works on a 24 x 7 basis, IRCTC offers no guarantees whatsoever for the
accuracy or timeliness of the refunds reaching the Customers card/bank accounts. This is on account of the multiplicity of
organizations involved in processing of online transactions, the problems with Internet infrastructure currently available and
working days/holidays of financial institutions.
''')
    print('''In case a passenger faces any problem in cancelling an E-Ticket online, He should apply for cancellation by sending the
E-ticket details through email to etickets@irctc.co.in. IRCTC will process such cases with the Railways for grant of the due refund on
behalf of the customer. The time taken and amount of refund granted in such cases is dependent on the merit of each case and is to be
decided by the Railways and IRCTC will not be responsible for delays at the Railway end in any such case. Amount of Refund whenever
received from the Railways shall be credited to the customer's account immediately.
''')
    print('-'*141)
    print()
    while True:
        choice = input("Enter any key to go back: ")
        if choice!='':
            break

def train_guidlines():
    print("===================")
    print("RULES AND GUIDLINES")
    print("-------------------")
    print()
    print("1. Passengers with confirmed e-tickets will be permitted to enter the railway station premises.")
    print()
    print('''2. Both the passenger movement and the driver of the vehicle
    ferrying passengers to and from the station will be allowed entry depending on the confirmed e-ticket.''')
    print()
    print('''3. All the passengers will be screened to identify and give entry to only asymptomatic passengers to board the train.''')
    print()
    print('''4. Passengers will have to arrive at the departure station at least 90 minutes before the departure time of the train.''')
    print()
    print('''5. Passengers will be given hand sanitizers at all entry and exit points as well as on board the train.''')
    print()
    print('''6. All the passengers will have to wear face cover in the station premises and during train travel.''')
    print()
    print('''7. Social distancing has to be strictly maintained during the train journey.
    Health advisories and guidelines will be spread by the Railway Ministry with the help of Information, Education
    and Communication campaign for the railways staff and passengers.''')
    print()
    print('''8. Trains will not be equipped with linen, blankets or curtains this time.
    No stalls or booths on station platforms will be allowed to open. No vendor shall be allowed
    to sell on the platforms. Passengers can either bring their own food or buy ready-to-eat meals
    from the IRCTC. The ticket fare will not include meal cost.''')
    print()
    print('''9. The travelling passengers, on arrival at their destinations,
    will have to adhere to such health protocols as prescribed by the destination states and Union Territories.''')
    print()
    print('''10. Tatkal, Premium Tatkal, Unreserved Tickets (UTS) and current bookings have been suspended for now.
    Passengers can cancel their ticket 24 hours before the train’s departure time. The cancellation fee
    will be 50 percent of the total fare.''')
    print('-'*141)
    print()
    while True:
        choice = input("Enter any key to go back: ")
        if choice!='':
            break
    
    print()
    print()
    

