from Pokemon import *
from CPU_trainers import *
from grid import *
from player import *
import random

starter_poke_dict = {
    1 : pokemon(1,'Treecko','M','Grass',[moves(1,'Frenzy Plant',10), moves(2,'Power Whip', 20)],stats(45,3)),
    2 : pokemon(2,'Torchic','F','Fire',[moves(1,'Ember',15), moves(2,'Quick Attack', 17)],stats(45,3)),
    3 : pokemon(3,'Mudkip','M','Water',[moves(1,'Water Gun',12), moves(2,'Whirl Power', 20)],stats(45,2))
}

trainer_pokemon_dict = {
    1 : pokemon(1,'Pikachu','M','Electric',[moves(1,'Thunder Shock',20), moves(2,'Tackle', 5)],stats(35,4)),
    2 : pokemon(2,'Mewto','F','Psychic',[moves(1,'Psychic',10), moves(2,'Confusion', 15)],stats(40,1)),
    3 : pokemon(3,'Charizard','M','Fire',[moves(1,'Flamethrower',20), moves(2,'Ember', 15)],stats(45,5))
}

wild_pokemon_dict = {
    1 : pokemon(1,'Blastoise','M','Water',[moves(1,'Thunder Shock',20), moves(2,'Tackle', 5)],stats(35,4)),
    2 : pokemon(2,'Pidgeot','F','Flying',[moves(1,'Tackle',15), moves(2,'Gust', 10)],stats(35,1))

}
def prompt():
    nature = random.choices(['mean', 'funny','serious','easygoing','kind'])
    money = random.randint(1, 10000)
    starter_item = item(1,"Potion", "heals 25 percent of initial health before starting a certain battle")
    print("Hi!!! Welcome to Pokemon Battle Simulator!!!")
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    ##########
    
    starter_pokemon = int(input('Choose your starter pokemon: \n1) Treecko \n2) Torchic \n3) Mudkip\nEnter a number(from 1-3): '))
    #setting up players
    player_1 = player(name, gender, nature, [starter_poke_dict[starter_pokemon]], [starter_item], money)
    ##########
    #setting up trainers, items, and wild pokemon
    trainer_name = random.choices(['Mark', 'John','Gary', 'Red'])
    trainer_1 = CPU_trainers(trainer_name,[trainer_pokemon_dict[1], trainer_pokemon_dict[2]],10000, trainer_pokemon_dict[1],"Pikachu was ash first pokemon") 
    trainer_2 = CPU_trainers(trainer_name,[trainer_pokemon_dict[3]],15000, trainer_pokemon_dict[3],"Charizard is the best")

    item_1 = item(2, "Potion",  "heals 25 percent of initial health before starting a certain battle")
    item_2 = item(3,"Full Potion", "heals to original initial health before starting a certain battle")
    
    wild_pokemon_1 = wild_pokemon_dict[1]
    wild_pokemon_2 = wild_pokemon_dict[2]
    #####
    game_board = Grid()
    game_board.create_grid() #creates 8*8 by default
    # placing items, pokemon and trainers
    game_board.grid[1][1] = Grid_square('I',item_1)
    game_board.grid[5][6] = Grid_square('I',item_2)
    game_board.grid[3][3] = Grid_square('P',wild_pokemon_1)
    game_board.grid[1][7] = Grid_square('P',wild_pokemon_2)
    game_board.grid[5][3] = Grid_square('T', trainer_1)
    game_board.grid[2][6] = Grid_square('T',trainer_2)
    #starts the game
    game_board.play_game([2,2], player_1)
    game_board.print_grid()



if __name__ == "__main__":
    prompt()