# See https://en.wikipedia.org/wiki/Prime_number

from sympy import primerange, isprime, nextprime, totient

if __name__ == "__main__":
    cases = [
        "list(primerange(0, 100))",
        "list(primerange(1000000, 1000100))",
        "isprime(6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151)",
        "nextprime(6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151)",
        "totient(271)",
        "totient(2718281)",
        "totient(27182818284)",
        "totient(271828182845904)",
        "totient(2718281828459045235360287471352662497757247)"
    ]

    for c in cases:
        print('[] :python-result "%s = %s".' % (c, eval(c)))
