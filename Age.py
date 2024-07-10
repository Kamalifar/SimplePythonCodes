from datetime import datetime
from dateutil.relativedelta import relativedelta


class Age:
    def __init__(self,date):
        self.date=date
    def getAge(self):
        age=relativedelta(datetime.strptime("2019/02/01","%Y/%m/%d"),datetime.strptime(self.date,"%Y/%m/%d"))
        return age.years+1
    
inputDate=input("Please give me your birthdate in yyyy/mm/dd format: ")
year,month,day=inputDate.split("/")
isValidDate=True
try:
    datetime(int(year),int(month),int(day))
except:
    isValidDate=False

if isValidDate:
    CalculateAge = Age(inputDate)
    print("Your age is " + str(CalculateAge.getAge()))
else:
    print("Your birthdate is not a correct format")