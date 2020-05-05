import new_parser


def test_parse_individual_games():
    lst, ratios, kick_depth = new_parser.parse_games("pgns/mir_khan.pgn", 3, False)
    assert len(lst) == 156

test_parse_individual_games()
