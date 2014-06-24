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
