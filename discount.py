class Customer:
    def __init__(self, loyal, uni):
        self.loyal= bool
        self.uni = bool

test_case = Customer(True, True)
public_holiday = [25_12, 26_01] #Would have other public holidays
current_date = 25_12

if current_date in public_holiday:
    print("No Discount")
elif test_case.loyal is True:
    print("Discount")
elif test_case.uni is True:
    print("Discount")
else:
    print("No Discount")