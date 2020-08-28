This is a Python Game created by Innocent1 (EyesGammer)

To play:
	./game_base.py

- The game_base.py's script use ennemies.txt, walls.txt, items.txt and player.txt

-- player.txt ( by lines ):<br/>
	1: player_pos_x:player_pos_y;player_life<br/>
	2: player_coins<br/>
	3: player_item_identifier:item_inventory_count:item_durability ( Can have infinite items, but delimited by ";" )<br/>

-- items.txt:<br/>
	ItemName:Strength:Health:Durability:Price
= One item per line

-- walls.txt:<br/>
	x:y
= One pos per line

-- ennemies.txt:<br/>
	ennemy_pos_x:enemy_pos_y;EnnemyName;ennemy_life;ennemy_strength;ennemy_killed_coins_reward
= One ennemy per line


The map.py is a script to create walls.txt and ennemies.txt to play on ( this is a map creator like script ):<br/>
  -> To play on your maps: move current ennemies.txt and walls.txt to another folder.<br/>
  -> Create your own ennemies.txt and walls.txt using map.py ( that will create: NameYouChoose_ennemies.txt and NameYouChoose_walls.txt )<br/>
  -> Move these new 2 txt files to ennemies.txt and walls.txt on the same directory of game_base.py<br/>
  -> Start game_base.py and your new map is on<br/>


You can modify items.txt to create new items.
You can modify player.txt to change all player's informations.

Have a good game
