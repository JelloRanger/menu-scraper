"""Name:     Sodexo Food Library.
File name:   sodexo_food.py
Description: This is the implementation for the SodexoFood class
             required by the SodexoDiningHall class.
Contents:
    Classes:   SodexoFood
    Constants: Empty String (ISO-8859-1)
               White Space (ISO-8859-1)
               New Line (ISO-8859-1)
               Carriage Return (ISO-8859-1)
"""

# Let's not have UTF-8 encoded strings because the HTML is encoded in
# ISO-8859-1.
EMPTY_STRING = "".encode().decode("iso-8859-1")
WHITESPACE = " ".encode().decode("iso-8859-1")
NEW_LINE = "\n".encode().decode("iso-8859-1")
CARRIAGE_RETURN = "\r".encode().decode("iso-8859-1")


class SodexoFood():
    """Sodexo Food Class.
    Holds the information about a particular food item.
    """

    # This main dictionary should not be directly accessed because
    # this allows for modification of data, which, for our purposes
    # is strictly forbidden by this code. I have included an underscore
    # to indicate this in accordance to PEP8. Please use the data()
    # function defined in the following code to access the main
    # dictionary.
    _main_dictionary = {}

    def __init__(self, name, day_of_week, meal, station, attributes):
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
        main_dictionary = {"name": EMPTY_STRING, "dayOfWeek": EMPTY_STRING,
                           "meal": EMPTY_STRING, "station": EMPTY_STRING,
                           "attributes": []
                           }

        # We typically need to clean up our name variable.
        # This is because Sodexo uses names with excess
        # white spaces, new lines, and carriage returns.
        WHITESPACE.join(name.split())
        name.replace(NEW_LINE, EMPTY_STRING)
        name.replace(CARRIAGE_RETURN, EMPTY_STRING)
        self._main_dictionary["name"] = name

        # We typically need to clean up our station variable
        # because it suffers from the same design problems
        # as the name variable.
        # TODO: We should be able to circumvent
        # the problem that plagued the original code with
        # non-UTF-8 characters using strings that are decoded
        # into ISO-8859-1. However, this is not a certainty.
        # Therefore, we must make modifications to this comment
        # after testing to ensure that this comment is correct.
        # Change in code, however, is needed only under the
        # circumstance that this code does not work.
        # Please, DO NOT EDIT this comment UNLESS proper testing
        # has verified the behaviour of this code.
        WHITESPACE.join(station.split())
        station.replace(NEW_LINE, EMPTY_STRING)
        station.replace(CARRIAGE_RETURN, EMPTY_STRING)
        self._main_dictionary["station"] = station

        self._main_dictionary["dayOfWeek"] = day_of_week
        self._main_dictionary["meal"] = meal
        self._main_dictionary["attributes"] = attributes

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
