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

    Name=input ("Name")
    Surname=input("Surname : ")
    Access = True
    Buy = input("Buy :")
    Sell = input ("Sell :")

    with open('users.csv', 'w', newline='') as csvfile:
        employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if Access:
            sAccess = 1
        else:
            sAccess = 0

        employee_writer.writerow([Name, Surname, sAccess, Buy, Sell])


def getUserName():
    UserName=input ("login Name :")
    AccessType="None"
    with open('employee_birthday.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row["Name"] =="UserName":
                Access = row["Access"]
                buy=row["buy"]
                Sell=row.["Sell"]
        if Access==1:
            if buy==1 and Sell==1:
                AccessType="Full"
            if buy=1 and Sell==0:
                AccessType="buy"
            if buy=0 and Sell==1:
                AccessType="Sell"

    return (AccessType)


getUserName()