def fare(self):
        return self.seating_capacity() * 100

class Bus :
    
    def seating_capacity(self):
        return 50
    
    def fare(self):
        total = super().fare()
        return total + (total * 10 / 100)


b = Bus()

print("Total Bus Fare:", b.fare())
