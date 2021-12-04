import re, itertools

lines = open("input.txt").read().splitlines()
draws = lines[0].split(",")
boards = []
for i in range(2, len(lines), 6):
    boards.append([re.split("\\s+", l.strip()) for l in lines[i:i + 5]])

win = [0] * 5
winners = []
for draw in draws:
    for board in boards[:]:
        for line in board:
            if draw in line:
                line[line.index(draw)] = 0
                break

        if win in board or tuple(win) in list(zip(*board)):
            winners.append((draw, board))
            boards.remove(board)

print([int(w[0]) * sum([int(a) for a in itertools.chain(*w[1]) if a != 0]) for w in (winners[0], winners[-1])])
