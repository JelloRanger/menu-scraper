import re

class FoodItem():

    def __init__(self, diningHall, name, dayOfWeek,
                 mealTime, station, attribute):

        # remove excess whitespace, \n, and \r characters
        name = re.sub(r"\s+", " ", name)
        station = re.sub(r"\s+", " ", station)

        # entree is recorded differently in terms of
        # the e with accent on the various menus,
        # so to make things simpler, we avoid the e with accent
        # character by checking first 4 letters, and set it to entree
        if station.lower()[0:4] == "entr":
            station = "entree"

        self.name = name
        self.diningHall = diningHall
        self.mealTime = mealTime.lower()
        self.dayOfWeek = dayOfWeek.lower()
        self.station = station.lower()
        self.attribute = attribute

        # future attributes to record
        #self.vegetarian
        #self.calories
        #self.station

    # print out relevant food information in a clean format
    def __str__(self):
        self.output = (self.dayOfWeek + ", " + self.mealTime + ", " + self.station + ": " + self.name)
        if (len(self.attribute) > 0):
            self.output += (": {}".format(self.attribute[0]))
            for attr in self.attribute[1:]:
                self.output += (", {}".format(attr))
        return self.output

    # get the dining hall for a FoodItem
    def getDiningHall(self):
        return self.diningHall
