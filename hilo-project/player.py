from card import Card
import random


class Player:
    """
    draw method,
    have it remember last card to know if higher or lower,
    have draw funciton in card.py,

    
    
    """

    def __init__(self):

        self.score = 300
        self.value = 0
        self.points = 0


    def start_game(self):
        
        self.display_card = random.randint(1, 13)
        print(f'The card is: {self.display_card}')

        self.get_inputs()
        self.do_updates()
        self.do_outputs()
    
    
    def get_inputs(self):

        self.hol = input('Higher or lower? [h/l] ')
        

            
    def do_updates(self):

        self.second_card = random.randint(1, 13)

        print(f'Next card was: {self.second_card}')

        if self.hol == 'h':

            if self.second_card > self.display_card:
                self.points = 100
                self.score += self.points

            elif self.second_card < self.display_card:
                self.points = 75
                self.score -= self.points
            
            else:
                print('oops, same card :/')

        elif self.hol == 'l':

            if self.second_card < self.display_card:
                self.points = 100
                self.score += self.points

            elif self.second_card > self.display_card:
                self.points = 75
                self.score -= self.points
            
            else:
                print('oops, same card :/')
                


    def do_outputs(self):
        
        print(f'Your score is: {self.score}')
        self.replay = input('Play again? [y/n] ')

        if self.replay == 'y':
            Player()