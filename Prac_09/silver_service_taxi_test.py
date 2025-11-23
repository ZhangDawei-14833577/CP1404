"""Test SilverServiceTaxi class."""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi functionality."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness = 2

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Limo fare for 18km trip = {fare:.2f}")

    # assert expected result
    assert abs(fare - 48.78) < 0.01, "Fare calculation incorrect!"


main()
