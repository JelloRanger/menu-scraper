import re

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

    def __str__(self, diningHall=None, day=None, meal=None):
        # print out all items in menu
        if diningHall is None:
            
            for food in foodList:
                print (food)
