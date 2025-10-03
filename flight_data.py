class FlightData:
    def __init__(self, icao, departure, arrival, description):
        self.icao = icao
        self.departure = departure
        self.arrival = arrival 
        self.description = description

    def __str__(self):
        if (self.description == "Unknown"):
            return f"Flight {self.icao}, Departing from {self.departure}, Arriving at {self.arrival}"
        return self.description