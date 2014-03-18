import menuparser
import FoodMenu

f = open("output.txt", 'w', encoding = 'iso-8859-1')
f.write("")
f.close()

f = open("output.json", 'w', encoding = 'iso-8859-1')
f.write("")
f.close()


class DiningHallMenu():

    # instantiate parser and generate dict of webpage urls for each dining hall
    def __init__(self):
        self.parser = menuparser.MenuParser()
        self.urls = {
                  "Commons":  "http://rpi.sodexomyway.com/Menu/Commons1.htm",
                  "Commons2": "http://rpi.sodexomyway.com/Menu/Commons2.htm",
                  "Sage":     "http://rpi.sodexomyway.com/Menu/Sage.htm",
                  "Sage2":    "http://rpi.sodexomyway.com/Menu/Sage2.htm",
                  "BARH":     "http://rpi.sodexomyway.com/Menu/BARH.htm",
                  "BARH2":    "http://rpi.sodexomyway.com/Menu/BARH2.htm",
                  "Blitman":  "http://rpi.sodexomyway.com/Menu/Blitmans.htm" }               

    # begins parsing on a given webpage, or all if none specified
    def parse(self, url=None):

        # parse all the menus
        if url is None:

            for name, webpage in self.urls.items():

                # Output
                f = open("output.txt", 'a', encoding = 'iso-8859-1')
                f.write(name + "\n")
                f.close()
                f = open("output.json", 'a', encoding = 'iso-8859-1')
                f.write("{\n" + "\t\"name\" : \"" + name + "\",\n\t\"food\":\n\t\t[\n")
                f.close()
                self.parser.begin_parsing(webpage, name)
                f = open("output.json", 'a', encoding = 'iso-8859-1')
                f.write("\t\t]\n}\n")
                f.close()

        # otherwise parse the specified menu
        else:
            assert url in self.urls, "Invalid url"
            self.parser.begin_parsing(self.urls[url], url)
                
                


# instantiate DiningHallMenu and begin parsing menus
menu = DiningHallMenu()
menu.parse()

        
