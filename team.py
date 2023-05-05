class Team:
    def __init__(self, name, 
                points=0, victory=0,
                draw=0, lost=0, 
                goals_scored=0, goals_against=0,
                ):
        self.name = name
        self.points = points
        self.victory = victory
        self.draw = draw
        self.lost = lost
        self.goals_scored = goals_scored
        self.goals_against = goals_against
        
        self.players = []

class Player:
    def __init__(self, name,
                 position, goals=0):
        self.name = name
        self.position = position
        self.goals = goals
        
    
def score_goal(Player):
    Player.goals += 1