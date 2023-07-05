import random

def get_choices():
  player_choice = input("Meow! Rudder wants you to enter a choice! (treats, taylor, luna): ")
  options = ["treats", "taylor", "luna"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"you chose {player}!", f"computer chose {computer}!")
  if player == computer:
    return "its a tie!"
  elif player == "treats":
    if computer == "taylor":
      return "treats win priority over taylor! you win meow!"
    else:
      return "luna eats rudders treats! you lose hissss!"
  elif player == "taylor":
    if computer == "luna":
      return "taylor is more fun to annoy than luna! you win meow!"
    else:
      return "treats win priority over taylor! you lose hissss!"
  elif player == "luna":
    if computer == "treats":
      return "luna gives you some of her treats! you win meow!"
    else:
      return "luna tries to lick taylor's face! you lose hissss!"
      
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)