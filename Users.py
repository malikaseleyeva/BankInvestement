import csv


class User:
    def __init__(self, Id, Name, Surname, Access, Buy, Sell):
        self.Id=Id
        self.Name=Name
        self.Surname=Surname
        self.Access = Access #True=Access ok False= No Access
        self.Buy = Buy
        self.Sell = Sell
    def __str__(self):
        sUser = self.Name + " " + self.Surname
        if self.Access:
            SAccess="User has Access"
        else:
            SAccess = "User has no Access"

def newUser():
    Name = input("Name: ")
    Surname = input("Surname: ")
    Access = True
    Buy = input("Buy (y is yes): ")
    Sell = input("Sell (y if yes): ")

    with open('users.csv', 'a', newline='') as csvfile:  
        employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if Access:
            sAccess = 1 
        else:
            sAccess = 0

        employee_writer.writerow([Name, Surname, sAccess, Buy, Sell])



def getUserName():
    UserName = input("Name: ")
    AccessType = "None"
    Access = 0

    with open('users.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == UserName:
                Access = str(row[2])
                buy = str(row[3])
                sell = str(row[4])
                break  # Exit the loop once the user is found

    if Access == '1':
        if buy == 'y' and sell == 'y':
            AccessType = "Full"
        elif buy == 'y' and sell != 'y':
            AccessType = "Buy"
        elif buy != 'y' and sell == 'y':
            AccessType = "Sell"
            
    print(f"The user has {AccessType} access")
    return (UserName, AccessType)