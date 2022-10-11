USD = 0.73
EUR = 0.85
BLR = 0.074
YEN = 0.0063
TRY = 0.0015
def rateexchange(currentrate):
    if currentrate == "USD":
        print("The rate is", USD)
        return USD
    elif currentrate == "EUR":
        print("The rate is", EUR)
        return (EUR)
    elif currentrate == "BLR":
        print("The rate is", BLR)
        return (BLR)
    elif currentrate == "YEN":
        print("The rate is", YEN)
        return(YEN)
    elif currentrate == "TRY":
        print("The rate is", TRY)
        return(TRY)
    print (currentrate)


rate = rateexchange(input("Please provide the currency you wish to exchange: USD/EUR/BLR/YEN/TRY"))
while True:
    open = input("Would you like to calculate your own value?:")
    if open == "n":
        print ("Thank you for using the application")
        break
    else:
        cal = float(input("Please enter your value:"))
        print("The return rate is £", rate * cal)
