print('''
     _~
  _~ )_)_~
  )_))_))_)
  _!__!__!_
  \\______t/
~~~~~~~~~~~~~
''')
print("your name is Luffy. you will be setting out of the sea in search of the one piece and become the pirate king.")

choice_1 = input('You finally turn 18. what will you do? "Set on a journey" or "Continue to stay"\n').lower()

if choice_1 == "Set on a journey".lower():
  choice_2 = input('you decided to set out on a journey. what should you do next? "look for teammate" or "eat"\n').lower()
  if choice_2 == "look for teammate":
    choice_3 = input("you have found the pirate hunter, Zoro tied up. what should you do? 'help him' or 'ignore him'\n").lower()
    if choice_3 == 'help him':
      choice_4 = input("congratualtion you have a new team, zoro. the marine is after you guys, what should you do? 'stay' or 'escape'\n").lower()
      if choice_4 == 'escape':
        choice_5 = input("you have escape. along the way you meet Nami. should you help her? 'Yes' or 'no'\n").lower()

      #to be continued
      
      else:
        print("you have been caught by the marine. the end")
    else:
      print("you have lost the pirate hunter and he was killed by the marine. the end.")
  elif choice_2 == "eat":
    second_choice = input("you continue to eat, but your boat is sinking. what should you do? 'hop into the barrel' or 'swim'\n").lower()
    if second_choice == 'hop into the barrel'.lower():
      second_choice_0 = input("you have been diffting in the ocean for hr. suddenly you start hearing noise coming from outside. 'come out of the barrel' or 'sleep'").lower()
      if second_choice_0 == "come out of the barrel":
        second_choice_1 = input("congratuation, you have saved koby and inspire him to join the marine to help the innocent.")
      else:
        print("you have fallen asleep, a storm went by and you acomplish nothing. the end.")
    else:
      print("luffy cant swim because he ate the gumgum fruit. you drown. the end.")
else:
  print("you decided to not set sail. you have acomplish nothing but continue to eat. the end.")
