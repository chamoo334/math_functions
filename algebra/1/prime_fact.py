import sys
#TODO: attempt recursion after improving recursion limit safely
# print(sys.getrecursionlimit())

# function that divides num_a by primes until = 1.
# maintains list of primes for later use
def get_primes(num_a, list_p, num_b):

    while num_a != 1:  # terminate when input = 1
        
        while not num_a % num_b:  # reduce as much as possible by num_b
            list_p.append(num_b)
            num_a = int(num_a / num_b)
    
        num_b += 1
        pos = 0

        while pos < len(list_p):  # verify and find next prime
            if num_b % list_p[pos] == 0:
                pos = 0
                num_b += 1
            elif num_b % list_p[pos] == 1:
                break
            else:
                pos += 1

    return

x = int(sys.argv[1],)
primes = []

get_primes(x, primes, 2)
print(primes)
