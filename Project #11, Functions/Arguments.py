#Function arguments project
#January 23rd, 2020

from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords,to_coords,shipping_type="Overnight"):
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  distance = get_distance(from_lat,from_long,to_lat,to_long)
  shipping_rate = SHIPPING_PRICES.get(shipping_type)
  price = distance * shipping_rate
  return format_price(price)
  
# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance,*drivers):
  #declaring two variables
  #cheapest driver will eventually contain a driver object
  #cheapest_driver_price will eventually contain the price of the cheapest driver
  cheapest_driver = None
  cheapest_driver_price = None

  #for each driver contained in the tuple of drivers argument
  for eachDriver in drivers:
    #calculate the the time the driver will take as well as the cost of the driver
    driver_time = eachDriver.speed * distance
    price_for_driver = eachDriver.salary * driver_time
    #if the for loop is currently on the first driver in the tuple, set cheapest_driver and cheapest_driver_price to the corresponding values of the first driver
    if cheapest_driver == None:
      cheapest_driver = eachDriver
      cheapest_driver_price = price_for_driver
    #if the current driver has a price less than the driver currently listed as having the least price, reassign cheapest_driver and cheapest_driver price to the current driver's corresponding values to account for this
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = eachDriver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
  #declaring a variable that will hold the total amount of money made
  total_money_made = 0
  #for each trip contained in the trips dictionary, calculate the revenue earned from that trip and add it to the total money made
  for trip_id,trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made += trip_revenue
  #return the total amount of money made
  return total_money_made


# Test the function by calling 
test_function(calculate_money_made)
