import menuparser

class DiningHallMenu():

    # instantiate parser and generate dict of webpage urls for each dining hall
    def __init__(self):
        self.parser = menuparser.MenuParser()
        self.urls = { ("Commons", "http://rpi.sodexomyway.com/Menu/Commons1.htm"),
                 ("Commons2", "http://rpi.sodexomyway.com/Menu/Commons2.htm"),
                 ("Sage", "http://rpi.sodexomyway.com/Menu/Sage.htm"),
                 ("Sage2", "http://rpi.sodexomyway.com/Menu/Sage2.htm"),
                 ("BARH", "http://rpi.sodexomyway.com/Menu/BARH.htm"),
                 ("BARH2", "http://rpi.sodexomyway.com/Menu/BARH2.htm"),
                 ("Blitman", "http://rpi.sodexomyway.com/Menu/Blitmans.htm") }
                 
    # begins parsing on a given webpage, or all if none specified
    def parse(self, url=None):

        # parse all the menus
        if url is None:

            for url in self.urls:

                # debugging
                print ("\n", url[0], "\n")
                self.parser.begin_parsing(url[1])


# instantiate DiningHallMenu and begin parsing menus
menu = DiningHallMenu()
menu.parse()

        
