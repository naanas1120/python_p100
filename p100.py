class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber

    def CashWithdrawl(self):
        input("how much do you want to withdraw: ")

    def BalanceEnquiry(self):
        print("your balance is:10,000")

sbiAtm=Atm("3413234565471712","6765")

sbiAtm.CashWithdrawl()
sbiAtm.BalanceEnquiry()

