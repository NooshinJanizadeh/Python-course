# checker class
class Checker:
    def __init__(self, color):
        self.color = color  # "white" یا "black"
        self.is_king = False

    def __str__(self):
        if self.is_king:
            return "K" if self.color == "white" else "k"
        return "W" if self.color == "white" else "B"


# class  (Player)
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = 0

    def __str__(self):
        return f"{self.name} ({self.color})"


# class(Board)
class Board:
    def __init__(self):
        self.size = 8
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup()

    def setup(self):
        # چیدن مهره‌های سیاه (بالا)
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("black")

        # چیدن مهره‌های سفید (پایین)
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("white")

    def display(self):
        print("\n   0 1 2 3 4 5 6 7")
        for row in range(8):
            line = f"{row}  "
            for col in range(8):
                piece = self.grid[row][col]
                line += (str(piece) if piece else ".") + " "
            print(line)
        print()

    def get_piece(self, row, col):
        return self.grid[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.grid[from_row][from_col]
        self.grid[to_row][to_col] = piece
        self.grid[from_row][from_col] = None


# class (Game)
class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "white")
        self.player2 = Player("Player 2", "black")
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        print("=== Checkers Game ===")
        print(f"{self.player1} vs {self.player2}\n")

        while True:
            self.board.display()
            print(f"Turn: {self.current_player}")

            # گرفتن ورودی
            try:
                from_row = int(input("From row: "))
                from_col = int(input("From col: "))
                to_row = int(input("To row: "))
                to_col = int(input("To col: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            # بررسی مهره
            piece = self.board.get_piece(from_row, from_col)

            if piece is None:
                print("No piece at this position.")
                continue

            if piece.color != self.current_player.color:
                print("That is not your piece.")
                continue

            # simple movement
            if abs(to_row - from_row) == 1 and abs(to_col - from_col) == 1:
                if self.board.get_piece(to_row, to_col) is None:
                    self.board.move_piece(from_row, from_col, to_row, to_col)
                    self.current_player.moves += 1
                    self.switch_player()
                else:
                    print("Destination is not empty.")
            else:
                print("Invalid move. Only diagonal moves of 1 step are allowed.")

            # شرط پایان بازی (ساده)
            if self.player1.moves + self.player2.moves >= 20:
                print("Game over! (Move limit reached)")
                break


# اجرای بازی
if __name__ == "__main__":
    game = Game()
    game.play()