from musician import Musician, Guitarist, Drummer, Singer

class Band:
    """A band made up of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician (of any type) to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make the whole band play."""
        print(f"{self.name} is now playing!")
        for musician in self.musicians:
            musician.play()

def main():
    """Create the Extreme band with specific musician roles and make them play."""
    extreme = Band("Extreme")

    gary = Singer("Gary Cherone")
    nuno = Guitarist("Nuno Bettencourt")
    pat = Musician("Pat Badger")
    kevin = Drummer("Kevin Figueiredo")

    # 把成员加进 band
    extreme.add(gary)
    extreme.add(nuno)
    extreme.add(pat)
    extreme.add(kevin)

    extreme.play()

if __name__ == "__main__":
    main()
