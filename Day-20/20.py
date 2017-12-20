from collections import defaultdict
import sys

abssum = lambda l: sum(abs(x) for x in l)
sumlist = lambda l1, l2: [l1[i] + l2[i] for i in range(len(l1))]

particles = [eval(l[:-2].replace('p=<','[[').replace('>, v=<', '],[').replace('>, a=<', '],[') + ']]') for l in sys.stdin]

sortedparticles = list(enumerate(particles))
sortedparticles.sort(key=lambda x:(abssum(x[1][2]), abssum(x[1][1]), abssum(x[1][0])))
print('Part 1: {:d}'.format(sortedparticles[0][0]))

ticks = 4000
for _ in range(ticks):
    taken = defaultdict(int)
    for i in range(len(particles)):
        particles[i][1] = sumlist(*particles[i][1:])
        particles[i][0] = sumlist(*particles[i][:2])
        taken[tuple(particles[i][0])] += 1
    particles = list(filter(lambda x: taken[tuple(x[0])] == 1, particles))

print('Part 2: {:d}'.format(len(particles)))
