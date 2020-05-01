import game_parser


def test_parse_individual_games():
    pgn = open("pgns/mir_khan.pgn")
    assert len(game_parser.parse_individual_games(pgn, 3, False)) == 156
