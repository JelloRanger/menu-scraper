"""Name:     Dining Hall Menu.
File name:   dining_hall_menu.py
Description: Controls what sites we are accessing and where the output
             is sent.
Content:
         Classes:
                  DiningHallMenu
         "Main Code"
Required libraries:
                    Sodexo Menu Parser
"""

import sodexo_parser


class DiningHallMenu():
    """Dining Hall Menu Class.
    Here, we define the parser's default HTML URLs that the class
    searches.
    The current default is the RPI Sodexo Menu URLs.
    """

    def __init__(self):
        """Sodexo Dining Hall Menu Constructor
        Here, we define our default parser and default URLs.

        Arguments: self - Used to reference parent class.
        """

        self.parser = sodexo_parser.MenuParser()
        self.urls = {
            "Commons":  "http://rpi.sodexomyway.com/Menu/Commons1.htm",
            "Commons2": "http://rpi.sodexomyway.com/Menu/Commons2.htm",
            "Sage":     "http://rpi.sodexomyway.com/Menu/Sage.htm",
            "Sage2":    "http://rpi.sodexomyway.com/Menu/Sage2.htm",
            "BARH":     "http://rpi.sodexomyway.com/Menu/BARH.htm",
            "BARH2":    "http://rpi.sodexomyway.com/Menu/BARH2.htm",
            "Blitman":  "http://rpi.sodexomyway.com/Menu/Blitmans.htm"}

    def parse(self, hall_name=None, file=None):
        """Sodexo Dining Hall Menu Parse Command
        The function begins parsing on the passed URL in the argument, if
        no arguments have been passed, then we will parse through all the
        default URLs as defined in self.urls

        Arguments: self - Used to reference parent class.

        hall_name - Allows a specific dining hall to be parsed.

        file - Allows a file stream to be passed. If none is specified the
        default will be used.
        """

        # If no file is specified, then we will provide a file stream.
        if file is None:

            file = open("output.json", 'w', encoding='iso-8859-1')

        # Parse through all the menus because none is specified.
        if hall_name is None:

            for name, webpage in self.urls.items():

                # Output
                self.parser.begin_parsing(webpage, name)
                self.parser.print_food(file)

        # Otherwise, parse through the menu for the specific dining
        # hall. Dining hall must be in self.urls.
        else:

            assert hall_name in self.urls, "Invalid URL"
            self.parser.begin_parsing(self.urls[hall_name], hall_name)

# Instantiate DiningHallMenu and begin parsing menus.
menu = DiningHallMenu()
menu.parse()
