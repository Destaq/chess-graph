import new_parser


def test_parse_individual_games():
    lst, ratios, kick_depth = new_parser.parse_games("mir_khan_test.pgn", 5, False, color = 'both', name = '')
    assert len(lst) == 156

test_parse_individual_games()
