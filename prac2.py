Spain = {'wins': 0,'loses': 0,'draws': 0,'goal difference': 0,'points': 0}
Iran = {'wins': 0,'loses': 0,'draws': 0,'goal difference': 0,'points': 0}
Portugal = {'wins': 0,'loses': 0,'draws': 0,'goal difference': 0,'points': 0}
Morocco = {'wins': 0,'loses': 0,'draws': 0,'goal difference': 0,'points': 0}


def game_calculator(result, teamA, teamB):
    if int(result[0]) == int(result[1]):
        teamA['draws'] += 1
        teamB['draws'] += 1
        teamA['points'] += 1
        teamB['points'] += 1
    if int(result[0]) > int(result[1]):
        teamA['wins'] += 1
        teamB['loses'] += 1
        teamA['goal difference'] += int(result[0]) - int(result[1])
        teamB['goal difference']  += (int(result[1]) - int(result[0]))
        teamA['points'] += 3
    if int(result[0]) < int(result[1]):
        teamB['wins'] += 1
        teamA['loses'] += 1
        teamB['goal difference'] += int(result[1]) - int(result[0])
        teamA['goal difference'] += (int(result[0]) - int(result[1]))
        teamB['points'] += 3


games = [(Iran, Spain), (Iran, Portugal), (Iran, Morocco), \
         (Spain, Portugal), (Spain, Morocco), (Portugal, Morocco)]

for i in range(6):
    result = input().split('-')
    game_calculator(result, games[i][0], games[i][1])

teams = {'Spain': Spain, 'Iran': Iran, 'Portugal': Portugal, 'Morocco': Morocco}
teams_sorted = sorted(teams.items(), key=lambda x: (-x[1]['points'], -x[1]['wins'], x[0]))

for i in range(4):
    print(teams_sorted[i][0], ' wins:', teams_sorted[i][1]['wins'], \
          ' , loses:', teams_sorted[i][1]['loses'], ' , draws:', teams_sorted[i][1]['draws'], \
          ' , goal difference:', teams_sorted[i][1]['goal difference'], \
          ' , points:', teams_sorted[i][1]['points'], sep='')