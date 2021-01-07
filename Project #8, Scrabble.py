#Project for dictionaries
#Note that code is organized chronologically (in order of projects steps/directions)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#using a list comprehension to create a dictionary that maps letters (keys) to points (values)
letters_to_points = {key:value for key,value in zip(letters,points)}

#adding an element to letters_to_points dictionary
letters_to_points[" "] = 0

#calculating the total amount of points earned for a word played in scrabble
def score_word(word):
  point_total = 0
  word = word.upper()
  for eachLetter in word:
    point_total += letters_to_points.get(eachLetter,0)
  return point_total

#testing the above function with the word "brownie"
brownie_points = score_word("BROWNIE")
print(brownie_points)

#dictionary that contains the names of each player along with the words he or she has played
player_to_words = {"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

#creating a new dictionary that will eventually hold each player's point total thus far
players_to_points = {}

#populating the players_to_points dictionary
for player,words in player_to_words.items():
  player_points = 0
  for eachWord in words:
    player_points += score_word(eachWord)
  players_to_points[player] = player_points

#printing the players_to_points dictionary to make sure it's right
print(players_to_points)

#adds a word to a player's played words list
def play_word(player,word):
  player_to_words.get(player).append(word)

#turning the above nested for loops code into a function
def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for eachWord in words:
      player_points += score_word(eachWord)
    players_to_points[player] = player_points



