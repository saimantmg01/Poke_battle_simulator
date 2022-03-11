"""
For the CPU-trainers:
    You need attributes/methods for their name, 
    Pokemon they own, the amount of money they award the player upon losing, 
    the Pokemon they gift to the player if any, and a fun fact about them 
    ("Jessica the rich girl fantasizes about ruling her town with an iron fist" for example [I wouldn't want to live in her town lol!])
"""
from Pokemon import * 

class CPU_trainers:
    def __init__(self,name, pokemon_list, award_money, prize_pokemon, fun_fact):
        self.name = name
        self.pokemon_list = pokemon_list
        self.award_money = award_money
        self.prize_pokemon = prize_pokemon
        self.fun_fact = fun_fact
    
    def __str__(self) -> str:
        return "Trainer info: \n Name: {} \n Pokemon Possession: {} \n Award money: {} \n Prize_pokemon: {} \n Fun fact: {}".format(self.name, self.pokemon_list,self.award_money, self.prize_pokemon, self.fun_fact)

if __name__ == "__main__":
    blastoise = pokemon(5, 'Blastoise', 'F', 'Water', [moves(1, 'tackle', 5), moves(2, 'water punch', 15)], stats(27,5))
    mewto = pokemon(6, 'Mewto', 'F', 'Psychic', [moves(1, 'Invisible Punch', 15), moves(2, 'hypnosis', 7)], stats(27, 2))
    trainer = CPU_trainers('Gary', [blastoise, mewto], 10000, blastoise, "Gary became researcher")
    print(trainer)