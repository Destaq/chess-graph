import plotly.graph_objects as go
import chess.pgn, time, random, collections
from collections import Counter

mine = open('pgns/last50.pgn')
mine_short = open('pgns/last5.pgn')
wonder = open('pgns/Carlsen.pgn')
most_games = open('pgns/Korchnoi.pgn')

def create_game_list(pgn, depth):
    ''' we have one massive pgn that we convert to a list of normal game pgns '''
    game_list = []
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None: #continue until exhausted all games
            break
        else:
            if len(list(game.mainline_moves())) > depth-1: #for graph visualization
                game_list.append(game)
    return game_list

def parse_individual_games(pgn, depth):
    ''' convert each game in the list to SAN format '''
    full_list = []
    game_list = create_game_list(pgn, depth)
    for game in game_list:
        small_list = [] #essentially only that game's list
        board = game.board()
        i = 0
        for move in game.mainline_moves():
            if i<depth: #only count moves to needed depth
                i+=1
                small_list.append(chess.Board.san(board, move = move))
                board.push(move)
            else:
                break
        full_list.append(small_list)

    return full_list

def form_values(depth):

    firstx = [lst[i][:depth] for i in range(len(lst))] #probably unneeded but for safety's sake...

    all_level_moves, exclude_first_moves = [], [] #for parent/labels later
    counter = 0
    holder = [firstx[i][0] for i in range(len(firstx))]
    holder = dict(Counter(holder))

    while counter < depth:
        if counter == 0:
            firstmove = list(Counter([tuple(firstx[i][:1]) for i in range(len(lst))]).items()) #list of first ply moves based on popularity
            all_level_moves.append(firstmove)
            counter += 1

        else:
            counter += 1
            othermove = list(Counter([tuple(firstx[i][:counter]) for i in range(len(lst))]).items())
            all_level_moves.append(othermove)
            exclude_first_moves.append(othermove)

    r = 0
    labels = []
    pz = []
    true_ids, truu_ids = [], []

    # all_level_moves works well, it displays the proper amount to each proper level. Each 'level' has it's own list
    mmmz = []
    labs = []

    for i in range(len(all_level_moves)):
        r += len(all_level_moves[i])

        labs += [all_level_moves[i][f][0][i] for f in range(len(all_level_moves[i]))]
        if i == 0:
            labels += [z[0][0] for z in firstmove]
            true_ids = [all_level_moves[0][r][0] for r in range(len(all_level_moves[0]))]
            true_ids = [item for sublist in true_ids for item in sublist] #functions perfectly
            firstcount = len(labels)
        else:
            #print(labels)
            #print('\n\n',exclude_first_moves,'\n\n')
            #labels += [z[i] for ply_depth in exclude_first_moves[i-1] for z in ply_depth if type(z) == tuple]
            true_ids += [all_level_moves[i][r][0] for r in range(len(all_level_moves[i]))]
            mmmz += [all_level_moves[i][r][0][:len(all_level_moves[i][r][0])-1] for r in range(len(all_level_moves[i]))]

        pz += [z[0][:i] for ply_depth in exclude_first_moves for z in ply_depth]

    parents = ['']*firstcount + mmmz #flattening

    ids = true_ids
    labels = labs
    values = [i[1] for i in firstmove] + [i[1] for move in exclude_first_moves for i in move]

    #print(f'\n\nIDS: {ids}\n\nLABELS: {labels}\n\nPARENTS: {parents}\n\nVALUES: {values}')

    return ids, labels, parents, values


def form(ids, labels, parents, values):
    fig = go.Figure(go.Sunburst(
        ids = ids,
        labels = labels,
        parents = parents,
        values = values,
        branchvalues = 'total', #if children exceed parent, graph will crash
        insidetextorientation = 'horizontal' #text displays PP
    ))
    return fig


lst = parse_individual_games(wonder, 5) #ask for input here

ids, labels, parents, values = form_values(5)

fig = form(ids, labels, parents, values)

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
