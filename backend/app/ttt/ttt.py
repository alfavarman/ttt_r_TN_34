import random


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = random.choice(["X", "O"])

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("* moves row_1: 0,1,2 \n row_2: 3,4,5 \n row_3: 6,7,8")

    def make_move(self, position: int) -> None:
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Please try again.")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]

        for combination in winning_combinations:
            a, b, c = combination
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return "tie"

        return None


    def minimax(self, board, player):
        """minimax algorithm for computer moves"""
        available_positions = [i for i, spot in enumerate(board) if spot == " "]

        if self.check_winner() == "X":
            return {"score": -1}
        elif self.check_winner() == "O":
            return {"score": 1}
        elif self.check_winner() == "tie":
            return {"score": 0}

        moves = []

        for position in available_positions:
            move = {}
            move["position"] = position
            board[position] = player

            if player == "O":
                result = self.minimax(board, "X")
                move["score"] = result["score"]
            else:
                result = self.minimax(board, "O")
                move["score"] = result["score"]

            board[position] = " "
            moves.append(move)

        if player == "O":
            best_move = max(moves, key=lambda x: x["score"])
        else:
            best_move = min(moves, key=lambda x: x["score"])

        return best_move


    def computer_make_move(self):
        """computer turn"""
        best_move = self.minimax(self.board, self.current_player)["position"]
        self.make_move(best_move)