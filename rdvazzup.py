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

def main():
    seed = int(input('Enter the seed value').strip())
    a = int(input('Enter the a value').strip())
    b = int(input('Enter the b value').strip())
    mod = int(input('Enter the mod value').strip())
    random_gen = lcm(seed, a, b, mod)
    set_num = set()
    count = 0
    while True:
        x =  random_gen.rand()
        if x in set_num:
            break
        else:
            set_num.add(x)
            count += 1
    print("The function repeats after", count, "numbers")
    return

if __name__ == '__main__':
    main()
