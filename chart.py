# A Graphical Visualization of Chess Openings
# April 2020

# Provides a colorful multi-level pie chart which shows the popularity of openings after moves
# For more info, go to www.github.com/Destaq/chess_graph


import plotly.graph_objects as go
from collections import Counter
import new_parser
import find_opening

import pandas as pd
import numpy as np



def form_values(gammme, depth, fragmentation_percentage, should_defragment, custom_branching, color, name):
    """Create parent, id, labels, and values """
    lst, ratios, kick_depth = new_parser.parse_games(gammme, depth, custom_branching, color, name) #whether or not to implement custom branching
    firstx = [
        lst[i][:depth+kick_depth] for i in range(len(lst))
    ]  # probably unneeded but for safety's sake...

    all_level_moves, exclude_first_moves = [], []  # for parent/labels later
    counter = kick_depth
    holder = [firstx[i][0] for i in range(len(firstx))]
    holder = dict(Counter(holder))

    percentage_holder, firstmove = [], []

    while counter < depth + kick_depth:
        counter += 1
        othermove = list(
            Counter([tuple(firstx[i][kick_depth:counter]) for i in range(len(lst))]).items()
        )
        all_level_moves.append(othermove)
        exclude_first_moves.append(
            othermove
        )  # obviously excluding first moves (for parent creation)
    pz = []
    true_ids = []  # the ids, that is
    parents = []
    labels = []

    for i in range(len(all_level_moves)):

        if i == 0:
            true_ids = [
                all_level_moves[0][r][0] for r in range(len(all_level_moves[0]))
            ]  # special ids for original parents
            true_ids = [
                item for sublist in true_ids for item in sublist
            ]  # functions perfectly
            labels += [
                all_level_moves[i][f][0][0] for f in range(len(all_level_moves[i]))
            ]  # similar to hackerrank diagonal
            firstcount = len(labels)
        else:
            labels += [
                all_level_moves[i][f][0][i] for f in range(len(all_level_moves[i]))
            ]  # similar to hackerrank diagonal
            true_ids += [
                all_level_moves[i][r][0] for r in range(len(all_level_moves[i]))
            ]
            parents += [
                all_level_moves[i][r][0][: len(all_level_moves[i][r][0]) - 1]
                for r in range(len(all_level_moves[i]))
            ]

        pz += [z[0][:i] for ply_depth in exclude_first_moves for z in ply_depth]

    parents = [""] * firstcount + parents  # flattening

    ids = true_ids
    values = [i[1] for i in firstmove] + [
        i[1] for move in exclude_first_moves for i in move
    ]

    game_count = 0

    for i in range(len(values)):
        if parents[i] == "":
            game_count += values[i]

    for i in range(len(values)):  # e.g e6 has 50, parent e4, with value 100
        if parents[i] != "":  # each child has parent, this one is e4 so yes
            parent_id = parents[i]  # parent id = e4
            aka = list(parent_id)
            if len(aka) >= 2:
                aka = tuple(aka)
            else:
                aka = "".join(aka)

            parent_value = ids.index(aka)
            parent_value = values[parent_value]
            complete_value = round((values[i] / parent_value) * 100, 2)
            percentage_holder.append(complete_value)
        else:
            complete_value = round((values[i] / game_count) * 100, 2)
            percentage_holder.append(complete_value)

    num_games = 0
    for i in range(len(parents)):
        if parents[i] == '':
            num_games+=values[i]

    if should_defragment == True:
        del_list = []
        for i in range(len(values)):
            if values[i]/num_games <= fragmentation_percentage:
                del_list.append(i)

        percentage_holder = [percentage_holder[i] for i in range(len(percentage_holder)) if i not in del_list]
        ids = [ids[i] for i in range(len(ids)) if i not in del_list]
        labels = [labels[i] for i in range(len(labels)) if i not in del_list]
        parents = [parents[i] for i in range(len(parents)) if i not in del_list]
        values = [values[i] for i in range(len(values)) if i not in del_list]

    return ids, labels, parents, values, percentage_holder, lst, ratios, kick_depth

# fig = form(ids, labels, parents, values, full_ratios, full_ratios, percentage_everything, hovertip_openings, shade)
def form(ids, labels, parents, values, colors, ratios, percentage_everything, hovertip_openings, shade):
    if shade:
        fig = go.Figure(
            go.Sunburst(
                ids=ids,
                labels=labels,
                parents=parents,
                values=values,
                marker = dict(
                        colors = colors,
                        colorscale = 'Greys_r',
                        colorbar = dict(
                                    thickness = 20,
                                    title = dict(
                                            text = 'White/Black Winning Percentage',
                                            side = 'right'
                                            )
                                    )
                        ),
                leaf = {
                        'opacity': 1.0
                        },
                branchvalues="total",  # if children exceed parent, graph will crash and not show
                insidetextorientation="horizontal",  # text displays PP
                hovertext=[
                    str(percentage_everything[i])
                    + "% of Parent<br>Game Count: "
                    + str(values[i])
                    + '<br>Opening: '
                    + hovertip_openings[i]
                    + '<br>W/B Winning Percentage: ' # Note: this is wins+1/2draws/wins+losses+draws
                    + str(ratios[i])
                    for i in range(len(percentage_everything))
                ],
                hovertemplate="%{hovertext}<extra></extra>",
            )
        )
        fig.update_layout(
            margin=dict(t=30, l=30, r=30, b=0),
            title = {
                'text': "The Chess Opening Graph",
                'xanchor': 'center',
                'y':0.995,
                'x':0.4715,
                'yanchor': 'top',
                'font': {
                    'size': 25
                        }
                })
    else:
        fig = go.Figure(
            go.Sunburst(
                ids=ids,
                labels=labels,
                parents=parents,
                values=values,
                leaf = {
                        'opacity': 1.0
                        },
                branchvalues="total",  # if children exceed parent, graph will crash and not show
                insidetextorientation="horizontal",  # text displays PP
                hovertext=[
                    str(percentage_everything[i])
                    + "% of Parent<br>Game Count: "
                    + str(values[i])
                    + '<br>Opening: '
                    + hovertip_openings[i]
                    + '<br>W/B Winning Percentage: ' # Note: this is wins+1/2draws/wins+losses+draws
                    + str(ratios[i])
                    for i in range(len(percentage_everything))
                ],
                hovertemplate="%{hovertext}<extra></extra>",
            )
        )
        fig.update_layout(
            margin=dict(t=30, l=30, r=30, b=0),
            title = {
                'text': "The Chess Opening Graph",
                'xanchor': 'center',
                'y':0.995,
                'x':0.50,
                'yanchor': 'top',
                'font': {
                    'size': 25
                        }
                })

    return fig #nasty thing should be fixed by autopep8

def find_colors(ids, ratios, lst, kick_depth):
    holder = []
    for i in range(len(ids)):
        if type(ids[i]) != str:
            holder.append(list(ids[i]))
        else:
            holder.append(list(ids[i].split(' ')))

    lst = [lst[i][kick_depth:] for i in range(len(lst))]
    white_list = [0]*len(holder)
    black_list = [0]*len(holder)
    draw_list = [0]*len(holder)
    for i in range(len(holder)):
        a = len(holder[i])
        for r in range(len(lst)):
            if lst[r][:a] == holder[i]:
                if ratios[r] == '1-0':
                    white_list[i] += 1
                elif ratios[r] == '0-1':
                    black_list[i] += 1
                else:
                    draw_list[i] += 1

    full_ratios = []
    for i in range(len(white_list)):

        result = round((white_list[i]+draw_list[i])/(black_list[i]+white_list[i]+draw_list[i]+draw_list[i]), 3)

        full_ratios.append(result)

    return full_ratios


def best_worst(ids, labels, parents, values, percentage_everything, full_ratios, min_games_best_lines):

    df = pd.DataFrame()

    df['ids'] = ids
    df['labels'] = labels
    df['parents'] = parents
    df['values'] = values
    df['percentage_everything'] = percentage_everything
    df['full_ratios'] = full_ratios

    def semimove_number(l):
        a=len(l.parents)+1
        return a

    tmp = df.apply(semimove_number, axis=1)
    tmp = tmp.to_frame()
    tmp.columns = ['semimove']
    
    df['semimove'] = tmp['semimove']
    
    
    best_worst = pd.DataFrame(columns=['move', 'Best', 'b_score', 'b_games', 'Worst', 'w_score', 'w_games'])

    for i in np.unique(df.semimove):
        semimove_df = df[(df.semimove == i) & (df['values'] >= min_games_best_lines)]
    
        if (len(semimove_df) > 0):
            semimove_df = semimove_df.sort_values('full_ratios', ascending=False)
            best = semimove_df.head(1)
            worst = semimove_df.tail(1)
        
            move = semimove_df.semimove.values[0]
            Best = best['ids'].values[0]
            b_score = best['full_ratios'].values[0]
            b_games = best['values'].values[0]
            Worst = best['ids'].values[0]
            w_score = worst['full_ratios'].values[0]
            w_games = worst['values'].values[0]
    
            best_worst.loc[len(best_worst)] = [move, Best, b_score, b_games, Worst, w_score, w_games] 
    
        else:
            out_warning = 'No lines at move ' + str(i) + ' with at least ' + str(min_games_best_lines) + ' games'
            print(out_warning)

    print('\n')
    print(best_worst)

def graph(database, depth=5, shade = True, fragmentation_percentage=0.0032, should_defragment=False, custom_branching=False, should_download = False, download_format = 'png', download_name = 'fig1', color = 'both', name = '', print_best_lines=False, min_games_best_lines=1): # need file path, depth,

    ids, labels, parents, values, percentage_everything, lst, ratios, kick_depth = form_values(database, depth, fragmentation_percentage, should_defragment, custom_branching, color, name) # a good value is about 10x the smallest value

    full_ratios = find_colors(ids, ratios, lst, kick_depth)

    eco_codes, eco_names, eco_positions = find_opening.create_openings()
    hovertip_openings = []

    for i in range(len(ids)):
        if ids[i] in eco_positions:
            analyzed = eco_positions.index(ids[i])
            hovertip_openings.append(eco_names[analyzed])
        else:
            hovertip_openings.append('Non-ECO Opening')

    fig = form(ids, labels, parents, values, full_ratios, full_ratios, percentage_everything, hovertip_openings, shade)

    fig.show()

    def download(format, name = 'fig1'):
        fig.write_image(name+'.'+format)

    def download_html(name = 'fig1'):
        fig.write_html(name+'.html')

    static_download_formats = ['png', 'jpeg', 'svg', 'pdf', 'jpg', 'webp']

    if should_download == True:
        if download_format in static_download_formats:
            download(download_format, download_name)
        else:
            download_html(download_name)
            
    if print_best_lines == True:
        best_worst(ids, labels, parents, values, percentage_everything, full_ratios, min_games_best_lines)
