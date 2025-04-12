from datetime import datetime


class Birth:
    def __init__ (self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def Age(self):
        curYear = datetime.now().year
        if self.year > curYear:
            return 'WRONG'
        else:
            return curYear - self.year
        

birth_date = [int(i) for i in input().split('/')]

if 0 < birth_date[1] < 13 and 0 < birth_date[2] < 32:
    person1 = Birth(birth_date[0], birth_date[1], birth_date[2])
    print(person1.Age())
else:
    print('WRONG')