class Player:
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for index in range(len(team_list)):
            new_team.append(Player(players[index]))
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
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
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

for index in range(len(players)):
    new_team.append(Player(players[index]))

newerTeam = Player.get_team(players)
