class Trip():
    def __init__(self, pickup = None, dropoff= None, time = None, date = None):
        self.pickup = pickup
        self.dropoff = dropoff
        self.time = time
        self.date = date


    # Getters
    def getPickup(self):
        return self.pickup
    def getDropoff(self):
        return self.dropoff
    def getTime(self):
        return self.time
    def getDate(self):
        return self.date

    # Setters
    def setPickup(self, pickup):
        self.pickup = pickup
    def setDropoff(self, dropoff):
        self.dropoff = dropoff
    def setTime(self, time):
        self.time = time
    def setDate(self, date):
        self.date = date

    # str
    def __str__(self):
        return self.pickup+", "+self.dropoff+", "+self.time+", "+self.date