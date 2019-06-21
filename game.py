# init tableu des mains (ROCK, PAPER, SCISSORS)
# règle du jeu ?

# initialiser MAX_SCORE à 3
# initialiser score ordi à 0
# initialiser score joueur à 0

# lancer le jeu

# ordinateur fait son choix (random)
# demander au jouer son choix
# comparer les mains
# afficher résultat de la manche (win/lose/draw)
# incrémenter score du gagnant (si pas draw)
# si un joueur atteint MAX_SCORE => Arrete
#   sinon: boucler sur choix ordinateur
import random

class Game:
    CHOICES = ['ROCK', 'PAPER', 'SCISSORS']
    MAX_SCORE = 3
    RULES = {
        'ROCK_PAPER': False,
        'ROCK_SCISSORS': True,
        'PAPER_SCISSORS': False,
        'PAPER_ROCK': True,
        'SCISSORS_PAPER': True,
        'SCISSORS_ROCK': False}

    def __init__(self):
        self.user_score = 0
        self.cpu_score = 0

    def _compare_choices(self, cpu_choice, user_choice):
        if cpu_choice == user_choice:
            print('DRAW :(')
        else:
            rules_key = f'{user_choice}_{cpu_choice}'
            if self.RULES[rules_key]:
                print('WIN :)')
                self.user_score += 1
            else:
                print("LOOSE :''(")
                self.cpu_score += 1
        print(f'USER SCORE : {self.user_score}')
        print(f'COMPUTER SCORE : {self.cpu_score}')

    def play(self):
        while self.user_score < self.MAX_SCORE and self.cpu_score < self.MAX_SCORE:
            cpu_choice = random.choice(self.CHOICES)
            user_choice = None
            while user_choice not in self.CHOICES:
                user_choice = input("What's your choice ? : ")
            print(f'COMPUTER CHOICE : {cpu_choice}')
            self._compare_choices(cpu_choice, user_choice)
        if self.user_score > self.cpu_score:
            print('Congratulations, you won !!!')
        else:
            print('LOOOOOOOOOSER !!!!!!!!!')

if __name__ == '__main__':
    game = Game()
    game.play()
