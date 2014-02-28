import re
import menuparser
import FoodItem

# TO BE UTILIZED LATER
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

        for food in self.foodList:
            if food.getDiningHall() == diningHall:
                result += str(food)
                result += "\n"

        print (result)
