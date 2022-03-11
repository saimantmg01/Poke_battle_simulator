"""
For the player:
    You need attributes/methods for the Pokemon the player owns, 
    the amount of money in the player's possession, the player's bag, 
    the player's name, gender and nature (kind, mean, funny etc)
"""
from Pokemon import pokemon, moves, stats


class player:
    def __init__(self, name, gender, nature, pokemon_list = [], bag = [], money = 0):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money
    
    def __str__(self):
        return "Player Info: \n Name: {} \n Gender: {} \n Nature: {} \n Pokemons: {}  \n Bag: {} \n Money: {}"\
        .format(self.name, self.gender, self.nature,self.pokemon_list,self.bag, self.money)

class item:
    def __init__(self, item_id, item_name, item_properties):
        self.item_id = item_id
        self.item_name = item_name
        self.item_properties = item_properties
    
    def __repr__(self):
        return self.item_name

    def __str__(self) -> str:
        return "Bag contains: \n Item Id: {} \n Item Name: {} \n Item Properties: {} \n".format(self.item_id,self.item_name,self.item_properties)

if __name__ == "__main__":
    item_1 = item(1,"Potion", "Heals 25 percent of health")
    item_2 = item(1,"Full Potion", "Heals 100 percent of health")
    watergun = moves(1, 'WaterGun', 75)
    tackle = moves(2, "Tackle", 55)
    squirtle_stats = stats(27, 5)
    
    squirtle = pokemon(1,'Squirtle','M', 'Water',[watergun, tackle], squirtle_stats)
    player_1 = player('Ash','M','kind', [squirtle],[item_1, item_2],10000)
    print(player_1)
