import math

def prime_len(numer):
    for x in range(1, numer):
        x1 = (x - 1)
        result1 = math.prod(range(x1, 0, -1))
        p = ((result1)**2) % x
        if p == 1:
            print(x)


def prime_rap(numer):
    prime = [True for i in range(numer + 1)]
    p = 2
    while (p * p <= numer):
        if (prime[p] == True):
            for i in range(p * 2, numer + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, numer):
        if prime[p]:
            print(p)


def main():
    numer = 10000
    prime_rap(numer)
    print("The Sieve of Eratosthenes")

    #prime_len(numer)
    #print("Teorema de Wilson")


if __name__ == "__main__":
    main()
