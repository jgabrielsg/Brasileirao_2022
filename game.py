import random
from team import score_goal

def soccer_match(team_home, team_away, 
                 goals_home, goals_away):
    if goals_home > goals_away:
        team_home.points += 3
        team_home.victory += 1
        team_away.lost += 1
        
    elif goals_away > goals_home:
        team_away.points += 3
        team_away.victory += 1
        team_home.lost += 1
        
    else:
        team_home.points += 1
        team_away.points += 1
        team_home.draw += 1
        team_away.draw += 1
    
    team_home.goals_scored += goals_home
    team_home.goals_against += goals_away
    
    team_away.goals_against += goals_home
    team_away.goals_scored += goals_away
    
    
    for goal in range(goals_home):
        random_goal(team_home)
    
    for goal in range(goals_away):
        random_goal(team_away)

def semifinal(first, second,
                goals1, goals2):
    finalist = ''
    
    print(f'{first} {goals1} x {goals2} {second}')
    if goals1 > goals2:
        finalist = first
    elif goals2 > goals1:
        finalist = second
    else:
        print("Haverá pênaltis! Haja coração!")
        penalties_home = random.randint(1,5)
        penalties_away = random.randint(1,5)
        if penalties_home > penalties_away:
            finalist = first
        elif penalties_home < penalties_away:
            finalist = second
        else:
            penalties_home += 1
            finalist = first
        print(f'{first} {penalties_home} x {penalties_away} {second}')
    
    
    #for goal in range(goals1):
        #random_goal(first)
    
    #for goal in range(goals2):
        #random_goal(second)
    
    
    print(f'O {finalist} está na final!')
    return finalist

def final(team1, team2, 
            goals1, goals2):
    print(f'{team1} {goals1} x {goals2} {team2}')
    if goals1 > goals2:
        champion = team1
    elif goals2 > goals1:
        champion = team2
    else:
        print("Haverá pênaltis! Haja coração!")
        penalties_home = random.randint(1,5)
        penalties_away = random.randint(1,5)
        if penalties_home > penalties_away:
            champion = team1
        elif penalties_home < penalties_away:
            champion = team2
        else:
            penalties_home += 1
            champion = team1
        print(f'{team1} {penalties_home} x {penalties_away} {team2}')
    
    #for goal in range(goals1):
        #random_goal(team1)
    
    #for goal in range(goals2):
        #random_goal(team2)
    
    print(f'O {champion} FOI CAMPEÃO DO BRASILEIRÃO!')
    return champion

def random_goal(team):
    rand = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                    weights=[0.02, 0.02, 0.03, 0.03, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2])[0]
    
    score_goal(team.players[rand])  