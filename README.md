# Final Project
- Put your main function within `main.py`!
- Describe your project here!
- Commit often.
- Push or Sync to submit your work!


# Type Castle - Terminal Game
* For my final project, I decided to make a text-based, turn-based RPG 'roguelite' terminal game. 

* Gameplay features:
  - Working menus
  - Battle loop
  - Linear dungeon progression
  - Shop system
  - Typing quick-time-events
  - Randomized enemies and boss fights

* The main gameplay loop consists of the player entering a "Floor," that contains multiple enemy encounters, shops, and then a boss fight at the end.

* The structure of each floor is linear (as it stands), with the map being:
  BATTLE > SHOP > BATTLE > BOSS FIGHT > SHOP

* In a battle, the player and a random enemy take turns acting. The player can choose to attack the enemy, defend themselves and reduce the amount of incoming damage from the enemy's turn, or view the stats of both the player and enemy.

* Defending isn't the only way to reduce incoming damage however. When an enemy takes its turn and attacks the player, a prompt will appear on the screen. If the player successfully inputs the prompt (must be exactly the same; the input is case-sensitive) before the timer runs out,  the damage will be completely negated. When fighting more difficult enemies and bosses, the prompts will be harder to read and/or type.

* Shops consist of different items to aide the player in future rooms and floors. Normal shops sell items that increase the player's individual stats. Blacksmiths sell special items that can alter gameplay (not yet implemented).
