import exceptions
import settings
import models


def play():
    # Starts the logic of the game, creates objects with which the code will work.
    try:
        # Check for the correctness of data entry, and conditions for
        # the end of the game. And you can change game mod.
        name = input("\nInput you`re name: ")
        print("\nLet`s start the game.")
        print("You can change game mod.")
        game_mod = input("Enter Normal or Hand: ")
        print("""You can change one of heroes:
                1 ---> is Magician, he beats the warrior;
                2 ---> is Warrior, he beats the rogue;
                3 ---> is Rogue, he beats the magician\n""")
        input("Click Enter to continue\n")
        player = models.Player(name)
        level_enemy = 1
        enemy = models.Enemy(level_enemy)
        if game_mod.lower() == "normal":
            while True:
                print("\nLife left: ")
                print(f"Player: {player.lives}")
                print(f"Enemy: {enemy.lives}\n")
                pl_score = player.score
                models.Player.attack(player, enemy)
                if enemy.lives == 0:
                    level_enemy += 1
                    enemy = models.Enemy(level_enemy)
                    player.lives += 5
                models.Player.defence(player, enemy)
                if player.lives == 0:
                    print(exceptions.GameOver())
                    exceptions.Score.save_raiting(name, pl_score, game_mod)
                    input("Click Enter to continue")
                    game()
        elif game_mod.lower() == "hard":
            enemy.lives = enemy.lives * settings.N
            while True:
                print("\nLife left: ")
                print(f"Player: {player.lives}")
                print(f"Enemy: {enemy.lives}\n")
                pl_score = player.score*settings.N
                models.Player.attack(player, enemy)
                if enemy.lives == 0:
                    level_enemy += 1
                    enemy = models.Enemy(level_enemy)
                    enemy.lives = enemy.lives * settings.N
                    player.lives += 5
                models.Player.defence(player, enemy)
                if player.lives == 0:
                    print(exceptions.GameOver())
                    exceptions.Score.save_raiting(name, pl_score, game_mod)
                    input("Click Enter to continue")
                    game()
        else:
            print("Please, enter only Normal or Hard")
            play()
    except Exception:
        print("Something exception. Watch on code.")



def game():
    # Issues which commands the player can use and checks
    # the text for correct input.
    print("""Hello, master!
    You can change the command:
        start       --->    if you want start game
        show scores --->    if you want to see player rating
        help        --->    if you want to see all rules and commands
        exit        --->    if you want finish game""")
    print("_____________________________________________________________________\n")
    try:
        command = input("Input command: ")
        if command.lower() == 'start':
            play()
        elif command.lower() == 'show scores':
            with open("scores.txt") as fp:
                print(fp.read())
            input("Click Enter to continue\n")
            game()
        elif command.lower() == 'help':
            print("\n", settings.HELP)
            print("_________________________________________")
            input("Click Enter to continue\n")
            game()
        elif command.lower() == 'exit':
            print("\n", exceptions.GameOver(), "\n")
            print("_________________________________________")
        else:
            print("!!!Please, change one of standard command.!!!")
            game()
    except exceptions.GameOver:
        print(exceptions.GameOver())
    except KeyboardInterrupt:
        pass
    finally:
        print("\n Good bye! \n")

if __name__ == '__main__':
    game = game()
