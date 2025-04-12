result = []
NumOfPeople = int(input())

for _ in range(NumOfPeople):
    result.append(input().lower().split('.'))

sorted_result = sorted(result, key=lambda x: (x[0], x[1]))

for i in range(NumOfPeople):
    if sorted_result[i][2] == 'c++' or sorted_result[i][2] == 'c':
        sorted_result[i][2] = sorted_result[i][2].capitalize()
    print(sorted_result[i][0], sorted_result[i][1].capitalize(), sorted_result[i][2])