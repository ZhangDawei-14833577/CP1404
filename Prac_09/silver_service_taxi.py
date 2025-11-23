"""SilverServiceTaxi class derived from Taxi."""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes fanciness and flagfall charges."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # scale the price_per_km based on fanciness
        self.price_per_km *= fanciness
