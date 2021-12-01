groups = open("input.txt", "r").read().split("\n\n")
anyone = sum([len(set(g.replace("\n", ""))) for g in groups])
everyone = sum([len(set(h[0]).intersection(*h[1:])) for h in [list(filter(None, g.split("\n"))) for g in groups]])
print(anyone, everyone)
