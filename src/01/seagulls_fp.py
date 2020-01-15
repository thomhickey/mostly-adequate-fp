conjoin = (lambda flockX, flockY: flockX + flockY)
breed = (lambda flockX, flockY: flockX * flockY)

if __name__ == '__main__':
    flockA = 4
    flockB = 2
    flockC = 0
    print(conjoin(breed(flockB, conjoin(flockA, flockC)), breed(flockA, flockB)))
