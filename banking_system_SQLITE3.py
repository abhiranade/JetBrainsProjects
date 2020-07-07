import sqlite3
import random

# Establish connection to a Database and create a cursur inside the connection
conn = sqlite3.connect("card.s3db")
c = conn.cursor()

#create a table in DB if it not aleady exists
c.execute('''CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY , number TEXT, pin TEXT, balance INTEGER default 0)''')


keep_running = True  # variable to keep running the program in loop

while keep_running:
    print("\n1. Create an account \n2. Log into account \n0. Exit ")
    option = input()
    
    # if user chooses 0 as option then close the DB connection and exit the program
    if option == "0":
        print("Bye!")
        conn.close()
        keep_running = False

    # If user chooses option 1 then system will create a new 16 didgit CC and 4 digit pin
    # code to generate Credit Card Number and Pin using randint function and storing details in a dictonary
    # this code also creates the credit card number that follows luhns alogorithm
    if option == "1":
        # randomly generate 9 numbers and append them to "4000000" to get a 15 digit string
        acc_no = ""
        pin = ""
        for i in range(0, 9):
            x = random.randint(0, 9)
            acc_no += str(x)
        cc_no_15 = "400000" + acc_no
        
        # double all the numbers at the odd positions and after doubling if number is greater than 9 then subtract 9 from the number and save the remaining number
        luhns_cc_num = ""
        for num1 in range(0,15):
            if num1%2 == 0:
                mid_num = int(cc_no_15[num1])
                mid_num = mid_num * 2
                if mid_num > 9:
                    mid_num = mid_num - 9
                luhns_cc_num = luhns_cc_num + str(mid_num)
            else:
                luhns_cc_num = luhns_cc_num + cc_no_15[num1]
        
        # get the last digit and append it to the end of the 15 digit CC number
        # for doing this, sum all the 15 digits and find a number that should be added to the sum so that the entire number becomes divisible by 10.
        cc_sum = 0
        for num2 in range(0,15):
            cc_sum = cc_sum + int(luhns_cc_num[num2])
        if cc_sum % 10 ==0:
            checksum = 0
        else:
            checksum = 10 - (cc_sum % 10)
        cc_no = cc_no_15 + str(checksum)
        
        # generate a 4 digit pin by randomly selecting 4 digits between 0 and 9
        for j in range(0, 4):
            y = random.randint(0, 9)
            pin += str(y)
        
        print("Your card number:")
        print(f"{cc_no}")
        print("Your card PIN:")
        print(int(pin))

        # Insert the newly generated CC and Pin in Database
        c.execute("INSERT INTO card (number,pin) VALUES (?, ?)",(cc_no, pin))
        conn.commit()

    # If user chooses option 2 then user should be able to login by providing correct details
    # code to verify if entered credit card number and pin are valid and do further transactions
    if option == "2":
        enter_cc = input("Enter your card number: \n")
        enter_cc = str(enter_cc)
        enter_pin = input("Enter your PIN: \n")
        
        # Extract data from DB based on CC and pin provided. If both CC and pin are valid then go further else error message
        c.execute("SELECT * FROM card where number = ?", [enter_cc])
        check_card = c.fetchall()
        #if check_card is empty it means no records are present in DB for given CC else go ahead
        if check_card:
            # check if given pin matches with pin present in DB for the given CC
            if check_card[0][2] == enter_pin:
                logged_in = True  # variable to keep the loop running
                print("You have successfully logged in!")
                while logged_in:
                    print("\n1. Balance \n2. Add Income \n3. Do transfer \n4. Close Account \n5. Log out \n0. Exit ")
                    choice = input()
                    if choice == "1":
                        c.execute("SELECT * FROM card where number = ?", [enter_cc])
                        balance_check = c.fetchall()
                        b = balance_check[0][3]
                        print(f"Balance: {b}")
                    elif choice == "2":
                        income = int(input("Enter income:\n"))
                        c.execute("SELECT * FROM card where number = ?", [enter_cc])
                        balance_check = c.fetchall()
                        money = balance_check[0][3]
                        total_money = income + money
                        # add money in DB by updating balance
                        c.execute("UPDATE card SET balance = ? WHERE number = ?",(total_money,enter_cc))
                        conn.commit()
                        print("Income was added!")
                    elif choice == "3":
                        print("Transfer")
                        c.execute("SELECT * FROM card where number = ?", [enter_cc])
                        balance_check = c.fetchall()
                        b = balance_check[0][3]
                        transfer_card = input("Enter card number: \n")
                        if len(transfer_card) != 16:
                            print("Probably you made mistake in the card number. Please try again!")
                        else:
                            # if the card to which money needs to be transfered is the same as the original card then give error
                            if transfer_card == balance_check[0][1]:
                                print("You can't transfer money to the same account!")
                            else:
                                # card is 16 digits long and doesnot match original card so now check if transfer card follows luhns algorithm
                                last_digit = transfer_card[15]
                                fifteen_digits = transfer_card[0:15]
                                luhns_cc_num = ""
                                # double the numbers at Odd places for first 15 digits and if the resulting number is greater than 9 then subtract 9 from that number
                                for num1 in range(0,15):
                                    if num1%2 == 0:
                                        mid_num = int(fifteen_digits[num1])
                                        mid_num = mid_num * 2
                                        if mid_num > 9:
                                            mid_num = mid_num - 9
                                        luhns_cc_num = luhns_cc_num + str(mid_num)
                                    else:
                                        luhns_cc_num = luhns_cc_num + fifteen_digits[num1]
                                
                                # find out the last number of the CC and check if it matches with the given number
                                cc_sum = 0
                                for num2 in range(0,15):
                                    cc_sum = cc_sum + int(luhns_cc_num[num2])
                                if cc_sum % 10 ==0:
                                    checksum = 0
                                else:
                                    checksum = 10 - (cc_sum % 10)

                                if str(checksum) ==  last_digit:
                                    # transfer card follows luhns algorith so now check if the card exists in DB, if yes then make transfer
                                    c.execute("SELECT * FROM card where number = ?", [transfer_card])
                                    check_transfer = c.fetchall()
                                    if check_transfer:
                                        transfer_money = int(input("Enter how much money you want to transfer: \n"))
                                        c.execute("SELECT * FROM card where number = ?", [enter_cc])
                                        balance_check = c.fetchall()
                                        b = balance_check[0][3]
                                        if transfer_money > b :
                                            print("Not enough money!")
                                        else:
                                            # deduct money from original CC
                                            new_balance = b - transfer_money
                                            c.execute("UPDATE card SET balance = ? WHERE number = ?",(new_balance,enter_cc))
                                            conn.commit()
                                            # add money to the tranfer card
                                            c.execute("SELECT * FROM card where number = ?", [transfer_card])
                                            check_transfer = c.fetchall()
                                            tcard_balance = check_transfer[0][3]
                                            new_tcard_balance = tcard_balance + transfer_money
                                            c.execute("UPDATE card SET balance = ? WHERE number = ?",(new_tcard_balance,transfer_card))
                                            conn.commit()

                                            print("Success!")

                                    else:
                                        print("Such a card does not exist.")

                                else:
                                    print("Probably you made mistake in the card number. Please try again!")


                    elif choice == "4":
                        c.execute("DELETE FROM card WHERE number = ?", [enter_cc])
                        conn.commit()
                        print("The account has been closed!")
                        logged_in = False
                    elif choice == "5":
                        print("You have successfully logged out!")
                        logged_in = False
                    elif choice == "0":
                        print("Bye!")
                        logged_in = False
                        keep_running = False
                        conn.close()

            else:
                print("Wrong card number or PIN!")

        else:
            print("Wrong card number or PIN!")

