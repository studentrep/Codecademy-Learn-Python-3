#Project #5, Len's Slice
#Lists

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices,toppings))
pizzas.sort()

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[6]
three_cheapest = pizzas[0:3]
num_two_dollar_slices = prices.count(2)

#print(num_two_dollar_slices)
