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
            if len(list(game.mainline_moves())) > depth-1:
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
            if i<depth:
                i+=1
                small_list.append(chess.Board.san(board, move = move))
                board.push(move)
            else:
                break
        full_list.append(small_list)
    return full_list

def form(ids, labels, parents, values):
    fig = go.Figure(go.Sunburst(
        ids = ids,
        labels = labels,
        parents = parents,
        values = values,
        branchvalues = 'total', #if children exceed parent, graph will crash
        insidetextorientation = 'horizontal'
    ))
    return fig

def form_values(depth):
    print("here", lst)

    first3 = [lst[i][:depth] for i in range(len(lst))]
    print("yeehaw", first3)

    rids, zids = [], []
    counter = 0
    holder = [first3[i][0] for i in range(len(first3))]
    holder = dict(Counter(holder))
    acceps = list(holder.keys())

    while counter < depth:
        if counter == 0:
            firstmove = list(Counter([tuple(first3[i][:1]) for i in range(len(lst))]).items())
            rids.append(firstmove)
            counter = 1
            acceps = [firstmove[i][0] for i in range(len(acceps))]
            acceps = [item for sublist in acceps for item in sublist]

        else:
            counter+=1
            othermove = list(Counter([tuple(first3[i][:counter]) for i in range(len(lst)) if first3[i][0] in acceps]).items())
            rids.append(othermove)
            zids.append(othermove)

    r = 0
    labels = []
    pz = []
    true_ids, truu_ids = [], []

    # RIDS works well, it displays the proper amount to each proper level. Each 'level' has it's own list
    mmmz = []
    labs = []

    for i in range(len(rids)):
        r += len(rids[i])

        labs += [rids[i][f][0][i] for f in range(len(rids[i]))]
        if i == 0:
            labels += [z[0][0] for z in firstmove]
            true_ids = [rids[0][r][0] for r in range(len(rids[0]))]
            true_ids = [item for sublist in true_ids for item in sublist] #functions perfectly
            firstcount = len(labels)
        else:
            #print(labels)
            #print('\n\n',zids,'\n\n')
            #labels += [z[i] for ply_depth in zids[i-1] for z in ply_depth if type(z) == tuple]
            true_ids += [rids[i][r][0] for r in range(len(rids[i]))]
            mmmz += [rids[i][r][0][:len(rids[i][r][0])-1] for r in range(len(rids[i]))]

        pz += [z[0][:i] for ply_depth in zids for z in ply_depth]

    parents = ['']*firstcount + mmmz #flattening

    ids = true_ids
    labels = labs
    values = [i[1] for i in firstmove] + [i[1] for move in zids for i in move]

    #print(f'\n\nIDS: {ids}\n\nLABELS: {labels}\n\nPARENTS: {parents}\n\nVALUES: {values}')

    return ids, labels, parents, values

lst = parse_individual_games(wonder, 5) #ask for input here

ids, labels, parents, values = form_values(5)

fig = form(ids, labels, parents, values)

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
