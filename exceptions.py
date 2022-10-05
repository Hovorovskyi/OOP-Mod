from datetime import datetime

class GameOver(Exception):
    # Exception when the player has run out of lives.
    def __str__(self):
        return "You lost. Game over!"


class EnemyDown(Exception):
    # Exception when the AI has run out of lives.
    def __str__(self):
        return "Enemy down!"


class Score:
    # The logic of recording the player's achievements in a certain file,
    # transmits the name of the player, the result and the exact time
    # when the game ended.
    @staticmethod
    def save_raiting(name, result_of_game, mode):
        time = datetime.now()
        print(f"You have {result_of_game} scores. Congrats!\n")
        with open('scores.txt', "a+") as fp:
            fp.write(f"Name: {name} Scores: {result_of_game} Mode: {mode} | {time}\n")
