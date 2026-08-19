class Common:
    PM = "Narendra Modi"

    def display(self):
        print("1. PM + PM")
        print("2. CM + CM")


class AndhraPradesh(Common):
    def set_dim(self, place, value):
        self.place = place
        self.value = value

    def display(self):
        print("State: Andhra Pradesh")
        print("Place:", self.place)
        print("Value:", self.value)
        print("PM:", self.PM)
        print()


class TamilNadu(Common):
    def set_dim(self, place, value):
        self.place = place
        self.value = value

    def display(self):
        print("State: Tamil Nadu")
        print("Place:", self.place)
        print("Value:", self.value)
        print("PM:", self.PM)
        print()


# Creating Andhra Pradesh objects
a = AndhraPradesh()
b = AndhraPradesh()
c = AndhraPradesh()

# Creating Tamil Nadu objects
a1 = TamilNadu()
b1 = TamilNadu()

# Setting Andhra Pradesh details
a.set_dim("Amaravathi", 35)
b.set_dim("Srirampuram", 45)
c.set_dim("East Godavari", 25)

# Display Andhra Pradesh details
a.display()
b.display()
c.display()

print("...................")

# Setting Tamil Nadu details
a1.set_dim("Chennai", 55)
b1.set_dim("Navalur", 75)

# Display Tamil Nadu details
a1.display()
b1.display()
