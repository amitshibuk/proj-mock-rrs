import function_searchandbook
import function_updatendelete
import function_status
import function_information

from tabulate import tabulate


while True:
    '''
    print('=' * 80)
    print("\t\t    RAILWAY RESERVATION SYSTEM")
    print("\t\t\t       IRCTC")
    print('*' * 80)
    '''
    print('='*141)
    print('''
               ___    _  _     ___     ___     ___    _  _              ___     ___     ___     _    __      __ ___   __   __ 
              |_ _|  | \| |   |   \   |_ _|   /   \  | \| |     o O O  | _ \   /   \   |_ _|   | |   \ \    / //   \  \ \ / / 
               | |   | .` |   | |) |   | |    | - |  | .` |    o       |   /   | - |    | |    | |__  \ \/\/ / | - |   \ V /  
              |___|  |_|\_|   |___/   |___|   |_|_|  |_|\_|   TS__[O]  |_|_\   |_|_|   |___|   |____|  \_/\_/  |_|_|   _|_|_  
            _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_| """ | 
            "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''.center(180))
    print()
    print("IRCTC Next Generation eTicketing System".center(141))
    print()
    tagline='"𝐿𝒾𝒻𝑒𝓁𝒾𝓃𝑒 𝑜𝒻 𝓉𝒽𝑒 𝒩𝒶𝓉𝒾𝑜𝓃"'
    print(tagline.center(141))
    print()
    print()
    print('-'*141)
    print()
    
    print("MAIN MENU".center(141))
    '''choice_list = [['1.','Search and Book Tickets'],['2.','Manage Booking'],['3.','Booking Info'],['4.','Quit']]'''
    print('''                                                        =  ========================= 
                                                        1. Search and Book
                                                        2. Manage Booking
                                                        3. Booking Status
                                                        4. General Information
                                                        5. Quit
                                                        =  =========================
        ''')
    '''print(tabulate(choice_list,tablefmt='rst').center(180))'''
    print()
    print("Note: Enter number corresponding to your choice")
    choice = int(input("Choice: "))
    print('=' * 141)
    if choice==1:
        function_searchandbook.search_train()
    elif choice==2:
        function_updatendelete.module_choice()
    elif choice==3:
        function_status.ticket_info()
    elif choice==4:
        function_information.info_module_choice()
    elif choice==5:
        print("Thank you for using our service".center(141))
        print("Have a splendid day!".center(141))
        break
    else:
        print("Invalid Choice")
