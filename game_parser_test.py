import game_parser


def test_parse_individual_games():
    pgn = open("pgns/mir_khan.pgn")
    lst, ratios = game_parser.parse_individual_games(pgn, 3, False)
    assert len(lst) == 156

test_parse_individual_games()
