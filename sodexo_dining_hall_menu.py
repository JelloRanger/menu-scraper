"""Name:     Dining Hall Menu.
File name:   dining_hall_menu.py
Description: Controls what sites we are accessing and where the output
             is sent.
Content:
         Classes:
                  DiningHallMenu
         "Main Code"
Required libraries:
                    Python Standard JSON Library
                    Sodexo Menu Parser
"""

import json
import sodexo_parser


class DiningHallMenu():
    """Dining Hall Menu Class.
    Here, we define the parser's default HTML URLs that the class
    searches.
    The current default is the RPI Sodexo Menu URLs.
    """
    
    _output_array = []

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
                self._output_array.append(self.parser.return_data())

            file.close()
        # Otherwise, parse through the menu for the specific dining
        # hall. Dining hall must be in self.urls.
        else:

            assert hall_name in self.urls, "Invalid URL"
            self.parser.begin_parsing(self.urls[hall_name], hall_name)
            file.close()
    
    def return_data(self):
        """Return data from parser and compile it all under an array because
        JSON requires a single head object.
        
        Arguments:
        
        self -- Allows the function to reference parent class
        properties. It is unnecessary to specify self during function
        calls as it is implied."""
        
        return _output_array
    
    def output_data(self, file=None):
        """Output JSON data into file stream.
        
        Arguments: self - Used to reference parent class.
        
        file - Allows a file stream to be passed. If none is specified the
        default will be used.
        """
        
        if file is None:
            file = open("output.json", 'w', encoding='iso-8859-1')
        
        file.write(json.dumps(self._output_array))

# Instantiate DiningHallMenu and begin parsing menus.
menu = DiningHallMenu()
menu.parse()
menu.output_data()
