from random import sample

from numpy import maximum

num = tuple(sample(range(20), 5))

print(f'Os números gerados foram {sorted(num)}')
