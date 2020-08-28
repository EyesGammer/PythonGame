#!/bin/python3

import os

texture_ennemies, texture_player, ground, delim, wall = "\u001b[31mE\u001b[0m", "\u001b[33mX\u001b[0m", "\u001b[36mO\u001b[0m", "\u001b[34m|\u001b[0m", "\u001b[35mW\u001b[0m"

display_map = lambda: {(xx, yy): f"{delim}{ground}{delim}\n" if xx == width - 1 else f"{delim}{ground}" for yy in range(0, width) for xx in range(0, height)}
display_ent = lambda m, pos_ent, texture_ent: {pos: ele.replace(ground, texture_ent) if pos_ent == pos else ele for pos, ele in m.items()}

get_tile = lambda m, pos: [t_val for t_pos, t_val in m.items() if pos == t_pos][0].split("m")[3].split("\u001b")[0]

create_ennemies = lambda ennemies: {e[0]: f"{e[1]}:{e[2]}:{e[3]}:{e[4]}" for e in ennemies}

render_map = lambda m: "".join([element for element in m.values()])

width, height = 20, 20
pos = (0, 0)

ennemies_list = []
ennemies = {}
walls = []

while 1:
    m = display_map()
    m = display_ent(m, pos, texture_player)
    ennemies = create_ennemies(ennemies_list)
    for e_pos, e_inf in ennemies.items():
        m = display_ent(m, e_pos, texture_ennemies)
    for w_pos in walls:
        m = display_ent(m, w_pos, wall)
    renderer = render_map(m)
    e = 1
    actions = { "3": (pos[0] + 1, pos[1]), "1": (pos[0] - 1, pos[1]), "5": (pos[0], pos[1] - 1), "2": (pos[0], pos[1] + 1) }
    os.system("clear")
    print(renderer)
    choose = input("\n1. Left\n2. Bottom\n3. Right\n5. Top\nW. Wall\nE. Ennemi\nN. Nothing\n8. Quit Without Saving\n9. Save and Quit\n[+] Choose: ")
    if choose == "9":
        os.system("clear")
        name = input("[+] Output file name: ")
        with open(f"{name}_ennemies.txt", "w") as output:
            for e in ennemies_list:
                output.write(f"{e[0][0]}:{e[0][1]};{e[1]};{e[2]};{e[3]};{e[4]}\n")
        with open(f"{name}_walls.txt", "w") as output:
            for w in walls:
                output.write(f"{w[0]}:{w[1]}\n")
        exit()
    elif choose == "8":
        exit()
    elif choose not in actions.keys():
        if choose.lower() == "w":
            walls.append(pos)
        elif choose.lower() == "e":
            os.system("clear")
            print("=== Ennemy's informations ===")
            name = input("[+] Ennemy's name (default: Ennemy): ")
            name = "Ennemy" if name == "" else name
            life = input("[+] Ennemy's pv (default: 100): ")
            life = 100 if life == "" else life
            while not str(life).isnumeric():
                os.system("clear")
                print("[!] Error: Please enter number")
                print(f"\n[+] Ennemy's name (default: Ennemy): {name}")
                life = input("[+] Ennemy's pv (default: 100): ")
                life = 100 if life == "" else life
            strength = input("[+] Ennemy's strength (default: 10): ")
            strength = 10 if strength == "" else strength
            while not str(strength).isnumeric():
                os.system("clear")
                print("[!] Error: Please enter number")
                print(f"\n[+] Ennemy's name (default: Ennemy): {name}\n[+] Ennemy's pv (default: 100): {life}")
                strength = input("[+] Ennemy's strength (default: 10): ")
                strength = 10 if strength == "" else strength
            coins = input("[+] Ennemy's killed reward (default: 20): ")
            coins = 20 if coins == "" else coins
            while not str(coins).isnumeric():
                os.system("clear")
                print("[!] Error: Please enter number")
                print(f"\n[+] Ennemy's name (default: Ennemy): {name}\n[+] Ennemy's pv (default: 100): {life}\nEnnemy's strength (default: 10): {strength}")
                coins = input("[+] Ennemy's killed reward (default: 20): ")
                coins = 20 if coins == "" else coins
            ennemies_list.append([pos, name, life, strength, coins])
        elif choose.lower() == "n":
            for i, e in enumerate(ennemies_list):
                if e[0] == pos:
                    ennemies_list.remove(ennemies_list[i])
                    break
            for w in walls:
                if w == pos:
                    walls.remove(w)
                    break
        else:
            input("[!] Error: Please choose action in list...\nENTER to retry")
    else:
        tmp = actions.get(choose)
        pos = tmp if tmp[0] < width and tmp[1] < height and tmp[0] >= 0 and tmp[1] >= 0 else pos
