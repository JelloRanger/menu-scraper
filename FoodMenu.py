import re
import menuparser
import FoodItem

class FoodMenu():

    def __init__(self):
        self.foodList = []

    # add a food to the menu
    def addFood(self, foodItem):
        self.foodList.append(foodItem)

    # implement later
    def getFood(self, name):
        pass

    def __str__(self):
        # print out all items in menu
        result = ""
            
        for food in self.foodList:
            result += str(food)
            result += "\n"

        return result

    def printDiningHall(self, diningHall):
        result = ""

        tempArray = []

        for food in self.foodList:
            if food.getDiningHall() == diningHall:
                tempArray.append(food)

        # write all foods to output.txt and JSON file
        # else block is for last element, no comma in JSON for last element
        for food in tempArray[:-1]:
            result += str(food)
            result += "\n"

            # write to json
            food.writeToJSON()
            j = open("output.json", 'a', encoding = 'iso-8859-1')
            j.write(",\n")
            j.close()
        # handle last element
        else:
            food.writeToJSON()
            j = open("output.json", 'a', encoding = 'iso-8859-1')
            j.write("\n")
            j.close()

        f = open("output.txt", 'a', encoding = 'iso-8859-1')
        f.write(result)
        f.close()
