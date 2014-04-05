from html.parser import HTMLParser
import urllib.request
import re
from FoodMenu import FoodMenu
from FoodItem import FoodItem
import time

# ***** JACOB ABRAMSON *****
# *****    DAN BAEK    *****

class MenuParser(HTMLParser):

    def __init__(self):
        
        HTMLParser.__init__(self)

        # lets us know when to record specific data
        self.recordName = False
        self.recordMealTime = False
        self.recordStation = False
        self.recordAttribute = False

        # keep track of day of week, mealTime, station ...
        self.day = ""
        self.mealTime = ""
        self.station = ""
        self.attribute = []
        self.date = ""

        # record the names of the food items in a food menu
        self.foodMenu = FoodMenu()
        
        # used to deal with multiple calls to handle_data
        # in the case an & is in a food name
        self.text = []
        self.stationText = []


    # begin the scraping of the provided webpage
    def begin_parsing(self, url, name):

        # grab the html and decode it
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()

        # name of dining hall
        self.diningHall = name

        # feed the text into the parser
        self.feed(htmltext.decode('iso-8859-1'))

        # print food names we have scraped
        self.foodMenu.printDiningHall(self.diningHall)


    def handle_starttag(self, tag, attrs):

        # food item name is ready to be read
        if tag == "span" and attrs[0][0] == "class" and attrs[0][1] == "ul":
            self.recordName = True

        # food attribute is ready to be read
        if tag == "img" and attrs[0][0] == "class" and attrs[0][1] == "icon":
            for group in attrs:
                if group[0] == "alt":
                    self.attribute.append(group[1])
        self.recordAttribute = True

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

        # record attributes
        if self.recordAttribute:
            self.recordAttribute = False
            self.attribute = []

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
            self.foodMenu.addFood(FoodItem(self.diningHall, "".join(self.text), self.day,
                                       self.mealTime, self.station, self.attribute, self.date))

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

        # read in the date
        if data[0:4] == "Week":
            date = time.strptime((data[8:].strip("\n")).replace(",", ""), "%A %B %d %Y")
            time.strftime("%d/%m/%Y", date)
            self.date = date


    # debugging function to print list of food items
    def printFoods(self):
        f = open("output.txt", 'a', encoding = 'iso-8859-1')
        for food in self.foods:
            f.write(food)
        f.close()






