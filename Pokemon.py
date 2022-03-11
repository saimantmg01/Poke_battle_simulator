"""
For the Pokemon:
    You need attributes/methods for the name, 
    health points, gender, nature and 
    moves the Pokemon can use. 
    Please note that moves might be better made as a class than a dict of move: attack power.
"""

from pprint import pprint

class pokemon:
    def __init__(self, id, name, gender, nature, moves_list, stats_info):
        self.poke_id = id
        self.poke_name = name
        self.poke_gender = gender
        self.poke_type = nature
        self.moves = moves_list
        self.stats = stats_info
    
    def __str__(self) :
        return "Pokemon: \n ID: {} \n Name: {} \n Gender: {} \n Type: {} \n Moves: {} \n Stats: {} \n".format(self.poke_id,self.poke_name,self.poke_gender,self.poke_type,self.moves,self.stats)
    
    #move class
class moves():
    def __init__(self, attack_id, attack_name, attack_power):
        self.id = attack_id
        self.name = attack_name
        self.power = attack_power
    
    def __str__(self):
        return "Moves: \n ID: {} \n Attack Name: {} \n Attack Power: {} \n".format(self.id, self.name, self.power)
    
    def attack_power(self):
        return self.power
#stats class
class stats:
    def __init__(self, base_health, level):
        self.health = base_health + round(level*2.5)
        self.level = level

    def __str__(self):
        return "\n  Health: {} \n  Level: {}".format(self.health, self.level)

    def getHealth(self):
        return self.health


if __name__ == "__main__":
    #for pokemon class
    watergun = moves(1, 'WaterGun', 75)
    tackle = moves(2, "Tackle", 55)
    squirtle_stats = stats(27, 5)
    
    squirtle = pokemon(1,'Squirtle','M', 'Water',[watergun, tackle], squirtle_stats)
    
    print(squirtle)
    print(squirtle.moves[0]) 
    print(squirtle.moves[1])
    
    firepunch = moves(1, 'Fire Punch', 75)
    torchic_stats = stats(27, 5)
    print(torchic_stats)
    
    torchic = pokemon(1, 'Torchic', 'F', 'Fire', [firepunch], torchic_stats)
    print(torchic)
    print('*' * 7)


