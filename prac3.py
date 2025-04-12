result = [['Action', 0], ['Adventure', 0], ['History', 0], ['Comedy', 0], ['Romance', 0], ['Horror',0]]
NumOfPeople = int(input())

for _ in range(NumOfPeople):
    NameAndGenre = input().lower()
    NameAndGenre = NameAndGenre.split()
    result[0][1] += NameAndGenre.count('action')
    result[1][1] += NameAndGenre.count('adventure')
    result[2][1] += NameAndGenre.count('history')
    result[3][1] += NameAndGenre.count('comedy')
    result[4][1] += NameAndGenre.count('romance')
    result[5][1] += NameAndGenre.count('horror')
    
sorted_result = sorted(result, key=lambda x: (-x[1], x[0]))
print(sorted_result[0][0], ' : ', sorted_result[0][1], '\n', sorted_result[1][0], ' : ', sorted_result[1][1], '\n', \
      sorted_result[2][0], ' : ', sorted_result[2][1], '\n', sorted_result[3][0], ' : ', sorted_result[3][1], '\n', \
      sorted_result[4][0], ' : ', sorted_result[4][1], '\n', sorted_result[5][0], ' : ', sorted_result[5][1], sep='')
