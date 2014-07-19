"""Name:     Sodexo Dining Hall Library.
File name:   sodexo_dining_hall.py
Description: This is the implementation for the SodexoDiningHall class
             required for the Sodexo Menu Parser class.
             It divides the menus to their respective dining halls.
Contents:
          Classes:
                   SodexoDiningHall
Required libraries:
                    Python Standard JSON Library.
                    Sodexo Food Library.
"""

import json
from sodexo_food import *


class SodexoDiningHall():
    """SodexoDiningHall Class.
    Each instance of this class holds the data for a dining hall.
    """

    # This main dictionary should not be directly accessed because
    # this allows for modification of data, which, for our purposes
    # is strictly forbidden by this code. I have included an underscore
    # to indicate this in accordance to PEP8. Please use the data()
    # or output function defined in the following code to access the
    # main dictionary.
    _main_dictionary = {}

    def __init__(self, dininghall):
        """Constructor of the SodexoFood class.
        Note that there are no default values for any of our arguments.
        There is, therefore, no such thing as a default constructor.
        We expect that all of the arguments are to be defined by the
        constructor call. In other words, we expect that the data
        entered into the constructor call is FINAL and will NOT be
        modified!

        Arguments:

        self -- Reference to self as needed. In our circumstance, this
        is unnecessary. However, it is there for those who wish to
        modify the code and is complacent with PEP8.

        dininghall -- A string containing the name of the dining hall
        that this data is representing.
        """

        self._main_dictionary = {"diningHall": EMPTY_STRING, "menu": []}
        self._main_dictionary["diningHall"] = dininghall

    def add_food(self, name, dayofweek, meal, station, attributes):
        """This function allows us to add a food item into our menu of
        food items in a dining hall. Note that the function follows
        the constructor of the SodexoFood class.

        Arguments:

        self -- Reference to self as needed. In our circumstance, this
        is unnecessary. However, it is there for those who wish to
        modify the code and is complacent with PEP8.

        name -- A string containing the name of the food that this
        data is representing.

        day_of_week -- A string containing the name of the day that is
        food is served.

        meal -- A string containing the name of the meal of the day
        that this food is served.

        station -- A string containing the name of the station that
        this food is served at.

        attributes -- A list containing strings of attributes that are
        associated with this food.
        """

        # Create a Sodexo Food variable and add it to our dictionary.
        new_food = SodexoFood(name, dayofweek, meal, station, attributes)
        if (new_food.data())["name"] != EMPTY_STRING:
            self._main_dictionary["menu"].append(new_food.data())

    def data(self):
        """A function that returns the data stored in our
        _main_dictionary. Please use this function as an accessory
        function for _main_dictionary and do not explicitly use
        _main_dictionary.

        Arguments:

        self -- Reference to self as needed. In our circumstance, this
        is unnecessary. However, it is there for those who wish to
        modify the code and is complacent with PEP8.
        """

        return self._main_dictionary

    def output(self, file=None):
        """A JSON output function.
        This function outputs data from the main dictionary to a JSON
        format.

        self -- Reference to self as needed. In our circumstance, this
        is unnecessary. However, it is there for those who wish to
        modify the code and is complacent with PEP8.

        file -- A file object that is defaulted to None. During actual
        operation, this file object should be specified. The default
        value may be used to output the data into the output stream,
        which is useful for debugging."""

        if file is not None:
            file.write(json.dumps(self._main_dictionary))
        else:
            print(json.dumps(self._main_dictionary))
