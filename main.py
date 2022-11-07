
# Zadanie 1. Posortowałem listę na dwa sposoby - komendą sort (sortowanie na stałe) oraz sorted (sortowanie jednorazowe)

if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    primes.remove(5)
    primes.append(5)
    print(primes)

    primes.sort(reverse=True)
    print(primes)

    primes_ascending_order = sorted(primes)
    print(primes_ascending_order)

    print(primes)

# Zadanie 2 - utworzyłem dwie listy stringów i umieściłem je tak w pętli for, aby drukował się każdy element z obydwu list.

    actors = ['Ryan_Gosling', 'Roman_Wilhelmi', 'Marcello_Mastroianni']
    actresses = ['Gina_Lollobrigida', 'Krystyna_Janda', 'Penelope_Cruz']
    for celebrity in [actors + actresses]:
        print(celebrity)




