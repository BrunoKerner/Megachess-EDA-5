import unittest
from board import get_board, white_piece, best_move_white, black_piece, best_move_black, valid_white_move, valid_black_move

class test_sample(unittest.TestCase):

    def setUp(self):
        self.starting_board = [                                                                                      
            ["r","r","h","h","b","b","q","q","k","k","b","b","h","h","r","r"],
            ["r","r","h","h","b","b","q","q","k","k","b","b","h","h","r","r"],
            ["p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p"],
            ["p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P"],
            ["P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P"],
            ["R","R","H","H","B","B","Q","Q","K","K","B","B","H","H","R","R"],
            ["R","R","H","H","B","B","Q","Q","K","K","B","B","H","H","R","R"]
        ]

        self.starting_board_string = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"

    def test_get_board(self):
        expected_result_black_rook = self.starting_board[0][0]
        expected_result_white_rook = self.starting_board[15][15]
        result = get_board(self.starting_board_string)
        result_black_rook = result[0][0]
        result_white_rook = result[15][15]
        self.assertEqual(expected_result_black_rook, result_black_rook)
        self.assertEqual(expected_result_white_rook, result_white_rook)

    def test_white_piece(self):

        is_white = white_piece(self.starting_board, 15, 15)

        self.assertTrue(is_white)

    def test_is_not_white_piece(self):

        is_white = white_piece(self.starting_board, 0, 0)

        self.assertFalse(is_white)

    def test_black_piece(self):

        is_black = black_piece(self.starting_board, 0, 0)

        self.assertTrue(is_black)

    def test_is_not_black_piece(self):

        is_black = black_piece(self.starting_board, 15, 15)

        self.assertFalse(is_black)

    def test_best_move_white(self):
        # el primer movimiento es el mejor, porque es el que mas puntaje tiene
        valid_white_moves_sample = [[3,2,5,2,10],[5,7,5,8,5],[1,1,2,1,2]]
        result = best_move_white(valid_white_moves_sample)
        self.assertEqual(result[0], valid_white_moves_sample[0][0:4])

    def test_best_move_black(self):
        # el primer movimiento es el mejor, porque es el que mas puntaje tiene
        valid_black_moves_sample = [[3,2,5,2,10],[5,7,5,8,5],[1,1,2,1,2]]
        result = best_move_black(valid_black_moves_sample)
        self.assertEqual(result[0], valid_black_moves_sample[0][0:4])

    def test_valid_white_move_pawn(self):
        board_string_sample_pawns = "                                                                                                                       P                                                        q q              P                    P                                         "
        valid_white_pawns_moves_sample = [[7, 7, 6, 7, 4], [7, 7, 6, 7, 1], [12, 1, 11, 0, 10], [12, 1, 11, 2, 10], [12, 1, 10, 1, 3], [12, 1, 11, 1, 1], [13, 6, 11, 6, 3], [13, 6, 12, 6, 1]]
        get_board_sample_1 = get_board(board_string_sample_pawns)
        result = valid_white_move(get_board_sample_1)
        self.assertEqual(result, valid_white_pawns_moves_sample)

    def test_valid_white_move_queen(self):
        board_string_sample_queens = "                                                                                                                                  Q                                             qqq             qQq             qqq                                             "
        valid_white_queens_moves_sample = [[12, 1, 11, 1, 5], [12, 1, 12, 2, 5], [12, 1, 12, 0, 5], [12, 1, 13, 1, 5], [12, 1, 11, 0, 5], [12, 1, 13, 0, 5], [12, 1, 11, 2, 5], [12, 1, 13, 2, 5]]
        get_board_sample_2 = get_board(board_string_sample_queens)
        result = valid_white_move(get_board_sample_2)
        self.assertEqual(result, valid_white_queens_moves_sample)

    def test_valid_white_move_rook(self):
        board_string_sample_rook = "                                                                                                                                  R                                              q              qRq              q                                              "
        valid_white_rooks_moves_sample = [[8, 2, 7, 2, 1], [8, 2, 8, 3, 1], [8, 2, 8, 1, 1], [8, 2, 9, 2, 2], [12, 1, 11, 1, 10], [12, 1, 12, 2, 10], [12, 1, 12, 0, 10], [12, 1, 13, 1, 10]]
        get_board_sample_3 = get_board(board_string_sample_rook)
        result = valid_white_move(get_board_sample_3)
        self.assertEqual(result, valid_white_rooks_moves_sample)

    def test_valid_white_move_bishop(self):
        board_string_sample_bishop = "                                                                                                                                                                                qqq             qBq             qqq                                             "
        valid_white_bishops_moves_sample = [[12, 1, 11, 0, 10], [12, 1, 13, 0, 10], [12, 1, 11, 2, 10], [12, 1, 13, 2, 10]]
        get_board_sample_4 = get_board(board_string_sample_bishop)
        result = valid_white_move(get_board_sample_4)
        self.assertEqual(result, valid_white_bishops_moves_sample)

    def test_valid_white_move_king(self):
        board_string_sample_kings = "                                                                                                                                  K                                             qqq             qKq             qqq                                             "
        valid_white_kings_moves_sample = [[8, 2, 7, 2, 1], [8, 2, 8, 3, 1], [8, 2, 8, 1, 1], [8, 2, 9, 2, 2], [8, 2, 7, 1, 1], [8, 2, 9, 1, 1], [8, 2, 7, 3, 1], [8, 2, 9, 3, 1], [12, 1, 11, 1, 10], [12, 1, 12, 2, 10], [12, 1, 12, 0, 10], [12, 1, 13, 1, 10], [12, 1, 11, 0, 10], [12, 1, 13, 0, 10], [12, 1, 11, 2, 10], [12, 1, 13, 2, 10]]
        get_board_sample_5 = get_board(board_string_sample_kings)
        result = valid_white_move(get_board_sample_5)
        self.assertEqual(result, valid_white_kings_moves_sample)

    def test_valid_black_move_pawn(self):
        board_string_sample_black_pawns = "                                                 p              Q Q    p                              p                                                                                                                                                         "
        valid_black_pawns_moves_sample = [[6, 6, 7, 6, 4], [6, 6, 7, 6, 1], [4, 7, 5, 7, 4], [4, 7, 5, 7, 1], [3, 1, 4, 2, 10], [3, 1, 4, 0, 10], [3, 1, 5, 1, 3], [3, 1, 4, 1, 1]]
        get_board_sample_6 = get_board(board_string_sample_black_pawns)
        result = valid_black_move(get_board_sample_6)
        self.assertEqual(result, valid_black_pawns_moves_sample)

    def test_valid_black_move_queen(self):
        board_string_sample_black_queen = "                                QQQ             QqQ             QQQ                                                                                                                                                                                             "
        valid_black_queen_moves_sample = [[3, 1, 4, 1, 5], [3, 1, 3, 0, 5], [3, 1, 3, 2, 5], [3, 1, 2, 1, 5], [3, 1, 4, 2, 5], [3, 1, 2, 2, 5], [3, 1, 4, 0, 5], [3, 1, 2, 0, 5]]
        get_board_sample_7 = get_board(board_string_sample_black_queen)
        result = valid_black_move(get_board_sample_7)
        self.assertEqual(result, valid_black_queen_moves_sample)

    def test_valid_black_move_rook(self):
        board_string_sample_black_rook = "                                QQQ             QrQ             QQQ                                                                      r                                                                                                                      "
        valid_black_rooks_moves_sample = [[2, 0, 3, 1, 5], [2, 1, 3, 1, 5], [2, 2, 3, 1, 5], [3, 0, 3, 1, 5], [3, 2, 3, 1, 5], [4, 0, 3, 1, 5], [4, 1, 3, 1, 5], [4, 2, 3, 1, 5]]
        get_board_sample_8 = get_board(board_string_sample_black_rook)
        result = valid_white_move(get_board_sample_8)
        self.assertEqual(result, valid_black_rooks_moves_sample)

    def test_valid_black_move_bishop(self):
        board_string_sample_black_bishop = "                                QQQ             QbQ             QQQ                                                                                                                                                                                             "
        valid_black_bishops_moves_sample = [[3, 1, 4, 2, 10], [3, 1, 2, 2, 10], [3, 1, 4, 0, 10], [3, 1, 2, 0, 10]]
        get_board_sample_9 = get_board(board_string_sample_black_bishop)
        result = valid_black_move(get_board_sample_9)
        self.assertEqual(result, valid_black_bishops_moves_sample)

    def test_valid_black_move_king(self):
        board_string_sample_black_kings = "                                QQQ             QkQ             QQQ                                                                      k                                                                                                                      "
        valid_black_kings_moves_sample = [[8, 9, 9, 9, 1], [8, 9, 8, 8, 1], [8, 9, 8, 10, 1], [8, 9, 7, 9, 2], [8, 9, 9, 10, 1], [8, 9, 7, 10, 1], [8, 9, 9, 8, 1], [8, 9, 7, 8, 1], [3, 1, 4, 1, 10], [3, 1, 3, 0, 10], [3, 1, 3, 2, 10], [3, 1, 2, 1, 10], [3, 1, 4, 2, 10], [3, 1, 2, 2, 10], [3, 1, 4, 0, 10], [3, 1, 2, 0, 10]]
        get_board_sample_10 = get_board(board_string_sample_black_kings)
        result = valid_black_move(get_board_sample_10)
        self.assertEqual(result, valid_black_kings_moves_sample)
