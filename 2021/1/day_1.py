with open("input.txt", "r") as d:
    n = [int(x) for x in d.readlines()]
    x = sum([n[i] < n[i + 1] for i in range(len(n) - 1)])
    y = sum([sum(n[i:i + 3]) < sum(n[i + 1:i + 4]) for i in range(len(n) - 3)])
    print(x, y)
