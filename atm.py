class Bank:
    acbal=10000
    limit=3
    def viewoptions(self):
        print("1. Deposit\n2. Withdraw\n3. Balance Enquiry\n0. Exit")
        option=int(input("Enter your choice: "))
        if option==1:
            obj.deposit()
            obj.confirm()
        elif option==2:
            obj.withdraw()
            obj.limit-=1
            obj.confirm()
        elif option==3:
            obj.balenq()
            obj.confirm()
        elif option==0:
            print("THANK YOU! VISIT AGAIN :)")
        else:
            print("Choose given options only..!")
            obj.viewoptions()
    def confirm(self):
        print("1. Continue\n0. Exit")
        option=int(input("Choose your option:"))
        if option==1:
            obj.viewoptions()
        elif option==0:
            print("THANK YOU! VISIT AGAIN :)")
        else:
            print("Choose given options only..!")
            obj.confirm()
    def balenq(self):
        print(f"Available account balance is Rs.{self.acbal}/-")
    def notes(self,amount):
            if amount>=500:
                fn=amount//500
                amount-=fn*500
                if amount==0:
                    print(f"{fn} 500/- notes..!")
                else:
                    print(f"{fn} 500/- notes and")
            if amount>=200:
                sn=amount//200
                amount-=sn*200
                if amount==0:
                    print(f"{sn} 200/- notes..!")
                else:
                    print(f"{sn} 200/- notes and")
            if amount>=100:
                on=amount//100
                amount-=on*100
                print(f"{on} 100/- notes..!")
            
    def withdraw(self):
        if obj.limit>0:
            amount=int(input("Enter amount to withdraw:"))
            if amount>self.acbal:
                print("Insuffient balance in your account!")
                obj.withdraw()
            elif (amount
                  <100):
                print("SORRY..! Minimum amount of RS.100/- must be withdrawn. Please try again!")
                obj.withdraw()
            elif amount%100!=0:
                print("SORRY..! The amount must be the multiple of 100. Please try again!")
                obj.withdraw()
            elif amount>20000:
                print("SORRY..! Rs.20000/- is the maximum limit. Please try again!")
                obj.withdraw()
            else:
                self.acbal-=amount
                print("Withdraw done successfully..! :)")
                obj.notes(amount)
                print(f"Available account balance is Rs.{self.acbal}/-")
        else:
            print("SORRY..! Maximum withdrawls limit reached for today!")
    def deposit(self):
        amount=int(input("Enter amount to deposit:"))
        if amount<100:
            print("SORRY..!Minimum amount of RS.100/- must be deposited. Please try again!")
            obj.deposit()
        elif amount%100!=0:
            print("SORRY..! The amount must be the multiple of 100. Please try again!")
            obj.deposit()
        elif amount>50000:
            print("SORRY..! Rs.50000/- is the maximum limit. Please try again!")
            obj.deposit()
        else:
            self.acbal+=amount
            print("Amount deposited successfully..! :)")
            print(f"Available account balance is Rs.{self.acbal}/-")
    def validate(self,ch):
        pin=1234
        print("-------Welcome to RKCE bank-------")
        upin=int(input("Enter your pin:"))
    
        if upin==pin:
            obj.viewoptions()
                    
        else:
            ch-=1
            if ch>0:
                print("Invalid pin....! Please try again :)")
                self.validate(ch)
            else:
                print("OOPS..! Sorry, your card has been blocked for today :(")
chances=3
obj=Bank()
obj.validate(chances)
 
