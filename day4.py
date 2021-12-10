class Board():
    def __init__(self, board_str):
        self.won = False
        self.board_nums = self.str_to_2dlist(board_str)
        self.board_marks = [[False for i in range(5)] for i in range(5)]

    def str_to_2dlist(self, board_str):
        lines = board_str.split('\n')
        board = [[int (i) for i in line.split()] for line in lines]
        return board

    def mark(self, num):
        for i, row in enumerate(self.board_nums):
            for j, board_n in enumerate(row):
                if board_n == num:
                    self.board_marks[i][j] = True

    def does_win(self):
        # rows
        for row in self.board_marks:
            if all(row):
                return True
        # Columns
        for i in range(len(self.board_marks[0])):
            if all([x[i] for x in self.board_marks]):
                return True

    def tally(self):
        tally = 0
        for i, row in enumerate(self.board_nums):
            for j, num in enumerate(row):
                if not self.board_marks[i][j]:
                    tally += num
                    print(tally)
        return tally

        
        # # Diagonals
        # if all([self.board_marks[i][i] for i in range(5)]):
        #     return True
        # if all([self.board_marks[i][4 - i] for i in range(5)]):
        #     return True

        return False


def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        d = f.read()
        d = d.split("\n\n")
        order = [int(i) for i in d[0].split(",")]
        bs = d[1:]
        boards = []
        for b in bs:
            boards.append(Board(b))

    return order, boards


order, boards = get_data("day4.txt")

round = 0
while len(boards) > 0:
    num = order[round]
    print("Round: ", round + 1, " = ", num)
    remaining_boards = []
    for i, board in enumerate(boards):
        board.mark(num)
        win = board.does_win()
        if win:
            board.won = True
            if len(boards) == 1:
                board_score = board.tally()
                score = board_score * num
                print(num)
                print(score)
                print("score", score)
                            
        else:
            remaining_boards.append(board)
    boards = remaining_boards
    round += 1




        
        # print(board.board_nums)
        # print(board.board_marks)
    # if round == 2:
    #     break

    
    
