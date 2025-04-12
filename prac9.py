import random


class Human:
    count = 0
    names = []
    def __init__ (self, name):
        self.name = name
        Human.names += self.name
        Human.count += 1


class Footballer(Human):
    teamA = ['None'] * 11
    teamB = ['None'] * 11
    def getTeam(self):
        for i in range(len(Footballer.teamA)):
            Footballer.teamA[i] = random.choice(Human.names)
            Human.names.remove(Footballer.teamA[i])
        Footballer.teamB = Human.names

    
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

for i in names:
    footballer = Footballer(i)

footballer.getTeam()
print('team A =', end=' ')

for i in range(len(Footballer.teamA)):
    print(Footballer.teamA[i], sep='', end=' ')

print('\nteam B =', end=' ')

for i in range(len(Footballer.teamB)):
    print(Footballer.teamB[i], sep='', end=' ')