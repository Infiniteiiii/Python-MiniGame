"""
| Programmer:  Arham Arsalan                                 |
| Course:      ICS2O1                                        |
| Date:        Jan. 19th, 2024                               |
|------------------------------------------------------------|
|This program has two games Trivia and Hangman.              | 
"""

#Importing Libraries
import os
import random

print(
    " ----------------------------------------- \n |---------------------------------------|\n |   Welcome to the Mini Game Arcade     |\n |---------------------------------------|\n -----------------------------------------"
)
print("%30s" % "Hangman  or  Trivia ")
game = input("\n      Enter the game name to play: ")

os.system("clear")

game = game.upper()
while game != "HANGMAN" and game != "TRIVIA":
  game = input("\nEnter a valid game name to play either Hangman or Trivia: ")
  game = game.upper()

os.system("clear")

#Start Variables
wrongAnswer = 0
correctAnswer = 0

#Game is Trivia
if game == "TRIVIA":
  print(
      " ------------------------- \n |-----------------------|\n |   Welcome to Trivia   |\n |-----------------------|\n -------------------------"
  )
  print(
      "Choose a topic \n 1. Animals \n 2. Countries \n 3. Education \n 4. Sports"
  )
  topic = input("Enter the number of the topic you want to play: ")
  while topic != "1" and topic != "2" and topic != "3" and topic != "4":
    topic = input("Enter a valid number: ")
  input("Press ENTER to continue.")
  os.system("clear")

  #TOPIC NUMBER ONE
  if topic == "1":
    usedNumbers = []
    for i in range(1, 6):
      randQuestion = (random.randint(1, 10))
      while randQuestion in usedNumbers:
        randQuestion = (random.randint(1, 10))
      usedNumbers.append(randQuestion)
      os.system("clear")
      if randQuestion == 1:
        print("What is the largest mammal in the world?")
        print(
            "The choices are \n 1. Blue Whale \n 2. Elephant \n 3. Cheetah \n 4. Girraffe"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 2
      elif randQuestion == 2:
        print(
            "Which mammal is known to have the most powerful bite in the world?"
        )
        print(
            "The choices are \n 1. Lion \n 2. Crocodile \n 3. Monkey \n 4. Hippopotamus"
        )
        answer = (input("Enter your answer number: "))
        if answer != "4":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "4":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 3
      elif randQuestion == 3:
        print("What male sea creature gives birth to its young?")
        print(
            "The choices are \n 1. Lionfish \n 2. Sea Eel \n 3. Clownfish \n 4. Seahorse"
        )
        answer = (input("Enter your answer number: "))
        if answer != "4":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "4":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 4
      elif randQuestion == 4:
        print("What is the only place dogs have sweat glands?")
        print("The choices are \n 1. Arms \n 2. Legs \n 3. Paws \n 4. Ears")
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 5
      elif randQuestion == 5:
        print("What is the smallest mammal in the world?")
        print(
            "The choices are \n 1. Human \n 2. Bumblebee Bat \n 3. Squirrel \n 4. Fox"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 6
      elif randQuestion == 6:
        print("How many legs does a lobster have?")
        print("The choices are \n 1. 10 \n 2. 6 \n 3. 8 \n 4. 12")
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 7
      elif randQuestion == 7:
        print("What is the fastest sea creature?")
        print(
            "The choices are \n 1. Sailfish \n 2. Great White Shark \n 3. Blue Whale \n 4. Lobster"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 8
      elif randQuestion == 8:
        print("What is the only large cat that does not roar?")
        print(
            "The choices are \n 1. Lion \n 2. Tiger \n 3. Cheetah \n 4. Leopard"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 9
      elif randQuestion == 9:
        print("What animal has the thickest fur of any mammal?")
        print(
            "The choices are \n 1. Polar Bear \n 2. Human \n 3. Sea Otter \n 4. Wolf"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 10
      elif randQuestion == 10:
        print("What animal has the longest lifespan?")
        print(
            "The choices are \n 1. Clam \n 2. Tortoise \n 3. Blue Whale \n 4. Elephant"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")

#TOPIC NUMBER TWO
  if topic == "2":
    usedNumbers = []
    for i in range(1, 6):
      randQuestion = (random.randint(1, 10))
      while randQuestion in usedNumbers:
        randQuestion = (random.randint(1, 10))
      usedNumbers.append(randQuestion)
      os.system("clear")

      if randQuestion == 1:
        print("Which country is known as the 'Land of the Rising Sun?'")
        print(
            "The choices are \n 1. China \n 2. Japan \n 3. South Korea \n 4. Vietnam"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 2
      elif randQuestion == 2:
        print("What is the capital city of Brazil?")
        print(
            "The choices are \n 1. Rio de Janeiro \n 2. Brasilia \n 3. Sao Paulo \n 4. Buenos Aires"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 3
      elif randQuestion == 3:
        print(
            "The Great Barrier Reef, one of the world's largest coral reef systems, is located off the coast of which country?"
        )
        print(
            "The choices are \n 1.  Brazil \n 2.  Australia \n 3. Mexico \n 4. Indonesia"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 4
      elif randQuestion == 4:
        print("In which country is the famous ancient city of Petra located?")
        print(
            "The choices are \n 1. Greece \n 2. Egypt \n 3. Jordan \n 4. Italy"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 5
      elif randQuestion == 5:
        print("Which country is known as the Land of a Thousand Lakes?")
        print(
            "The choices are \n 1. Canada \n 2. Finland \n 3. Norway \n 4. Russia"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 6
      elif randQuestion == 6:
        print("What is the capital city of Canada?")
        print(
            "The choices are \n 1. Toronto \n 2. Ottawa \n 3. Vancouver \n 4. Montreal"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 7
      elif randQuestion == 7:
        print(
            "Which of the following countries is the smallest in terms of land area?"
        )
        print(
            "The choices are \n 1. Russia \n 2. Canada \n 3. Monaco \n 4. Australia"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 8
      elif randQuestion == 8:
        print("In which continent is the Sahara Desert primarily located?")
        print(
            "The choices are \n 1. Asia \n 2. Africa \n 3. South America \n 4. North America"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 9
      elif randQuestion == 9:
        print(
            "Which European country is known as the Land of Fire and Ice due to its volcanic activity and glaciers?"
        )
        print(
            "The choices are \n 1. Norway \n 2. Iceland \n 3. Switzerland \n 4. Greece"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 10
      elif randQuestion == 10:
        print("What is the official language of Brazil?")
        print(
            "The choices are \n 1. Spanish \n 2. Portugese \n 3. Italian \n 4. French"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")

#TOPIC NUMBER THREE
  if topic == "3":
    usedNumbers = []
    for i in range(1, 6):
      randQuestion = (random.randint(1, 10))
      while randQuestion in usedNumbers:
        randQuestion = (random.randint(1, 10))
      usedNumbers.append(randQuestion)
      os.system("clear")

      if randQuestion == 1:
        print("Mathematics: What is the result of the multiplication 7 x 8?")
        print("The choices are \n 1. 48 \n 2. 56 \n 3. 64 \n 4. 72")
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 2
      elif randQuestion == 2:
        print("Literature: Who wrote the play Romeo and Juliet?")
        print(
            "The choices are \n 1. William Wordsworth \n 2. William Shakespeare \n 3. Jane Austen \n 4. Charles Dickens"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 3
      elif randQuestion == 3:
        print("Science: What is the chemical symbol for gold?")
        print("The choices are \n 1. Au \n 2. Ag \n 3. Fe \n 4. Hg")
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 4
      elif randQuestion == 4:
        print(
            "History: In which year did the United States declare its independence?"
        )
        print("The choices are \n 1. 1776 \n 2. 1789 \n 3. 1800 \n 4. 1812")
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 5
      elif randQuestion == 5:
        print(
            "Geography: Which of the following is the longest river in the world?"
        )
        print(
            "The choices are \n 1. Amazon River \n 2. Nile River \n 3. Yangtze River \n 4. Mississippi River"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 6
      elif randQuestion == 6:
        print("Physics: What is the SI unit of force?")
        print("The choices are \n 1. Newton \n 2. Joule \n 3. Watt \n 4. Ohm")
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 7
      elif randQuestion == 7:
        print("Art: Who painted the Mona Lisa?")
        print(
            "The choices are \n 1. Vincent van Gogh \n 2. Leonardo da Vinci \n 3. Pablo Picasso \n 4. Michelangelo"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 8
      elif randQuestion == 8:
        print(
            "Biology: Which organelle is known as the powerhouse of the cell?")
        print(
            "The choices are \n 1. Nucleus \n 2. Golgi apparatus \n 3. Mitochondrion \n 4. Endoplasmic reticulum"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 9
      elif randQuestion == 9:
        print("Chemistry: Which element has the chemical symbol O?")
        print(
            "The choices are \n 1. Oxygen \n 2. Osmium \n 3. Oganesson \n 4. Orpiment"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 10
      elif randQuestion == 10:
        print(
            "Computer Science: What does HTML stand for in the context of web development?"
        )
        print(
            "The choices are \n 1. HyperText Markup Language \n 2. High-Level Texting Language \n 3. Hyperlink and Text Management Language \n 4. Human-Technology Markup Logic"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")

#TOPIC NUMBER FOUR
  if topic == "4":
    usedNumbers = []
    for i in range(1, 6):
      randQuestion = (random.randint(1, 10))
      while randQuestion in usedNumbers:
        randQuestion = (random.randint(1, 10))
      usedNumbers.append(randQuestion)
      os.system("clear")

      if randQuestion == 1:
        print("Football: Which country hosted the FIFA World Cup in 2018?")
        print(
            "The choices are \n 1. Brazil \n 2. Germany \n 3. Russia \n 4. France"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 2
      elif randQuestion == 2:
        print(
            "Basketball: Who is widely considered the greatest basketball player of all time?"
        )
        print(
            "The choices are \n 1. Kobe Bryant \n 2. LeBron James \n 3. Michael Jordan \n 4. Magic Johnson"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 3
      elif randQuestion == 3:
        print(
            "Soccer: In which country did the sport of soccer (football) originate?"
        )
        print(
            "The choices are \n 1. England \n 2. Brazil \n 3. Italy \n 4. Germany"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 4
      elif randQuestion == 4:
        print(
            "Tennis: Who holds the record for the most Grand Slam singles titles in tennis?"
        )
        print(
            "The choices are \n 1. Serena Williams \n 2. Roger Federer \n 3. Rafael Nadal \n 4. Novak Djokovic"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 5
      elif randQuestion == 5:
        print(
            "Golf: Which major golf tournament is held annually at Augusta National Golf Club?"
        )
        print(
            "The choices are \n 1. The Open Championship \n 2. PGA Championship \n 3. Masters Tournament \n 4. U.S. Open"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 6
      elif randQuestion == 6:
        print(
            "Olympics: In which city did the 2016 Summer Olympics take place?")
        print(
            "The choices are \n 1. Tokyo \n 2. Rio De Janeiro \n 3. London \n 4. Beijing"
        )
        answer = (input("Enter your answer number: "))
        if answer != "2":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "2":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 7
      elif randQuestion == 7:
        print(
            "Baseball: What is the term for a batter hitting the ball out of the playing field in one swing?"
        )
        print(
            "The choices are \n 1. Home Run \n 2. Grand Slam \n 3. Strikeout \n 4. Double Play"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 8
      elif randQuestion == 8:
        print(
            "Cricket: How many players are there in a standard cricket team?")
        print("The choices are \n 1. 8 \n 2. 10 \n 3. 11 \n 4. 12")
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 9
      elif randQuestion == 9:
        print(
            "Athletics: In which track and field event would you perform a Fosbury Flop?"
        )
        print(
            "The choices are \n 1. High Jump \n 2. Pole Vault \n 3. Long Jump \n 4. Triple Jump"
        )
        answer = (input("Enter your answer number: "))
        if answer != "1":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "1":
          correctAnswer = correctAnswer + 1
          os.system("clear")
    #Question Possibility 10
      elif randQuestion == 10:
        print(
            "Boxing: Who is known as The Greatest and The Champ in the sport of boxing?"
        )
        print(
            "The choices are \n 1. Floyd Mayweather \n 2. Mike Tyson \n 3. Muhammad Ali \n 4.  Manny Pacquiao"
        )
        answer = (input("Enter your answer number: "))
        if answer != "3":
          wrongAnswer = wrongAnswer + 1
          os.system("clear")
        elif answer == "3":
          correctAnswer = correctAnswer + 1
          os.system("clear")
  print(
      "--------------------------------------- \n| Correct Answers: |  Wrong Answers:  |\n|------------------|------------------|\n|        {}         |         {}        |\n|------------------|------------------|"
      .format(correctAnswer, wrongAnswer))

#IF GAME HANGMAN

if game == "HANGMAN":
  print(
      " |--------------------| \n | Welcome to Hangman | \n |--------------------|"
  )

  wordDictionary = [
      "about", "above", "abuse", "accept", "accident", "accuse", "across",
      "activist", "actor", "administration", "admit", "adult", "advertise",
      "advise", "affect", "afraid", "after", "again", "against", "agency",
      "aggression", "agree", "agriculture", "force", "airplane", "airport",
      "album", "alcohol", "alive", "almost", "alone", "along", "already",
      "although", "always", "ambassador", "amend", "ammunition", "among",
      "amount", "anarchy", "ancestor", "ancient", "anger", "animal",
      "anniversary", "announce", "another", "answer", "apologize", "appeal",
      "appear", "appoint", "approve", "archeology", "argue", "around",
      "arrest", "arrive", "artillery", "assist", "astronaut", "astronomy",
      "asylum", "atmosphere", "attach", "attack", "attempt", "attend",
      "attention", "automobile", "autumn", "available", "average", "avoid",
      "awake", "award", "balance", "balloon", "ballot", "barrier", "battle",
      "beauty", "because", "become", "before", "begin", "behavior", "behind",
      "believe", "belong", "below", "betray", "better", "between", "biology",
      "black", "blame", "bleed", "blind", "block", "blood", "border", "borrow",
      "bottle", "bottom", "boycott", "brain", "brave", "bread", "break",
      "breathe", "bridge", "brief", "bright", "bring", "broadcast", "brother",
      "brown", "budget", "build", "building", "bullet", "burst", "business",
      "cabinet", "camera", "campaign", "cancel", "cancer", "candidate",
      "capital", "capture", "career", "careful", "carry", "catch", "cause",
      "ceasefire", "celebrate", "center", "century", "ceremony", "chairman",
      "champion", "chance", "change", "charge", "chase", "cheat", "cheer",
      "chemicals", "chemistry", "chief", "child", "children", "choose",
      "circle", "citizen", "civilian", "civil", "rights", "claim", "clash",
      "class", "clean", "clear", "clergy", "climate", "climb", "clock",
      "close", "cloth", "clothes", "cloud", "coalition", "coast", "coffee",
      "collapse", "collect", "college", "colony", "color", "combine",
      "command", "comment", "committee", "common", "communicate", "community",
      "company", "compare", "compete", "complete", "complex", "compromise",
      "computer", "concern", "condemn", "condition", "conference", "confirm",
      "conflict", "congratulate", "Congress", "connect", "conservative",
      "consider", "constitution", "contact", "contain", "container",
      "continent", "continue", "control", "convention", "cooperate", "correct",
      "corruption", "cotton", "count", "country", "court", "cover", "crash",
      "create", "creature", "credit", "crime", "criminal", "crisis",
      "criticize", "crops", "cross", "crowd", "crush", "culture", "curfew",
      "current", "custom", "customs", "damage", "dance", "danger", "daughter",
      "debate", "decide", "declare", "decrease", "defeat", "defend", "deficit",
      "define", "degree", "delay", "delegate", "demand", "democracy",
      "demonstrate", "denounce", "depend", "deplore", "deploy", "depression",
      "describe", "desert", "design", "desire", "destroy", "detail", "detain",
      "develop", "device", "dictator", "different", "difficult", "dinner",
      "diplomat", "direct", "direction", "disappear", "disarm", "disaster",
      "discover", "discrimination", "discuss", "disease", "dismiss", "dispute",
      "dissident", "distance", "divide", "doctor", "document", "dollar",
      "donate", "double", "dream", "drink", "drive", "drown", "during",
      "early", "earth", "earthquake", "ecology", "economy", "education",
      "effect", "effort", "either", "elect", "electricity", "embassy",
      "embryo", "emergency", "emotion", "employ", "empty", "enemy", "energy",
      "enforce", "engine", "engineer", "enjoy", "enough", "enter",
      "environment", "equal", "equipment", "escape", "especially", "establish",
      "estimate", "ethnic", "evaporate", "event", "every", "evidence", "exact",
      "examine", "example", "excellent", "except", "exchange", "excuse",
      "execute", "exercise", "exile", "exist", "expand", "expect", "expel",
      "experience", "experiment", "expert", "explain", "explode", "explore",
      "export", "express", "extend", "extra", "extraordinary", "extreme",
      "extremist", "factory", "false", "family", "famous", "father",
      "favorite", "federal", "female", "fence", "fertile", "field", "fierce",
      "fight", "final", "financial", "finish", "fireworks", "first", "float",
      "flood", "floor", "flower", "fluid", "follow", "force", "foreign",
      "forest", "forget", "forgive", "former", "forward", "freedom", "freeze",
      "fresh", "friend", "frighten", "front", "fruit", "funeral", "future",
      "gather", "general", "generation", "genocide", "gentle", "glass",
      "goods", "govern", "government", "grain", "grass", "great", "green",
      "grind", "ground", "group", "guarantee", "guard", "guerrilla", "guide",
      "guilty", "happen", "happy", "harvest", "headquarters", "health",
      "heavy", "helicopter", "hijack", "history", "holiday", "honest", "honor",
      "horrible", "horse", "hospital", "hostage", "hostile", "hotel", "house",
      "however", "human", "humor", "hunger", "hurry", "husband", "identify",
      "ignore", "illegal", "imagine", "immediate", "immigrant", "import",
      "important", "improve", "incident", "incite", "include", "increase",
      "independent", "individual", "industry", "infect", "inflation",
      "influence", "inform", "information", "inject", "injure", "innocent",
      "insane", "insect", "inspect", "instead", "instrument", "insult",
      "intelligence", "intelligent", "intense", "interest", "interfere",
      "international", "Internet", "intervene", "invade", "invent", "invest",
      "investigate", "invite", "involve", "island", "issue", "jewel", "joint",
      "judge", "justice", "kidnap", "knife", "knowledge", "labor",
      "laboratory", "language", "large", "laugh", "launch", "learn", "leave",
      "legal", "legislature", "letter", "level", "liberal", "light",
      "lightning", "limit", "liquid", "listen", "literature", "little",
      "local", "lonely", "loyal", "machine", "magazine", "major", "majority",
      "manufacture", "march", "market", "marry", "material", "mathematics",
      "matter", "mayor", "measure", "media", "medicine", "member", "memorial",
      "memory", "mental", "message", "metal", "method", "microscope", "middle",
      "militant", "military", "militia", "mineral", "minister", "minor",
      "minority", "minute", "missile", "missing", "mistake", "model",
      "moderate", "modern", "money", "month", "moral", "morning", "mother",
      "motion", "mountain", "mourn", "movement", "movie", "murder", "music",
      "mystery", "narrow", "nation", "native", "natural", "nature",
      "necessary", "negotiate", "neighbor", "neither", "neutral", "never",
      "night", "noise", "nominate", "normal", "north", "nothing", "nowhere",
      "nuclear", "number", "object", "observe", "occupy", "ocean", "offensive",
      "offer", "office", "officer", "official", "often", "operate", "opinion",
      "oppose", "opposite", "oppress", "orbit", "order", "organize", "other",
      "overthrow", "paint", "paper", "parachute", "parade", "pardon", "parent",
      "parliament", "partner", "party", "passenger", "passport", "patient",
      "peace", "people", "percent", "perfect", "perform", "period",
      "permanent", "permit", "person", "persuade", "physical", "physics",
      "picture", "piece", "pilot", "place", "planet", "plant", "plastic",
      "please", "plenty", "point", "poison", "police", "policy", "politics",
      "pollute", "popular", "population", "position", "possess", "possible",
      "postpone", "poverty", "power", "praise", "predict", "pregnant",
      "present", "president", "press", "pressure", "prevent", "price",
      "prison", "private", "prize", "probably", "problem", "process",
      "produce", "profession", "professor", "profit", "program", "progress",
      "project", "promise", "propaganda", "property", "propose", "protect",
      "protest", "prove", "provide", "public", "publication", "publish",
      "punish", "purchase", "purpose", "quality", "question", "quick", "quiet",
      "radar", "radiation", "radio", "railroad", "raise", "reach", "react",
      "ready", "realistic", "reason", "reasonable", "rebel", "receive",
      "recent", "recession", "recognize", "record", "recover", "reduce",
      "reform", "refugee", "refuse", "register", "regret", "reject",
      "relations", "release", "religion", "remain", "remains", "remember",
      "remove", "repair", "repeat", "report", "represent", "repress",
      "request", "require", "rescue", "research", "resign", "resist",
      "resolution", "resource", "respect", "responsible", "restaurant",
      "restrain", "restrict", "result", "retire", "return", "revolt", "right",
      "river", "rocket", "rough", "round", "rubber", "rural", "sabotage",
      "sacrifice", "sailor", "satellite", "satisfy", "school", "science",
      "search", "season", "second", "secret", "security", "seeking", "seize",
      "Senate", "sense", "sentence", "separate", "series", "serious", "serve",
      "service", "settle", "several", "severe", "shake", "shape", "share",
      "sharp", "sheep", "shell", "shelter", "shine", "shock", "shoot", "short",
      "should", "shout", "shrink", "sickness", "signal", "silence", "silver",
      "similar", "simple", "since", "single", "sister", "situation",
      "skeleton", "skill", "slave", "sleep", "slide", "small", "smash",
      "smell", "smoke", "smooth", "social", "soldier", "solid", "solve",
      "sound", "south", "space", "speak", "special", "speech", "speed",
      "spend", "spill", "spirit", "split", "sport", "spread", "spring",
      "square", "stand", "start", "starve", "state", "station", "statue",
      "steal", "steam", "steel", "stick", "still", "stone", "store", "storm",
      "story", "stove", "straight", "strange", "street", "stretch", "strike",
      "strong", "structure", "struggle", "study", "stupid", "subject",
      "submarine", "substance", "substitute", "subversion", "succeed",
      "sudden", "suffer", "sugar", "suggest", "suicide", "summer", "supervise",
      "supply", "support", "suppose", "suppress", "surface", "surplus",
      "surprise", "surrender", "surround", "survive", "suspect", "suspend",
      "swallow", "swear", "sweet", "sympathy", "system", "target", "taste",
      "teach", "technical", "technology", "telephone", "telescope",
      "television", "temperature", "temporary", "tense", "terrible",
      "territory", "terror", "terrorist", "thank", "theater", "theory",
      "there", "these", "thick", "thing", "think", "third", "threaten",
      "through", "throw", "tired", "today", "together", "tomorrow", "tonight",
      "torture", "total", "touch", "toward", "trade", "tradition", "traffic",
      "tragic", "train", "transport", "transportation", "travel", "treason",
      "treasure", "treat", "treatment", "treaty", "trial", "tribe", "trick",
      "troops", "trouble", "truce", "truck", "trust", "under", "understand",
      "unite", "universe", "university", "unless", "until", "urgent", "usual",
      "vacation", "vaccine", "valley", "value", "vegetable", "vehicle",
      "version", "victim", "victory", "video", "village", "violate",
      "violence", "visit", "voice", "volcano", "volunteer", "wages", "waste",
      "watch", "water", "wealth", "weapon", "weather", "weigh", "welcome",
      "wheat", "wheel", "where", "whether", "which", "while", "white", "whole",
      "willing", "window", "winter", "withdraw", "without", "witness", "woman",
      "wonder", "wonderful", "world", "worry", "worse", "worth", "wound",
      "wreck", "wreckage", "write", "wrong", "yellow", "yesterday", "young"
  ]

  ### Choose a random word
  randomWord = random.choice(
      wordDictionary).lower()  # Convert the random word to lowercase

  for i in randomWord:
    print("_", end=" ")

  def print_hangman(wrong):
    if wrong == 0:
      print("\n+---+")
      print("    |")
      print("    |")
      print("    |")
      print("   ===")
    elif wrong == 1:
      print("\n+---+")
      print("O   |")
      print("    |")
      print("    |")
      print("   ===")
    elif wrong == 2:
      print("\n+---+")
      print("O   |")
      print("|   |")
      print("    |")
      print("   ===")
    elif wrong == 3:
      print("\n+---+")
      print(" O  |")
      print("/|  |")
      print("    |")
      print("   ===")
    elif wrong == 4:
      print("\n+---+")
      print(" O  |")
      print("/|\\ |")
      print("    |")
      print("   ===")
    elif wrong == 5:
      print("\n+---+")
      print(" O  |")
      print("/|\\ |")
      print("/   |")
      print("   ===")
    elif wrong == 6:
      print("\n+---+")
      print(" O   |")
      print("/|\\  |")
      print("/ \\  |")
      print("    ===")

  def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
      if char in guessedLetters:
        print(char, end=" ")
        rightLetters += 1
      else:
        print(" ", end=" ")
      counter += 1
    return rightLetters

  def printLines():
    print("\r")
    for char in randomWord:
      print("\u203E", end=" ")

  length_of_word_to_guess = len(randomWord)
  amount_of_times_wrong = 0
  current_guess_index = 0
  current_letters_guessed = set()
  current_letters_right = 0

  while amount_of_times_wrong < 6 and current_letters_right < length_of_word_to_guess:
    print_hangman(amount_of_times_wrong)
    print("\nLetters guessed so far: ")
    print(" ".join(current_letters_guessed))
    ### Prompt user for input
    letterGuessed = input(
        "\nGuess a letter: ").lower()  # Convert user input to lowercase

    if letterGuessed.isalpha() and len(
        letterGuessed) == 1:  # Check if the input is a single letter
      ### Check if letter was guessed before
      if letterGuessed in current_letters_guessed:
        print("You already guessed this letter. Try again.")
        continue

      ### Check if the guessed letter is incorrect
      if letterGuessed not in randomWord:
        # Increment the count of wrong guesses
        amount_of_times_wrong += 1

        # Print hangman figure
        print_hangman(amount_of_times_wrong)

      ### User is right
      if randomWord[current_guess_index] == letterGuessed:
        ### Print word
        current_guess_index += 1
        current_letters_guessed.add(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
      ### User was wrong
      else:
        ### Print word
        current_letters_guessed.add(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    else:
      print("Invalid input. Please enter a single letter.")

  if amount_of_times_wrong == 6:
    print("You lost! The word was: %s" % randomWord)
  else:
    print("You got it! The word was: %s" % randomWord)
  print("You got it wrong %d times" % amount_of_times_wrong)
