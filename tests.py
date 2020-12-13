import unittest
from board import get_board, white_piece, best_move_white, black_piece, best_move_black

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

    def test_get_board(self):
        board_string = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        expected_result_black_rook = self.starting_board[0][0]
        expected_result_white_rook = self.starting_board[15][15]
        result = get_board(board_string)
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
