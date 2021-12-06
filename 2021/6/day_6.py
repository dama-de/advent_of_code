fishies = [0] * 9
for f in open("input.txt").read().split(","):
    fishies[int(f)] += 1
for i in range(256):
    fishies.append(fishies.pop(0))
    fishies[6] += fishies[-1]
    if i == 79 or i == 255:
        print(sum(fishies))
