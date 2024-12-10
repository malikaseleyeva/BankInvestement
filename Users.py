import csv

class User:
    """Class with functions to add a new user to csv and get the username and the accesstype"""
    def __init__(self, Name, Surname, Access, Buy, Sell):
        self.Name=Name
        self.Surname=Surname
        self.Access = Access #True=Access ok False= No Access
        self.Buy = Buy
        self.Sell = Sell


    def newUser(self):

        with open('users.csv', 'a', newline='') as csvfile:  
            employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if self.Access:
                 sAccess = 1 
            else:
                 sAccess = 0

            employee_writer.writerow([self.Name, self.Surname, sAccess, self.Buy, self.Sell])


    def getUserName(self):
        AccessType = "None"
        Access = '0'

        with open('users.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == self.Name:
                    Access = str(row[2])
                    buy = str(row[3])
                    sell = str(row[4])
                    break

        if Access == '1':
            if buy == 'y' and sell == 'y':
                AccessType = "Full"
            elif buy == 'y' and sell != 'y':
                AccessType = "Buy"
            elif buy != 'y' and sell == 'y':
                AccessType = "Sell"
        else:
            AccessType = "None"

        print(f"The user has {AccessType} access")
        return (self.Name, AccessType)