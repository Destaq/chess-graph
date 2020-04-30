# A Graphical Visualization of Chess Openings
# April 2020

# Provides a colorful multi-level pie chart which shows the popularity of openings after moves
# For more info, go to www.github.com/Destaq/opening_analysis

# TODO: shading
# TODO: custom branching e.g. ruy lopez
# TODO: prune slices that are too small, based on PERCENTAGE not count

# COMPLETE: gambit and opening identifications
# COMPLETE: percentages of parent
# COMPLETE: pick player and their color - use chess.com database OR input player name as if statement in header

import plotly.graph_objects as go
from collections import Counter
import game_parser
import find_opening


def form_values(depth, fragmentation_percentage, should_defragment):
    """Create parent, id, labels, and values """
    firstx = [
        lst[i][:depth] for i in range(len(lst))
    ]  # probably unneeded but for safety's sake...

    all_level_moves, exclude_first_moves = [], []  # for parent/labels later
    counter = 0
    holder = [firstx[i][0] for i in range(len(firstx))]
    holder = dict(Counter(holder))

    percentage_holder = []

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

    return ids, labels, parents, values, percentage_holder


def form(ids, labels, parents, values):
    fig = go.Figure(
        go.Sunburst(
            ids=ids,
            labels=labels,
            parents=parents,
            values=values,
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
                for i in range(len(percentage_everything))
            ],
            hovertemplate="%{hovertext}<extra></extra>",
        )
    )

    return fig


user_input_game_file = input(
    "Which game file should be analyzed? Provide FULL path file. "
)
gammme = open(user_input_game_file)
user_input_depth = int(input("To what ply depth should we visualize these games? "))

lst = game_parser.parse_individual_games(gammme, user_input_depth)
ids, labels, parents, values, percentage_everything = form_values(user_input_depth, 0.0032, True) # a good value is about 10x the smallest value

eco_codes, eco_names, eco_positions = find_opening.create_openings()
hovertip_openings = []

for i in range(len(ids)):
    if ids[i] in eco_positions:
        analyzed = eco_positions.index(ids[i])
        hovertip_openings.append(eco_names[analyzed])
    else:
        hovertip_openings.append('Non-ECO Opening')

fig = form(ids, labels, parents, values)

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

fig.show()

# download interactive HTML
# fig.write_html("fig1.html")

# Note: You can also download the image! You can do so in the following formats:
# SVG, PNG, JPEG, PDF, and WebP
# to do so, unhash the below line and fill the file type with your desired file type
# KEEP IN MIND THAT TO DOWNLOAD AN IMAGE, YOU NEED THE FOLLOWING IN YOUR TERMINAL: npm install -g electron@1.8.4 orca         pip install psutil requests      pip install psutil
# only then can you download the image without failure
# switch the.jpeg to your favourite format such as pdf or svg

# fig.write_image("fig1.jpeg")
