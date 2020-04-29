import chess.pgn
import game_parser

def test_parse_individual_games():
    pgn = open("pgns/short.pgn")
    assert len(game_parser.parse_individual_games(pgn, 3)) == 156
