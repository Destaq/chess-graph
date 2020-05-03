# A Graphical Visualization of Chess Openings
# April 2020

import chess.pgn

def create_game_list(pgn, depth):
    """We have one massive pgn that we convert to a list of normal game pgns"""
    game_list = []
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:  # continue until exhausted all games
            break
        else:
            if len(list(game.mainline_moves())) > depth - 1:  # for graph visualization
                game_list.append(game)
    return game_list


def parse_individual_games(pgn, depth, custom_branching):
    """Convert each game in the list to SAN format"""
    full_list, full_rats = [], []
    game_list = create_game_list(pgn, depth)
    for game in game_list:
        small_list = []  # essentially only that game's list
        board = game.board()
        i = 0
        for move in game.mainline_moves():
            if i < depth:  # only count moves to needed depth
                i += 1
                small_list.append(chess.Board.san(board, move=move))
                board.push(move)
            else:
                break
        full_list.append(small_list)
        full_rats.append(game.headers['Result'])

    kick_depth = 0

    if custom_branching == True:
        a = input('Custom Branching: ')
        a = list(a.split())
        del_list = []
        kick_depth = len(a)
        for i in range(len(full_list)):
            b = full_list[i][0:len(a)]
            if a == b:
                pass
            else:
                del_list.append(i)


        full_list = [full_list[i] for i in range(len(full_list)) if i not in del_list]
        full_rats = [full_rats[i] for i in range(len(full_rats)) if i not in del_list]


    return full_list, full_rats, kick_depth
