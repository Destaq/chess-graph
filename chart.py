# A Graphical Visualization of Chess Openings
# April 2020

# Provides a colorful multi-level pie chart which shows the popularity of openings after moves
# For more info, go to www.github.com/Destaq/opening_analysis


# TODO: better custom branching visualization

import plotly.graph_objects as go
from collections import Counter
import game_parser
import find_opening


def form_values(gammme, depth, fragmentation_percentage, should_defragment, custom_branching):
    lst, ratios, kick_depth = game_parser.parse_individual_games(gammme, depth, custom_branching) #whether or not to implement custom branching
    """Create parent, id, labels, and values """
    firstx = [
        lst[i][:depth] for i in range(len(lst))
    ]  # probably unneeded but for safety's sake...

    all_level_moves, exclude_first_moves = [], []  # for parent/labels later
    counter = 0
    holder = [firstx[i][0] for i in range(len(firstx))]
    holder = dict(Counter(holder))

    percentage_holder, firstmove = [], []

    while counter < depth:
        if counter == 0:
            firstmove = list(
                Counter([tuple(firstx[i][:1]) for i in range(len(lst))]).items()
            )  #  list of first ply moves based on popularity
            all_level_moves.append(firstmove)
            counter += 1

        else:
            counter += 1
            othermove = list(
                Counter([tuple(firstx[i][:counter]) for i in range(len(lst))]).items()
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
        labels += [
            all_level_moves[i][f][0][i] for f in range(len(all_level_moves[i]))
        ]  # similar to hackerrank diagonal

        if i == 0:
            true_ids = [
                all_level_moves[0][r][0] for r in range(len(all_level_moves[0]))
            ]  # special ids for original parents
            true_ids = [
                item for sublist in true_ids for item in sublist
            ]  # functions perfectly
            firstcount = len(labels)
        else:
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

    return ids, labels, parents, values, percentage_holder, lst, ratios


def form(ids, labels, parents, values, colors, ratios, percentage_everything, hovertip_openings):
    fig = go.Figure(
        go.Sunburst(
            ids=ids,
            labels=labels,
            parents=parents,
            values=values,
            marker = dict(
                    colors = colors
                    ),
            leaf = {
                    'opacity': 1.0
                    },
            branchvalues="total",  # if children exceed parent, graph will crash and not show
            insidetextorientation="horizontal",  # text displays PP
            # marker=dict(
            #    colorscale='RdBu',
            #    cmid=8
            #    )
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
            'x':0.5,
            'yanchor': 'top',
            'font': {
                'size': 25
                    }
            })

    return fig #nasty thing should be fixed by autopep8

def find_colors(ids, ratios, lst):
    holder = []
    for i in range(len(ids)):
        if type(ids[i]) != str:
            holder.append(list(ids[i]))
        else:
            holder.append(list(ids[i].split(' ')))

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


    rgb_codes = []
    max_rgb = 255
    for i in range(len(full_ratios)):
        rgb_codes.append((full_ratios[i])*max_rgb)

    for i in range(len(rgb_codes)):
        rgb_codes[i] = 'rgb('+str(int(rgb_codes[i])) + ',' + str(int(rgb_codes[i])) + ',' + str(int(rgb_codes[i])) + ')'

    return rgb_codes, full_ratios


def graph(database, depth=5, fragmentation_percentage=0.0032, should_defragment=False, custom_branching=False): # need file path, depth,

    database = open(database)

    ids, labels, parents, values, percentage_everything, lst, ratios = form_values(database, depth, fragmentation_percentage, should_defragment, custom_branching) # a good value is about 10x the smallest value

    rgb_codes, full_ratios = find_colors(ids, ratios, lst)

    eco_codes, eco_names, eco_positions = find_opening.create_openings()
    hovertip_openings = []

    for i in range(len(ids)):
        if ids[i] in eco_positions:
            analyzed = eco_positions.index(ids[i])
            hovertip_openings.append(eco_names[analyzed])
        else:
            hovertip_openings.append('Non-ECO Opening')

    fig = form(ids, labels, parents, values, rgb_codes, full_ratios, percentage_everything, hovertip_openings)

    fig.show()

# download interactive HTML
# fig.write_html("fig1.html")

# Note: You can also download the image! You can do so in the following formats:
# SVG, PNG, JPEG, PDF, and WebP
# to do so, unhash the below line and fill the file type with your desired file type
# KEEP IN MIND THAT TO DOWNLOAD AN IMAGE, YOU NEED THE FOLLOWING IN YOUR TERMINAL: npm install -g electron@1.8.4 orca         pip install psutil requests      pip install psutil
# only then can you download the image without failure
# switch the.jpeg to your favourite format such as pdf or svg

def download(fig, format):
    fig.write_image("fig1."+format)
