import statistics
pos = [int(p) for p in open("input.txt").read().split(",")]
print(sum([int(abs(statistics.median(pos) - p)) for p in pos]))
print(min([sum([sum(range(abs(int(statistics.mean(pos)) + t - p) + 1)) for p in pos]) for t in range(-3, 3)]))
