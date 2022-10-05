# Constants for game Magician, Warrior, Rogue
LIVES_OF_PLAYER = 3
SCORE = 0
N = 3
HELP = """A turn begins with a player's attack:
 the player chooses a magician(1), a warrior(2), or a rogue(3).
 Enemy selection is automatically selected.
 The sorcerer defeats the warrior. The warrior defeats the robber. The thief defeats the sorcerer.
 After the attack, display the result of the attack - hit, miss, draw. Ties if the same classes are selected.
 Next, the enemy attacks, the user chooses defense - the mechanism is the same.
 After a successful attack, the number of lives of the enemy decreases. The player gets 1 point.
 After a failed defense, the player loses one life.
 When the player runs out of lives, the game ends.
 When the enemy runs out of lives, the player gets an additional +5 points and a new enemy is generated."""
