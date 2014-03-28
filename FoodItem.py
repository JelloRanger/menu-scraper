import re
class FoodItem():

	def __init__(self, diningHall, name, dayOfWeek, mealTime, station, attribute):
	
		# remove excess whitespace, \n, and \r characters
		name = re.sub(r"\s+", " ", name)
		station = re.sub(r"\s+", " ", station)
		
		# entree is recorded differently in terms of
		# the e with accent on the various menus,
		# so to make things simpler, we avoid the e with accent
		# character by checking first 4 letters, and set it to entree
		if station.lower()[0:4] == "entr":
			station = "entree"
			
		self.name = name
		self.diningHall = diningHall
		self.mealTime = mealTime.lower()
		self.dayOfWeek = dayOfWeek.lower()
		self.station = station.lower()
		self.attribute = attribute
		
		# future attributes to record
		#self.vegetarian
		#self.calories
		#self.station
	# print out relevant food information in a clean format
	def __str__(self):
	
		f = open("output.json", 'a', encoding = 'iso-8859-1')
        f.write("\t\t\t{\n\t\t\t\t\"dayOfWeek\": \"" + self.dayOfWeek + "\",\n\t\t\t\t\"mealTime\":\"" + self.mealTime + "\",\n\t\t\t\t\"station\": \"" + self.station + "\",\n\t\t\t\t\"name\": \"" + self.name + "\",\n\t\t\t\t\"attribute\": ")
		
		self.output = (self.dayOfWeek + ", " + self.mealTime + ", " + self.station + ": " + self.name)
		
		if (len(self.attribute) > 0):
			self.output += (": {}".format(self.attribute[0]))
			
            f.write("\n\t\t\t\t\t[\n\t\t\t\t\t\t\"" + "{}".format(self.attribute[0]) + "\"")
			
			num = 1
			for attr in self.attribute[1:]:
				self.output += (", {}".format(attr))
				
                f.write(",\n\t\t\t\t\t\t\"{}".format(attr) + "\"")
				num += 1
				
            f.write("\n\t\t\t\t\t]")
			
		else:
			f.write("Null")
			
        f.write("\n\t\t\t}\n")
        f.close()
		
		return self.output
		
	# get the dining hall for a FoodItem
	def getDiningHall(self):
		return self.diningHall