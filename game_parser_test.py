import new_parser


def test_parse_individual_games():
    lst, ratios, kick_depth = new_parser.parse_games("pgns/mir_khan.pgn", 5, False, color = 'both', name = '')
    print(len(lst))
    assert len(lst) == 156

test_parse_individual_games()
