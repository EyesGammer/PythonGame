# This is a Python Game created by Kumo

To play:
```./game_base.py```

- The game_base.py's script use ennemies.txt, walls.txt, items.txt and player.txt
  1. **player.txt** (Lines) :<br/>
      - player_pos_x:player_pos_y;player_life<br/>
      - player_coins<br/>
      - player_item_identifier:item_inventory_count:item_durability ( Can have infinite items, but delimited by ";" )<br/>

  2. **items.txt** (One item per line) :<br/>
	ItemName:Strength:Health:Durability:Price
  3. **walls.txt** (One position per line) :<br/>
	x:y
  4. **ennemies.txt** (One ennemy per line) :<br/>
	ennemy_pos_x:enemy_pos_y;EnnemyName;ennemy_life;ennemy_strength;ennemy_killed_coins_reward


The **_map.py_** is a script to create **walls.txt** and **ennemies.txt** to play on (this is like a map creator script) :<br/>
  - To play on your maps: move current **ennemies.txt** and **walls.txt** to another folder.
  - Create your own **ennemies.txt** and **walls.txt** using **_map.py_** (that will create: **NameYouChoose_ennemies.txt** and **NameYouChoose_walls.txt**)
  - Move these new 2 txt files to **ennemies.txt** and **walls.txt** on the same directory of **_game_base.py_**
  - Start **game_base.py** and your new map is on


You can modify **items.txt** to create new items.
You can modify **player.txt** to change all player's informations.

Have a good time with this little game :)
