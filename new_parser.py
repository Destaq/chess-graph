import pgn


def parse_games(database, depth, custom_branching, color, name):
    database = open(database)
    pgn_text = database.read()
    database.close()

    color = color.lower()

    games = pgn.loads(pgn_text)

    all_games = []
    all_ratios = []
    kick_depth = 0

    name = name.split(' ')
    #od
    if len(name) >= 2:
        for i in range(len(name)):
            name.append(name[i][0])

    for game in games:
        if color == 'white' or color == 'w':
            other_name = str(game.white)
            other_name = other_name.replace(',', ' ')
            other_name = other_name.replace('  ', ' ')
            other_name = other_name.split(' ')

            if set(other_name).issubset(set(name)):
                if len(game.moves) >= depth+2:
                    all_games.append(game.moves)

        elif color == 'black' or color == 'b':
            other_name = str(game.black)
            other_name = other_name.replace(',', ' ')
            other_name = other_name.replace('  ', ' ')
            other_name = other_name.split(' ')

            if set(other_name).issubset(set(name)):
                if len(game.moves) >= depth+2:
                    all_games.append(game.moves)

        else:
            if name == ['']:
                if len(game.moves) >= depth+2:
                    all_games.append(game.moves)

            else:
                other_name = str(game.white)
                other_name = other_name.replace(',', ' ')
                other_name = other_name.replace('  ', ' ')
                other_name = other_name.split(' ')

                other_name2 = str(game.black)
                other_name2 = other_name2.replace(',', ' ')
                other_name2 = other_name2.replace('  ', ' ')
                other_name2 = other_name2.split(' ')

                if set(other_name).issubset(set(name)) or set(other_name2).issubset(set(name)):
                    if len(game.moves) >= depth+2:
                        all_games.append(game.moves)


    for i in range(len(all_games)):
        all_games[i].pop(-2)
        all_ratios.append(all_games[i][-1])
        all_games[i].pop(-1)

    if custom_branching:
        a = input('Custom Branching: ')
        a = list(a.split())

        del_list = []
        kick_depth = len(a)

        for i in range(len(all_games)):
            b = all_games[i][0:len(a)]
            if a == b:
                pass
            else:
                del_list.append(i)


        all_games = [all_games[i] for i in range(len(all_games)) if i not in del_list]
        all_ratios = [all_ratios[i] for i in range(len(all_ratios)) if i not in del_list]

    return all_games, all_ratios, kick_depth
