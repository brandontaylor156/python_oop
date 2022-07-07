class Player:
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(Player(player))
        return new_team

    def __init__(self, playerInfo):
        self.name = playerInfo["name"]
        self.age = playerInfo["age"]
        self.position = playerInfo["position"]
        self.team = playerInfo["team"]

new_team = []

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "Demar Derozan", 
    	"age":32, 
    	"position": "Shooting Guard", 
    	"team": "Chicago Bulls"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

playerKevin = Player(kevin)
playerJason = Player(jason)
playerKyrie = Player(kyrie)

for player in players:
    new_team.append(Player(player))

newerTeam = Player.get_team(players)

print(new_team)