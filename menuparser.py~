from html.parser import HTMLParser
import urllib.request
import re

# ***** JACOB ABRAMSON ***** 

class FoodItem():

    def __init__(self, name, dayOfWeek, mealTime):

        # remove excess whitespace, \n, and \r characters
        name = re.sub(r"\s+", " ", name)

        self.name = name
        self.diningHall = ""
        self.mealTime = mealTime.lower()
        self.dayOfWeek = dayOfWeek.lower()
        self.date = ""

        # future attributes to record
        #self.vegetarian
        #self.calories
        #self.station

    # print out relevant food information in a clean format
    def __str__(self):
        return self.dayOfWeek + ", "+ self.mealTime + ": " + self.name
        

class MenuParser(HTMLParser):

    def __init__(self):
        
        HTMLParser.__init__(self)

        # lets us know when to record specific data
        self.recordName = False
        self.recordMealTime = False

        # keep track of day of week, mealTime, ...
        self.day = ""
        self.mealTime = ""

        # record the names of the food items
        self.foods = []
        
        # used to deal with multiple calls to handle_data
        # in the case an & is in a food name
        self.text = []


    # begin the scraping of the provided webpage
    def begin_parsing(self, url):

        # grab the html and decode it
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()

        # feed the text into the parser
        self.feed(htmltext.decode('iso-8859-1'))

        # print food names we have scraped
        self.printFoods()


    # all the start tags are handled by this function
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


    # all the end tags are handled by this function
    def handle_endtag(self, tag):

        # add food item to list, and signify food item is done being recorded
        if self.recordName:
            self.recordName = False

            # create FoodItem w/ data: name, day, meal time
            self.foods.append(FoodItem("".join(self.text), self.day, self.mealTime))

            self.text = [] # clear to record next food name
            

    # all the data is handled by this function
    def handle_data(self, data):

        # ready to read in food item name
        if self.recordName:
            self.text.append(data)

        # ready to read in food item meal time
        if self.recordMealTime:
            self.mealTime = data
            self.recordMealTime = False


    # debugging function to print list of food items
    def printFoods(self):
        for food in self.foods:
            print (food)


# instantiate the parser and feed it some HTML
parser = MenuParser()
parser.begin_parsing("http://rpi.sodexomyway.com/Menu/Commons1.htm")
#parser.begin_parsing("http://rpi.sodexomyway.com/Menu/Sage.htm")


