#Classes section project

class Menu:
  #constructor
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #provides a description of the class
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + ":00 to " + str(self.end_time) + ":00"
  
  #takes a list of items purchased and calculates the total bill
  def calculate_bill(self,purchased_items):
    total = 0
    for each in purchased_items:
      total += self.items.get(each) 
    return total

class Franchise:
  #constructor
  def __init__(self,address, menus):
    self.address = address
    self.menus = menus
  #provides class description
  def __repr__(self):
    return ("The address of this franchise is: " + self.address)
  #takes a time parameter and returns a list of menus available at the franchise at the given time
  def available_menus(self,time):
    menusAvailable = []
    for eachMenu in self.menus:
      if time >= eachMenu.start_time and time <= eachMenu.end_time:
        menusAvailable.append(eachMenu)
    return menusAvailable

class Business:
  #constructor
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
  #class description
  def __repr__(self):
    return "This business is titled " + self.name + "."

#creating multiple menu objects
brunch = Menu("Brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }, 11, 16)
early_bird = Menu("Early Bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15,18)
dinner = Menu("Dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},17,23)
kids = Menu("Kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)
arepas_menus = ("Arepas",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

#creating multiple Franchise objects
flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menus])

#creating two Business objects
new_business = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
another_new_business = Business("Take a' Arepa",[flagship_store,new_installment])


#testing
print(brunch)
print(brunch.calculate_bill(["pancakes","home fries","coffee"]))
print(early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)"]))

print(flagship_store)
print(flagship_store.available_menus(17))

print(new_business)

