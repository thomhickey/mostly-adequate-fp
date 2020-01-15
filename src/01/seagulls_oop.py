class Flock():
    def __init__(self, seagulls: int):
        self.seagulls = seagulls

    def conjoin(self, other: 'Flock') -> 'Flock':
        self.seagulls += other.seagulls
        return self

    def breed(self, other: 'Flock') -> 'Flock':
        self.seagulls *= other.seagulls
        return self


if __name__ == '__main__':
    flockA = Flock(4)
    flockB = Flock(2)
    flockC = Flock(0)
    result = flockA.conjoin(flockC).breed(flockB).conjoin(flockA.breed(flockB)).seagulls
    print(result)
