#import chess_graph
from chart import graph

#graph("pgns/lichess_Lorenzo_2012_2020-11-29.pgn", 
graph("pgns/Carlsen.pgn", 
                  depth=5, 
                  shade = True, 
                  fragmentation_percentage=0.10, 
                  should_defragment=False,
                  print_best_lines=True, min_games_best_lines=10) 
