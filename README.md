# Final Project
- Put your main function within `main.py`!
- Describe your project here!
- Commit often.
- Push or Sync to submit your work!


## Type Castle - Terminal Game
* For my final project, I decided to make a text-based, turn-based RPG 'roguelite' terminal game. After learning about Object-Oriented Programming, I thought that Classes would be a useful tool for creating games that have different types of enemies with different stats and behaviors. With that in mind, I had the idea to create a turn-based RPG with randomized enemies and bosses. While thinking about different turn-based RPGs and how to implement a similar battle system, I realized that I actually haven't played a lot of RPGs. But from the few (one) I did play (Mario & Luigi Paper Jam), I remembered how much I enjoyed the dodge system. And so, I made it another goal to implement some kind of quick-time-event/ dodge mechanic to make gameplay more active and interesting.

## Game Features
* Game Features:
  - Working menus
  - Combat system
  - Linear dungeon map
  - Shop system
  - Typing quick-time-events
  - Randomized enemies and boss fights
 
## Gameplay

* The main gameplay loop consists of the player entering a "Floor," that contains multiple enemy encounters, shops, and then a boss fight at the end.

* The structure of each floor is linear (as it stands), with the map being:
  BATTLE > SHOP > BATTLE > BOSS FIGHT > SHOP

* In a battle, the player and a random enemy take turns acting. The player can choose to attack the enemy, defend themselves and reduce the amount of incoming damage from the enemy's turn, or view the stats of both the player and enemy.

* Defending isn't the only way to reduce incoming damage however. When an enemy takes its turn and attacks the player, a prompt will appear on the screen. If the player successfully inputs the prompt (must be exactly the same; the input is case-sensitive) before the timer runs out,  the damage will be completely negated. When fighting more difficult enemies and bosses, the prompts will be harder to read and/or type.

* Shops consist of different items to aide the player in future rooms and floors. Normal shops sell items that increase the player's individual stats. Blacksmiths sell special items that can alter gameplay (not yet implemented).
