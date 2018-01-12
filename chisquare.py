#!/usr/bin/env python3

class lcm:
    seed, a, b, mod = 0, 0, 0, 1
    def __init__(self, seed, a, b, mod):
        self.seed = seed
        self.a = a
        self.b = b
        self.mod = mod

    def rand(self):
        self.seed = (self.a * self.seed + self.b) % self.mod 
        return self.seed 

    def rand_quad(self):
        self.seed = (self.a * (self.seed**2) + self.b * self.seed) % self.mod
        return self.seed

def print_test(chi_square):
    n, m = chi_square.shape
    for i in range(n):
        for j in range(m):
            print(chi_square[i][j], end = ' ')
        print()
    return

def lcm_chisquare(seed, a, b, mod, n, num_buckets):
    print('Running Linear Random Number Generator...')
    import numpy as np
    import math
    random_gen = lcm(seed, a, b, mod)
    chi_square  = np.zeros((num_buckets, 5))
    for i in range(num_buckets):
        chi_square[i][1] = round(n / num_buckets)
    for i in range(n):
        x = random_gen.rand()
        chi_square[x // num_buckets][0] += 1 
    chi_square[:, 2] = chi_square[:, 0] - chi_square[:, 1]
    chi_square[:, 3] = chi_square[:, 2]**2
    chi_square[:, 4] = np.divide(chi_square[:, 3], chi_square[:, 1])
    print_test(chi_square)
    print('The chisquare value is ', np.squeeze(np.sum(chi_square[:, 4], keepdims = True, axis = 0)))
    return

def internal_chisquare(n, num_buckets):
    print('Running Internal Random Number Generator...')
    import numpy as np
    import math
    import random
    chi_square  = np.zeros((num_buckets, 5))
    for i in range(num_buckets):
        chi_square[i][1] = round(n / num_buckets)
    for i in range(n):
        x = random.randint(1, n - 1)
        chi_square[x // num_buckets][0] += 1 
    chi_square[:, 2] = chi_square[:, 0] - chi_square[:, 1]
    chi_square[:, 3] = chi_square[:, 2]**2
    chi_square[:, 4] = np.divide(chi_square[:, 3], chi_square[:, 1])
    print_test(chi_square)
    print('The chisquare value is ', np.squeeze(np.sum(chi_square[:, 4], keepdims = True, axis = 0)))
    return

def lcm_quad_chisquare(seed, a, b, mod, n, num_buckets):
    print('Running Quadratic Random Number Generator...')
    import numpy as np
    import math
    random_gen = lcm(seed, a, b, mod)
    chi_square  = np.zeros((num_buckets, 5))
    for i in range(num_buckets):
        chi_square[i][1] = round(n / num_buckets)
    for i in range(n):
        x = random_gen.rand_quad()
        chi_square[x // num_buckets][0] += 1 
    chi_square[:, 2] = chi_square[:, 0] - chi_square[:, 1]
    chi_square[:, 3] = chi_square[:, 2]**2
    chi_square[:, 4] = np.divide(chi_square[:, 3], chi_square[:, 1])
    print_test(chi_square)
    print('The chisquare value is ', np.squeeze(np.sum(chi_square[:, 4], keepdims = True, axis = 0)))
    return
def main():
    import numpy as np
    import math
    seed = int(input('Enter the seed value : ').strip())
    a = int(input('Enter the a value : ').strip())
    b = int(input('Enter the b value : ').strip())
    mod = int(input('Enter the mod value : ').strip())
    n = int(input('Enter the number of values to test with : '))
    num_buckets = int(input('Enter number of buckets : '))
    print()
    lcm_chisquare(seed, a, b, mod, n, num_buckets)
    print()
    internal_chisquare(n, num_buckets)
    print()
    lcm_quad_chisquare(seed, a, b, mod, n, num_buckets)
    print()
    return

if __name__ == '__main__':
    main()
