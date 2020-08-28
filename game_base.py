#!/bin/python3

import os

with open("player.txt", "r") as player_file:
    player_content = player_file.readlines()

with open("items.txt", "r") as items_file:
    items_content = items_file.readlines()

with open("ennemies.txt", "r") as ennemies_file:
    ennemies_content = ennemies_file.readlines()

with open("walls.txt", "r") as walls_file:
    walls_content = walls_file.readlines()

texture_ennemies, texture_player, ground, delim, wall = "\u001b[31mE\u001b[0m", "\u001b[33mX\u001b[0m", "\u001b[36mO\u001b[0m", "\u001b[34m|\u001b[0m", "\u001b[35mW\u001b[0m"
back_slash = '\n'

player_infos_ffile = lambda player_content: [player_content[0].strip("\n").split(";"), int(player_content[1].strip("\n")), player_content[2].strip("\n").split(";")]
format_player_items_list = lambda player_list: {int((x := item.strip("\n").split(":"))[0]): [int(x[1]), int(x[2])] for item in player_list}
create_player_items = lambda player_list, items_list: {i_name: [i_inf[0], player_list.get(i)[1], player_list.get(i)[0], i_inf[2]] for i, (i_name, i_inf) in enumerate(items_list.items()) if i in player_list.keys()}
get_player_items = lambda p_items, items: ";".join([f"{i}:{p_items.get(i_name)[2]}:{p_items.get(i_name)[1]}" for i, (i_name, i_inf) in enumerate(items.items()) if i_name in p_items.keys()])

display_map = lambda: {(xx, yy): f"{delim}{ground}{delim}\n" if xx == width - 1 else f"{delim}{ground}" for yy in range(0, width) for xx in range(0, height)}
display_ent = lambda m, pos_ent, texture_ent: {pos: ele.replace(ground, texture_ent) if pos_ent == pos else ele for pos, ele in m.items()}

box_collider = lambda pos, ent: [1 for e in ent if pos == e]
check_ennemi = lambda pos, enn: {1: e_pos for e_pos, e_inf in enn.items() if e_pos in pos}

render_map = lambda m: "".join([element for element in m.values()])

create_ennemies = lambda ennemies: {e[0]: f"{e[1]}:{e[2]}:{e[3]}:{e[4]}" for e in ennemies}
get_ennemi = lambda pos_e, ennemies: [[i for i, (e_pos) in enumerate(ennemies.keys()) if e_pos == pos_e][0], [e_inf.split(":") for e_pos, e_inf in ennemies.items() if e_pos == pos_e][0]]
ennemies_box_collider = lambda pos, ennemies: [1 for e_pos, e_inf in ennemies.items() if pos == e_pos]
ennemie_killed = lambda identifier, ennemies_list: [e for i, e in enumerate(ennemies_list) if i != identifier]
ennemies_infos_ffile = lambda e: [(int(e[0].split(":")[0]), int(e[0].split(":")[1])), e[1], int(e[2]), int(e[3]), int(e[4])]

items_infos_ffile = lambda items_content: {(x := item.strip("\n").split(":"))[0]: [int(x[1]), int(x[3]), int(x[2]), int(x[4])] for item in items_content}
print_p_items = lambda p_items: "\n".join([f"{i}. {i_inf[2]}x {i_name}: {f'P{i_inf[0]}' if i_inf[0] != 0 else f'H{i_inf[3]}'} D{i_inf[1]}" for i, (i_name, i_inf) in enumerate(p_items.items())])
get_item_stats = lambda item_name, p_items: [i_inf for i_name, i_inf in p_items.items() if item_name.lower() == i_name.lower()][0]
get_item_durability = lambda item_name, items: [i_inf[1] for i_name, i_inf in items.items() if i_name.lower() == item_name.lower()][0]

print_store = lambda store_items: "\n".join([f"{i_inf[0][2]}x {i_name}: {f'P{i_inf[0][0]}' if i_inf[0][0] != 0 else f'H{i_inf[0][3]}'} D{i_inf[0][1]} for {i_inf[1]} Coins" for i_name, i_inf in store_items.items()])
create_store_items = lambda items_list: {i_name: ([i_inf[0], i_inf[1], 1, i_inf[2]], i_inf[3]) for i_name, i_inf in items_list.items()}

create_walls = lambda walls_content: [(int(w.split(":")[0]), int(w.strip("\n").split(":")[1])) for w in walls_content]

player = player_infos_ffile(player_content)
items = items_infos_ffile(items_content)
player_items_list = create_player_items(format_player_items_list(player[2]), items)
store_items_list = create_store_items(items)

width, height = 20, 20
p_x, p_y = player[0][0].split(":")
pos, p_pv, p_po = (int(p_x), int(p_y)), int(player[0][1]), 0
p_items = player_items_list
p_coins = player[1]

ennemies_list = []
for e in ennemies_content:
    tmp = e.split(";")
    ennemies_list.append(ennemies_infos_ffile(tmp))
walls_list = create_walls(walls_content)
store_items = store_items_list

while 1:
    player = [pos, p_pv, p_po]
    entities = [ennemies_list, walls_list]
    ennemies, walls = entities
    ennemies = create_ennemies(ennemies)
    m = display_map()
    m = display_ent(m, pos, texture_player) # Player
    for xx in walls:
        m = display_ent(m, xx, wall) # Walls
    for e_pos, e_inf in ennemies.items():
        m = display_ent(m, e_pos, texture_ennemies) # Ennemies
    m = render_map(m)
    actions = { 3: (pos[0] + 1, pos[1]), 1: (pos[0] - 1, pos[1]), 5: (pos[0], pos[1] - 1), 2: (pos[0], pos[1] + 1), 4: "", 6: "", 7: "", 8: "", 9: "" }
    useless = 5
    e = 1
    while e:
        try:
            os.system("clear")
            print(f"=== Player's stats: ===\nLife: {p_pv}\nCoins: {p_coins}\n")
            print(m)
            attack = 1 if 1 in (pos_e := check_ennemi([xx for xx in actions.values()][:-useless], ennemies)).keys() else 0
            print_attack = "4. Attack\n" if attack else ""
            choose = int(input(f"\n1. Left\n2. Bottom\n3. Right\n5. Top\n{print_attack}6. Use item\n7. Store\n8. Quit without saving\n9. Save and Quit\n[+] Choose: "))
            e = 0 if choose in actions.keys() else 1
        except Exception:
            e = 1
    if choose == 9:
        with open("ennemies.txt", "w") as output:
            for e in ennemies_list:
                output.write(f"{e[0][0]}:{e[0][1]};{e[1]};{e[2]};{e[3]};{e[4]}\n")
        with open("walls.txt", "w") as output:
            for w in walls:
                output.write(f"{w[0]}:{w[1]}\n")
        with open("player.txt", "w") as output:
            output.write(f"{pos[0]}:{pos[1]};{p_pv}\n{p_coins}\n{get_player_items(p_items, items)}\n")
        exit()
    elif choose == 8:
        exit()
    elif choose == 7:
        while 1:
            os.system("clear")
            print("=== Store ===\n")
            print(f"=== Player's stuff: ===\n{print_p_items(p_items)}\n")
            print(f"=== Player's coins: {p_coins} ===\n")
            print(f"=== Store's items ===\n{print_store(store_items)}\n")
            item_choose = input("[+] Choose item to buy (name) or nothing to return: ")
            if item_choose == "":
                break
            if item_choose.lower() in [item.lower() for item in store_items.keys()]:
                for i_name, i_inf in store_items.items():
                    if i_name.lower() == item_choose.lower():
                        if p_coins - i_inf[1] >= 0:
                            p_coins -= i_inf[1]
                            if type(p_items.get(i_name)) != type(None):
                                item = get_item_stats(i_name, p_items)
                                p_items[i_name] = [item[0], item[1], item[2] + 1, item[3]]
                            else:
                                p_items[i_name] = i_inf[0]
                            input(f"[+] You successfully bought '{i_name}'\nENTER to continue")
                        else:
                            input(f"\n[!] You don't have enought money to buy: {i_name}\nENTER to continue")
                        break
            elif item_choose.lower() not in [item.lower() for item in store_items.keys()]:
                input("\nError: Item not in the list...\nENTER to retry")
    elif choose == 6:
        while 1:
            os.system("clear")
            print("=== Use an item ===\n")
            print(f"=== Player's stuff: ===\n{print_p_items(p_items)}\n")
            item_choose = input("[+] Choose item to use (name) or nothing to return: ")
            if item_choose == "":
                break
            if item_choose.lower() in [item.lower() for item in p_items.keys()]:
                i_strong, i_durability, i_count, i_health = get_item_stats(item_choose, p_items)
                if i_health != 0:
                    p_pv += i_health
                    i_durability -= 1
                    for i_name in p_items.keys():
                        if i_name.lower() == item_choose.lower():
                            tmp_i_count = i_count
                            i_count -= 1 if i_durability == 0 else 0
                            if i_count == 0:
                                p_items.pop(i_name)
                            else:
                                item_durability = get_item_durability(item_choose, items)
                                i_durability = item_durability if tmp_i_count - 1 == i_count else i_durability
                                p_items[i_name] = [i_strong, i_durability, i_count, i_health]
                            break
                    input("\n[+] Item used successfully...\nENTER to continue ")
                else:
                    print(f"\n[!] Error: You can't use '{item_choose}'")
                    break
            elif item_choose.lower() not in [item.lower() for item in p_items.keys()]:
                input("\n[!] Error: Item not in the list...\nENTER to retry")
    elif choose == 4:
        if attack:
            pos_e = pos_e.get(1)
            id_ennemi, actual_ennemi = get_ennemi(pos_e, ennemies)
            e_name, e_pv, e_strong, e_coins = actual_ennemi
            e_pv, e_strong, e_coins = int(e_pv), int(e_strong), int(e_coins)
            escape, switch, die, tmp_p_po = 0, 0, ("", 0), 0
            while 1:
                item_choose = "e"
                while not item_choose.isnumeric():
                    os.system("clear")
                    print(f"=== An ennemi attack the player: {e_name} ===\nPower: {e_strong}\nLife: {e_pv}\n")
                    print(f"=== Player's stats: ===\n{f'Power: {tmp_p_po}{back_slash}' if tmp_p_po != 0 else ''}Life: {p_pv}\nCoins: {p_coins}\n")
                    print(f"=== Player's stuff: ===\n{print_p_items(p_items)}\n")
                    item_choose = input("[+] E to escape, or choose item (number): ")
                    if not item_choose.isnumeric() and item_choose.lower() == "e":
                        break
                    elif not item_choose.isnumeric() and not item_choose.lower() == "e":
                        input("\n[!] Error: Please enter item's number...\nENTER to retry")
                if item_choose.lower() == "e":
                    escape = 1
                    break
                elif int(item_choose) in [i for i, item in enumerate(p_items.keys())]:
                    item_choose = [i_name for i, i_name in enumerate(p_items.keys()) if i == int(item_choose)][0]
                    i_strong, i_durability, i_count, i_health = get_item_stats(item_choose, p_items)
                    tmp_p_po = i_strong
                    e_pv -= i_strong
                    i_durability -= 1
                    if i_health != 0:
                        p_pv += i_health
                    p_pv -= e_strong if e_pv > 0 else 0
                    for i_name, i_inf in p_items.items():
                        if i_name.lower() == item_choose.lower():
                            tmp_i_count = i_count
                            i_count -= 1 if i_durability == 0 else 0
                            if i_count == 0:
                                p_items.pop(i_name)
                            else:
                                item_durability = get_item_durability(item_choose, items)
                                i_durability = item_durability if tmp_i_count - 1 == i_count else i_durability
                                p_items[i_name] = [i_strong, i_durability, i_count, i_health]
                            break
                    if p_pv <= 0:
                        die = (f"\n[-] You have been killed by: {e_name}", 1)
                    elif e_pv <= 0:
                        die = (f"\n[+] You killed {e_name} and you get {e_coins} coins", 2)
                        p_coins += e_coins
                elif int(item_choose) not in [i for i, item in enumerate(p_items.keys())]:
                    input("\n[!] Error: Item not in the list...\nENTER to retry")
                if die != ("", 0):
                    print(die[0])
                    if die[1] == 1:
                        exit()
                    else:
                        ennemies_list = ennemie_killed(id_ennemi, ennemies_list)
                    break
            if escape:
                input("[+] You just escaped...\nPress ENTER to continue ")
    else:
        tmp = actions.get(choose)
        tmp_walls = tmp if tmp[0] < width and tmp[1] < height and tmp[0] >= 0 and tmp[1] >= 0 else pos
        pos = tmp_walls if 1 not in box_collider(tmp, walls) and 1 not in ennemies_box_collider(tmp, ennemies) else pos
