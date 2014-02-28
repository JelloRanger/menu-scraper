import menuparser
import FoodMenu

class DiningHallMenu():

    # instantiate parser and generate dict of webpage urls for each dining hall
    def __init__(self):
        self.parser = menuparser.MenuParser()
        self.urls = {
                  "\nCommons":  "http://rpi.sodexomyway.com/Menu/Commons1.htm",
                  "\nCommons2": "http://rpi.sodexomyway.com/Menu/Commons2.htm",
                  "\nSage":     "http://rpi.sodexomyway.com/Menu/Sage.htm",
                  "\nSage2":    "http://rpi.sodexomyway.com/Menu/Sage2.htm",
                  "\nBARH":     "http://rpi.sodexomyway.com/Menu/BARH.htm",
                  "\nBARH2":    "http://rpi.sodexomyway.com/Menu/BARH2.htm",
                  "\nBlitman":  "http://rpi.sodexomyway.com/Menu/Blitmans.htm" }               

    # begins parsing on a given webpage, or all if none specified
    def parse(self, url=None):

        # parse all the menus
        if url is None:

            for name, webpage in self.urls.items():

                # debugging
                print (name)
                self.parser.begin_parsing(webpage, name)

        # otherwise parse the specified menu
        else:
            assert url in self.urls, "Invalid url"
            self.parser.begin_parsing(self.urls[url], url)
                
                


# instantiate DiningHallMenu and begin parsing menus
menu = DiningHallMenu()
menu.parse()

        
