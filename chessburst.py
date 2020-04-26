import plotly.graph_objects as go
import chess.pgn, time, random
from collections import Counter

mine = open('last50.pgn')
mine_short = open('last5.pgn')
wonder = open('Carlsen.pgn')

def create_game_list(pgn):
    ''' we have one massive pgn that we convert to a list of normal game pgns '''
    game_list = []
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None: #continue until exhausted all games
            break
        else:
            game_list.append(game)
    return game_list

def parse_individual_games(pgn):
    ''' convert each game in the list to SAN format '''
    full_list = []
    game_list = create_game_list(pgn)
    for game in game_list:
        small_list = [] #essentially only that game's list
        board = game.board()
        i = 0
        for move in game.mainline_moves():
            if i<3:
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
        branchvalues = 'total' #if children exceed parent, graph will crash
    ))
    return fig

def form_values():

    first3 = [lst[i][:3] for i in range(len(lst))]

    secondmove = list(Counter([tuple(first3[i][:2]) for i in range(len(lst)) if first3[i][0] == 'e4']).items())
    thirdmove = list(Counter([tuple(first3[i][:2]) for i in range(len(lst)) if first3[i][0] == 'd4']).items())
    rids = []
    counter = 0
    acceps = ['e4', 'd4']
    for i in range(len(first3)):
        if counter == 0:
            firstmove = list(Counter([tuple(first3[i][:1]) for i in range(len(lst))]).items())
            rids.append(firstmove)
            counter = 1
            acceps = [firstmove[i][0] for i in range(len(acceps))]
            acceps = [item for sublist in acceps for item in sublist]
            print(acceps)
        if counter == 1:
            secondmove = list(Counter([tuple(first3[i][:2]) for i in range(len(lst)) if first3[i][0] in acceps]).items())
            rids.append(secondmove)
            break


    r = 0
    for i in range(len(rids)):
        r += len(rids[i])


    ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    labels = [i[0] for i in firstmove] + [i[0][1] for i in secondmove]# + [i[0][1] for i in thirdmove]
    parents = [""]*len(firstmove) + [""]*len(secondmove)# + ['a']*len(thirdmove)
    values = [i[1] for i in firstmove] + [i[1] for i in secondmove]# + [i[1] for i in thirdmove]

    return ids, labels, parents, values

## NOTE:  for repeated labels, all you have to do is change the ID of the label e.g fig = go.figure. etc... (ids = 'joe', labels = 'what's displayed)

lst = parse_individual_games(mine) #ask for input here

ids, labels, parents, values = form_values()

fig = form(ids, labels, parents, values)

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
