from pprint import pprint
from Pokemon import *
from CPU_trainers import *
from grid import *
from player import *
import random

class Grid_square:
    def __init__(self, symbol , object = 0):
        self.symbol = symbol
        self.object = object
    
    def __repr__(self) -> str:
        #return "{} , {} , {}".format(self.row, self.column, self.object)
        #return "{}".format(self.object)
        return "{}".format(self.symbol)
    
    def __str__(self) -> str:
        return "{}".format(self.symbol)


class Grid:
    def __init__(self, grid_dimensions = [8,8]):
        self.grid_dimensions = grid_dimensions
        self.grid = []

    def __repr__(self) -> str:
        return str(self.grid)

    def create_grid(self):
        for row in range(self.grid_dimensions[0]):
            self.grid.append([])
            for column in range(self.grid_dimensions[1]):
                #self.grid[-1].append(Grid_square(row,column,0)) #working saving for later integration
                #self.grid[-1].append(0)
                self.grid[-1].append(Grid_square('-', None))

    """
    - : accessible spot
    I: item
    P: Pokemon
    T: CPU-trainer
    Player: X
    
    """  
    
    def print_grid(self):
        # for i in self.grid:
        #     #print(" --- " * 8)
        #     print(''.join(map(str,i)))
        #     #print(" --- " * 8)
        pprint(self.grid)   
    
    def validIndex(self, x , y):
        if (x >= 0 and y >=0 and x < self.grid_dimensions[0] and y < self.grid_dimensions[1]):
            return True
        return False

    def surviving_pokemon(self, pokemon_list):
        for pokemon in pokemon_list:
            if pokemon.stats.health > 0:
                return pokemon
        return None
     

    def battle_CPU(self, trainer, player_obj):
        # prompt where trainer challendes player_obj, random pokemon choice from trainer (assume all is health > 0) and own pokemon
        print(f'{trainer.name} challenges {player_obj.name} (you) for a quick batttle!!!')
        opponent_poke_choice = self.surviving_pokemon(trainer.pokemon_list)
        #print(opponent_poke_choice.poke_name)
        curr_poke_choice = self.surviving_pokemon(player_obj.pokemon_list)
        #print(curr_choice)
        
        # state to store what is status
        state = "lose"
        #get num of surviving pokemon for both trainer and obj
        opponent_surviving_pokemon_no = len(trainer.pokemon_list)
        #print(opponent_surviving_pokemon_no)
        player_surviving_pokemon_no = len(player_obj.pokemon_list)
        #print(player_surviving_pokemon_no)
        #get also original health of award pokemon before you fight it
        award_pokemon_orig_health = trainer.prize_pokemon.stats.health

        #get original health of own current pokemon
        orig_health_of_curr_pokemon = curr_poke_choice.stats.health

        #print(award_pokemon_orig_health)
        
        battle_on = True
        
        #while loop where battle is on until one of all pokemon die
        while battle_on:        
        #4 prompts:
            # run: state: ran away nothing happens 1
            print(f'Your Pokemon : {curr_poke_choice.poke_name} has health of ({curr_poke_choice.stats.health})is fighting against opponent Pokemon: {opponent_poke_choice.poke_name} has health of ({opponent_poke_choice.stats.health})')

            print('\nOptions:')
            print('1: Run')
            print('2: Fight')
            print('3: Use Bag')
            print('4: Change Pokemon\n')
            choice = int(input('Enter a choice (1-4): '))
            if choice == 1:
                print('Ran away')
                state = "Ran away"
            # battle: 2
            elif choice == 2:
                #pick a move from move list
                print('List of moves available: ')
                for move in curr_poke_choice.moves:
                    print(move.name)
                move_num = int(input("Enter a choice (a number): "))
                move_num = move_num -1 # 0 indexed array
                
                #check health of your pokemon too if it less than 0
                #choose another immediately
                # decrement your surviving pokemon
                if curr_poke_choice.stats.health <= 0:
                    print(f'{curr_poke_choice.poke_name} has fainted.')
                    curr_poke_choice = self.surviving_pokemon(player_obj.pokemon_list)
                    player_surviving_pokemon_no -= 1
                    #attack - reduce life of opponent pokemon
                else: 
                    opponent_poke_choice.stats.health -= curr_poke_choice.moves[move_num].power
                    print(f'{curr_poke_choice.poke_name} used {curr_poke_choice.moves[move_num].name} against {opponent_poke_choice.poke_name} which got {curr_poke_choice.moves[move_num].power} in damage')
                #check health of enemy curr pokemon health if it is less than 0 
            #   choose another immediately
            #   also decrement the counter of pokemon of enemy
                if opponent_poke_choice.stats.health <= 0:
                    print(f'{opponent_poke_choice.poke_name} has fainted.')
                    opponent_poke_choice = self.surviving_pokemon(trainer.pokemon_list)
                    opponent_surviving_pokemon_no -= 1
                else:
                    #opponent randomly chosen move
                    opponent_pokemon_move = random.choice(opponent_poke_choice.moves)
                    #attack - reduce life of your pokemon
                    curr_poke_choice.stats.health -= opponent_pokemon_move.power
                    print(f'{opponent_poke_choice.poke_name} used {opponent_pokemon_move.name} against {curr_poke_choice.poke_name} which got {opponent_pokemon_move.power} in damage')


            #choose a item in bag to use 3
            elif choice == 3:
                # use and remove that item from bag
                for items in player_obj.bag:
                    print(f'Item name: {items.item_name}')
                item_choice = input("Enter a name of item (as prompted before for use): ")
                if item_choice == 'Full Potion':
                    if curr_poke_choice.stats.health > 0 and curr_poke_choice.stats.health < orig_health_of_curr_pokemon:
                        curr_poke_choice.stats.health = orig_health_of_curr_pokemon
                        for items in player_obj.bag:
                            if items.item_name == item_choice:
                                player_obj.bag.remove(items)
                                break
                        print(player_obj.bag)
                    else:
                        print("Cant use it. Sorry.")
                if item_choice == 'Potion':
                    if curr_poke_choice.stats.health > 0 and curr_poke_choice.stats.health <= (orig_health_of_curr_pokemon * 0.75):
                        curr_poke_choice.stats.health += (curr_poke_choice.stats.health * 0.25) 
                        for items in player_obj.bag:
                            if items.item_name == item_choice:
                                player_obj.bag.remove(items)
                                break
                        print(player_obj.bag)
                    else:
                        print("Cant use it. Sorry.") 
            #change pokemon- 4
            elif choice == 4:
                #only get options of surviving pokemon
                survived = [pokemon for pokemon in player_obj.pokemon_list if pokemon.stats.health > 0]
                for pokemon in survived:
                    print(pokemon.poke_name)
                pokemon_choice = input("Choose a pokemon: (exactly as prompted above) ")
                for pokemon in survived:
                    if pokemon.poke_name == pokemon_choice:
                        curr_poke_choice = pokemon
                        break
                print(f'Curr Pokemon is: {curr_poke_choice}')
                #and after chosen change the current pokemon
                
               #if num of survivng pokemon of opponent is or less than 0, you won -> state
            if opponent_surviving_pokemon_no <= 0:
                state = "won"
               #you get award money appended to your money and price pokemon appended to your pokemon list
                player_obj.money += trainer.award_money
                print(f'You won!!! {trainer.name} lose')
                trainer.prize_pokemon.stats.health = award_pokemon_orig_health
                player_obj.pokemon_list.append(trainer.prize_pokemon)

            #criteria of batle stopped
            if opponent_surviving_pokemon_no <= 0 or choice == 1 or player_surviving_pokemon_no == 4:
                battle_on = False
            
            #if num of surving pokemon of yours is or less than 0, you lose -> state
            if player_surviving_pokemon_no <= 0:
                print("You lost the entire battle")
                state = "lose"
                break 
        
        return (player_obj, state)

    def battle_pokemon(self, wild_pokemon, player_obj):
        print(f'You found a wild {wild_pokemon.poke_name}')
        orig_health_of_wild_pokemon = wild_pokemon.stats.health
        player_pokemon_health  = 0
        for pokemon in player_obj.pokemon_list:
            player_pokemon_health += pokemon.stats.health
        state = "lose"
        num_of_surviving_pokemon = len(player_obj.pokemon_list)
        print(num_of_surviving_pokemon)
        curr_pokemon = self.surviving_pokemon(player_obj.pokemon_list)
        orig_health_of_curr_pokemon = curr_pokemon.stats.health
        battle_on = True
        while battle_on:
            print(f'Your Pokemon : {curr_pokemon.poke_name} has health of ({curr_pokemon.stats.health})is fighting against wild Pokemon: {wild_pokemon.poke_name} has health of ({wild_pokemon.stats.health})')
            print('\nOptions:')
            print('1: Run')
            print('2: Fight')
            print('3: Use Bag')
            print('4: Change Pokemon\n')
            choice = int(input('Enter a choice (1-4): '))
            if choice == 1:
                print('Ran away')
                state = "Ran away"
                # print(random.choice(wild_pokemon.moves))
            elif choice == 2:
                print('List of moves available: ')
                for move in curr_pokemon.moves:
                    print(move.name)
                move_num = int(input("Enter a choice (a number): "))
                move_num = move_num -1 # 0 indexed array
                
                if curr_pokemon.stats.health <= 0:
                    print(f'{curr_pokemon.poke_name} has fainted.')
                    curr_pokemon = self.surviving_pokemon(player_obj.pokemon_list)
                    num_of_surviving_pokemon -= 1
                else: 
                    #user choiced attack
                    wild_pokemon.stats.health -= curr_pokemon.moves[move_num].power
                    print(f'{curr_pokemon.poke_name} used {curr_pokemon.moves[move_num].name} against {wild_pokemon.poke_name} which got {curr_pokemon.moves[move_num].power} in damage')
                if wild_pokemon.stats.health <= 0:
                    print(f'You won!!! {wild_pokemon.poke_name} fainted')
                    wild_pokemon.stats.health = orig_health_of_wild_pokemon
                    player_obj.pokemon_list.append(wild_pokemon)
                    state = "won"
                    break
                else: 
                    #moves by wild pokemon
                    wild_pokemon_move = random.choice(wild_pokemon.moves)
                    curr_pokemon.stats.health -= wild_pokemon_move.power
                    print(f'{wild_pokemon.poke_name} used {wild_pokemon_move.name} against {curr_pokemon.poke_name} which got {wild_pokemon_move.power} in damage')
                
            elif choice == 3:
                #choosing a bag 
                for items in player_obj.bag:
                    print(f'Item name: {items.item_name}')
                item_choice = input("Enter a name of item (as prompted before for use): ")
                if item_choice == 'Full Potion':
                    if curr_pokemon.stats.health > 0 and curr_pokemon.stats.health < orig_health_of_curr_pokemon:
                        curr_pokemon.stats.health = orig_health_of_curr_pokemon
                        for items in player_obj.bag:
                            if items.item_name == item_choice:
                                player_obj.bag.remove(items)
                                break
                        print(player_obj.bag)
                    else:
                        print("Cant use it. Sorry.")
                if item_choice == 'Potion':
                    if curr_pokemon.stats.health > 0 and curr_pokemon.stats.health <= (orig_health_of_curr_pokemon * 0.75):
                        curr_pokemon.stats.health += (curr_pokemon.stats.health * 0.25) 
                        for items in player_obj.bag:
                            if items.item_name == item_choice:
                                player_obj.bag.remove(items)
                                break
                        print(player_obj.bag)
                    else:
                        print("Cant use it. Sorry.")
            elif choice == 4:
                survived = [pokemon for pokemon in player_obj.pokemon_list if pokemon.stats.health > 0]
                for pokemon in survived:
                    print(pokemon.poke_name)
                pokemon_choice = input("Choose a pokemon: (exactly as prompted above) ")
                for pokemon in survived:
                    if pokemon.poke_name == pokemon_choice:
                        curr_pokemon = pokemon
                        break
                print(f'Curr Pokemon is: {curr_pokemon}')
            
            #criteria of batle stopped
            if wild_pokemon.stats.health <= 0 or choice == 1 or num_of_surviving_pokemon == 4:
                battle_on = False
            if num_of_surviving_pokemon <= 0:
                print("You lost the entire battle")
                break 
        return (player_obj, state)

    def play_game(self, curr_pos, player_obj): 
        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('X', player_obj)
        pprint(self.grid)
        while True:
            direction = input('Which direction do you want to go?\nEnter a(for left),w(for up),s(for down),d(for right) for the direction\n')
            if direction == 'w':
                new_pos = [curr_pos[0] -1, curr_pos[1]]
                if (self.validIndex(new_pos[0], new_pos[1])):
                    if self.grid[new_pos[0]][new_pos[1]].symbol == '-':
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'T':
                        print("Battle time with Trainer!!!!!")
                        player__obj, state = self.battle_CPU(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'P':
                        print("Battle time with Pokemon!!!!!")
                        player__obj, state = self.battle_pokemon(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'I':
                        print(f'Before: {player_obj.bag}')
                        print("Item found which can be appended to Player items bag")
                        print(f'Item found {self.grid[new_pos[0]][new_pos[1]].object}. Congrats')
                        player_obj.bag.append(self.grid[new_pos[0]][new_pos[1]].object)
                        print(f'After: {player_obj.bag}')
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                else:
                    print("Invalid direction. Try again!!!")
            elif direction == 's':
                new_pos = [curr_pos[0] + 1 ,curr_pos[1]]
                if (self.validIndex(new_pos[0], new_pos[1])):
                    if self.grid[new_pos[0]][new_pos[1]].symbol == '-':
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'T':
                        print("Battle time with Trainer!!!!!")
                        player__obj, state = self.battle_CPU(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'P':
                        print("Battle time with Pokemon!!!!!")
                        player__obj, state = self.battle_pokemon(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'I':
                        print(f'Before: {player_obj.bag}')
                        print("Item found which can be appended to Player items bag")
                        print(f'Item found {self.grid[new_pos[0]][new_pos[1]].object}. Congrats')
                        player_obj.bag.append(self.grid[new_pos[0]][new_pos[1]].object)
                        print(f'After: {player_obj.bag}')
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                        
                else:
                    print("Invalid direction. Try again!!!")
            elif direction == 'a':
                new_pos = [curr_pos[0] , curr_pos[1]-1]
                if (self.validIndex(new_pos[0], new_pos[1])):
                    if self.grid[new_pos[0]][new_pos[1]].symbol == '-':
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'T':
                        print("Battle time with Trainer!!!!!")
                        player__obj, state = self.battle_CPU(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'P':
                        print("Battle time with Pokemon!!!!!")
                        player__obj, state = self.battle_pokemon(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'I':
                        print(f'Before: {player_obj.bag}')
                        print(f'Item found {self.grid[new_pos[0]][new_pos[1]].object}. Congrats')
                        player_obj.bag.append(self.grid[new_pos[0]][new_pos[1]].object)
                        print(f'After: {player_obj.bag}')
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                else:
                    print("Invalid direction. Try again!!!")
            elif direction == 'd':
                new_pos = [curr_pos[0] , curr_pos[1]+1]
                if (self.validIndex(new_pos[0], new_pos[1])):
                    if self.grid[new_pos[0]][new_pos[1]].symbol == '-':
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'T':
                        print("Battle time with Trainer!!!!!")
                        player__obj, state = self.battle_CPU(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'P':
                        print("Battle time with Pokemon!!!!!")
                        player__obj, state = self.battle_pokemon(self.grid[new_pos[0]][new_pos[1]].object, player_obj)
                        if state == "lose":
                            print("You lose entire game!!!")
                            break
                        if state == "won":
                            self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                            self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                            curr_pos = new_pos
                    elif self.grid[new_pos[0]][new_pos[1]].symbol == 'I':
                        print(f'Before: {player_obj.bag}')
                        print(f'Item found {self.grid[new_pos[0]][new_pos[1]].object}. Congrats')
                        player_obj.bag.append(self.grid[new_pos[0]][new_pos[1]].object)
                        print(f'After: {player_obj.bag}')
                        self.grid[curr_pos[0]][curr_pos[1]] = Grid_square('-', None)
                        self.grid[new_pos[0]][new_pos[1]] = Grid_square('X', player_obj)
                        curr_pos = new_pos
                else:
                    print("Invalid direction. Try again!!!")
            elif direction == 'exit':
                print("Thanks for playing !!!!")
                break
            #not sure
            if len(player_obj.pokemon_list) == 4:
                print("You won the game by collecting 4 pokemon")
                break
            pprint(self.grid)
        return None
 

if __name__ == "__main__":

    my_grid = Grid()
    my_grid.create_grid()

    #my_grid.print_grid()
    item_1 = item(1,"Potion", "Heals 25 percent of health")
    #wild pokemon
    firepunch = moves(1, 'Fire Punch', 10)
    torchic_stats = stats(27, 5)
    torchic = pokemon(1, 'Torchic', 'F', 'Fire', [firepunch], torchic_stats)
    my_grid.grid[3][3] = Grid_square('I', item_1) #item works
    my_grid.grid[1][1] = Grid_square('P', torchic)


    blastoise = pokemon(5, 'Blastoise', 'F', 'Water', [moves(1, 'tackle', 5), moves(2, 'water punch', 15)], stats(27,5))
    mewto = pokemon(6, 'Mewto', 'F', 'Psychic', [moves(1, 'Invisible Punch', 15), moves(2, 'hypnosis', 7)], stats(27, 2))
    trainer = CPU_trainers('Gary', [blastoise, mewto], 10000, blastoise, "Gary became researcher")


    my_grid.grid[1][2] = Grid_square('T', trainer)
    
    item_2 = item(1,"Full Potion", "Heals 100 percent of health")
    #print("Hello")
    watergun = moves(1, 'WaterGun', 1)
    tackle = moves(2, "Tackle", 10)
    squirtle_stats = stats(27, 5)

    #one more added
    charizard = pokemon(2,'Charizard','M','fire',[moves(1,'Flamethrower',20)],stats(30,5))
    pikachu = pokemon(3,'Pikachu','M','Electric',[moves(1,'Dash',20)],stats(30,5))
    squirtle = pokemon(1,'Squirtle','M', 'Water',[watergun, tackle], squirtle_stats)
    player_1 = player('Ash','M','kind', [squirtle, charizard, pikachu],[item_2],10000)
    #print(player_1.bag.item_name)
    pprint(my_grid.play_game([2,2], player_1))
 