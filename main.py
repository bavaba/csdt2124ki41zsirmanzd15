import chess_logic


def main():
    game = chess_logic.ChessGame()
    while not game.is_game_over():
        print(game.board)
        move = input("Enter your move: ")
        if not game.make_move(move):
            print("Invalid move, try again.")
    print("Game over!")


if __name__ == "__main__":
    main()
