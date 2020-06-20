# def fightingPits(k, fighters, queries):

#     allTeam = [[] for x in range(k)]
    
#     for i in fighters:
#         teamToAdd = i[1] - 1
#         strength = i[0]
#         allTeam[teamToAdd].append(strength)

#     for team in allTeam:
#         team.sort()

#     for query in queries:
#         if (query[0] == 1):         # 1 s t : add member with strength s to team t
#             strength = query[1]
#             teamToAdd = query[2] - 1
#             allTeam[teamToAdd].append(strength)
#             allTeam[teamToAdd].sort()
#         else:                       # 2 x y: matchup between team x and y, with x is alway have first turn
#             team1 = query[1] - 1
#             team2 = query[2] - 1
#             team1List = allTeam[team1].copy()
#             team2List = allTeam[team2].copy()
#             chooseTeam = 1
#             while (len(team1List) != 0 and len(team2List) != 0):
#                 if (chooseTeam == 1):
#                     fighterStrengthChoosen = team1List[-1]
#                     if (fighterStrengthChoosen > len(team2List)):
#                         team2List = []
#                     else:
#                         team2List = team2List[:-1 * fighterStrengthChoosen]
#                     chooseTeam = 2
#                 else:
#                     fighterStrengthChoosen = team2List[-1]
#                     if (fighterStrengthChoosen > len(team1List)):
#                         team1List = []
#                     else:
#                         team1List = team1List[:-1 * fighterStrengthChoosen]
#                     chooseTeam = 1
#             if (len(team1List) == 0):
#                 print(team2 + 1)
#             else:
#                 print(team1 + 1)

# fighters = [[1,1], [2,1], [1,1], [1,2], [2,2], [1,2], [1,2]]  # [strength, team]
# queries = [[2,1,2], [2,2,1], [1,2,1], [1,2,1],[2,1,2], [2,2,1]] 
# fightingPits(2, fighters, queries)


# def fightingPits(k, fighters, queries):

#     allTeam = [{} for x in range(k)]
#     allTeamStrength = [[] for x in range(k)]
    
#     for i in fighters:
#         teamToAdd = i[1] - 1
#         strength = i[0]
#         if (strength not in allTeam[teamToAdd]):
#             allTeam[teamToAdd][strength] = 1
#             allTeamStrength[teamToAdd].append(strength)
#         else:
#             allTeam[teamToAdd][strength] += 1

#     for query in queries:
#         if (query[0] == 1):         # 1 s t : add member with strength s to team t
#             strength = query[1]
#             teamToAdd = query[2] - 1
#             if (strength not in allTeam[teamToAdd]):
#                 allTeam[teamToAdd][strength] = 1
#                 allTeamStrength[teamToAdd].append(strength)
#             else:
#                 allTeam[teamToAdd][strength] += 1

#         else:                       # 2 x y: matchup between team x and y, with x is alway have first turn
#             team1 = query[1] - 1
#             team2 = query[2] - 1
#             team1List = allTeam[team1].copy()
#             team1Strength = allTeamStrength[team1].copy()
#             team2List = allTeam[team2].copy()
#             team2Strength = allTeamStrength[team2].copy()
#             chooseTeam = 1

#             while (len(team1List) != 0 and len(team2List) != 0):
#                 if (chooseTeam == 1):
#                     count = max(team1Strength)
#                     while(count > 0 and len(team2List) > 0):
#                         maxStrength2 = max(team2Strength)
#                         amount = team2List[maxStrength2]
#                         if (count >= amount):
#                             count = count - amount
#                             team2List.pop(maxStrength2)
#                             team2Strength.remove(maxStrength2)
#                         else:
#                             team2List[maxStrength2] = amount - count
#                             count = 0
#                     chooseTeam = 2
                    
#                 else:
#                     count = max(team2Strength)
#                     while(count > 0 and len(team1List) > 0):
#                         maxStrength1 = max(team1Strength)
#                         amount = team1List[maxStrength1]
#                         if (count >= amount):
#                             count = count - amount
#                             team1List.pop(maxStrength1)
#                             team1Strength.remove(maxStrength1)
#                         else:
#                             team1List[maxStrength1] = amount - count
#                             count = 0
#                     chooseTeam = 1
                

#             if (len(team1List) == 0):
#                 print(team2 + 1)
#             else:
#                 print(team1 + 1)

def fightingPits(k, fighters, queries):

    allTeam = [{} for x in range(k)]
    allTeamStrength = [[] for x in range(k)]
    
    for i in fighters:
        teamToAdd = i[1] - 1
        strength = i[0]
        if (strength not in allTeam[teamToAdd]):
            allTeam[teamToAdd][strength] = 1
            allTeamStrength[teamToAdd].append(strength)
        else:
            allTeam[teamToAdd][strength] += 1

    for team in allTeamStrength:
        team.sort()

    for query in queries:
        if (query[0] == 1):         # 1 s t : add member with strength s to team t
            strength = query[1]
            teamToAdd = query[2] - 1
            if (strength not in allTeam[teamToAdd]):
                allTeam[teamToAdd][strength] = 1
                allTeamStrength[teamToAdd].append(strength)
                allTeamStrength[teamToAdd].sort()
            else:
                allTeam[teamToAdd][strength] += 1

        else:                       # 2 x y: matchup between team x and y, with x is alway have first turn
            team1 = query[1] - 1
            team2 = query[2] - 1
            team1List = allTeam[team1].copy()
            team1Strength = allTeamStrength[team1].copy()
            team2List = allTeam[team2].copy()
            team2Strength = allTeamStrength[team2].copy()
            chooseTeam = 1

            while (len(team1List) != 0 and len(team2List) != 0):
                if (chooseTeam == 1):
                    count = team1Strength[-1]
                    while(count > 0 and len(team2List) > 0):
                        maxStrength2 = team2Strength[-1]
                        amount = team2List[maxStrength2]
                        if (count >= amount):
                            count = count - amount
                            team2List.pop(maxStrength2)
                            team2Strength = team2Strength[:-1]
                        else:
                            team2List[maxStrength2] = amount - count
                            count = 0
                    chooseTeam = 2
                    
                else:
                    count = team2Strength[-1]
                    while(count > 0 and len(team1List) > 0):
                        maxStrength1 = team1Strength[-1]
                        amount = team1List[maxStrength1]
                        if (count >= amount):
                            count = count - amount
                            team1List.pop(maxStrength1)
                            team1Strength = team1Strength[:-1]
                        else:
                            team1List[maxStrength1] = amount - count
                            count = 0
                    chooseTeam = 1
                

            if (len(team1List) == 0):
                print(team2 + 1)
            else:
                print(team1 + 1)
    


fighters = [[1,1], [2,1], [1,1], [1,2], [2,2], [1,2], [1,2]]  # [strength, team]
queries = [[2,1,2], [2,2,1], [1,2,1], [1,2,1],[2,1,2], [2,2,1]] 
fightingPits(2, fighters, queries)
    