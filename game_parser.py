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


def parse_individual_games(pgn, depth):
    """Convert each game in the list to SAN format"""
    full_list = []
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

    return full_list
