#Project 3, Control Flow
#Sal's Shipping
premiumGround = 125

def groundShipping(weight):
  if weight <= 2:
    cost = 1.50 * weight
  elif weight > 2 and weight <= 6:
    cost = 3.00 * weight
  elif weight > 6 and weight <= 10:
    cost = 4.00 * weight
  elif weight > 10:
    cost = 4.75 * weight
  return cost + 20

def droneShipping(weight):
  if weight <= 2:
    cost = 4.50 * weight
  elif weight > 2 and weight <= 6:
    cost = 9.00 * weight
  elif weight > 6 and weight <= 10:
    cost = 12.00 * weight
  elif weight > 10:
    cost = 14.25 * weight
  return cost

def cheapestOption(weight):
  groundCost = groundShipping(weight)
  droneCost = droneShipping(weight)
  premiumCost = premiumGround

  #If ground shipping is the cheapest option
  if groundCost < droneCost and groundCost < premiumCost:
    return "You should choose ground shipping for a total cost of " + str(groundCost) + " dollars."
  #If drone shipping is the cheapest option
  elif droneCost < groundCost and droneCost < premiumCost:
    return "You should choose drone shipping for a total cost of " + str(droneCost) + " dollars."
  #If premium ground shipping is the cheapest option
  elif premiumCost < groundCost and premiumCost < droneCost:
    return "You should choose premium ground shipping for a total cost of " + str(premiumCost) + " dollars."
  else:
    "There is no single cheapest option."

print(cheapestOption(4.8))
print(cheapestOption(41.5))
