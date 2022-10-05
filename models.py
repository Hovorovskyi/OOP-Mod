import random
import settings

class Enemy:
    # The artificial intelligence class for the game,
    # it is given a level equal to the number of lives the computer has.
    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_method():
        # Returns a random number that is matched against the player.
        return random.randint(1, 3)

    def decrease_lives(self):
        # Reduces the number of lives in the AI.
        self.lives -= 1

class Player:
    # The class of the player to which the name is passed.
    # In the class, the logic of the battle of the player with AI is implemented.
    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES_OF_PLAYER
        self.score = settings.SCORE

    @staticmethod
    def input_validation(text_input: str) -> int:
        # Validation of dates to numbers and verification of data entry.
        # The player must enter only 1, 2 or 3.
        while True:
            number = input(text_input)
            if number == '1':
                return 1
            elif number == '2':
                return 2
            elif number == '3':
                return 3
            else:
                print("Please, input one of this number: 1, 2, 3")


    @staticmethod
    def fight(attack, defence):
        # Implementation of the battle.
        if attack == defence:
            return 0
        elif (attack == 1 and defence == 2 or
              attack == 2 and defence == 3 or
              attack == 3 and defence == 1):
            return 1
        else:
            return -1

    def decrease_lives(self):
        # Reduces the number of lives in the player.
        self.lives -= 1

    def attack(self, enemy_obj: Enemy):
        # Battle logic if a player attacks and outputs a text result.
        attack_player = Player.input_validation("Select attack: ")
        result = self.fight(attack_player, enemy_obj.select_method())
        if result == 0:
            print("\nIt`s a draw!\n")
        elif result == 1:
            print("\nYou attacked successfully!\n")
            self.score += 1
            enemy_obj.decrease_lives()
        elif result == -1:
            print("\nYou missed!\n")

    def defence(self, enemy_obj: Enemy):
        # Battle logic if a player defence and outputs a text result.
        attack_player = Player.input_validation("Select defence: ")
        result = self.fight(enemy_obj.select_method(), attack_player)
        if result == 0:
            print("\nIt`s a draw!\n")
        elif result == 1:
            print("\nYou missed!\n")
            self.decrease_lives()
        elif result == -1:
            print("\nYou defence successfully!\n")
