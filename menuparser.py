from html.parser import HTMLParser
import urllib.request
import re

# ***** JACOB ABRAMSON *****

# TO BE UTILIZED LATER
class FoodMenu():

    def __init__(self):
        self.foodList = []

    # add a food to the menu
    def addFood(self, foodItem):
        self.foodList.append(foodItem)

    # implement later
    def getFood(self, name):
        pass

    def __str__(self, diningHall=None, day=None, meal=None):
        # print out all items in menu
        if diningHall is None:
            
            for food in foodList:
                print (food)    
        

class FoodItem():

    def __init__(self, name, dayOfWeek, mealTime, station):

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
        self.diningHall = ""
        self.mealTime = mealTime.lower()
        self.dayOfWeek = dayOfWeek.lower()
        self.station = station.lower()
        self.date = ""

        # future attributes to record
        #self.vegetarian
        #self.calories
        #self.station

    # print out relevant food information in a clean format
    def __str__(self):
        return (self.dayOfWeek + ", "+ self.mealTime + ", " +
               self.station + ": " + self.name)
        

class MenuParser(HTMLParser):

    def __init__(self):
        
        HTMLParser.__init__(self)

        # lets us know when to record specific data
        self.recordName = False
        self.recordMealTime = False
        self.recordStation = False

        # keep track of day of week, mealTime, station ...
        self.day = ""
        self.mealTime = ""
        self.station = ""

        # record the names of the food items
        self.foods = []
        
        # used to deal with multiple calls to handle_data
        # in the case an & is in a food name
        self.text = []
        self.stationText = []


    # begin the scraping of the provided webpage
    def begin_parsing(self, url):

        # grab the html and decode it
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()

        # feed the text into the parser
        self.feed(htmltext.decode('iso-8859-1'))

        # print food names we have scraped
        self.printFoods()

        # clear list
        self.foods = []


    def handle_starttag(self, tag, attrs):

        # food item name is ready to be read
        if tag == "span" and attrs[0][0] == "class" and attrs[0][1] == "ul":
            self.recordName = True

        # food item day of serving is ready to be read
        if tag == "a" and attrs[0][0] == "name" and attrs[0][1] != "pagetop":
            self.day = attrs[0][1]

        # food item meal time is ready to be read
        if tag == "td" and len(attrs) > 1:
            if attrs[1][0] == "class" and attrs[1][1] == "mealname":
                self.recordMealTime = True
            elif attrs[0][0] == "class" and attrs[0][1] == "mealname":
                self.recordMealTime = True

        # food item station is ready to be read
        if tag == "td" and len(attrs) > 0:
            if attrs[0][0] == "class" and attrs[0][1] == "station":
                self.recordStation = True


    def handle_endtag(self, tag):

        # record station
        if self.recordStation:
            self.recordStation = False
            
            # make sure it is new station name
            # (sodexo doesn't put same name for multiple food items
            # under same station)
            if len("".join(self.stationText)) > 0:
                self.station = "".join(self.stationText)

            self.stationText = [] # clear to record next station

        # add food item to list, and signify food item is done being recorded
        if self.recordName:
            self.recordName = False

            # create FoodItem w/ data: name, day, meal time
            self.foods.append(FoodItem("".join(self.text), self.day,
                                       self.mealTime, self.station))

            self.text = [] # clear to record next food name


    def handle_data(self, data):

        # ready to read in food item name
        if self.recordName:
            self.text.append(data)

        # ready to read in food item meal time
        if self.recordMealTime:
            self.mealTime = data
            self.recordMealTime = False

        # ready to read in station
        if self.recordStation:
            self.stationText.append(data)


    # debugging function to print list of food items
    def printFoods(self):
        for food in self.foods:
            print (food)






