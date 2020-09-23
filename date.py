class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day   = day
        self.year  = year
        
    def insert(self):
        self.month = int(input("Please enter a month: "))
        self.day   = int(input("Please enter a day: "))
        self.year  = int(input("Please enter a year: "))

    def size(self):
        return self.month + self.day + self.year

    def display(self):
       pass

class DateShort(Date):
    def __init__(self, month, day, year):
        super().__init__(month, day, year)
    
    def display(self):
        print("Date Short: {}/{}/{}".format(self.month, self.day, self.year))

class DateLong(Date):
    def __init__(self, month, day, year):
        super().__init__(month, day, year)
    
    def display(self):
        self.months = (
            "January", "February", "March"    , "April"  , "May"     , "June",
            "July"   , "August"  , "September", "October", "November", "December"
        )
        print("DateLong: {} {}, {}".format(self.months[self.month - 1], self.day,  self.year))

class DateJapan(Date):
    def __init__(self, month, day, year):
        super().__init__(month, day, year)
    
    def display(self):
        print("DateJapan: {}/{}/{}".format(self.year, self.month, self.day))

def main():
    date = Date(0, 0, 0)
    dateShort = DateShort
    dateLong  = DateLong
    dateJapan  = DateJapan

    # enter in an information for date
    date.insert()

    # display date short
    dateShort.display(date)

    # display date long
    dateLong.display(date)

    # display date japan
    dateJapan.display(date)

main()