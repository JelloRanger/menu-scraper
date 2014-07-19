"""Name:     Sodexo Menu Parser.
File name:   sodexo_parser.py
Description: Accesses a website HTML and parses through the data
             assuming that the data retains the form of a Sodexo menu
             site.
Contents:
          Classes:
                   MenuParser
Required libraries:
                    Python HTML Parser library (HTMLParser class).
                    Python URL Library (Python URL Request class).
                    Sodexo Dining Hall Library.
"""

from html.parser import HTMLParser
import urllib.request
from sodexo_dining_hall import *


class MenuParser(HTMLParser):
    """Menu Parser Class.
    Based on the HTML Parser class. Edited for specific use for
    Sodexo menu HTML files.
    """

    # Control where to send the data.
    _record_name = False
    _record_meal = False
    _record_station = False
    _record_attributes = False

    # Hold the data to be sent.
    _day = EMPTY_STRING
    _meal = EMPTY_STRING
    _station = EMPTY_STRING
    _name_text = []
    _station_text = []
    _attributes = []

    # Hold the container that will hold this data. This one can be
    # accessed directly. This will be used for outputs.
    menu = []

    def __init__(self):
        """An overload of the HTML Parser constructor.
        We use this initialization code to make sure that every
        variable is flushed.

        Arguments:

        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.
        """

        # Initialize the HTML Parser.
        HTMLParser.__init__(self)

        # Initialize the variables.
        self._record_name = False
        self._record_meal = False
        self._record_station = False
        self._record_attributes = False
        self._day = EMPTY_STRING
        self._meal = EMPTY_STRING
        self._station = EMPTY_STRING
        self._name_text = []
        self._station_text = []
        self._attributes = []

        # Hold all the dining hall menus.
        self.menu = []

    def begin_parsing(self, url, name):
        """An overload of the HTML Parser begin parsing method.
        We use this function to control what HTML file to parse.

        Arguments:

        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.

        url -- A string containing the Uniform Resource Locator (http
        only) that corresponds to the HTML file that we are looking
        for.

        name -- A string containing the name of the dining hall the url
        corresponds to.
        """

        # Find the HTML file.
        _HTML_file = urllib.request.urlopen(url)
        # Read the file into bytes and decode it into ISO-8859-1.
        _HTML_text = _HTML_file.read()
        # Initialize our dining hall and set its name.
        self.dining_hall = SodexoDiningHall(name)
        # Feed the text into the parser.
        self.feed(_HTML_text.decode("iso-8859-1"))

    def handle_starttag(self, tag, attrs):
        """An overload of the HTML Parser handle start tag method.
        We use this function to determine what data we are working on.

        Arguments:

        self -- Reference to self as needed. In our circumstance, this
        is unnecessary. However, it is there for those who wish to
        modify the code and is complacent with PEP8.

        tag -- A string containing the HTML tag that we are interested
        in analysing.

        attrs -- An array of an array of strings. We can look up the
        HTML attributes of a certain HTML object.
        """

        # We found the name of the food.
        if (tag == "span".encode().decode("iso-8859-1") and
                attrs[0][0] == "class".encode().decode("iso-8859-1") and
                attrs[0][1] == "ul".encode().decode("iso-8859-1")):
            self._record_name = True
        # We found attributes associated with the food.
        if (tag == "img".encode().decode("iso-8859-1") and
                attrs[0][0] == "class".encode().decode("iso-8859-1") and
                attrs[0][1] == "icon".encode().decode("iso-8859-1")):
            for group in attrs:
                if (group[0] == "alt".encode().decode("iso-8859-1")):
                    self._attributes.append(group[1])
            self._record_attributes = True
        # We found the day of the week.
        if (tag == "a".encode().decode("iso-8859-1") and
                attrs[0][0] == "name".encode().decode("iso-8859-1") and
                attrs[0][1] != "pagetop".encode().decode("iso-8859-1")):
            self._day = attrs[0][1]
        # We found the meal of the day.
        if (tag == "td".encode().decode("iso-8859-1") and len(attrs) > 1):
            if (attrs[1][0] == "class".encode().decode("iso-8859-1") and
                    attrs[1][1] == "mealname".encode().decode("iso-8859-1")):
                self._record_meal = True
            elif (attrs[0][0] == "class".encode().decode("iso-8859-1") and
                    attrs[0][1] == "mealname".encode().decode("iso-8859-1")):
                self._record_meal = True
        # We found the station that the meal is served.
        if (tag == "td".encode().decode("iso-8859-1") and len(attrs) > 0):
            if (attrs[0][0] == "class".encode().decode("iso-8859-1") and
                    attrs[0][1] == "station".encode().decode("iso-8859-1")):
                self._record_station = True

    def handle_endtag(self, tag):
        """An overload of the HTML Parser handle end tag method.
        We use this function to clear variables for further usage.

        Arguments:

        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.

        tag -- A string containing the HTML tag that we are interested
        in analysing.
        """

        # We finished recording the attributes. Clean up.
        if self._record_attributes:
            self._record_attributes = False
        # We recorded the station. Clean up the station name.
        if self._record_station:
            self._record_station = False
            # Make sure that we are properly recording the station.
            if (len(EMPTY_STRING.join(self._station_text)) > 0):
                self._station = EMPTY_STRING.join(self._station_text)
            self._station_text = []
        # We recorded the data. Now process the data into the container.
        if self._record_name:
            self._record_name = False
            self.dining_hall.add_food("".encode().decode("iso-8859-1").join(
                self._name_text), self._day, self._meal,
                self._station, self._attributes)
            self._name_text = []
            self._attributes = []

    def handle_data(self, data):
        """An overload of the HTML Parser handle data method.
        We use this function to compile certain data for various
        reasons. More information will be available as in-line
        comments.

        Arguments:

        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.

        data -- Holds the relevant data that we will use to create our
        results.
        """

        # We finished recording the name. Join and clean up.
        if self._record_name:
            self._name_text.append(data)
        # Since food names can consist of multiple words, we should join
        # all relevant words together.
        if self._record_attributes:
            self._name_text.append(data)
        # Record the meal time only once.
        if self._record_meal:
            self._meal = data
            self._record_meal = False
        # Since station names can consist of multiple words, we should
        # join all relevant words together.
        if self._record_station:
            self._station_text.append(data)

    def print_food(self, file=None):
        """Print food function. Exposes the output function in the
        Sodexo Dining Hall object.

        Arguments:

        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.

        file -- A file object that is defaulted to None. During actual
        operation, this file object should be specified. The default
        value may be used to output the data into the output stream,
        which is useful for debugging.
        """

        if file is not None:
            self.dining_hall.output(file)
        else:
            self.dining_hall.output()

    def return_data(self):
        """Return data from Sodexo Dining Hall object.
        
        Arguments:
        
        self-- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied.
        """
        
        return self.dining_hall.data()
