import statistics


class School:
    count = 0
    def __init__ (self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        School.count += 1
    def ave_age(self):
        return statistics.mean(self.age)
    def ave_height(self):
        return statistics.mean(self.height)
    def ave_weight(self):
        return statistics.mean(self.weight)


numA = int(input())
ageA = [float(i) for i in input().split()]
heightA = [float(i) for i in input().split()]
weightA = [float(i) for i in input().split()]
classA = School(ageA, heightA, weightA)
numB = int(input())
ageB = [float(i) for i in input().split()]
heightB = [float(i) for i in input().split()]
weightB = [float(i) for i in input().split()]
classB = School(ageB, heightB, weightB)
print(classA.ave_age(), classA.ave_height(), classA.ave_weight(), sep='\n')
print(classB.ave_age(), classB.ave_height(), classB.ave_weight(), sep='\n')
result = [['A', classA.ave_height(), classA.ave_weight()], ['B', classB.ave_height(), classB.ave_weight()]]

if classA.ave_height() == classB.ave_height():
    if classA.ave_weight() == classB.ave_weight():
        print('same')
    else:
        print((sorted(result, key=lambda item:item[2]))[0][0])
else:
    print((sorted(result, key=lambda item:item[1]))[1][0])